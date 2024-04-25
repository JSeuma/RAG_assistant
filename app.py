import streamlit as st
import retrieval

# Titol for the front-end
st.title("Buscador de información")
st.subheader(" ")
st.markdown('### Introce tu consulta detallada')

# Create list of messages
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Query for the argument query, the question the user wants to answwer
if query := st.chat_input("¿Cual es tua consulta?"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # Call the function retrieval to execute the RAG assistant
    with st.chat_message("assistant"):
        stream = retrieval(query)
        answer = stream["result"]
        response = st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})