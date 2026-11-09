import streamlit as st
import pandas as pd

st.set_page_config(page_title="레이아웃 데모", layout="wide")  # 반드시 첫 st 명령

# 사이드바: 필터·설정 등 보조 컨트롤의 표준 위치
category = st.sidebar.selectbox("카테고리", ["전체", "음료", "디저트"])

# 컬럼: 화면을 가로로 분할
col1, col2, col3 = st.columns(3)
col1.metric("총 매출", "1,250,000원", "+12%")
col2.metric("주문 건수", "342건", "-3%")
col3.metric("객단가", "3,655원", "+8%")

# 탭과 익스팬더: 내용을 접어 화면을 정리
tab1, tab2 = st.tabs(["차트", "원본 데이터"])
with st.expander("도움말 보기"):
    st.write("이 대시보드는 업로드된 CSV를 분석합니다.")
