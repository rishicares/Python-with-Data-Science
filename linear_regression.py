import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('cars_model.pkl')

# Define a function fsfor prediction
def predict(input_data):
    # Convert the input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    # Use the model to make predictions
    prediction = model.predict(input_df)
    return prediction

# Streamlit app
st.title('Model Prediction App')

# Input fields for user to enter data
st.header('Input Data')
input_data = {}
input_data['total_bill'] = st.number_input('total bill')
input_data['size'] = st.number_input('size')
# Add more input fields as required for your model

# Prediction button
if st.button('Predict'):
    prediction = predict(input_data)
    st.write(f'Prediction: {prediction[0]}')