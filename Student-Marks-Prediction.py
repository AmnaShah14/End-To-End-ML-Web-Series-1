# Student Marks Prediction using Linear Regression

import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 45, 50, 60, 65, 72, 80, 88, 85]
}

df = pd.DataFrame(data)
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

# Predict marks for 7.5 study hours
prediction = model.predict(pd.DataFrame([[7.5]], columns=["Hours"]))
print("Predicted Marks:", prediction[0])

# Predict on test data
test_prediction = model.predict(x_test)

# Calculate Mean Absolute Error
print("MAE:", mean_absolute_error(y_test, test_prediction))
