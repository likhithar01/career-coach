import streamlit as st
from chatbot import create_career_coach, ask_coach
from pypdf import PdfReader
import io

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🎯",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("🎯 Career Coach")
    st.markdown("---")
    st.markdown("### 💡 Ask me about:")
    st.markdown("- 📄 Resume writing")
    st.markdown("- 🎤 Interview preparation")
    st.markdown("- 🔍 Job search strategies")
    st.markdown("- 💰 Salary negotiation")
    st.markdown("- 🚀 Career paths")
    st.markdown("- 🛠️ In-demand skills")
    st.markdown("- 🌐 LinkedIn & personal brand")
    st.markdown("- 🎓 Higher education advice")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! 👋 I'm your AI Career Coach. Ask me anything!"}
        ]
        st.rerun()
    st.caption("Powered by Groq + LangChain + FAISS")

# Main UI
st.title("🎯 AI Career Coach")
st.caption("Your personal AI-powered career advisor — resumes, interviews, jobs & more!")

# Initialize
if "coach" not in st.session_state:
    with st.spinner("⚡ Loading your career coach..."):
        st.session_state.coach = create_career_coach()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 I'm your AI Career Coach. Ask me anything about resumes, interviews, salaries, or career paths! You can also upload your resume below for a personalized review! 📄"}
    ]

# ── Resume Upload Section (main page) ──
with st.expander("📄 Upload Your Resume for Personalized Review", expanded=False):
    uploaded_file = st.file_uploader("Choose your PDF resume", type=["pdf"])
    if uploaded_file:
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
        st.session_state.resume_text = resume_text
        st.success("✅ Resume uploaded successfully!")

        if st.button("🔍 Review My Resume"):
            review_prompt = f"Please review this resume and give detailed, specific feedback on how to improve it:\n\n{resume_text[:2000]}"
            with st.spinner("Analyzing your resume..."):
                response = ask_coach(st.session_state.coach, review_prompt)
                st.session_state.messages.append({"role": "user", "content": "Please review my uploaded resume."})
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

st.markdown("---")

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if user_input := st.chat_input("Ask your career question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_coach(st.session_state.coach, user_input)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})