# 🏠 House Price Prediction Web Application

An interactive web app built using **Streamlit** and **Python** to estimate residential property prices based on key property features and location metrics.

---

## 📌 Features

* **Real-Time Price Estimation**: Calculate estimated house prices based on user inputs.
* **Modern Dark-Mode Dashboard**: Sleek, responsive user interface inspired by modern web dashboards.
* **Property Metric Controls**: Adjustable parameters including square footage, bedrooms, bathrooms, property age, location grade, and garage availability.
* **Currency Support**: Switch display formats across USD ($), EUR (€), and INR (₹).

---

## 🛠️ Tech Stack

* **Language**: Python 3.8+
* **Frontend/Framework**: Streamlit
* **Libraries**: NumPy, Joblib / Pickle (for model loading), Scikit-Learn

---

## 📂 Project Directory Structure

```text
House Price Prediction/
├── app.py                   # Main Streamlit dashboard script
├── house_model.pkl          # Saved machine learning model file
├── House-Price-Predict.py   # Model training & EDA script
└── README.md                # Project documentation

🚀 Getting Started
1. Installation
Ensure you have Python installed, then install the required dependencies:

Bash
pip install streamlit numpy scikit-learn joblib
2. Running the Application
Launch the Streamlit app from your project directory:

Bash
python -m streamlit run app.py
Open your browser and navigate to http://localhost:8501.

💡 How It Works
Users input property parameters (Square Footage, Bedrooms, Bathrooms, Location, Age, Garage) in the dashboard UI.

The user clicks Predict Price.

The underlying algorithm evaluates the feature parameters and displays the estimated market value.


---

