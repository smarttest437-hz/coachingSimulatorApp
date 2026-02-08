"""
Scenario Manager - Extract and manage coaching scenarios from transcripts
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import streamlit as st

class ScenarioManager:
    """Manages extraction and storage of coaching scenarios from transcripts."""

    def __init__(self, storage_file: str = "custom_scenarios.json"):
        self.storage_file = storage_file
        self.scenarios = self._load_scenarios()

    def _load_scenarios(self) -> List[Dict]:
        """Load existing scenarios from JSON file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                st.warning(f"Could not load scenarios: {e}")
                return []
        return []

    def _save_scenarios(self):
        """Save scenarios to JSON file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.scenarios, f, indent=2)
            return True
        except Exception as e:
            st.error(f"Could not save scenarios: {e}")
            return False

    def extract_client_statements(self, transcript: str) -> List[Dict]:
        """
        Extract client statements from transcript, combining consecutive lines into complete paragraphs.
        Returns list of potential scenarios with metadata.
        """
        statements = []
        lines = transcript.split('\n')

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Find start of client statement
            if line.lower().startswith('client:'):
                # Get context (look back for most recent coach statement)
                context = ""
                for j in range(i - 1, -1, -1):
                    if lines[j].strip().lower().startswith('coach:'):
                        context = lines[j].strip()[6:].strip()
                        break

                # Combine consecutive client lines into one complete statement
                combined_statement = line[7:].strip()  # Remove "Client:" prefix
                start_line = i + 1
                i += 1

                # Keep adding consecutive client lines
                while i < len(lines):
                    next_line = lines[i].strip()
                    if next_line.lower().startswith('client:'):
                        # Remove "Client:" prefix and add to statement
                        combined_statement += " " + next_line[7:].strip()
                        i += 1
                    elif next_line.lower().startswith('coach:'):
                        # Stop at next coach statement
                        break
                    else:
                        # Skip empty lines or continue
                        i += 1

                # Clean up the statement
                combined_statement = combined_statement.strip()

                # Filter for substantive statements (longer than 30 chars for combined)
                if len(combined_statement) > 30:
                    statements.append({
                        'statement': combined_statement,
                        'context': context,
                        'line_number': start_line,
                        'length': len(combined_statement)
                    })
            else:
                i += 1

        return statements

    def categorize_scenarios_with_ai(self, statements: List[Dict], client, model_name: str = "llama3.1:8b") -> List[Dict]:
        """
        Use AI to categorize scenarios and assess quality.

        Args:
            statements: List of client statements
            client: OpenAI client instance

        Returns:
            List of scenarios with category and quality score
        """
        categorized = []

        for stmt in statements:
            prompt = f"""
Analyze this client statement from a coaching session and provide:
1. Category (one of: Career, Leadership, Relationship, Self Improvement, Value System)
2. Quality score (1-10, where 10 = excellent coaching moment)
3. Brief reason for quality score

