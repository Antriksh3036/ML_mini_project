#Decision Tree



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

df = pd.read_csv("preprocessed_gym.csv")
model = DecisionTreeClassifier()

X = df[['BMI','Fat_Percentage','Workout_Type','Workout_Frequency (days/week)','Diet_Type','Income_Level']]

y = df['Fitness_Goal']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

model.fit(X_train,y_train)

predicted = model.predict(X_test)
print(predicted)

print("accuracy_score:",accuracy_score(y_test,predicted))
print("precision_score:",precision_score(y_test,predicted, average='macro'))
print("recall_score:",recall_score(y_test,predicted, average='macro'))
print("f1_score:",f1_score(y_test,predicted, average='macro'))