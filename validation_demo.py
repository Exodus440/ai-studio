# -*- coding: utf-8 -*-
"""방어적 UX — 파일 업로드 검증 템플릿 (실행형)
   streamlit run validation_demo.py
동봉한 5개 CSV를 차례로 올려 각 분기(info/success/warning/error)를 확인한다.
"""
import streamlit as st
import pandas as pd

st.title("방어적 UX 데모 — CSV 업로드 검증")

REQUIRED_COLS = {"날짜", "카테고리", "매출액"}

file = st.file_uploader("판매 데이터 CSV", type="csv")
if file is None:
    st.info("CSV 파일을 업로드하면 분석이 시작됩니다.")
    st.stop()                       # 이하 코드 실행 중단 (앱은 정상 대기)

try:
    df = pd.read_csv(file)
except UnicodeDecodeError:
    try:
        file.seek(0)                # 파일 포인터 되감기 후 재시도
        df = pd.read_csv(file, encoding="cp949")
        st.warning("인코딩을 CP949로 감지하여 읽었습니다.")
    except Exception:
        st.error("파일을 읽을 수 없습니다. UTF-8 또는 CP949 CSV인지 확인해 주세요.")
        st.stop()
except pd.errors.EmptyDataError:
    st.error("빈 파일입니다. 데이터가 포함된 CSV를 업로드해 주세요.")
    st.stop()

missing = REQUIRED_COLS - set(df.columns)
if missing:
    st.error(f"필수 컬럼 누락: {', '.join(missing)}. 제공된 양식을 사용해 주세요.")
    st.stop()

if df.isna().any().any():
    n = int(df.isna().any(axis=1).sum())
    st.warning(f"결측치가 포함된 행 {n}건은 집계에서 제외됩니다.")
    df = df.dropna()

st.success(f"데이터 {len(df):,}행 로드 완료")
st.metric("총 매출액", f"{df['매출액'].sum():,.0f}원")
st.bar_chart(df.groupby("카테고리")["매출액"].sum())
st.dataframe(df)
