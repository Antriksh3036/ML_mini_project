import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from constants import get_code, get_labels, get_meaning, display_data_dictionary

st.set_page_config(page_title="Diet Type Classifier", layout="wide")

st.title("🥗 Diet Type Recommendation")
st.markdown("---")

# Data Dictionary Reference
with st.expander("📚 Data Dictionary - What do the options mean?"):
    display_data_dictionary()

# Load preprocessed data
df = pd.read_csv("preprocessed_gym.csv")


X = df[['BMI', 'Fat_Percentage', 'Workout_Type', 'Workout_Frequency (days/week)', 'Fitness_Goal', 'Income_Level']]
y = df['Diet_Type']


model = DecisionTreeClassifier()
model.fit(X, y)

st.subheader("Input Profile for Diet Prediction")
col1, col2 = st.columns(2)

with col1:
    bmi = st.number_input("BMI", 10.0, 50.0, 22.5)
    fat = st.number_input("Fat Percentage", 5.0, 50.0, 18.0)
    w_type_label = st.selectbox("Workout Type", get_labels("Workout_Type"))
    w_type = int(get_code("Workout_Type", w_type_label))

with col2:
    freq = st.slider("Workout Frequency (days/week)", 1, 7, 3)
    goal_label = st.selectbox("Fitness Goal", get_labels("Fitness_Goal"))
    goal = int(get_code("Fitness_Goal", goal_label))
    income_label = st.selectbox("Income Level", get_labels("Income_Level"))
    income = int(get_code("Income_Level", income_label))

if st.button("Predict Diet Type"):
    input_data = [[bmi, fat, w_type, freq, goal, income]]
    prediction = model.predict(input_data)
    diet = get_meaning("Diet_Type", str(int(prediction[0])))
    st.markdown("---")
    st.success(f"### Recommended Diet Type: :green[**{diet}**] (Code: {int(prediction[0])})") 