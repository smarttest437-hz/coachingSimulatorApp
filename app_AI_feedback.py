import streamlit as st
import pandas as pd
import random
from openai import OpenAI
from scenario_manager import ScenarioManager, display_extraction_interface, display_library_manager

def load_data(file_path, _custom_scenario_count=0):
    """
    Load all sheets from the Excel file and merge with custom scenarios.
    Note: Cache removed to ensure custom scenarios always load fresh.

    Args:
        file_path: Path to Excel file
        _custom_scenario_count: Number of custom scenarios (for cache invalidation)
    """
    try:
        excel_file = pd.ExcelFile(file_path)
        data = {}
        for sheet_name in excel_file.sheet_names:
            data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)

        # Merge with custom scenarios from JSON
        manager = ScenarioManager()
        if manager.get_stats()['total'] > 0:
            data = manager.merge_with_excel_data(data)

        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def get_random_scenario(df):
    """
    Get a random scenario from the dataframe.
    Gives 70% priority to custom scenarios (from real transcripts) if available.
    """
    if df is None or len(df) == 0:
        return None

    # Check if there are custom scenarios (identified by 'Source' column)
    if 'Source' in df.columns:
        custom_scenarios = df[df['Source'] == 'Real Transcript']

        if len(custom_scenarios) > 0:
            # 70% chance to select from custom scenarios
            if random.random() < 0.70:
                return custom_scenarios.sample(n=1).iloc[0]

    # Otherwise select from all scenarios (or 30% of the time even if custom exist)
    return df.sample(n=1).iloc[0]

def get_ai_client(llm_provider):
    """Get the appropriate AI client based on provider selection."""
    if llm_provider == "Ollama (Free, Local)":
        # Ollama uses OpenAI-compatible API
        return OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"  # Ollama doesn't need a real API key
        )
    else:
        # OpenAI - Check both secrets and environment variables
        import os
        api_key = None

        # Try secrets first (local development)
        if "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
        # Fallback to environment variable (for Render/production)
        elif "OPENAI_API_KEY" in os.environ:
            api_key = os.environ["OPENAI_API_KEY"]

        if not api_key:
            st.error("⚠️ OpenAI API key not found. Please add it to .streamlit/secrets.toml or set OPENAI_API_KEY environment variable.")
            return None

        return OpenAI(api_key=api_key)

# --- Setup ---
st.set_page_config(page_title="Coaching Practice Simulator", page_icon="💬")

st.title("💬 Coaching Practice Simulator (ICF PCC-Level)")

st.write("""
Welcome to your coaching practice simulator!
You'll see a **client scenario**, type your **coaching response**, and receive **AI-powered ICF PCC-style feedback**.
""")

# --- LLM Provider Selection (Sidebar) ---
with st.sidebar:
    st.header("⚙️ Settings")

    llm_provider = st.radio(
        "🤖 AI Provider:",
        ["Ollama (Free, Local)", "OpenAI (Paid)"],
        help="Ollama runs locally on your computer (free). OpenAI requires API key and credits."
    )

    if llm_provider == "Ollama (Free, Local)":
        model_name = st.selectbox(
            "Model:",
            ["llama3.2:3b (Fast, Low RAM)", "llama3.1:8b (Balanced)", "mistral:7b", "llama3.1:70b (Slow, High Quality)"],
            help="Recommended: llama3.2:3b for best speed on 16GB RAM"
        )
        # Map display names to actual model names
        model_mapping = {
            "llama3.2:3b (Fast, Low RAM)": "llama3.2:3b",
            "llama3.1:8b (Balanced)": "llama3.1:8b",
            "mistral:7b": "mistral:7b",
            "llama3.1:70b (Slow, High Quality)": "llama3.1:70b"
        }
        model_name = model_mapping.get(model_name, "llama3.2:3b")
        st.info("💡 **Using Ollama (Free)**\n\nMake sure Ollama is running:\n```\nollama serve\n```")
    else:
        model_name = "gpt-4o-mini"
        st.info("💳 **Using OpenAI (Paid)**\n\nRequires API key in `.streamlit/secrets.toml`")

    st.markdown("---")

    # Library Manager in sidebar
    st.header("📚 Scenario Library")
    manager = ScenarioManager()
    stats = manager.get_stats()

    if stats['total'] > 0:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total", stats['total'])
        with col2:
            st.metric("Quality", stats['avg_quality'])

        with st.expander("📊 Library Details"):
            st.write(f"**Categories:** {len(stats['by_category'])}")
            for category, count in sorted(stats['by_category'].items()):
                st.write(f"- {category}: {count}")

        if st.button("🔧 Manage Library"):
            st.session_state.show_library_manager = True
    else:
        st.info("💡 Analyze a transcript and extract scenarios to build your library!")

