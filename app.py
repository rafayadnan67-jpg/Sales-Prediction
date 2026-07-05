import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model_filename = 'linear_regression_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.title('Sales Prediction App')
st.write('Enter the advertising budgets to predict sales.')

# Input fields for advertising budgets
tv_budget = st.slider('TV Advertising Budget ($)', 0.0, 300.0, 150.0)
radio_budget = st.slider('Radio Advertising Budget ($)', 0.0, 50.0, 25.0)
newspaper_budget = st.slider('Newspaper Advertising Budget ($)', 0.0, 120.0, 30.0)

if st.button('Predict Sales'):
    # Create a DataFrame for the user input
    user_input = pd.DataFrame([[tv_budget, radio_budget, newspaper_budget]],
                              columns=['TV', 'Radio', 'Newspaper'])
    
    # Make prediction
    predicted_sales = model.predict(user_input)
    
    st.success(f'Predicted Sales: ${predicted_sales.flatten()[0]:.2f}')
