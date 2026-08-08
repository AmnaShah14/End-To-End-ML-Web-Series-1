import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample training data matching your single-feature ('Area') setup
# Replace this with your original training logic if you have specific data!
X = np.array([[500], [1000], [1500], [2000], [2500], [3000]])
y = np.array([150000, 250000, 350000, 450000, 550000, 650000])

model = LinearRegression()
model.fit(X, y)

# Save clean pkl file
joblib.dump(model, 'house_model.pkl')
print("✅ house_model.pkl successfully re-saved without hidden carriage returns!")