# Initialize AI client
client = get_ai_client(llm_provider)
if client is None:
    st.stop()

# --- Practice Mode Selection ---
practice_mode = st.radio(
    "🎯 Select Practice Mode:",
    ["General Coaching Practice", "Bottom-Lining Practice", "Transcript Analysis"],
    horizontal=True
)

if practice_mode == "Bottom-Lining Practice":
    st.info("""
    **💡 Bottom-Lining Focus:**
    Capture the essence of what the client said in 1-2 concise sentences.
    - Start with phrases like: "So what I'm hearing is...", "At the heart of this is...", "It sounds like..."
    - Stay client-centered (reflect their words, not your interpretation)
    - Be concise and clear
    """)
elif practice_mode == "Transcript Analysis":
    st.info("""
    **📄 Transcript Analysis:**
    Upload or paste a coaching session transcript for comprehensive ACC-level analysis.
    - We'll evaluate ICF competencies, questions, tone, acknowledgment, observations, and clean language
    - Identify missed opportunities to evoke awareness
    - Provide actionable feedback for improvement
    """)
else:
    st.info("**Practice any coaching response** and receive comprehensive ICF feedback.")

# --- Transcript Analysis Mode ---
if practice_mode == "Transcript Analysis":
    st.markdown("---")
    st.subheader("📤 Upload or Paste Your Coaching Transcript")

    # File upload option
    uploaded_file = st.file_uploader(
        "Upload transcript file (.txt)",
        type=['txt'],
        help="Upload a plain text file containing your coaching session transcript"
    )

    # Text area option
    st.markdown("**Or paste your transcript directly:**")
    transcript_text = st.text_area(
        "Coaching Transcript",
        placeholder="""Example format:
Coach: What would you like to focus on today?
Client: I've been struggling with work-life balance.
Coach: Tell me more about that.
Client: I work late every night and feel guilty about missing time with my family.
...""",
        height=300,
        help="Format: Each line should start with 'Coach:' or 'Client:' to identify speakers"
    )

    # Determine which input to use
    transcript_content = None
    if uploaded_file is not None:
        transcript_content = uploaded_file.read().decode("utf-8")
        st.success(f"✅ File uploaded: {uploaded_file.name} ({len(transcript_content)} characters)")
    elif transcript_text.strip():
        transcript_content = transcript_text

    # Show action buttons if transcript is available
    if transcript_content and transcript_content.strip():
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔍 Full Analysis", key="analyze_transcript", use_container_width=True,
                        help="Complete 10-point ICF analysis + scenario extraction"):
                st.session_state.analysis_mode = "full"

        with col2:
            if st.button("⚡ Quick Extract", key="quick_extract", use_container_width=True,
                        help="Skip analysis, go straight to scenario extraction"):
                st.session_state.analysis_mode = "quick"
                st.rerun()

    # Quick Extract path
    if transcript_content and st.session_state.get('analysis_mode') == 'quick':
        st.markdown("---")
        st.subheader("⚡ Quick Scenario Extraction")
        st.info("📋 Skipping full analysis - extracting scenarios directly...")

        # Display extraction interface immediately
        display_extraction_interface(transcript_content, client, model_name)

        # Back button
        if st.button("← Back to Upload"):
            st.session_state.analysis_mode = None
            st.rerun()

    # Full Analysis path
    elif transcript_content and st.session_state.get('analysis_mode') == 'full':
        if not transcript_content or not transcript_content.strip():
            st.warning("⚠️ Please upload a file or paste transcript text first.")
        else:
            with st.spinner("🔄 Analyzing your coaching session with ICF ACC-level criteria..."):
                # Parse transcript to count turns
                lines = [line.strip() for line in transcript_content.split('\n') if line.strip()]
                coach_turns = [line for line in lines if line.lower().startswith('coach:')]
                client_turns = [line for line in lines if line.lower().startswith('client:')]

                st.info(f"📊 Session overview: {len(coach_turns)} coach responses, {len(client_turns)} client statements")

                # Create comprehensive analysis prompt
                prompt = f"""
You are an ICF ACC-level mentor coach evaluating a complete coaching session transcript.

**TRANSCRIPT:**
{transcript_content}

**EVALUATION FRAMEWORK:**
Please provide a comprehensive analysis structured as follows:

**1. ACC-Level Competencies Demonstrated:**
Identify which ICF ACC competencies were demonstrated in this session:
- Establishes and Maintains Agreements
- Cultivates Trust and Safety
- Maintains Presence
- Listens Actively
- Evokes Awareness
- Facilitates Client Growth
- Embodies a Coaching Mindset

For each competency demonstrated, provide specific examples from the transcript.

**2. Missed Opportunities to Evoke Awareness:**
Identify 3-5 specific moments where the coach could have asked a more powerful question or made an observation that would have deepened the client's awareness. For each:
- Quote the coach's actual statement
- Explain what opportunity was missed
- Provide an example of what could have been said instead

**3. Questions Analysis:**
Evaluate the quality of questions asked:
- How many were open vs. closed questions?
- Were questions powerful and evocative, or leading/directive?
- Did questions help the client explore deeply or stay surface-level?
- Provide 2-3 examples of strong questions and 2-3 that could be improved

**4. Tone and Attunement:**
Assess how well the coach attuned to the client:
- Did the coach match the client's energy and pace?
- Were there moments of deep empathy and understanding?
- Did the coach seem present and fully engaged?
- Any moments where attunement could have been stronger?

**5. Acknowledgment:**
Evaluate how the coach acknowledged the client:
- Were there genuine moments of acknowledgment (not just praise)?
- Did acknowledgments recognize the client's strengths, growth, or insights?
- Provide examples of effective acknowledgments or missed opportunities

**6. Observations:**
Assess the coach's use of observations:
- Did the coach share observations about what they noticed?
- Were observations offered tentatively as gifts, not judgments?
- Examples of strong observations or missed opportunities to share observations

**7. Clean Language:**
Evaluate the coach's use of the client's own language:
- Did the coach use the client's words and metaphors, or impose their own?
- Were there moments of interpretation or assumption?
- Examples of good clean language usage and areas for improvement

**8. Overall Strengths:**
Summarize the top 3 strengths demonstrated in this session.

**9. Priority Development Areas:**
Identify the top 3 areas for focused development to progress toward PCC level.

**10. Action Steps:**
Provide 3 specific, actionable practices the coach can implement in their next session.

Keep tone encouraging, specific, and developmental. Use examples from the actual transcript to illustrate points.
"""

                # Call AI API
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                ai_feedback = response.choices[0].message.content

                st.markdown("---")
                st.markdown("## 📋 Comprehensive Coaching Session Analysis")
                st.markdown(ai_feedback)

                # Add download button for feedback
                st.markdown("---")
                st.download_button(
                    label="💾 Download Analysis",
                    data=ai_feedback,
                    file_name="coaching_transcript_analysis.txt",
                    mime="text/plain"
                )

                st.success("✨ Analysis complete! Review the feedback above and consider the action steps for your next session.")

                # Add scenario extraction interface
                display_extraction_interface(transcript_content, client, model_name)

                # Back button
                st.markdown("---")
                if st.button("← Start New Analysis"):
                    st.session_state.analysis_mode = None
                    st.session_state.reviewing_scenarios = False
                    st.session_state.extracted_scenarios = None
                    st.session_state.categorized_scenarios = None
                    st.rerun()

