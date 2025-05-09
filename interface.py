import streamlit as st

def show_chat_history(messages):
    """
    Exibe o histórico de mensagens no formato de chat.
    """
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    """
    Exibe o campo de entrada do usuário e retorna o texto digitado.
    """
    return st.chat_input("Digite sua mensagem...")
