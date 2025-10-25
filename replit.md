# Overview

This is a Coaching Practice Simulator application built with Streamlit that helps coaches practice their skills by presenting randomized coaching scenarios. The application loads coaching scenarios from an Excel file organized by different coaching categories (Career, Leadership, Relationship, Self Improvement, and Value System) following ICF PCC standards. Users can select a category and work through randomly selected scenarios to practice their coaching responses.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture

**Technology**: Streamlit-based web application
- **Rationale**: Streamlit provides a rapid development framework for data-centric applications with minimal frontend code
- **Approach**: Single-page application with interactive widgets for category selection and scenario display
- **State Management**: Uses Streamlit's session_state for maintaining current scenario, category, and user interaction state across reruns

## Data Architecture

**Data Storage**: Excel-based static data store
- **File Structure**: Multi-sheet Excel workbook (`Coach_Training_Scenarios_ICF_PCC.xlsx`)
- **Organization**: Each sheet represents a coaching category (Career, Leadership, Relationship, Self Improvement, Value System)
- **Rationale**: Excel format chosen for easy content management by non-technical users (likely coaches or training administrators)
- **Caching Strategy**: `@st.cache_data` decorator used on data loading function to prevent redundant file reads

## Application Logic

**Scenario Selection**: Random sampling mechanism
- **Method**: Uses pandas DataFrame.sample() to select random scenarios from chosen category
- **Session Persistence**: Current scenario stored in session state to maintain consistency during user interaction
- **Category Switching**: Automatically generates new scenario when user changes category

## Error Handling

**File Loading**: Graceful degradation with user-friendly error messages
- **Missing File**: Displays warning with instructions if Excel file not found
- **Loading Errors**: Generic error handling with error message display
- **Empty Data**: Validation checks for empty dataframes before scenario selection

# External Dependencies

## Python Libraries

**Streamlit** (primary framework)
- Purpose: Web application framework and UI components
- Usage: Page configuration, widgets (selectbox), layout (markdown), and session state management

**Pandas**
- Purpose: Data manipulation and Excel file processing
- Usage: Reading multi-sheet Excel files, dataframe operations, and random sampling

**Random**
- Purpose: Standard library for randomization utilities
- Note: Currently imported but not actively used (pandas.sample() handles randomization)

## Data Dependencies

**Excel File**: `Coach_Training_Scenarios_ICF_PCC.xlsx`
- Location: Expected in same directory as app.py
- Format: Multi-sheet Excel workbook with predefined category sheets
- Content: ICF PCC standard coaching scenarios organized by category
- Management: External content file that can be updated independently of application code