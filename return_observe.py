# rerun_observe.py — Rerun을 눈으로 확인하기
import streamlit as st
import datetime

st.title("Rerun 확인 테스트")
st.write(f"스크립트 실행 시각: {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
st.text_input("아무 글자나 입력 후 Enter")
st.slider("슬라이더를 움직여 보세요", 0, 100)
