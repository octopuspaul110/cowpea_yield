import streamlit as st

# Title and description
st.title("AI-Powered Integrated Cowpea management system for Nigerian Farmers.")
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
st.markdown("""3.2 Model Development. explanation of the choice of machine learning model.""")
st.markdown("""There is need to identify and state the features of the datasets that were selected for building the application. The feature engineering approach/method/technique and or algorithm.""")
st.markdown("""Result of model testing""")
st.markdown("""3.4 App Deployment and Feedback""")


# Add a section for PDF download
st.header("Download Report")
pdf_path = "example_report.pdf"  # Replace with the path to your PDF file

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
