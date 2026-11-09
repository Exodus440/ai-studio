# -*- coding: utf-8 -*-
"""패턴 ③ 대화 내역 누적 챗봇 (mock)  —  streamlit run chatbot_demo.py
13주차에 get_ai_reply 내부만 실제 Claude API 호출로 교체한다."""
import streamlit as st

def get_ai_reply(messages: list[dict]) -> str:
    """대화 내역을 받아 어시스턴트 응답 1개를 반환한다.
    [12주차] mock 구현 / [13주차] 함수 내부만 Claude API 호출로 교체.
    시그니처(입력: messages, 출력: str)는 절대 바꾸지 않는다."""
    last = messages[-1]["content"]
    return f"(mock 응답) '{last}'에 대한 분석 결과를 준비 중입니다."

st.title("매출 데이터 Q&A 챗봇")

# 1. 대화 내역 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "안녕하세요! 업로드된 매출 데이터에 대해 질문해 주세요."}
    ]

# 2. 지금까지의 대화 전체를 다시 그린다 (매 Rerun마다)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. 새 입력 처리: 사용자 메시지 추가 → 응답 생성 → 응답 추가
if prompt := st.chat_input("질문을 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    reply = get_ai_reply(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
