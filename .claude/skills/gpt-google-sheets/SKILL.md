---
name: gpt-google-sheets
description: "Google Sheets(구글 시트·스프레드시트) 분석·특정 범위 편집·수식·차트·탭 작업 요청에 사용. 실제 탭 이름과 유한 범위를 확인하고 수식·서식·유효성 검사를 보존."
---

# Google Sheets 분석·정확한 범위 편집·수식·차트

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

메타데이터·범위·수식·유효성 검사 읽기 및 범위/배치 쓰기 필요.

## Claude 도구 대응

- Claude의 Google Drive 커넥터에서 확인된 도구: `search_files`, `list_recent_files`, `get_file_metadata`, `read_file_content`(댓글 포함 읽기 지원), `download_file_content`, `create_file`, `update_file`, `copy_file`, `share_file`, `get_file_permissions`, `trash_file`. 도구 접두어는 환경마다 다르므로 실제 목록에서 이름을 확인한다.
- 스키마로 확인한 제약: `update_file`은 제목·설명·부모 폴더(이동)만 바꾸며 **파일 내용은 덮어쓰지 못한다**. `create_file`은 업로드한 docx·xlsx·pptx·텍스트를 기본적으로 Google 네이티브 형식으로 변환한다(`disableConversionToGoogleType: true`면 원형 유지). `download_file_content`는 네이티브 파일을 `exportMimeType`(docx·xlsx·pptx·pdf 등)으로 내보내며 지정하지 않으면 일반 텍스트/CSV다. `revisionId`로 이전 버전을 받을 수 있다. `read_file_content`는 큰 파일에서 일부만 반환할 수 있다.
- 따라서 기존 네이티브 문서의 내용 수정 결과는 **새 파일**(원본 옆 복사본 등)로 만들어진다. 원본 대체(이름 교환·원본 휴지통 이동)는 사용자가 요청할 때만 한다.
- 현재 커넥터에는 Sheets 범위 쓰기·수식·차트 API가 없다. `download_file_content`의 기본 CSV 내보내기는 **첫 번째 탭만** 담고 수식이 값으로 바뀌므로, 탭 이름·수식·서식이 필요하면 `exportMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`로 받아 `xlsx` 스킬(openpyxl)로 탭 목록·범위·수식을 확인한다.
- 정밀 편집: xlsx 내보내기 → `xlsx` 스킬로 지정 범위만 편집·재계산 확인 → `create_file`로 새 스프레드시트 생성(변환 기본값) → 다시 읽어 확인.
- 원본 시트를 덮어쓰지 말고 새 파일 또는 사용자가 지정한 위치에 저장한다. 수식·서식이 변환 과정에서 바뀔 수 있음을 알린다.

## 작업 지침

1. 스프레드시트 ID, 실제 탭 이름, sheetId, 열 제목, 읽고 쓸 범위를 확인한다.

2. 탭 이름이나 전체 격자를 추측해 읽지 말고 필요한 유한 범위만 사용한다.

3. 값·수식·서식·유효성 검사·스마트 칩·네이티브 표 구조를 구분하고 보존한다.

4. 참조 템플릿은 통합문서를 네이티브로 복사하며 사용자가 지정한 단일 탭 추출일 때만 범위를 줄인다.

5. 행·열 삽입은 인접 데이터와 수식 참조, 드롭다운 및 서식 전파를 확인한 뒤 수행한다.

6. 수식 오류, 상대·절대 참조, 데이터 형식, 차트의 원본 범위와 축·단위를 확인한다.

7. 새 시트는 실제 사용 가능한 작성 도구에 맞춰 직접 네이티브로 만들거나 로컬 파일을 변환한다.

8. 원문에 등장하는 ChatGPT Spreadsheets 플러그인의 존재를 가정하지 않는다.

9. 쓰기 후 변경 범위, 수식 결과, 오류와 시각적 가독성을 확인하고 검증한 네이티브 링크를 제공한다.

## 출처

google-drive:google-sheets. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
