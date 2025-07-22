import streamlit as st
from processors.agent import call_agent

# Chatbot setup
favicon = 'craft_favicon.png'
st.title("Craft Sourcing Assistant")
st.logo(favicon,size="large")


# TODO: Configure role avatars and styling

# Inititalise history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type your soucing query here"):
    with st.chat_message("user", avatar="user_avatar_4.png"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = call_agent(prompt).output
    # Display assistant response in chat message container
    with st.chat_message("assistant",avatar="craft_favicon.png"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    print("Hello from uv-sourcing-assistant!")


if __name__ == "__main__":
    main()
