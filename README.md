# 🎯 LLM-Powered Career Coach

An AI chatbot that gives personalized career advice using LangChain, Groq (LLaMA 3), and FAISS semantic search.

## Features
- 💬 Conversational chat with memory
- 🔍 Semantic search over career knowledge base (FAISS)
- ⚡ Powered by Groq's free LLaMA 3 API
- 🖥️ Clean Streamlit UI

## Tech Stack
- **LangChain** – LLM orchestration & chains
- **Groq + LLaMA 3** – Free, fast LLM
- **FAISS** – Vector similarity search
- **HuggingFace Embeddings** – Semantic embeddings
- **Streamlit** – Web UI

## Setup

1. Clone the repo
2. Install dependencies:
pip install -r requirements.txt
3. Add your Groq API key to `.env`:
GROQ_API_KEY=your_key_here
4. Build the vector store:
python vector_store.py
5. Run the app:
streamlit run app.py

## Project Structure
career-coach/
├── data/career_data.txt     ← Knowledge base
├── vector_store.py          ← FAISS index builder
├── chatbot.py               ← LangChain + Groq logic
├── app.py                   ← Streamlit UI
├── requirements.txt
└── .env
🌐 **Live Demo:** [Click here](https://career-coach-7cflzzmsshx5w6wkux5qhf.streamlit.app/)
