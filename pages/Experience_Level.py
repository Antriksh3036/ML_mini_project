import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from constants import display_data_dictionary

st.title("🏆 Gym Experience Level")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()
df = pd.read_csv("preprocessed_gym.csv")


X = df[['Membership_Duration (months)', 'Workout_Frequency (days/week)', 'Session_Duration (hours)', 'Calories_Burned', 'Fat_Percentage', 'BMI', 'Age', 'Rest_Days_Per_Week']]
y = df['Experience_Level']
model = LogisticRegression().fit(X, y)

st.subheader("Training Metrics & Profile")
col1, col2 = st.columns(2)
with col1:
    mem = st.number_input("Membership (Months)", 0, 120, 12)
    freq = st.slider("Frequency (Days/Week)", 1, 7, 4)
    dur = st.number_input("Session Duration (Hours)", 0.5, 4.0, 1.0)
    cal = st.number_input("Calories Burned/Session", 100, 2000, 500)
with col2:
    fat = st.number_input("Fat Percentage", 5, 50, 20)
    bmi = st.number_input("BMI", 15.0, 45.0, 23.0)
    age = st.number_input("Age", 18, 90, 25)
    rest = st.slider("Rest Days/Week", 0, 6, 2)

if st.button("Determine Experience Level"):
    res = model.predict([[mem, freq, dur, cal, fat, bmi, age, rest]])
    st.success(f"Experience Level: {res[0]}")