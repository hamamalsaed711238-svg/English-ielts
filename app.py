import streamlit as st
import google.generativeai as genai

st.title("🎓 IELTS Master AI")

# إعداد المفتاح في الجانب
with st.sidebar:
    api_key = st.text_input("Gemini API Key:", type="password")

essay = st.text_area("Write your essay here:", height=300)

if st.button("Analyze"):
    if api_key and essay:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(f"Analyze this IELTS essay and provide a band score: {essay}")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter API Key and Essay.")

