import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Title and description
st.title("Regression Model Inference")
st.markdown("""
 Please ensure the data format matches the required features: GID, PLOTNO, STAND, and SEEDS. 
""")

# Placeholder for model path
model_path = "D:\cowpea_yield_app\cowpea_yield_project\cowpea_yield\models\yield_model.pkl"  # Replace with your model's path

# Load the model
def load_model(path):
    try:
        model = joblib.load(path)
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model(model_path)

# Input data for inference
st.header("Input Data")
GID = st.number_input("Enter GID (e.g., 799):", min_value=0, max_value=100000, step=1)
PLOTNO = st.number_input("Enter PLOTNO (e.g., 101):", min_value=0, max_value=500000, step=1)
STAND = st.number_input("Enter STAND (e.g., 14):", min_value=0, max_value=100000, step=1)
SEEDS = st.number_input("Enter SEEDS (e.g., 100.0):", min_value=0.0, max_value=500000.0, step=0.1)

input_data = pd.DataFrame({
    "GID": [GID],
    "PLOTNO": [PLOTNO],
    "STAND": [STAND],
    "SEEDS": [SEEDS],
})

# Predict button
if model:
    if st.button("Predict"):
        st.header("Inference")
        try:
            predictions = model.predict(input_data)
            st.write("Predicted YIELD (SEEDKGHA):", predictions[0])
        except Exception as e:
            st.error(f"Error during inference: {e}")
else:
    st.warning("Model not loaded.")