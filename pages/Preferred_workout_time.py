import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.title("⏰ Best Workout Time Predictor")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()
df = pd.read_csv("preprocessed_gym.csv")

X = df[['Age', 'Avg_BPM', 'Sleep_Hours_Per_Day', 'Experience_Level','Income_Level','Workout_Frequency (days/week)','Rest_Days_Per_Week','Medical_Condition','Membership_Duration (months)']]
y = df['Preferred_Workout_Time']
model = LogisticRegression().fit(X, y)

st.write("Find out when you are most likely to train:")
age = st.number_input("Age", 18, 80, 25)
bpm = st.number_input("Avg BPM", 50, 180, 70)
sleep = st.slider("Sleep Hours", 4, 12, 8)
experience = st.number_input("Experience Level (ID)", 0, 3, 1)
income_label = st.selectbox("Income Level", get_labels("Income_Level"))
income = int(get_code("Income_Level", income_label))
freq = st.slider("Workout Frequency", 1, 7, 4)
rest = st.slider("Rest Days", 0, 6, 1)
med_label = st.selectbox("Medical Condition", get_labels("Medical_Condition"))
med = int(get_code("Medical_Condition", med_label))
mem = st.number_input("Membership Months", 1, 60, 6)

if st.button("Predict Optimal Time"):
    data = [age, bpm, sleep, experience, income, freq, rest, med, mem]
    res = model.predict([data])
    time_slot = get_meaning("Preferred_Workout_Time", str(int(res[0])))
    st.success(f"Predicted Best Time to Workout: **{time_slot}** (Code: {int(res[0])})") 
