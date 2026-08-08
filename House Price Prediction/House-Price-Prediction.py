import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Ensure X has all 6 features matching your Streamlit app
# Example structure:
# X = df[['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Location_Grade', 'Garage_Spaces']]

# Dummy training example with 6 features:
X_train = pd.DataFrame([
    [1500, 3, 2, 10, 4, 1],
    [2000, 4, 3, 5, 5, 2],
    [1200, 2, 1, 15, 3, 1],
    [2500, 4, 3, 2, 5, 2]
], columns=['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Location_Grade', 'Garage_Spaces'])

y_train = [300000, 450000, 220000, 550000]

# 2. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Export the model trained on 6 features
joblib.dump(model, 'house_model.pkl')
print("✅ house_model.pkl retrained and saved with 6 features!")