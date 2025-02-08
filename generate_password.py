import streamlit as st
import secrets
import string

def generate_password(length, use_uppercase, use_symbols):
    characters = string.ascii_lowercase + string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += "!#$%&@+-_"

    return ''.join(secrets.choice(characters) for _ in range(length))

st.title("🔐 Password Generator")

# Options
length = st.number_input("Password Length", min_value=4, max_value=50, value=17, step=1)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

password = ""

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_symbols)
    st.session_state["password"] = password

if "password" in st.session_state and st.session_state["password"]:
    st.code(f"{st.session_state['password']}", language="planetext")

    if st.button("Clear Password"):
        st.session_state["password"] = ""
        st.rerun()