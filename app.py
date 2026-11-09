# app.py
import streamlit as st

st.title("나의 첫 Streamlit 앱")
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"환영합니다, {name}님!")
