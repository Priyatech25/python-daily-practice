import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Performance Dashboard")

# Load Data
df = pd.read_csv("data/sales_data.csv")

df["revenue"] = df["quantity"] * df["price"]
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# KPIs
total_revenue = df["revenue"].sum()
top_product = df.groupby("product")["revenue"].sum().idxmax()
top_region = df.groupby("region")["revenue"].sum().idxmax()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,}")
col2.metric("Top Product", top_product)
col3.metric("Best Region", top_region)

# Monthly Revenue Chart
st.subheader("📈 Monthly Revenue Trend")

monthly_sales = df.groupby("month")["revenue"].sum()

fig, ax = plt.subplots()
monthly_sales.plot(kind="bar", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Revenue")

st.pyplot(fig)

# Raw Data
st.subheader("📂 Sales Data")
st.dataframe(df)