Client statement: "{stmt['statement']}"
Context (coach's previous question): "{stmt['context']}"

Respond in JSON format:
{{
    "category": "Career",
    "quality_score": 8,
    "reason": "Clear dilemma with emotional weight, good for practicing evocative questions"
}}
"""

            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5
                )

                # Parse AI response
                ai_response = response.choices[0].message.content

                # Try to extract JSON from response
                import re
                json_match = re.search(r'\{[^}]+\}', ai_response)
                if json_match:
                    analysis = json.loads(json_match.group())

                    categorized.append({
                        **stmt,
                        'category': analysis.get('category', 'Self Improvement'),
                        'quality_score': analysis.get('quality_score', 5),
                        'reason': analysis.get('reason', ''),
                        'extracted_date': datetime.now().isoformat(),
                        'source': 'transcript_extraction'
                    })
            except Exception as e:
                # Fallback: default category
                categorized.append({
                    **stmt,
                    'category': 'Self Improvement',
                    'quality_score': 5,
                    'reason': 'Auto-extracted, needs review',
                    'extracted_date': datetime.now().isoformat(),
                    'source': 'transcript_extraction'
                })

        return categorized

    def add_scenario(self, scenario: Dict) -> bool:
        """
        Add a new scenario to the library.

        Args:
            scenario: Dictionary with keys: statement, category, quality_score, etc.

        Returns:
            True if successful
        """
        # Generate unique ID
        scenario['id'] = f"custom_{datetime.now().strftime('%Y%m%d%H%M%S')}_{len(self.scenarios)}"

        self.scenarios.append(scenario)
        return self._save_scenarios()

    def get_scenarios_by_category(self, category: str) -> List[Dict]:
        """Get all scenarios for a specific category."""
        return [s for s in self.scenarios if s.get('category') == category]

    def get_all_categories(self) -> List[str]:
        """Get list of unique categories in the library."""
        categories = set(s.get('category', 'Self Improvement') for s in self.scenarios)
        return sorted(list(categories))

    def get_stats(self) -> Dict:
        """Get statistics about the scenario library."""
        if not self.scenarios:
            return {
                'total': 0,
                'by_category': {},
                'avg_quality': 0,
                'last_added': None
            }

        by_category = {}
        for scenario in self.scenarios:
            cat = scenario.get('category', 'Unknown')
            by_category[cat] = by_category.get(cat, 0) + 1

        quality_scores = [s.get('quality_score', 0) for s in self.scenarios]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        dates = [s.get('extracted_date', '') for s in self.scenarios]
        last_added = max(dates) if dates else None

        return {
            'total': len(self.scenarios),
            'by_category': by_category,
            'avg_quality': round(avg_quality, 1),
            'last_added': last_added
        }

    def merge_with_excel_data(self, excel_data: Dict) -> Dict:
        """
        Merge custom scenarios with Excel scenarios.

        Args:
            excel_data: Dictionary of DataFrames from Excel (category -> DataFrame)

        Returns:
            Merged dictionary with custom scenarios added
        """
        import pandas as pd

        merged = excel_data.copy()

        # Group custom scenarios by category
        for category in self.get_all_categories():
            custom_scenarios = self.get_scenarios_by_category(category)

            if not custom_scenarios:
                continue

            # Convert to DataFrame format matching Excel structure
            custom_df = pd.DataFrame([
                {
                    'ID': s['id'],
                    'Client Question / Scenario': s['statement'],
                    'Coach Response 1': f"[From your transcript - practice your response]",
                    'Coach Response 2': '',
                    'Coach Response 3': '',
                    'Quality Score': s.get('quality_score', 5),
                    'Source': 'Real Transcript'
                }
                for s in custom_scenarios
            ])

            # Merge with existing category or create new
            if category in merged:
                merged[category] = pd.concat([merged[category], custom_df], ignore_index=True)
            else:
                merged[category] = custom_df

        return merged

    def delete_scenario(self, scenario_id: str) -> bool:
        """Delete a scenario by ID."""
        self.scenarios = [s for s in self.scenarios if s.get('id') != scenario_id]
        return self._save_scenarios()

    def update_scenario_category(self, scenario_id: str, new_category: str) -> bool:
        """Update the category of a scenario."""
        for scenario in self.scenarios:
            if scenario.get('id') == scenario_id:
                scenario['category'] = new_category
                return self._save_scenarios()
        return False


def display_extraction_interface(transcript: str, client, model_name: str):
    """
    Display UI for extracting and reviewing scenarios from transcript.

    Args:
        transcript: The coaching transcript text
        client: AI client instance
        model_name: Name of the model to use
    """
    st.markdown("---")
    st.subheader("📚 Extract Practice Scenarios")
    st.write("Extract client statements from this transcript to add to your practice library.")

    manager = ScenarioManager()

    # Show current library stats
    stats = manager.get_stats()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Scenarios", stats['total'])
    with col2:
        st.metric("Categories", len(stats['by_category']))
    with col3:
        st.metric("Avg Quality", stats['avg_quality'])

    if st.button("🔍 Extract Scenarios from This Transcript", key="extract_btn"):
        with st.spinner("Extracting client statements..."):
            # Extract statements
            statements = manager.extract_client_statements(transcript)

            if not statements:
                st.warning("No substantive client statements found in transcript.")
                return

            st.success(f"Found {len(statements)} potential scenarios!")

            # Store in session state for review
            st.session_state.extracted_scenarios = statements
            st.session_state.reviewing_scenarios = True
            st.rerun()  # Force refresh to show review interface

    # Review interface
    if st.session_state.get('reviewing_scenarios', False):
        st.markdown("---")
        st.subheader("✅ Review & Approve Scenarios")

        if st.button("🤖 Auto-Categorize with AI", key="categorize_btn"):
            with st.spinner("AI is categorizing scenarios..."):
                statements = st.session_state.extracted_scenarios
                categorized = manager.categorize_scenarios_with_ai(statements, client, model_name)
                st.session_state.categorized_scenarios = categorized
                st.success("Categorization complete!")
                st.rerun()  # Refresh to show categorized scenarios

        # Display scenarios for review
        if st.session_state.get('categorized_scenarios'):
            scenarios = st.session_state.categorized_scenarios

            # Filter by quality threshold
            quality_threshold = st.slider("Quality threshold", 1, 10, 6,
                                         help="Only show scenarios with quality score >= this value")

            filtered_scenarios = [s for s in scenarios if s.get('quality_score', 0) >= quality_threshold]

            st.write(f"Showing {len(filtered_scenarios)} scenarios (quality >= {quality_threshold})")

            for i, scenario in enumerate(filtered_scenarios):
                with st.expander(f"Scenario {i+1} - {scenario['category']} (Quality: {scenario['quality_score']}/10)"):
                    st.markdown(f"**Client Statement:**")
                    st.write(scenario['statement'])

                    if scenario.get('context'):
                        st.markdown(f"**Context (Coach's question):**")
                        st.info(scenario['context'])

                    st.markdown(f"**AI Assessment:** {scenario.get('reason', 'N/A')}")

                    col1, col2 = st.columns([1, 3])

                    with col1:
                        # Allow category override
                        new_category = st.selectbox(
                            "Category",
                            ["Career", "Leadership", "Relationship", "Self Improvement", "Value System"],
                            index=["Career", "Leadership", "Relationship", "Self Improvement", "Value System"].index(scenario['category']),
                            key=f"cat_{i}"
                        )

                    with col2:
                        if st.button(f"✅ Add to Practice Library", key=f"add_{i}"):
                            scenario['category'] = new_category
                            if manager.add_scenario(scenario):
                                st.success("Added to library!")
                                st.rerun()
                            else:
                                st.error("Failed to add scenario")

            # Bulk actions
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Approve All"):
                    count = 0
                    for scenario in filtered_scenarios:
                        if manager.add_scenario(scenario):
                            count += 1
                    st.success(f"Added {count} scenarios to library!")
                    st.session_state.reviewing_scenarios = False
                    st.rerun()

            with col2:
                if st.button("❌ Cancel"):
                    st.session_state.reviewing_scenarios = False
                    st.rerun()


def display_library_manager():
    """Display interface for managing the custom scenario library."""
    st.subheader("📚 Scenario Library Manager")

    manager = ScenarioManager()
    stats = manager.get_stats()

    if stats['total'] == 0:
        st.info("Your scenario library is empty. Analyze a transcript and extract scenarios to get started!")
        return

    # Stats overview
    st.markdown("### Library Statistics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Scenarios", stats['total'])
    with col2:
        st.metric("Categories", len(stats['by_category']))
    with col3:
        st.metric("Avg Quality", stats['avg_quality'])
    with col4:
        if stats['last_added']:
            last_date = stats['last_added'][:10]  # Just the date part
            st.metric("Last Added", last_date)

    # Category breakdown
    st.markdown("### Scenarios by Category")
    for category, count in sorted(stats['by_category'].items()):
        st.write(f"- **{category}**: {count} scenarios")

    # Export option
    st.markdown("---")
    st.markdown("### Export Options")

    if st.button("💾 Export Library as JSON"):
        with open(manager.storage_file, 'r') as f:
            data = f.read()

        st.download_button(
            label="Download custom_scenarios.json",
            data=data,
            file_name=f"custom_scenarios_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

    # Clear library option
    st.markdown("---")
    st.markdown("### Danger Zone")
    if st.button("🗑️ Clear All Custom Scenarios", type="secondary"):
        if st.button("⚠️ Confirm Delete All", type="primary"):
            manager.scenarios = []
            manager._save_scenarios()
            st.success("Library cleared!")
            st.rerun()
