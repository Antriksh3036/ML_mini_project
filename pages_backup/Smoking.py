import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.title("🚬 Smoking Habit Classifier")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()
df = pd.read_csv("preprocessed_gym.csv")

X = df[['Age', 'Sleep_Hours_Per_Day', 'Alcohol_Consumption', 'Medical_Condition', 'Work_Type', 'Avg_BPM', 'Fat_Percentage', 'Income_Level', 'Experience_Level']]
y = df['Smoking']
model = LogisticRegression().fit(X, y)

st.write("Input lifestyle indicators:")
age = st.number_input("Age", 18, 90, 30)
sleep = st.slider("Sleep Hours", 4, 12, 7)
alcohol_label = st.selectbox("Alcohol Consumption", get_labels("Alcohol_Consumption"))
alcohol = int(get_code("Alcohol_Consumption", alcohol_label))
medical_label = st.selectbox("Medical Condition", get_labels("Medical_Condition"))
medical = int(get_code("Medical_Condition", medical_label))
work_label = st.selectbox("Work Type", get_labels("Work_Type"))
work = int(get_code("Work_Type", work_label))
bpm = st.number_input("Avg BPM", 50, 160, 80)
fat = st.number_input("Fat %", 5, 50, 22)
income_label = st.selectbox("Income Level", get_labels("Income_Level"))
income = int(get_code("Income_Level", income_label))
experience = st.number_input("Experience Level (ID)", 0, 3, 1)

if st.button("Predict Smoking Status"):
    inputs = [age, sleep, alcohol, medical, work, bpm, fat, income, experience]
    res = model.predict([inputs])
    smoking = get_meaning("Smoking", str(int(res[0])))
    st.warning(f"Predicted Smoking Status: **{smoking}** (Code: {int(res[0])})") 