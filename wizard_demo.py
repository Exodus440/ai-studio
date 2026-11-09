# -*- coding: utf-8 -*-
"""패턴 ② 다단계 조건 입력 (Multi-step Wizard)  —  streamlit run wizard_demo.py"""
import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.wizard = {}            # 단계별 입력 누적 저장소

def go_next():
    st.session_state.step += 1

def go_prev():
    st.session_state.step -= 1

st.progress((st.session_state.step - 1) / 2)     # 진행률 표시 (3단계 기준)

if st.session_state.step == 1:
    st.header("1단계: 데이터 업로드")
    file = st.file_uploader("판매 데이터 CSV", type="csv")
    if file is not None:
        st.session_state.wizard["file"] = file
    st.button("다음 →", on_click=go_next,
              disabled=("file" not in st.session_state.wizard))

elif st.session_state.step == 2:
    st.header("2단계: 분석 옵션 선택")
    st.session_state.wizard["period"] = st.selectbox(
        "집계 단위", ["월별", "주별", "일별"])
    st.session_state.wizard["metric"] = st.radio(
        "분석 지표", ["매출 합계", "평균 주문 금액"])
    col1, col2 = st.columns(2)
    col1.button("← 이전", on_click=go_prev)
    col2.button("다음 →", on_click=go_next)

elif st.session_state.step == 3:
    st.header("3단계: 결과 확인")
    w = st.session_state.wizard
    st.write(f"선택: {w['period']} / {w['metric']}")
    # 실제 분석: 10주차에 완성한 백엔드 함수 호출
    # result = run_analysis(w["file"], w["period"], w["metric"])
    st.success("이 단계에서 백엔드 함수에 wizard 딕셔너리를 넘겨 분석을 실행합니다.")
    st.json({k: (v.name if hasattr(v, "name") else v) for k, v in w.items()})
    st.button("← 이전", on_click=go_prev)
