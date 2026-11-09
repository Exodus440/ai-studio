# 11주차 Streamlit 대시보드 실습 자료

## 포함 파일
- `app.py` — 강의 골격 대시보드 (Streamlit UI)
- `backend.py` — 데이터 가공 모듈 (`summarize_by_month` 등, Streamlit 비의존)
- `sample_sales.csv` — 정상 데이터 (UTF-8), 컬럼: order_date, product, category, month, amount
- `sample_sales_cp949.csv` — 동일 데이터의 CP949 인코딩본 (인코딩 재시도 시나리오)
- `sample_sales_broken.csv` — `amount` 컬럼 누락본 (잘못된 CSV 방어 시나리오)
- `tests/test_backend.py` — 백엔드 pytest 예시
- `requirements.txt`

## 실행 방법
```bash
pip install -r requirements.txt
streamlit run app.py        # python app.py 가 아님에 주의!
```
브라우저(기본 http://localhost:8501)가 열리면 위 세 CSV를 차례로 업로드해 본다.

## 수동 검증 3종 시나리오 (과제 제출용)
1. `sample_sales.csv` 업로드 → 정상 동작(KPI·차트·표)
2. `sample_sales_cp949.csv` 업로드 → UnicodeDecodeError 없이 cp949로 재시도되어 동작
3. `sample_sales_broken.csv` 업로드 → 앱이 죽지 않고 "필수 컬럼이 없습니다" 안내 후 중단

## session_state 사용 설명 (예시)
`st.session_state.df`에 업로드·정제를 마친 DataFrame을 보관한다. 사이드바 필터를
바꾸면 Rerun이 일어나지만, 원본 데이터를 매번 다시 읽지 않고 session_state에서
재사용하기 위함이다.

## 백엔드 테스트
```bash
pytest -q
```
