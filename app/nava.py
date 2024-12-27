import streamlit as st

# Title and description
st.title("AI-Powered Integrated Cowpea management system for Nigerian Farmers.")
st.markdown("""
This dashboard allows you to navigate to different Ai powered application for Cowpea management system.
""")
st.markdown("""This Application is developed to help farmers monitor growth, pest infestation and predict yield of cowpea in Nigeria.
The Software consists of three panels.
i. A section that predict the severity of pest and disease infestation
ii. A section that recommends the treatment option
iii. A section that predict the yield
 
For the app development, the explanation of the exploratory data analysis (EDA) and model development is presented in the sections below
3.1 Exploratory data analysis of the three datasets
3.2 Model Development. explanation of the choice of machine learning model.
There is need to identify and state the features of the datasets that were selected for building the application. The feature engineering approach/method/technique and or algorithm. 
 
3.3 Result of model testing
3.4 App Deployment and Feedback
 """)

# Navigation links
st.header("Available Apps")
st.markdown("""
- [Cowpea Disease Predictor](https://cowpea-project-23ni8gknzgwryhzuhp7kcs.streamlit.app/)  
- [Treatment Predictor](https://cowpeatreatment-hyb7fw82sltrlwfmiypyjt.streamlit.app/)  
- [Yield Predictor](https://cowpeayield-9extd5lp5lptxwtw3bdmqg.streamlit.app/)  
""")

# Optionally, provide a dropdown for navigation
