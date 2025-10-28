from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def build_qa_chain(vectorstore):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = ChatGroq(
        model="mixtral-8x7b",
        temperature=0.3,
        api_key=os.getenv("GROQ_API_KEY")
    )
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
