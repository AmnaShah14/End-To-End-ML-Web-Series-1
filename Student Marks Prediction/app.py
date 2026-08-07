import os
import joblib
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dark Theme Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton > button {
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
    .result-box {
        background-color: #1E222D;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2E364F;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Load Trained Model
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "student_model.pkl")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None


model = load_model()

# Sidebar Controls
with st.sidebar:
    st.title("🎓 Model Control")
    st.subheader("Model Information")
    st.markdown("🔹 **Algorithm**: Linear Regression")
    st.markdown("🔹 **Target Variable**: Marks (Percentage)")
    st.markdown("🔹 **Feature**: Study Hours")
    st.markdown("---")
    if model is not None:
        st.success("`student_model.pkl` loaded successfully!")
    else:
        st.error(
            "`student_model.pkl` missing. Run `Student-Marks-Prediction.py` first."
        )

# Main Header
st.title("🎓 Student Marks Prediction System")
st.caption("Estimate exam performance based on total daily study hours.")
st.markdown("---")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Study Parameters")
    hours = st.slider(
        "Select Daily Study Hours",
        min_value=1.0,
        max_value=12.0,
        value=7.5,
        step=0.5,
    )

with col2:
    st.subheader("Action")
    predict_btn = st.button("🚀 Predict Marks", type="primary")

# Prediction Execution
if predict_btn:
    if model is not None:
        # Pass input using the exact column name used during training
        input_data = pd.DataFrame([[hours]], columns=["Hours"])
        predicted_mark = model.predict(input_data)[0]

        # Bound predictions between 0% and 100%
        final_score = min(max(predicted_mark, 0.0), 100.0)

        st.markdown(
            f"""
            <div class="result-box">
                <h3 style="color: #888;">Predicted Score</h3>
                <h1 style="color: #4CAF50; font-size: 3rem;">{final_score:.1f}%</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("Cannot perform prediction because `student_model.pkl` is missing.")


 #  python -m streamlit run app.py