import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Custom CSS for Background and Text Styling
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa; /* Light grey background */
            color: #333; /* Darker text */
        }
        .main {
            background-color: #ffffff; /* White card background */
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        }
        h1, h2, h3 {
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            color: #4e73df; /* Blue accent */
        }
        .stButton>button {
            background-color: #4e73df; /* Blue button background */
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #375ab7; /* Darker blue hover effect */
        }
    </style>
""", unsafe_allow_html=True)

# Sample Data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=100)
    data = pd.DataFrame({
        "Date": dates,
        "Sales": np.random.randint(100, 500, size=len(dates)),
        "Region": np.random.choice(["North", "South", "East", "West"], size=len(dates)),
        "Category": np.random.choice(["Electronics", "Clothing", "Furniture"], size=len(dates))
    })
    return data

# Load data
data = load_data()

# Streamlit App
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🌟 Business Analytics Dashboard")

# Overview
st.markdown("### **📊 Sales Overview**")
st.dataframe(data)

# Sales Over Time
st.markdown("### **📈 Sales Over Time**")
fig = px.line(data, x="Date", y="Sales", title="Sales Trend", color_discrete_sequence=["#4e73df"])
st.plotly_chart(fig)

# Sales by Region
st.markdown("### **📍 Sales by Region**")
sales_by_region = data.groupby("Region")["Sales"].sum().reset_index()
fig = px.bar(sales_by_region, x="Region", y="Sales", title="Sales by Region", color_discrete_sequence=["#4e73df"])
st.plotly_chart(fig)

# Sales by Category
st.markdown("### **🛍️ Sales by Category**")
sales_by_category = data.groupby("Category")["Sales"].sum().reset_index()
fig = px.pie(sales_by_category, names="Category", values="Sales", title="Sales by Category", color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.markdown("</div>", unsafe_allow_html=True)
