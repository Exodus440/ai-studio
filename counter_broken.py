# counter_broken.py — 의도대로 동작하지 않는 코드
import streamlit as st

count = 0              # (1) Rerun마다 매번 여기서 0으로 초기화
st.title("Counter 테스트")
if st.button("클릭"):  # (2) 방금 클릭했다면 이번 Rerun에서만 True
    count += 1         # (3) 0 + 1 = 1
st.write(f"클릭 수: {count}")  # 결과: 누를 때마다 항상 1, 다른 위젯 만지면 0
