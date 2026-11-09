# 12주차 Streamlit II 실습 자료 (상태 관리 3대 패턴 · 방어적 UX)

## 실행 파일 (각각 독립 실행)
| 파일 | 내용 | 실행 |
|---|---|---|
| `login_demo.py` | 패턴 ① 로그인/권한 상태 유지 | `streamlit run login_demo.py` |
| `wizard_demo.py` | 패턴 ② 다단계 조건 입력(Wizard) | `streamlit run wizard_demo.py` |
| `chatbot_demo.py` | 패턴 ③ 대화 내역 누적 챗봇(mock) | `streamlit run chatbot_demo.py` |
| `validation_demo.py` | 방어적 UX 파일 업로드 검증 템플릿 | `streamlit run validation_demo.py` |

- 로그인 데모 계정: `admin` / `1234` (관리자), `guest` / `1111` (뷰어)
- `chatbot_demo.py`의 `get_ai_reply`는 mock이며, 13주차에 함수 **내부만** 실제 Claude API 호출로 교체한다(시그니처 고정).

## 데이터 파일 — 검증 분기별 트리거 (교차 테스트 '오입력 3종 이상'용)
| 파일 | 올렸을 때 결과 |
|---|---|
| `sample_sales.csv` | 정상 → `st.success` (총매출·차트·표) |
| `sample_sales_cp949.csv` | `st.warning`("CP949로 감지하여 읽었습니다") 후 정상 |
| `sample_sales_missing.csv` | `st.error`("필수 컬럼 누락: 매출액") 후 중단 |
| `sample_sales_with_na.csv` | `st.warning`("결측치 … 행 제외") 후 정상 |
| `empty.csv` | `st.error`("빈 파일입니다") 후 중단 |

컬럼 스키마: `날짜, 카테고리, 상품명, 매출액` (검증 템플릿의 필수 컬럼 = 날짜/카테고리/매출액)

## 설치·실행
```bash
pip install -r requirements.txt
streamlit run validation_demo.py     # 4개 데모 중 하나 선택 실행
```
`python xxx.py` 가 아니라 반드시 `streamlit run xxx.py` 로 실행한다.
