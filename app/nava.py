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
    st.image(image, use_container_width=True)
except FileNotFoundError:
    st.error("Image file not found. Please ensure the file path is correct.")
    
st.markdown("""
This dashboard allows you to navigate the various sections of the Ai powered application for Cowpea management system.
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
- [Treatment Recommender](https://cowpeatreatment-hyb7fw82sltrlwfmiypyjt.streamlit.app/)  
- [Yield Predictor](https://cowpeayield-9extd5lp5lptxwtw3bdmqg.streamlit.app/)  
""")

# Add a section for PDF download
# st.header("Download Report")
# pdf_path = "example_report.pdf"  # Replace with the path to your PDF file


# pdf_path = './app/cowpea_eda_and_model_explanation_file.pdf'

# try:
#     with open(pdf_path, "rb") as pdf_file:
#         pdf_bytes = pdf_file.read()
#     st.download_button(
#         label="Download PDF Report",
#         data=pdf_bytes,
#         file_name="report.pdf",
#         mime="application/pdf",
#     )
# except FileNotFoundError:
#     st.error("PDF file not found. Please ensure the file path is correct.")

import streamlit as st

st.title("Feedback Form")
st.markdown("We value your feedback. Please click the button below to fill out our feedback form.")

# Add a button to open the form
if st.button("Open Feedback Form"):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc569ZHw3OsUJ4PW2dc-tnllUpu0UvrqLCW8ZrRLUise2LKgA/viewform?usp=header"  # Replace with your Google Form URL
    st.markdown(f"[Click here to open the form]({form_url})", unsafe_allow_html=True)


# Optionally, provide a dropdown for navigation
