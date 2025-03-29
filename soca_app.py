# soca_app.py
import streamlit as st
import pandas as pd
from questions import get_questions
from analysis import get_soca_analysis

st.title("📊 JEE SOCA Analysis Tool - Powered by Free Gemini AI - Created by Aryan")

questions = get_questions()
user_responses = {}

# Display Questions
for section, q_list in questions.items():
    st.subheader(f"📌 {section} Section")
    for question in q_list:
        response = st.slider(question, 1, 10, 5)
        user_responses[question] = response

if st.button("🚀 Generate Analysis"):
    with st.spinner("Generating your SOCA report..."):
        soca_report = get_soca_analysis(user_responses)
        st.subheader("📌 Your Personalized SOCA Report")
        st.write(soca_report)

st.markdown("---")
st.write("🔹 Powered by Free Gemini AI | Developed for JEE Aspirants | Created by Aryan")
