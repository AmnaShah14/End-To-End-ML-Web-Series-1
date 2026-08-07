# Student Marks Prediction using Linear Regression
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Dataset setup
data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 45, 50, 60, 65, 72, 80, 88, 85],
}

df = pd.DataFrame(data)
print("--- Dataset ---")
print(df)

x = df[["Hours"]]
y = df["Marks"]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Test single inference
sample_hours = 7.5
prediction = model.predict(pd.DataFrame([[sample_hours]], columns=["Hours"]))
print(f"\nPredicted Marks for {sample_hours} study hours: {prediction[0]:.2f}")

# Predict on test data & calculate evaluation metrics
test_prediction = model.predict(x_test)
mae = mean_absolute_error(y_test, test_prediction)
print(f"Mean Absolute Error (MAE): {mae:.2f}")

# Save the trained model to disk
joblib.dump(model, "student_model.pkl")
print("\nModel saved successfully as 'student_model.pkl'!")