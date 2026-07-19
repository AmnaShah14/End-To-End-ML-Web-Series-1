# House Price Prediction using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area": [600, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price": [30, 40, 50, 60, 75, 90, 100, 110, 125]
}

df = pd.DataFrame(data)

x = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(x, y)

price = model.predict(pd.DataFrame([[1700]], columns=["Area"]))

print("Predicted House Price:", round(price[0], 2), "Lakhs")