import streamlit as st
import pickle
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Taxi Fare Prediction",
    page_icon="🚖",
    layout="centered"
)

# -------------------------
# Load Model
# -------------------------
with open("taxi_model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------------
# Header
# -------------------------
st.title("🚖 Taxi Fare Prediction")
st.markdown(
    "### Predict the estimated taxi fare based on travel distance."
)

st.divider()

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("About")
st.sidebar.write(
    """
    **Machine Learning Model:** Linear Regression
    
    **Input:** Distance
    
    **Output:** Estimated Taxi Fare
    """
)

# -------------------------
# User Input
# -------------------------
distance = st.number_input(
    "📍 Enter Distance (km)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

st.write(f"**Selected Distance:** {distance:.1f} km")

st.divider()

# -------------------------
# Prediction
# -------------------------
if st.button("🚕 Total Fare", use_container_width=True):

    input_data = pd.DataFrame({
        "distance": [distance]
    })

    prediction = model.predict(input_data)

    st.success(f"💵 Estimated Fare: ${prediction[0]:.2f}")