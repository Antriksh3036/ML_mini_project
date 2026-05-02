#linear Regression


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,root_mean_squared_error

df = pd.read_csv("preprocessed_gym.csv")

model = LinearRegression()

X = df[['Age', 'Weight (kg)', 'BMI', 'Avg_BPM', 'Session_Duration (hours)', 'Workout_Type','Fitness_Goal','Sleep_Hours_Per_Day']]
y = df['Calories_Burned']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

model.fit(X_train,y_train)
predicted = model.predict(X_test)

mse = mean_squared_error(y_test,predicted)
mae = mean_absolute_error(y_test,predicted)
rmse = root_mean_squared_error(y_test,predicted)

print("mse:",mse)
print("mae:",mae)
print("rmse:",rmse)

plt.plot(y_test,y_test)
plt.scatter(y_test,predicted)
plt.show()