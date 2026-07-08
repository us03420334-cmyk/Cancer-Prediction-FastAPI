import pandas as pd
import numpy as np
from sklearn import linear_model
lr = linear_model.LogisticRegression(max_iter=1000)
df = pd.read_csv("C:/Python/.venv/Lib/global_cancer_patients_2015_2024.csv")
X = df[['Age', 'Air_Pollution', 'Alcohol_Use', 'Smoking', 'Obesity_Level']]
y = df['Cancer_Type']
lr.fit(X, y)



import joblib

joblib.dump(lr, "cancer_model.pkl")

print("Model saved successfully!!!")