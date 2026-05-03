import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from constants import get_code, get_labels, display_data_dictionary

st.title("🔥 Calories Burned Predictor")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()


df = pd.read_csv("preprocessed_gym.csv")
X = df[['Age', 'Weight (kg)', 'BMI', 'Avg_BPM', 'Session_Duration (hours)', 'Workout_Type','Fitness_Goal','Sleep_Hours_Per_Day']]
y = df['Calories_Burned']

model = LinearRegression()
model.fit(X, y) 

with st.expander("Input Data:"):
    st.header("Enter Your Metrics")
    age = st.number_input("Age", 18, 100, 25)
    weight = st.number_input("Weight (kg)", 40, 150, 70)
    bmi = st.number_input("BMI", 10.0, 50.0, 22.5)
    bpm = st.slider("Average BPM", 60, 200, 120)
    duration = st.slider("Session Duration (hours)", 0.5, 4.0, 1.0)
    w_type_label = st.selectbox("Workout Type", get_labels("Workout_Type"))
    w_type = int(get_code("Workout_Type", w_type_label))
    goal_label = st.selectbox("Fitness Goal", get_labels("Fitness_Goal"))
    goal = int(get_code("Fitness_Goal", goal_label))
    sleep = st.slider("Sleep Hours", 4, 12, 7)

if st.button("Predict Calories"):
    input_data = [[age, weight, bmi, bpm, duration, w_type, goal, sleep]]
    prediction = model.predict(input_data)
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f} kcal")