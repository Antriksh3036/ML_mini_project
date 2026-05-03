import streamlit as st 
import pandas as pd
from constants import display_data_dictionary, CATEGORICAL_MAPPINGS

df_real = pd.read_csv("gym_members_enhanced_v2.csv")
df_pre = pd.read_csv("preprocessed_gym.csv")

st.title(":red[DataFrame]")

st.header(":orange[Original DataFrame]")
st.dataframe(df_real)

st.write("---")

st.header(":orange[DataFrame after Preprocessing]")
st.dataframe(df_pre)

# Display data dictionary using helper function
display_data_dictionary()

# Create a reference table
st.write("---")
st.subheader("📋 Quick Reference Table")
all_mappings_data = []
for column, mapping in CATEGORICAL_MAPPINGS.items():
    for code, meaning in mapping.items():
        all_mappings_data.append({"Column": column, "Code": code, "Meaning": meaning})

mapping_df = pd.DataFrame(all_mappings_data)
st.dataframe(mapping_df, use_container_width=True)

# Download button
csv = mapping_df.to_csv(index=False)
st.download_button(
    label="📥 Download Data Dictionary as CSV",
    data=csv,
    file_name="data_dictionary.csv",
    mime="text/csv"
)

with st.expander("Code for preprocessing"):
    st.code('''
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

ohe = OneHotEncoder(sparse_output=False).set_output(transform='pandas')
le = LabelEncoder()


df = pd.read_csv("gym_members_enhanced_v2.csv")
df_copy = df.copy()

#Label encoding for gender
df_copy['Gender'] = le.fit_transform(df_copy['Gender'])

#Label encoding for workout type
df_copy['Workout_Type'] = le.fit_transform(df_copy['Workout_Type'])

#Label encoding for Fitness Goal
df_copy['Fitness_Goal'] = le.fit_transform(df_copy['Fitness_Goal'])

#Label encoding for Preferred Workout Time
df_copy['Preferred_Workout_Time'] = le.fit_transform(df_copy['Preferred_Workout_Time'])

#Label encoding for Work Type
df_copy['Work_Type'] = le.fit_transform(df_copy['Work_Type'])

#Label encoding for Income Level
df_copy['Income_Level'] = le.fit_transform(df_copy['Income_Level'])

#Label encoding for Diet Type
df_copy['Diet_Type'] = le.fit_transform(df_copy['Diet_Type'])

#Label encoding for gender
df_copy['Smoking'] = le.fit_transform(df_copy['Smoking'])

#Label encoding for Alcohol Consumption
df_copy['Alcohol_Consumption'] = le.fit_transform(df_copy['Alcohol_Consumption'])

#Label encoding for Medical Condition
df_copy['Medical_Condition'] = le.fit_transform(df_copy['Medical_Condition'])

print(df_copy.head())

df_copy.to_csv('preprocessed_gym.csv',index=False)
    
    ''')