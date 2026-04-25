from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_vector_store():
    # Load the career data
    loader = TextLoader("data/career_data.txt")
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    # Create embeddings using free HuggingFace model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Build and save FAISS index
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local("faiss_index")
    print("✅ Vector store built and saved!")

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store

if __name__ == "__main__":
    build_vector_store()