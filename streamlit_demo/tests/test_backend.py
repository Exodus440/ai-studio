# -*- coding: utf-8 -*-
"""backend 모듈 pytest 예시 — UI 없이 데이터 로직만 독립 검증."""
import pandas as pd
from backend import summarize_by_month, summarize_by_category, validate_columns


def _sample():
    return pd.DataFrame({
        "category": ["음료", "음료", "디저트", "디저트"],
        "month": ["2026-01", "2026-02", "2026-01", "2026-02"],
        "amount": [1000, 2000, 3000, 4000],
    })


def test_summarize_by_month():
    out = summarize_by_month(_sample())
    assert list(out.columns) == ["month", "amount"]
    assert out.loc[out["month"] == "2026-01", "amount"].iloc[0] == 4000
    assert out["amount"].sum() == 10000


def test_summarize_by_category():
    out = summarize_by_category(_sample())
    assert out.iloc[0]["category"] == "디저트"  # 합계가 더 큰 쪽이 먼저


def test_validate_columns():
    assert validate_columns(_sample()) == []
    broken = _sample().drop(columns=["amount"])
    assert validate_columns(broken) == ["amount"]
