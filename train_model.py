import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Input features
X = df[
    [
        "Attendance",
        "Study_Hours",
        "Previous_Marks",
        "Assignment_Marks",
        "Internal_Marks"
    ]
]

# Target
y = df["Final_Marks"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully!")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save model
os.makedirs("model", exist_ok=True)

model_path = os.path.join("model", "student_model.pkl")
joblib.dump(model, model_path)

print("Model saved successfully!")
print("Model location:", model_path)


print("Model saved successfully!")