# -*- coding: utf-8 -*-
"""패턴 ① 로그인/권한 상태 유지  —  streamlit run login_demo.py
데모 계정: admin/1234 (role=admin), guest/1111 (role=viewer)"""
import streamlit as st

# --- 데모용 사용자 DB (실제로는 인증 서버/DB. 비밀번호 평문 저장 금지) ---
USERS = {"admin": {"pw": "1234", "role": "admin"},
         "guest": {"pw": "1111", "role": "viewer"}}

# 1. 초기화 가드: 최초 실행 시에만 기본값 설정
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None

def login(username, pw):
    user = USERS.get(username)
    if user and user["pw"] == pw:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user["role"]
        return True
    return False

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None

# 2. 화면 분기: 로그인 전 / 후
if not st.session_state.logged_in:
    st.title("로그인")
    uid = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    if st.button("로그인"):
        if login(uid, pw):
            st.rerun()                # 상태 변경 직후 화면 즉시 갱신
        else:
            st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
else:
    st.sidebar.write(f"{st.session_state.username} 님")
    st.sidebar.button("로그아웃", on_click=logout)

    st.title("대시보드")
    st.write("모든 사용자가 보는 영역")
    # 3. 권한(role) 기반 화면 제어
    if st.session_state.role == "admin":
        st.subheader("관리자 전용: 데이터 업로드")
        st.file_uploader("원본 CSV 업로드")
