import streamlit as st
import pandas as pd
import random

@st.cache_data
def load_data(file_path):
    """Load all sheets from the Excel file."""
    try:
        excel_file = pd.ExcelFile(file_path)
        data = {}
        for sheet_name in excel_file.sheet_names:
            data[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def get_random_scenario(df):
    """Get a random scenario from the dataframe."""
    if df is not None and len(df) > 0:
        return df.sample(n=1).iloc[0]
    return None

st.set_page_config(page_title="Coaching Practice Simulator", page_icon="🎯")

st.title("🎯 Coaching Practice Simulator")

file_path = "Coach_Training_Scenarios_ICF_PCC.xlsx"
data = load_data(file_path)

if 'scenario_counter' not in st.session_state:
    st.session_state.scenario_counter = 0

if data is None:
    st.warning("⚠️ Please ensure 'Coach_Training_Scenarios_ICF_PCC.xlsx' is in the same directory as app.py")
    st.info("The Excel file should contain sheets for: Career, Leadership, Relationship, Self Improvement, and Value System")
else:
    categories = list(data.keys())
    
    st.markdown("---")
    
    category = st.selectbox("📂 Select a Category", categories)
    
    if 'current_scenario' not in st.session_state or st.session_state.get('current_category') != category:
        st.session_state.current_category = category
        st.session_state.current_scenario = get_random_scenario(data[category])
        st.session_state.show_examples = False
        st.session_state.scenario_counter += 1
    
    st.markdown("---")
    
    if st.session_state.current_scenario is not None:
        scenario = st.session_state.current_scenario
        
        st.markdown("### 💬 Client Scenario")
        st.info(f"**Scenario ID:** {scenario['ID']}")
        st.markdown(f"**Client says:**")
        st.write(f"_{scenario['Client Question / Scenario']}_")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💡 Show Example PCC-Level Responses", use_container_width=True):
                st.session_state.show_examples = not st.session_state.show_examples
        
        with col2:
            if st.button("🔄 New Scenario", use_container_width=True):
                st.session_state.current_scenario = get_random_scenario(data[category])
                st.session_state.show_examples = False
                st.session_state.scenario_counter += 1
                st.rerun()
        
        if st.session_state.show_examples:
            st.markdown("---")
            st.markdown("### 📚 Example PCC-Level Responses")
            
            st.markdown("**Example Response 1:**")
            st.success(scenario['Coach Response 1'])
            
            st.markdown("**Example Response 2:**")
            st.success(scenario['Coach Response 2'])
            
            st.markdown("**Example Response 3:**")
            st.success(scenario['Coach Response 3'])
    else:
        st.error("No scenarios available in this category.")
    
    st.markdown("---")
    # --- Simple rule-based ICF feedback engine ---
    competency_map = {
        "Evokes Awareness": ["what", "how", "could", "might", "imagine", "notice"],
        "Active Listening": ["I hear", "you said", "it sounds", "you mentioned"],
        "Maintains Presence": ["let’s pause", "take a moment", "what are you feeling"],
        "Cultivates Trust & Safety": ["thank you for sharing", "that sounds hard", "I appreciate your honesty"],
        "Facilitates Growth": ["next step", "apply", "move forward", "experiment", "commit"]
    }

    # --- Feedback section ---
    def evaluate_icf_feedback(coach_input):
    # This function should probably have access to `competency_map`
    # which should be defined elsewhere in your global scope.
        coach_input_lower = coach_input.lower()
        matched = [c for c, kws in competency_map.items() if any(k in coach_input_lower for k in kws)]
        if not coach_input.strip():
            return "Please enter your coaching response to get feedback."
        if matched:
            return f"✅ Your response aligns with: {', '.join(matched)}.\n\nGreat use of curiosity and reflection!"
        return "🤔 I didn’t detect clear ICF-aligned phrasing.\nTry using more open-ended or awareness-based questions (e.g., starting with *what* or *how*)."

    # --- Main app layout and logic ---
    # ✅ Define `coach_input` in the main script body using a widget.
    # This ensures it is always defined and available during each rerun.
    coach_input = st.text_area("✍️ Enter your coaching response here:")

    # --- Feedback section ---
    if st.button("💬 Get Feedback"):
        # The button logic now correctly uses the globally available `coach_input`
        feedback = evaluate_icf_feedback(coach_input)
        st.markdown("### 🧠 Feedback")
        st.success(feedback)
