import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from constants import display_data_dictionary

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

inputs = []
for feat in features:
    val = st.number_input(f"Enter {feat}", value=float(df[feat].mean()))
    inputs.append(val)

if st.button("Estimate Fat Percentage"):
    res = model.predict([inputs])
    st.info(f"Predicted Fat Percentage: {res[0]:.2f}%")