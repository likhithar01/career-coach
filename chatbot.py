from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from vector_store import load_vector_store
import os

load_dotenv()

def create_career_coach():
    # Load FAISS vector store
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Load Groq LLM (free & fast)
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )

    # Memory so it remembers the conversation
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    # Custom career coach personality prompt
    prompt = PromptTemplate.from_template("""
You are an expert AI Career Coach. You help people with:
- Resume writing and review
- Interview preparation
- Job search strategies
- Salary negotiation
- Career path guidance

Use the context below to answer the question. Be friendly, 
specific, and encouraging. If you don't know something, say so honestly.

Context: {context}

Chat History: {chat_history}

Question: {question}

Answer:
""")

    # Build the full chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return chain


def ask_coach(chain, question):
    response = chain.invoke({"question": question})
    return response["answer"]