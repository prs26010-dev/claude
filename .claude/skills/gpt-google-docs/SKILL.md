---
name: gpt-google-docs
description: "Google Docs(구글 문서) 작성·수정·서식 유지·템플릿 복사 요청에 사용. 표·목록·스마트칩을 평탄화하지 않고 필요한 범위만 편집하며, 편집 후 다시 읽어 검증."
---

# Google Docs 작성·편집·서식 유지

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

네이티브 문서 읽기와 batch update에 해당하는 쓰기 기능 필요.

## Claude 도구 대응

- Claude의 Google Drive 커넥터에서 확인된 도구: `search_files`, `list_recent_files`, `get_file_metadata`, `read_file_content`(댓글 포함 읽기 지원), `download_file_content`, `create_file`, `update_file`, `copy_file`, `share_file`, `get_file_permissions`, `trash_file`. 도구 접두어는 환경마다 다르므로 실제 목록에서 이름을 확인한다.
- 현재 Drive 커넥터에는 Docs `batchUpdate`(인덱스 단위 삽입·삭제)가 없다. 읽기는 `read_file_content`, 새 문서는 `create_file`로 만든다.
- 기존 문서의 서식 보존 편집이 필요하면 `download_file_content`로 .docx를 받아 `anthropic-skills:docx` 스킬로 편집한 뒤 사용자에게 업로드 방식을 확인한다. 원본 네이티브 문서를 덮어쓰기 전에 반드시 확인한다.
- 인덱스·requiredRevisionId 관련 지침은 Docs API를 직접 쓰는 MCP가 연결된 경우에만 적용한다.

## 작업 지침

1. 문서 ID, 대상 탭, 현재 문단·표·목록·내장 요소를 읽는다.

2. 작은 변경은 필요한 범위만 편집하고 표·드롭다운·스마트 칩을 일반 텍스트로 평탄화하지 않는다.

3. 제목과 본문은 네이티브 문단 스타일을 쓰고 기존 문서에서는 주변 형식을 따른다.

4. Google Docs 인덱스는 UTF-16 코드 단위이며, 배치의 앞선 삽입·삭제가 뒤 인덱스를 바꾼다는 점을 반영한다.

5. 가능하면 requiredRevisionId와 같은 쓰기 제어로 동시 수정 충돌을 막는다.

6. 결과가 불확실하면 재시도 전에 현재 상태를 확인한다.

7. 템플릿은 네이티브 복사로 보존한다.

8. Word 변환은 사용자가 변환을 요청한 경우에 수행하고 소스 파일을 보존한다.

9. 적용한 영역을 다시 읽어 내용·위치·주변 구조를 확인한다.

10. 페이지 적합성이나 이미지 배치가 중요하면 PDF로 내보내 렌더링을 확인한다.

11. 일반 링크로 출처와 산출물을 전달한다.

12. 원문 라우터와 Docs 본문에는 새 문서 생성 방식에 차이가 있으므로, 실제 연결 기능과 사용자가 원하는 파일 형식을 기준으로 선택하고 과거 지침만으로 불필요한 형식 변환을 강제하지 않는다.

## 출처

google-drive:google-docs. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
