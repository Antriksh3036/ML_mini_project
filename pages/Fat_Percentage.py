import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from constants import display_data_dictionary, get_code, get_labels

st.title("⚖️ Fat Percentage Predictor")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()
df = pd.read_csv("preprocessed_gym.csv")


features = ['Age', 'Gender', 'Height (m)','Weight (kg)', 'BMI', 'Avg_BPM', 'Medical_Condition', 
            'Workout_Frequency (days/week)','Experience_Level','Diet_Type','Protein_Intake (g/day)',
            'Sleep_Hours_Per_Day','Calories_Burned']
X = df[features]
y = df['Fat_Percentage']
model = LinearRegression().fit(X, y)

st.write("Enter your full physiological and workout profile:")

col1, col2 = st.columns(2)
inputs = []

# Map categorical columns
categorical_cols = {
    'Gender': get_labels('Gender'),
    'Medical_Condition': get_labels('Medical_Condition'),
    'Diet_Type': get_labels('Diet_Type'),
}

with col1:
    for i, feat in enumerate(features[:7]):
        if feat == 'Gender':
            gender_label = st.selectbox("Gender", categorical_cols['Gender'])
            val = int(get_code('Gender', gender_label))
        elif feat == 'Medical_Condition':
            med_label = st.selectbox("Medical Condition", categorical_cols['Medical_Condition'])
            val = int(get_code('Medical_Condition', med_label))
        else:
            val = st.number_input(f"Enter {feat}", value=float(df[feat].mean()))
        inputs.append(val)

with col2:
    for feat in features[7:]:
        if feat == 'Experience_Level':
            exp_label = st.selectbox("Experience Level", ['1', '2', '3'])
            val = int(exp_label)
        elif feat == 'Diet_Type':
            diet_label = st.selectbox("Diet Type", categorical_cols['Diet_Type'])
            val = int(get_code('Diet_Type', diet_label))
        else:
            val = st.number_input(f"Enter {feat}", value=float(df[feat].mean()))
        inputs.append(val)

if st.button("Estimate Fat Percentage"):
    res = model.predict([inputs])
    st.info(f"Predicted Fat Percentage: {res[0]:.2f}%")
