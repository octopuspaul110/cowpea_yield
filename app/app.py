import streamlit as st
import pandas as pd
import numpy as np
import joblib
import path
import sys
from PIL import Image
import sqlite
from sqlalchemy import create_engine


# Initialize database connection
DB_FILE = "app_data.db"
engine = create_engine(f"sqlite:///{DB_FILE}")

def initialize_db():
    with engine.connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            GID INTEGER,
            PLOTNO INTEGER,
            STAND INTEGER,
            SEEDS REAL,
            SEEDKGHA REAL
        );
        """)
# Save data to database
def save_to_db(data):
    with engine.connect() as conn:
        data.to_sql("predictions", con=conn, if_exists="append", index=False)

# Fetch all data from database
def fetch_all_data():
    with engine.connect() as conn:
        query = "SELECT * FROM predictions"
        return pd.read_sql(query, conn)

# Initialize database
initialize_db()

# Title and description
st.title("Cowpea Yield Predictor")
image_path = "./app/yield.jpeg"  # Replace with the actual path to your image
try:
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please ensure the file path is correct.")
st.markdown("""
 Please ensure the data format matches the required features: GID, PLOTNO, STAND, and SEEDS. 
""")

# Placeholder for model path
#model_path = "D:\cowpea_yield_app\cowpea_yield_project\cowpea_yield\models\yield_model.pkl"  # Replace with your model's path

# Load the model
@st.cache_resource
def load_model():
    try:
        dir = path.Path(__file__)
     
        sys.path.append(dir.parent.parent)
        
        # load model
        path_to_model = './models/yield_model.pkl'
        
        with open(path_to_model, 'rb') as file:
            model = joblib.load(file)
         
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

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
            input_data["SEEDKGHA"] = predictions[0]
            save_to_db(input_data)
            st.success("Prediction saved to database!")
        except Exception as e:
            st.error(f"Error during inference: {e}")
else:
    st.warning("Model not loaded.")
# Display stored predictions
st.header("Stored Predictions")
stored_data = fetch_all_data()
if not stored_data.empty:
    st.dataframe(stored_data)
else:
    st.info("No data stored yet.")
