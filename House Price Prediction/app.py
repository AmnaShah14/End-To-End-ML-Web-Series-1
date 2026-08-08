import os
import joblib
import numpy as np
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dark theme styling
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
    .price-box {
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


# Load Trained Model safely
@st.cache_resource
def load_model():
    model_path = "house_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None


model = load_model()

# Sidebar - Model Info & Parameters
with st.sidebar:
    st.title("🏠 Model Control")
    st.subheader("Model Info")
    st.markdown("🔹 **Algorithm**: Linear Regression")
    st.markdown("🔹 **Dataset**: House Prices")
    st.markdown("---")
    st.subheader("Settings")
    currency = st.selectbox(
        "Currency Display", ["USD ($)", "EUR (€)", "INR (₹)"]
    )

# Currency Mapping
currency_symbols = {"USD ($)": "$", "EUR (€)": "€", "INR (₹)": "₹ "}
currency_rates = {"USD ($)": 1.0, "EUR (€)": 0.92, "INR (₹)": 83.0}

# Main interface header
st.title("🏠 House Price Prediction Model")
st.caption(
    "Enter the property specifications below to estimate the market value."
)

st.markdown("---")

# Input Form in Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Property Features")
    sqft = st.number_input(
        "Total Square Feet", min_value=100, max_value=10000, value=1500, step=50
    )
    bedrooms = st.slider("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.slider("Bathrooms", min_value=1, max_value=8, value=2)

with col2:
    st.subheader("Location & Quality")
    location = st.selectbox(
        "Neighborhood / Location Grade",
        ["Downtown / Prime", "Suburbs", "Rural"],
    )
    age = st.number_input(
        "Property Age (Years)", min_value=0, max_value=100, value=10
    )
    garage = st.radio("Garage Included?", ["Yes", "No"], horizontal=True)

st.markdown("---")

# Action Buttons
btn_col1, btn_col2 = st.columns([1, 4])
with btn_col1:
    predict_btn = st.button("🚀 Predict Price", type="primary")

# Prediction Execution
if predict_btn:
    # Encode categorical inputs into numeric values
    loc_val = (
        2 if location == "Downtown / Prime" else (1 if location == "Suburbs" else 0)
    )
    garage_val = 1 if garage == "Yes" else 0

    # Ensure array shape is (1, 6) matching training feature order
    input_features = np.array(
        [[sqft, bedrooms, bathrooms, loc_val, age, garage_val]]
    )

    if model is not None:
        try:
            raw_price = model.predict(input_features)[0]
        except Exception as e:
            st.error(f"Prediction Error: Ensure model feature inputs match: {e}")
            raw_price = 0
    else:
        st.warning("`house_model.pkl` not found. Using fallback math calculation.")
        base_price = sqft * 150
        bedroom_val = bedrooms * 10000
        location_mult = (
            1.5
            if location == "Downtown / Prime"
            else (1.1 if location == "Suburbs" else 0.9)
        )
        raw_price = (base_price + bedroom_val) * location_mult

    if raw_price > 0:
        converted_price = raw_price * currency_rates[currency]
        symbol = currency_symbols[currency]

        st.markdown(
            f"""
            <div class="price-box">
                <h3 style="color: #888;">Estimated Market Price</h3>
                <h1 style="color: #4CAF50; font-size: 2.8rem;">{symbol}{converted_price:,.2f}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )