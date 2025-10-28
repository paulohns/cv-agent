from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
    return FAISS.from_documents(docs, embeddings)
