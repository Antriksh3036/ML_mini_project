import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.title("🍺 Alcohol Consumption Predictor")

# Data Dictionary Reference
with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()
df = pd.read_csv("preprocessed_gym.csv")
df_real = pd.read_csv("gym_members_enhanced_v2.csv")


X = df[['Age', 'Income_Level', 'Work_Type', 'Sleep_Hours_Per_Day', 'Medical_Condition', 'Smoking', 'Avg_BPM', 'Workout_Frequency (days/week)']]
y = df['Alcohol_Consumption']
model = LogisticRegression().fit(X, y)

with st.expander("Input Personal & Lifestyle Data"):
    age = st.number_input("Age", 18, 100, 25)
    income_label = st.selectbox("Income Level", get_labels("Income_Level"))
    income = int(get_code("Income_Level", income_label))
    work_label = st.selectbox("Work Type", get_labels("Work_Type"))
    work = int(get_code("Work_Type", work_label))
    sleep = st.slider("Sleep Hours/Day", 4, 12, 7)
    med_label = st.selectbox("Medical Condition", get_labels("Medical_Condition"))
    med = int(get_code("Medical_Condition", med_label))
    smoke_label = st.selectbox("Smoking", get_labels("Smoking"))
    smoke = int(get_code("Smoking", smoke_label))
    bpm = st.number_input("Average BPM", 50, 180, 75)
    freq = st.slider("Workout Frequency (days/week)", 1, 7, 3)

if st.button("Predict Consumption Level"):
    res = model.predict([[age, income, work, sleep, med, smoke, bpm, freq]])
    consumption = get_meaning("Alcohol_Consumption", str(int(res[0])))
    st.write(f"### Predicted Alcohol Consumption: **{consumption}** (Code: {int(res[0])})") 