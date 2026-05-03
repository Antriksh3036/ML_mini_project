import streamlit as st

st.set_page_config(page_title="Gym Data Science Project", layout="wide")

# Header Section with Logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("central_university_jammu_logo.png", width=150)
with col2:
    st.title(":red[Central University Of Jammu]")
    st.header(":orange[Mini Project: Gym Member Data Analysis & Prediction]")

st.markdown("---")

# Project Introduction
st.subheader("About the Project")
st.write("""
This application uses Machine Learning to analyze gym member data and predict various health and lifestyle outcomes. 
Using the **Gym Members Enhanced Dataset**, we have implemented several models:
* **Regression**: Predicting Calories Burned and Fat Percentage.
* **Classification**: Predicting Fitness Goals, Medical Conditions, and Lifestyle habits.
""")

# Collaborators Section
st.header(":blue[Collaborators]")
cols = st.columns(2)
with cols[0]:
    st.write(":violet-badge[Antriksh Baskotra  - 25BECSE18]")
    st.write(":violet-badge[Arun Kumar  - 25BECSE21]")
with cols[1]:
    st.write(":violet-badge[Nikhil Kumar  - 25BECSE46]")
    st.write(":violet-badge[Sidharth Sharma  - 25BECSE68]")

st.info("👈 Use the sidebar to navigate between different Prediction Models and Data Analysis.")

st.sidebar.write("Predict")

st.write("---")
st.header("📚 Quick Links")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Data Dictionary")
    st.write("""
    **Check the 'Dataframe' page to see:**
    - Original dataset with human-readable values
    - Preprocessed dataset with encoded numbers
    - Complete data dictionary mapping all encoded values
    
    **Example:**
    - Medical Condition `2` = **Hypertension**
    - Diet Type `1` = **High-Protein**
    - Smoking `1` = **Yes**
    """)
with col2:
    st.markdown("### 🎯 How to Use")
    st.write("""
    1. Start with **Data Analysis** to explore the dataset
    2. Use **Dataframe** page to understand the data encoding
    3. Visit specific analysis pages for predictions
    4. Hover over column names for quick reference
    """)
