# counter_fixed.py — session_state로 해결한 카운터
import streamlit as st

# [1단계: 초기화] 키가 없을 때만 최초 1회 생성 — 반드시 이 관용구를 사용
if "count" not in st.session_state:
    st.session_state.count = 0

# [3단계: 쓰기] 이벤트가 발생한 Rerun에서 값을 갱신
if st.button("클릭"):
    st.session_state.count += 1

# [2단계: 읽기] 항상 session_state에서 읽어 표시
st.write(f"클릭 수: {st.session_state.count}")

# 위젯에 key를 주면 그 값이 자동으로 session_state에 등록된다
st.text_input("검색어", key="query")
st.write(f"현재 검색어: {st.session_state.query}")

# 반환값 방식과 key 방식은 같은 값을 가리킨다
keyword = st.text_input("키워드", key="kw")
assert keyword == st.session_state.kw   # 항상 참
