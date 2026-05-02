import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

ohe = OneHotEncoder(sparse_output=False).set_output(transform='pandas')
le = LabelEncoder()


df = pd.read_csv("gym_members_enhanced_v2.csv")
df_copy = df.copy()

#Label encoding for gender
df_copy['Gender'] = le.fit_transform(df_copy['Gender'])

#Label encoding for workout type
df_copy['Workout_Type'] = le.fit_transform(df_copy['Workout_Type'])

#Label encoding for Fitness Goal
df_copy['Fitness_Goal'] = le.fit_transform(df_copy['Fitness_Goal'])

#Label encoding for Preferred Workout Time
df_copy['Preferred_Workout_Time'] = le.fit_transform(df_copy['Preferred_Workout_Time'])

#Label encoding for Work Type
df_copy['Work_Type'] = le.fit_transform(df_copy['Work_Type'])

#Label encoding for Income Level
df_copy['Income_Level'] = le.fit_transform(df_copy['Income_Level'])

#Label encoding for Diet Type
df_copy['Diet_Type'] = le.fit_transform(df_copy['Diet_Type'])

#Label encoding for gender
df_copy['Smoking'] = le.fit_transform(df_copy['Smoking'])

#Label encoding for Alcohol Consumption
df_copy['Alcohol_Consumption'] = le.fit_transform(df_copy['Alcohol_Consumption'])

#Label encoding for Medical Condition
df_copy['Medical_Condition'] = le.fit_transform(df_copy['Medical_Condition'])

print(df_copy.head())

df_copy.to_csv('preprocessed_gym.csv',index=False)