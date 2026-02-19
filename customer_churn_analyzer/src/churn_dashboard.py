import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("📊 Customer Churn Analysis & Prediction")

# Load Data
df = pd.read_csv("data/churn_data.csv")

# Churn Rate
churn_rate = (df["churn"] == "Yes").mean() * 100

st.metric("Churn Rate", f"{churn_rate:.2f}%")

# Encode churn
df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=["gender", "contract_type"], drop_first=True)

X = df_encoded.drop(["customer_id", "churn"], axis=1)
y = df_encoded["churn"]

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# ===== Prediction Section =====
st.subheader("🔮 Predict Customer Churn")

tenure = st.slider("Tenure (Months)", 0, 60, 12)
monthly_charges = st.number_input("Monthly Charges", 100, 2000, 500)
gender = st.selectbox("Gender", ["Male", "Female"])
contract = st.selectbox("Contract Type", ["Monthly", "Yearly"])

# Manual encoding
gender_Male = 1 if gender == "Male" else 0
contract_Yearly = 1 if contract == "Yearly" else 0

input_data = pd.DataFrame({
    "tenure": [tenure],
    "monthly_charges": [monthly_charges],
    "gender_Male": [gender_Male],
    "contract_type_Yearly": [contract_Yearly]
})

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠ Customer likely to churn ({probability*100:.2f}% probability)")
    else:
        st.success(f"✅ Customer likely to stay ({(1-probability)*100:.2f}% confidence)")

# ===== Data Preview =====
st.subheader("📂 Dataset Preview")
st.dataframe(df)
