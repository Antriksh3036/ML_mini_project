# Data Dictionary - Categorical Mappings
# This file contains all the categorical encoding mappings used in the preprocessing

CATEGORICAL_MAPPINGS = {
    "Gender": {"0": "Female", "1": "Male"},
    "Workout_Type": {"0": "Cardio", "1": "HIIT", "2": "Strength", "3": "Yoga"},
    "Fitness_Goal": {"0": "Endurance", "1": "General Fitness", "2": "Muscle Gain", "3": "Weight Loss"},
    "Preferred_Workout_Time": {"0": "Afternoon", "1": "Evening", "2": "Morning", "3": "Night"},
    "Work_Type": {"0": "Active", "1": "Mixed", "2": "Sedentary"},
    "Income_Level": {"0": "High", "1": "Low", "2": "Middle"},
    "Diet_Type": {"0": "Balanced", "1": "High-Protein", "2": "Vegan", "3": "Vegetarian"},
    "Smoking": {"0": "No", "1": "Yes"},
    "Alcohol_Consumption": {"0": "None", "1": "Occasional", "2": "Regular"},
    "Medical_Condition": {"0": "Diabetes", "1": "High Cholesterol", "2": "Hypertension", "3": "None", "4": "Obesity"},
}

# Helper function to get meaning from code
def get_meaning(column, code):
    """
    Get the meaning of an encoded value
    
    Args:
        column (str): Column name
        code (str or int): Encoded value
        
    Returns:
        str: Meaning of the encoded value, or "Unknown" if not found
    """
    if column in CATEGORICAL_MAPPINGS:
        return CATEGORICAL_MAPPINGS[column].get(str(code), "Unknown")
    return "Unknown"


# Helper function to get code from meaning
def get_code(column, meaning):
    """
    Get the encoded value from meaning
    
    Args:
        column (str): Column name
        meaning (str): Human-readable meaning
        
    Returns:
        str: Encoded value, or "Unknown" if not found
    """
    if column in CATEGORICAL_MAPPINGS:
        for code, val in CATEGORICAL_MAPPINGS[column].items():
            if val.lower() == meaning.lower():
                return code
    return "Unknown"


# Helper function to get all labels for a column
def get_labels(column):
    """
    Get all human-readable labels for a column
    
    Args:
        column (str): Column name
        
    Returns:
        list: List of human-readable labels, or empty list if not found
    """
    if column in CATEGORICAL_MAPPINGS:
        return list(CATEGORICAL_MAPPINGS[column].values())
    return []


# Helper function to display data dictionary in Streamlit
def display_data_dictionary():
    """Display the data dictionary in a Streamlit app"""
    import streamlit as st
    
    st.write("---")
    st.header(":orange[📚 Data Dictionary - Categorical Mappings]")
    st.info("Use this guide to understand what each encoded number means for categorical columns.")
    
    for column, mapping in CATEGORICAL_MAPPINGS.items():
        with st.expander(f"🏷️ {column}"):
            cols = st.columns(2)
            with cols[0]:
                st.write("**Code**")
                for code in mapping.keys():
                    st.write(f"`{code}`")
            with cols[1]:
                st.write("**Meaning**")
                for meaning in mapping.values():
                    st.write(meaning)
