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
        st.session_state.user_response = ""
        st.session_state.show_examples = False
    
    st.markdown("---")
    
    if st.session_state.current_scenario is not None:
        scenario = st.session_state.current_scenario
        
        st.markdown("### 💬 Client Scenario")
        st.info(f"**Scenario ID:** {scenario['ID']}")
        st.markdown(f"**Client says:**")
        st.write(f"_{scenario['Client Question / Scenario']}_")
        
        st.markdown("---")
        
        st.markdown("### ✍️ Your Coaching Response")
        user_response = st.text_area(
            "Type your coaching response here:",
            value=st.session_state.user_response,
            height=150,
            key="response_input",
            placeholder="Practice asking a powerful, open-ended question that helps the client explore their situation..."
        )
        st.session_state.user_response = user_response
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💡 Show Example PCC-Level Responses", use_container_width=True):
                st.session_state.show_examples = not st.session_state.show_examples
        
        with col2:
            if st.button("🔄 New Scenario", use_container_width=True):
                st.session_state.current_scenario = get_random_scenario(data[category])
                st.session_state.user_response = ""
                st.session_state.show_examples = False
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
    st.markdown("💡 **Future feature:** AI feedback on your response based on ICF competencies.")
