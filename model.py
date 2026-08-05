import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/IBM HR Employee Attrition Data.csv")

# Convert all text columns to numbers
df = pd.get_dummies(df, drop_first=True)

# Target column
target = [c for c in df.columns if c.startswith("Attrition")][0]

X = df.drop(target, axis=1)
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", round(accuracy * 100, 2), "%")
import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
y.value_counts().plot(kind="bar", color=["green","red"])
plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Employees")
plt.show()

import joblib

joblib.dump(model, "employee_attrition_model.pkl")
print("Model saved successfully!")