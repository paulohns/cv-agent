import streamlit as st
from utils.cv_loader import load_cv
from utils.embeddings import create_vectorstore
from chains.qa_chain import build_qa_chain
from agents.router import route_question

st.set_page_config(page_title="Analisador de CV com IA", layout="wide")
st.title("🤖 Analisador Inteligente de Currículos")

uploaded_file = st.file_uploader("Carregue o CV (PDF, imagem ou HTML)", type=["pdf", "png", "jpg", "html"])
if uploaded_file:
    with st.spinner("Processando o CV..."):
        docs = load_cv(uploaded_file)
        vectorstore = create_vectorstore(docs)
        qa_chain = build_qa_chain(vectorstore)

    st.success("CV processado com sucesso!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Pergunte sobre o candidato")
    if user_input:
        specialist = route_question(user_input)
        response = qa_chain.run(user_input)
        st.session_state.chat_history.append((user_input, response))

    for q, r in st.session_state.chat_history:
        st.chat_message("user").write(q)
        st.chat_message("assistant").write(r)