# --- Dynamic Scenario (only for General and Bottom-Lining modes) ---
if practice_mode != "Transcript Analysis":
    file_path = "Coach_Training_Scenarios_ICF_PCC.xlsx"
    # Pass custom scenario count to invalidate cache when scenarios change
    custom_count = ScenarioManager().get_stats()['total']
    data = load_data(file_path, _custom_scenario_count=custom_count)

    if 'scenario_counter' not in st.session_state:
        st.session_state.scenario_counter = 0

    if data is None:
        st.warning("⚠️ Please ensure 'Coach_Training_Scenarios_ICF_PCC.xlsx' is in the same directory as app.py")
        st.info("The Excel file should contain sheets for: Career, Leadership, Relationship, Self Improvement, and Value System")
    else:
        categories = list(data.keys())

        st.markdown("---")

        category = st.selectbox("📂 Select a Category", categories)

        # Debug info: Show scenario counts
        if category in data:
            total = len(data[category])
            custom = len(data[category][data[category]['Source'] == 'Real Transcript']) if 'Source' in data[category].columns else 0
            st.caption(f"📊 {total} total scenarios ({custom} custom, {total-custom} from library)")

        if 'current_scenario' not in st.session_state or st.session_state.get('current_category') != category:
            st.session_state.current_category = category
            st.session_state.current_scenario = get_random_scenario(data[category])
            st.session_state.show_examples = False
            st.session_state.scenario_counter += 1

        st.markdown("---")

        if st.session_state.current_scenario is not None:
            scenario = st.session_state.current_scenario

            st.subheader("🧭 Client Scenario")

            # Show badge if custom scenario
            is_custom = scenario.get('Source') == 'Real Transcript'
            if is_custom:
                st.success("⭐ **Custom Scenario** (from your real transcript!)")

            col1, col2 = st.columns([3, 1])
            with col1:
                st.info(f"**Scenario ID:** {scenario['ID']}")
            with col2:
                if st.button("🔄 New Scenario"):
                    st.session_state.current_scenario = get_random_scenario(data[category])
                    st.session_state.show_examples = False
                    st.rerun()

            st.markdown(f"**Client says:**")
            st.write(f"_{scenario['Client Question / Scenario']}_")

