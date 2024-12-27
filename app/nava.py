import streamlit as st
import path
import sys
from PIL import Image

# Title and description
st.title("AI-Powered Integrated Cowpea management system for Nigerian Farmers.")
dir = path.Path(__file__)
sys.path.append(dir.parent.parent)

image_path = "./app/cowpea_images.jpeg"  # Replace with the actual path to your image
try:
    image = Image.open(image_path)
    st.image(image, caption="Cowpea Yield", use_container_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please ensure the file path is correct.")
    
st.markdown("""
This dashboard allows you to navigate to different Ai powered application for Cowpea management system.
""")
st.markdown("""This Application is developed to help farmers monitor growth, pest infestation and predict yield of cowpea in Nigeria.
The Software consists of three panels.""")

st.markdown("""i. A section that predict the severity of pest and disease infestation""")
st.markdown("""ii. A section that recommends the treatment option""")
st.markdown("""iii. A section that predict the yield""")

# Navigation links
st.header("Available Apps")
st.markdown("""
- [Cowpea Disease Predictor](https://cowpea-project-23ni8gknzgwryhzuhp7kcs.streamlit.app/)  
- [Treatment Predictor](https://cowpeatreatment-hyb7fw82sltrlwfmiypyjt.streamlit.app/)  
- [Yield Predictor](https://cowpeayield-9extd5lp5lptxwtw3bdmqg.streamlit.app/)  
""")

st.markdown("""For the app development, the explanation of the exploratory data analysis (EDA) and model development is presented in the sections below""")
st.markdown("""3.1 Exploratory data analysis of the three datasets""")
st.markdown("""3.2 Model Development. explanation of the choice of machine learning model.There is need to identify and state the features of the datasets that were selected for building the application. The feature engineering approach/method/technique and or algorithm.""")
st.markdown("""3.3 Result of model testing""")
st.markdown("""3.4 App Deployment and Feedback""")


# Add a section for PDF download
st.header("Download Report")
pdf_path = "example_report.pdf"  # Replace with the path to your PDF file


pdf_path = './app/cowpea_eda_and_model_explanation_file.pdf'

try:
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    st.download_button(
        label="Download PDF Report",
        data=pdf_bytes,
        file_name="report.pdf",
        mime="application/pdf",
    )
except FileNotFoundError:
    st.error("PDF file not found. Please ensure the file path is correct.")

# Optionally, provide a dropdown for navigation
