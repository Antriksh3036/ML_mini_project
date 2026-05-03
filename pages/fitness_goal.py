import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.title("🎯 Fitness Goal Classifier")


with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()

df = pd.read_csv("preprocessed_gym.csv")
X = df[['BMI','Fat_Percentage','Workout_Type','Workout_Frequency (days/week)','Diet_Type','Income_Level']]
y = df['Fitness_Goal']

model = DecisionTreeClassifier()
model.fit(X, y)

st.subheader("Input Parameters")
col1, col2 = st.columns(2)

with col1:
    bmi = st.number_input("BMI", 10.0, 50.0, 24.0)
    fat = st.number_input("Fat Percentage", 5.0, 50.0, 20.0)
    w_type_label = st.selectbox("Workout Type", get_labels("Workout_Type"))
    w_type = int(get_code("Workout_Type", w_type_label))

with col2:
    freq = st.slider("Workouts per Week", 1, 7, 3)
    diet_label = st.selectbox("Diet Type", get_labels("Diet_Type"))
    diet = int(get_code("Diet_Type", diet_label))
    income_label = st.selectbox("Income Level", get_labels("Income_Level"))
    income = int(get_code("Income_Level", income_label))

if st.button("Classify Goal"):
    res = model.predict([[bmi, fat, w_type, freq, diet, income]])
    goal = get_meaning("Fitness_Goal", str(int(res[0])))
    st.write(f"### Predicted Fitness Goal: :green[**{goal}**] (Code: {int(res[0])})") 