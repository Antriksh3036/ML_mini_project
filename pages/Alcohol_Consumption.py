#LogisticRegression

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("preprocessed_gym.csv")
model = LogisticRegression()


X = df[['Age', 'Income_Level', 'Work_Type', 'Sleep_Hours_Per_Day', 'Medical_Condition', 'Smoking', 'Avg_BPM', 'Workout_Frequency (days/week)']]
y = df['Alcohol_Consumption']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

model.fit(X_train,y_train)
predicted = model.predict(X_test)

print(accuracy_score(y_test,predicted))