# --- User Input (for General and Bottom-Lining modes only) ---
if practice_mode != "Transcript Analysis":
    if practice_mode == "Bottom-Lining Practice":
        coach_input = st.text_area(
            "Your bottom-lining response:",
            placeholder="Type your bottom-line statement (1-2 sentences)...",
            help="Aim for 20-40 words to keep it concise"
        )
        if coach_input:
            word_count = len(coach_input.split())
            char_count = len(coach_input)
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"📝 Words: {word_count}")
            with col2:
                if word_count > 50:
                    st.caption(f"⚠️ Characters: {char_count} (Consider shortening)")
                else:
                    st.caption(f"✅ Characters: {char_count}")
    else:
        coach_input = st.text_area("Your coaching response:", placeholder="Type what you would say as a coach...")

    # --- Feedback Button ---
    if st.button("✨ Get Feedback"):
        if not coach_input.strip():
            st.warning("Please enter your coaching response first.")
        else:
            with st.spinner("Analyzing your response with ICF criteria..."):
                if practice_mode == "Bottom-Lining Practice":
                    prompt = f"""
You are an ICF PCC-level mentor coach evaluating a trainee coach's BOTTOM-LINING skill.

Client says: "{scenario['Client Question / Scenario']}"
Coach's bottom-line statement: "{coach_input}"

Bottom-lining is the skill of distilling a client's complex or lengthy narrative into its essence in 1-2 concise sentences.

Please evaluate specifically for bottom-lining effectiveness:

**Bottom-Lining Assessment:**
- Did the coach capture the CORE issue/theme? (not just repeat details)
- Was it concise (1-2 sentences, ideally 20-40 words)?
- Did it stay client-centered (their words/perspective, not coach's interpretation)?
- Did it avoid adding advice or questions?

**What Worked:**
- [Specific strengths in this bottom-line attempt]

**Opportunities for Growth:**
- [Specific suggestions to improve the bottom-lining]

**Example ACC-Level Bottom-Line:**
Provide one bottom-line statement at ACC level (captures main point, somewhat wordy).

**Example PCC-Level Bottom-Line:**
Provide one bottom-line statement at PCC level (captures essence elegantly, client-centered, concise).

Keep tone encouraging and developmental.
"""
                else:
                    prompt = f"""
You are an ICF PCC-level mentor coach evaluating a trainee coach's response.
Client says: "{scenario['Client Question / Scenario']}"
Coach says: "{coach_input}"

Please evaluate the coach's response using the ICF PCC markers. Provide feedback in this format:

**Competencies Demonstrated:**
- [List them]

**Opportunities for Growth:**
- [List them]

**Observations:**
- [3 bullet points summarizing strengths and areas to refine]

**Example ACC-Level Response:**
Provide one improved response that demonstrates a ACC-level question or reflection.

**Example PCC-Level Response:**
Provide one improved response that demonstrates a PCC-level question or reflection.

Keep tone encouraging, developmental, and aligned with ICF standards.
"""

                # --- Call the AI model ---
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                ai_feedback = response.choices[0].message.content
                st.markdown("### 📊 AI Feedback")
                st.markdown(ai_feedback)

                if practice_mode == "Bottom-Lining Practice":
                    st.success("💡 Reflect: Did you capture the essence? Could you make it more concise?")
                else:
                    st.success("💡 Reflect: What would you do differently next time?")

