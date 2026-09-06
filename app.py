# %%writefile app.py

import streamlit as st
import joblib
import numpy as np

# Load the trained model
# Make sure 'linear_regression_model.sav' is in the same directory as this app.py file
model = joblib.load('linear_regression_model.sav')

st.title('Sales Prediction App')
st.write('Enter the advertising budgets to predict sales.')

# Input fields for features
tv = st.number_input('TV Advertising Budget (in thousands)', min_value=0.0, max_value=300.0, value=50.0)
radio = st.number_input('Radio Advertising Budget (in thousands)', min_value=0.0, max_value=50.0, value=20.0)
newspaper = st.number_input('Newspaper Advertising Budget (in thousands)', min_value=0.0, max_value=100.0, value=10.0)

if st.button('Predict Sales'):
    # Create a NumPy array from the input values
    features = np.array([[tv, radio, newspaper]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    st.success(f'Predicted Sales: {prediction:.2f} (in thousands)')
