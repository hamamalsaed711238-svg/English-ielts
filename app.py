import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="IELTS Global Master", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton button { background: linear-gradient(90deg, #1f6feb, #7928ca); color: white; border-radius: 10px; width: 100%; height: 3em; }
    .result-box { background-color: #161b22; padding: 20px; border-radius: 15px; border-left: 5px solid #1f6feb; }
    </style>
    """, unsafe_update=True)

with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Integrated Sources: IELTS Academic | Liz | EZ Academy")

st.title("🎓 IELTS Master AI Tutor")
st.write("Your personal professional coach based on world-class standards.")

tabs = st.tabs(["✍️ Writing Analysis", "🗣️ Speaking Practice", "⚡ EZ Tactics"])

with tabs[0]:
    essay = st.text_area("Paste your essay here for deep analysis:", height=300)
    if st.button("Analyze Essay"):
        if api_key and essay:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-pro')
                prompt = f"As an IELTS Examiner, analyze this essay using IELTS Liz structure and EZ Academy tactics. Provide a band score and specific corrections: {essay}"
                with st.spinner("Analyzing using global standards..."):
                    response = model.generate_content(prompt)
                    st.markdown(f"<div class='result-box'>{response.text}</div>", unsafe_update=True)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter your API Key and Essay.")

with tabs[1]:
    st.subheader("Speaking Coach")
    st.info("Use your phone's microphone to speak, then paste the text here for evaluation.")
    st.write("**Topic:** Describe a successful person you admire.")
    st.text_area("Transcription of your speech:")

with tabs[2]:
    st.subheader("⚡ EZ Academy Tactics")
    st.success("Tactic 1: In Task 1, the 'Overview' is the most important part for a Band 7+.")
    st.info("Tactic 2: Use a mix of complex and simple sentences to show grammatical range.")