# --- Sidebar with Tips ---
with st.sidebar:
    st.header("📚 Coaching Resources")

    if practice_mode == "Bottom-Lining Practice":
        st.markdown("""
        ### What is Bottom-Lining?
        Distilling a client's complex story into its essence - the core issue, feeling, or theme.

        ### Key Principles:
        - **Be concise**: 1-2 sentences
        - **Stay client-centered**: Use their language
        - **Capture essence**: Not just details
        - **No interpretation**: Reflect, don't analyze

        ### Starter Phrases:
        - "So what I'm hearing is..."
        - "At the heart of this is..."
        - "It sounds like..."
        - "The core challenge seems to be..."
        - "What you're really grappling with is..."

        ### Example:
        **Client:** "I've been at this company for 5 years, and I love my team, but lately I've been feeling like I'm not growing. I see other opportunities, but I'm scared to leave. What if I fail? But what if I stay and regret it?"

        **ACC Bottom-Line:** "You're feeling stuck between staying in a comfortable situation and taking a risk for growth."

        **PCC Bottom-Line:** "You're torn between the safety of what you know and the pull toward growth."
        """)

    elif practice_mode == "Transcript Analysis":
        st.markdown("""
        ### Transcript Analysis Guidelines

        **Format Requirements:**
        - Each line should identify the speaker: "Coach:" or "Client:"
        - Keep the natural flow of the conversation
        - Include all interactions, not just highlights

        **What Gets Analyzed:**
        - **ACC Competencies**: All 8 core ICF competencies
        - **Evokes Awareness**: Missed opportunities for deeper exploration
        - **Questions**: Quality, open vs. closed, powerful vs. leading
        - **Tone/Attunement**: Empathy, presence, matching client energy
        - **Acknowledgment**: Recognition of client strengths and insights
        - **Observations**: What the coach noticed and shared
        - **Clean Language**: Using client's words vs. coach's interpretation

        **Example Format:**
        ```
        Coach: What would you like to focus on today?
        Client: I'm struggling with my team dynamics.
        Coach: Tell me more about that.
        Client: My team doesn't communicate well.
        Coach: What specifically do you notice?
        ```

        **Benefits:**
        - Comprehensive session review
        - Specific examples from your work
        - Actionable development areas
        - Track progress over multiple sessions
        """)

    else:
        st.markdown("""
        ### ICF Core Competencies

        **ACC-Level Focus:**
        1. Establishes and Maintains Agreements
        2. Cultivates Trust and Safety
        3. Maintains Presence
        4. Listens Actively
        5. Evokes Awareness
        6. Facilitates Client Growth
        7. Embodies a Coaching Mindset

        ### Powerful Question Starters:
        - "What do you notice about...?"
        - "How does that connect to...?"
        - "What would be possible if...?"
        - "What's important about that?"
        - "What are you learning?"

        ### Active Listening Signals:
        - Reflecting key words
        - Summarizing essence
        - Noticing patterns
        - Acknowledging emotions
        - Staying curious
        """)

# --- Library Manager Section ---
if st.session_state.get('show_library_manager', False):
    st.markdown("---")
    display_library_manager()

    if st.button("← Back to Practice"):
        st.session_state.show_library_manager = False
        st.rerun()

# Dynamic "Powered by" text based on selected LLM
if llm_provider == "Ollama (Free, Local)":
    st.caption(f"Powered by Ollama ({model_name}) + ICF Coaching Framework")
else:
    st.caption(f"Powered by OpenAI ({model_name}) + ICF Coaching Framework")
