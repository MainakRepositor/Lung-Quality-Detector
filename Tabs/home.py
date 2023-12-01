"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Lungs Diseases Predictor")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Lung disease detection involves using medical imaging (like X-rays or CT scans) to analyze lung structure, identifying abnormalities such as nodules, tumors, or inflammation. Machine learning algorithms aid in pattern recognition to distinguish healthy and diseased lung tissue. These algorithms interpret image features, detecting specific markers or anomalies indicative of conditions like pneumonia, tuberculosis, or lung cancer. Integration of patient data, AI analysis, and expert validation enables accurate diagnosis, aiding in early intervention and treatment planning for improved patient outcomes.
        </p>
    """, unsafe_allow_html=True)