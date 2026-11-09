# -*- coding: utf-8 -*-
"""
backend.py — 데이터 가공 모듈 (10주차 팀 백엔드 예시)

원칙: 이 모듈은 Streamlit을 전혀 모른다(import 하지 않는다).
      순수 pandas 함수만 두어 pytest로 독립 테스트할 수 있게 한다.
      app.py(UI)는 이 함수들을 '호출'만 한다.
"""
import pandas as pd

REQUIRED_COLUMNS = ["category", "month", "amount"]


def validate_columns(df: pd.DataFrame) -> list[str]:
    """필수 컬럼 중 빠진 것들의 목록을 반환한다(없으면 빈 리스트)."""
    return [c for c in REQUIRED_COLUMNS if c not in df.columns]


def summarize_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """월별 매출 합계 DataFrame을 반환한다. (columns: month, amount)

    app.py에서 st.bar_chart(monthly, x="month", y="amount")로 바로 그릴 수 있는
    형태로 돌려준다.
    """
    result = (
        df.groupby("month", as_index=False)["amount"]
          .sum()
          .sort_values("month")
          .reset_index(drop=True)
    )
    return result


def summarize_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """카테고리별 매출 합계 DataFrame. (columns: category, amount)"""
    result = (
        df.groupby("category", as_index=False)["amount"]
          .sum()
          .sort_values("amount", ascending=False)
          .reset_index(drop=True)
    )
    return result
