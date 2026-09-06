
import streamlit as st
import joblib
import pandas as pd

# Load the saved model
loaded_model = joblib.load('lr.sav')

st.title('Sales Prediction using Linear Regression')
st.write('Enter the advertising budgets to predict sales.')

# Input fields for features
tv = st.number_input('TV Advertising Budget ($)', min_value=0.0, max_value=300.0, value=150.0)
radio = st.number_input('Radio Advertising Budget ($)', min_value=0.0, max_value=50.0, value=25.0)
newspaper = st.number_input('Newspaper Advertising Budget ($)', min_value=0.0, max_value=120.0, value=20.0)

if st.button('Predict Sales'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])

    # Make prediction
    prediction = loaded_model.predict(input_data)[0]

    st.success(f'Predicted Sales: {prediction:.2f}')
