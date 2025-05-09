import streamlit as st
from ai import get_ai_response
from interface import show_chat_history, get_user_input

st.title("Chat com IA (Streamlit)")

# Inicializa o histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens
show_chat_history(st.session_state.messages)

# Campo de entrada do usuário
prompt = get_user_input()
if prompt:
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtém resposta da IA e exibe
    with st.chat_message("assistant"):
        response = get_ai_response(prompt, st.session_state.messages)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
