import streamlit as st
import pandas as pd
import joblib

# Load model and label encoders
model = joblib.load('models/random_forest_model.pkl')
label_encoders = joblib.load('models/label_encoders.pkl')

# Title
st.title("💸 Insurance Charges Predictor")
st.markdown("This app predicts **insurance charges** based on your personal details.")

# User Inputs
st.header("🧍 Enter your details")

age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male", "female"])
height_cm = st.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
weight_kg = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Do you smoke?", ["yes", "no"])
region = st.selectbox("Region", ['southwest', 'southeast', 'northwest', 'northeast'])

# BMI calculation
height_m = height_cm / 100
bmi = round(weight_kg / (height_m ** 2), 2)
st.markdown(f"📏 **Calculated BMI:** `{bmi}`")

# Create input DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

# Label encode categorical inputs
for col in ['sex', 'smoker', 'region']:
    input_data[col] = label_encoders[col].transform(input_data[col])

# Prediction
if st.button("🎯 Predict Charges"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Insurance Charges: ₹{round(prediction, 2)}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Harsh")
