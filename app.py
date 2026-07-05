import streamlit as st
import pandas as pd
import pickle
import numpy as np

# 1. Page Configuration (App ka title aur layout thoda behtar karne ke liye)
st.set_page_config(
    page_title="Sales Predictor Pro",
    page_icon="📈",
    layout="centered"
)

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Main Header
st.title("📊 Sales Prediction Dashboard")
st.caption("Machine Learning model to optimize your advertising strategy across multiple channels.")
st.write("---")

# 3. Load the Model Safely
model_filename = 'linear_regression_model.pkl'
try:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("🚨 Model file not found. Please upload 'linear_regression_model.pkl'.")

# 4. Input Fields in Columns (Ab sliders side-by-side bano taake space achhi lage)
st.subheader("💵 Marketing Budget Allocation")
st.write("Adjust the sliders below to set the budget for each channel (in thousands of dollars):")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📺 TV")
    tv_budget = st.slider('Budget ($)', 0.0, 300.0, 150.0, key='tv')

with col2:
    st.markdown("### 📻 Radio")
    radio_budget = st.slider('Budget ($)', 0.0, 50.0, 25.0, key='radio')

with col3:
    st.markdown("### 📰 Newspaper")
    newspaper_budget = st.slider('Budget ($)', 0.0, 120.0, 30.0, key='news')

st.write("---")

# 5. Prediction Logic and Beautiful Display
if st.button('✨ Calculate Expected Sales'):
    user_input = pd.DataFrame([[tv_budget, radio_budget, newspaper_budget]], 
                             columns=['TV', 'Radio', 'Newspaper'])
    
    predicted_sales = model.predict(user_input)
    final_output = predicted_sales.flatten()[0]
    
    # Ek bare metric widget mein output show hoga jo bohot professional lagta hai
    st.markdown("### 🎯 Prediction Result")
    st.metric(label="Estimated Total Sales Units", value=f"${final_output:.2f}K")
    st.balloons() # Ek mazaahiya animation app ke live hone ki khushi mein!
