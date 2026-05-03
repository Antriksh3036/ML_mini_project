import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.title("🏥 Medical Condition Risk")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()

df = pd.read_csv("preprocessed_gym.csv")

X = df[['Age', 'BMI', 'Smoking', 'Alcohol_Consumption', 'Sleep_Hours_Per_Day', 'Work_Type', 'Fat_Percentage', 'Avg_BPM']]
y = df['Medical_Condition']
model = LogisticRegression().fit(X, y)

age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
smoke = st.toggle("Smoking")
alcohol_label = st.selectbox("Alcohol Consumption", get_labels("Alcohol_Consumption"))
alcohol = int(get_code("Alcohol_Consumption", alcohol_label))
sleep = st.slider("Sleep", 4, 12, 8)
work_label = st.selectbox("Work Type", get_labels("Work_Type"))
work = int(get_code("Work_Type", work_label))
fat = st.number_input("Fat %", 5.0, 50.0, 20.0)
bpm = st.number_input("Avg BPM", 50, 150, 75)

if st.button("Analyze Risk"):
    pred = model.predict([[age, bmi, int(smoke), alcohol, sleep, work, fat, bpm]])
    condition = get_meaning("Medical_Condition", str(int(pred[0])))
    st.warning(f"Predicted Medical Condition: **{condition}** (Code: {int(pred[0])})")
