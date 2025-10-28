from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings()
    return FAISS.from_documents(docs, embeddings)
