# 🎓 Student Marks Prediction Web Application

An end-to-end Machine Learning web application that predicts a student's examination marks based on their daily study hours using Linear Regression and Streamlit.

---

## 📌 Project Overview

This application demonstrates a complete machine learning pipeline: from data processing and model training to deployment as an interactive, dark-themed dashboard. Users can input their dedicated study hours using an intuitive slider and receive an instant estimation of their predicted percentage score.

---

## 🛠️ Tech Stack & Dependencies

* **Language**: Python 3.8+
* **Frontend Dashboard**: [Streamlit](https://streamlit.io/)
* **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/)
* **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Model Serialization**: [Joblib](https://joblib.readthedocs.io/)

---

## 📁 Recommended Project Structure

To maintain a clean working directory, structure your project files as follows:

```text
Student Marks Prediction/
├── train_model.py        # Python script to train and save the regression model
├── student_model.pkl     # Serialized trained model weights
├── app.py                # Main Streamlit web application dashboard
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
🚀 Getting Started1. Installation & Environment SetupClone or open your project directory in your terminal and install all required libraries:Bashpython -m pip install -r requirements.txt
2. Train and Export the ModelRun the training script to evaluate the algorithm and export student_model.pkl:Bashpython train_model.py
3. Launch the Web ApplicationStart the Streamlit development server:Bashpython -m streamlit run app.py
Once executed, open your web browser and navigate to http://localhost:8501.💡 How It WorksModel Training: A Simple Linear Regression model fits the functional relationship between study hours ($X$) and exam scores ($Y$).User Input: The user selects a target study duration (between 1.0 and 12.0 hours) via the Streamlit interface.Inference: The application loads student_model.pkl and predicts the corresponding score in real time.Boundary Formatting: Outputs are formatted and bounded within realistic academic bounds ($0\%$ to $100\%$).