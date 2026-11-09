# -*- coding: utf-8 -*-
"""
app.py — CSV 업로드 대시보드 (11주차 강의 골격 코드)

실행:  streamlit run app.py      (python app.py 가 아님에 주의!)
샘플:  sample_sales.csv (정상) / sample_sales_cp949.csv (인코딩) /
       sample_sales_broken.csv (amount 컬럼 누락 — 방어 동작 확인용)
"""
import streamlit as st
import pandas as pd
from backend import summarize_by_month, validate_columns

st.set_page_config(page_title="매출 대시보드", layout="wide")
st.title("월별 매출 분석 대시보드")

# 1. 입력: 파일 업로드
uploaded = st.file_uploader("판매 데이터 CSV를 드래그 앤 드롭하세요", type="csv")
if uploaded is None:
    st.info("CSV 파일을 업로드하면 분석이 시작됩니다.")
    st.stop()  # 이후 코드 실행 중단 — 조건 미충족 시 표준 패턴

# 2. 처리: 인코딩 이슈 대응(3주차) 후 로드
try:
    df = pd.read_csv(uploaded)
except UnicodeDecodeError:
    uploaded.seek(0)  # 파일 포인터를 처음으로 되돌린 뒤 재시도
    df = pd.read_csv(uploaded, encoding="cp949")

# 2-1. 잘못된 입력 방어: 필수 컬럼 확인 (앱이 죽지 않고 안내)
missing = validate_columns(df)
if missing:
    st.error(f"필수 컬럼이 없습니다: {missing}. "
             f"category, month, amount 컬럼이 있는 CSV를 올려 주세요.")
    st.stop()

# 3. 가공 결과를 session_state에 보관 (이후 Rerun에서 재사용)
st.session_state.df = df
monthly = summarize_by_month(df)  # 백엔드: 월별 매출 합계 DataFrame 반환

# 4. 필터 (사이드바)
categories = ["전체"] + sorted(df["category"].unique().tolist())
selected = st.sidebar.selectbox("상품 카테고리", categories)
view = df if selected == "전체" else df[df["category"] == selected]

# 5. 출력: KPI → 차트 → 원본 표
col1, col2 = st.columns(2)
col1.metric("총 매출", f"{view['amount'].sum():,.0f}원")
col2.metric("주문 건수", f"{len(view):,}건")
st.bar_chart(monthly, x="month", y="amount")
st.dataframe(view)
