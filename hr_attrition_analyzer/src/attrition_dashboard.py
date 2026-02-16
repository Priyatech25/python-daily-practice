import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="HR Attrition Prediction", layout="centered")

st.title("💼 HR Employee Attrition Prediction")

# Load model
model = joblib.load("best_attrition_model.pkl")

# User Inputs
salary = st.number_input("Salary", min_value=10000, max_value=100000, value=40000)
years = st.slider("Years at Company", 0, 15, 3)

department = st.selectbox("Department", ["HR", "IT", "Sales"])

# Convert department into encoded format
dept_IT = 1 if department == "IT" else 0
dept_Sales = 1 if department == "Sales" else 0

# Create input dataframe (must match training features)
input_data = pd.DataFrame({
    "salary": [salary],
    "years_at_company": [years],
    "department_IT": [dept_IT],
    "department_Sales": [dept_Sales]
})

# Prediction
if st.button("Predict Attrition"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ Employee is likely to Leave")
    else:
        st.success("✅ Employee is likely to Stay")
