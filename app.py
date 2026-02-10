import streamlit as st
from google import genai
import time

# ==========================
# GEMINI CLIENT
# ==========================
client = genai.Client(
    api_key="AIzaSyCv0sITlQAr9R01zlmNmA3h25-uyB23KNs"
)

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ==========================
# CUSTOM CSS (RESPONSIVE)
# ==========================
st.markdown("""
<style>
.chat-wrapper {
    max-width: 760px;
    margin: auto;
}
.stChatMessage {
    padding: 12px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.title("⚙️ Controls")
    st.write("Gemini-powered chatbot")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ==========================
# MAIN TITLE
# ==========================
st.markdown("<div class='chat-wrapper'>", unsafe_allow_html=True)
st.title("🤖 Gemini Chatbot")
st.caption("Fast • Responsive • Streamlit UI")

# ==========================
# SESSION STATE
# ==========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# DISPLAY CHAT HISTORY
# ==========================
for role, content in st.session_state.messages:
    with st.chat_message(
        role,
        avatar="🧑" if role == "user" else "🤖"
    ):
        st.markdown(content)

# ==========================
# CHAT INPUT
# ==========================
prompt = st.chat_input("Type your message…")

if prompt:
    # Show user message
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # Bot response with typing effect
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            time.sleep(0.4)
            st.markdown(response.text)

    st.session_state.messages.append(("assistant", response.text))

st.markdown("</div>", unsafe_allow_html=True)
