# answer-fill

> 사회문화 해설지 PDF 첫 페이지의 정답표(번호·정답①~⑤·배점)를 vision으로 읽어
> 표준 분류표 xlsx 템플릿의 정답·배점 컬럼에 자동 입력하는 Claude Code 스킬.

한국 입시 모의고사 출제팀이 매주 반복하는 "해설지 → 분류표 정답 옮기기" 작업을
**10분 → 30초**로 단축한다.

## 동작

1. PDF 첫 페이지를 `pypdfium2`로 PNG 렌더링
2. Claude Code의 vision으로 4×5 정답표 (20문항) 읽기
3. `openpyxl`로 표준 템플릿 복사 → B/C열(배점·정답) 교체
4. 해설지와 같은 폴더에 결과 xlsx 저장 (템플릿 원본은 안 건드림)

## 사용

```
/answer-fill {해설지.pdf}
/answer-fill {해설지.pdf} --template {다른_xlsx}
```

## 핵심 차별점

- PDF 텍스트 추출이 깨지는 **한글·원숫자(①~⑤)**를 vision으로 우회
- 일반 OCR보다 안정적
- 템플릿 구조(2~21행, B열 배점, C열 정답)는 오버라이드 가능

## 파일

- `SKILL.md` — Claude Code 스킬 정의·워크플로우
- `scripts/render_page.py` — PDF 페이지 → PNG
- `scripts/fill_answer.py` — xlsx 복사 + B/C열 교체

## 의존성

```
pip install openpyxl pypdfium2
```

## 타겟 사용자

사회문화 출제 콘텐츠팀. 현재 사용자 1명 (본인), 주 1회 사용 (회차 마감일).
