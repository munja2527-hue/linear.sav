import streamlit as st
import joblib
import pandas as pd

# Load the trained model
lr = joblib.load('linear.sav')

st.title('Sales Prediction App')
st.write('Enter the advertising spending to predict sales.')

# Input fields for advertising spend
tv = st.slider('TV Advertising Spend', 0.0, 300.0, 150.0)
radio = st.slider('Radio Advertising Spend', 0.0, 50.0, 25.0)
newspaper = st.slider('Newspaper Advertising Spend', 0.0, 100.0, 30.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame([{
    'TV': tv,
    'Radio': radio,
    'Newspaper': newspaper
}])

# Predict sales
predicted_sales = lr.predict(input_data)[0]

st.subheader('Predicted Sales')
st.write(f'Based on your inputs, the predicted sales are: {predicted_sales:.2f}')

st.markdown("""
To run this Streamlit app, save this file as `app.py` and then execute the following command in your terminal:
`streamlit run app.py`
""")
