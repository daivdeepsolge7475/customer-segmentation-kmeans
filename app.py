import streamlit as st
import joblib
import numpy as np

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍",
    layout="wide"
)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("About")

st.sidebar.write("""
This application segments mall customers
using the K-Means Clustering algorithm.

**Developer:** Daivdeep Solge
""")

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("kmeans_model.pkl")

# ---------------------------
# Title
# ---------------------------
st.title("🛍 Customer Segmentation using K-Means")

# ---------------------------
# Inputs
# ---------------------------
income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    value=50.0
)

score = st.number_input(
    "Spending Score (1-100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

# ---------------------------
# Dictionaries
# ---------------------------
segment_names = {
    0: "🛒 Regular Customer",
    1: "💎 High Income - High Spending",
    2: "💰 Low Income - Low Spending",
    3: "🎯 High Income - Low Spending",
    4: "🌟 Low Income - High Spending"
}

recommendations = {
    0: "Offer loyalty programs and seasonal discounts.",
    1: "Provide VIP membership and premium products.",
    2: "Offer budget-friendly products and discounts.",
    3: "Target with personalized marketing campaigns.",
    4: "Retain them using reward points and cashback offers."
}

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Customer Segment"):

    customer = np.array([[income, score]])

    cluster = model.predict(customer)[0]

    st.success(
        f"Customer Segment: {segment_names.get(cluster, f'Cluster {cluster}')}"
    )

    st.info(
        recommendations.get(cluster, "No recommendation available.")
    )
