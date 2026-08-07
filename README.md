# 🚀 End-To-End ML Web Series — Series 1

Welcome to **Day 12** of my Machine Learning Journey! This repository marks **Series 1** of converting trained Machine Learning models into interactive, user-friendly web applications using **Streamlit** and **Scikit-Learn**.

---

## 📌 Projects Included

### 1. 🎓 Student Marks Predictor
* **Algorithm**: Simple Linear Regression
* **Input Feature**: Daily Study Hours
* **Target Variable**: Predicted Exam Percentage (%)
* **Highlights**: Modern dark-mode interface with dynamic prediction outputs and model state checks.

### 2. 🏠 House Price Predictor
* **Algorithm**: Multiple Linear Regression
* **Input Features**: Square Footage, Bedrooms, Bathrooms, Location Grade, House Age, Garage Capacity
* **Target Variable**: Estimated Property Price ($)
* **Highlights**: Interactive input controls with real-time value calculation powered by trained model weights.

---

## 📁 Repository Structure

```text
End-To-End-ML-Web-Series-1/
├── House Price Prediction/
│   ├── app.py                      # Streamlit Web App Interface
│   ├── house_model.pkl             # Trained Model Weights
│   ├── House-Price-Prediction.py   # Model Training Script
│   └── requirements.txt
└── Student Marks Prediction/
    ├── app.py                      # Streamlit Web App Interface
    ├── student_model.pkl           # Trained Model Weights
    ├── Student-Marks-Prediction.py # Model Training Script
    └── requirements.txt
🛠️ Getting Started
1. Clone the Repository
Bash
git clone [https://github.com/AmnaShah14/End-To-End-ML-Web-Series-1.git](https://github.com/AmnaShah14/End-To-End-ML-Web-Series-1.git)
cd End-To-End-ML-Web-Series-1
2. Install Required Dependencies
Bash
pip install streamlit pandas scikit-learn joblib numpy
3. Run the Applications
To launch the Student Marks Predictor:

Bash
cd "Student Marks Prediction"
python -m streamlit run app.py
To launch the House Price Predictor:

Bash
cd "House Price Prediction"
python -m streamlit run app.py
