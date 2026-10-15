---
name: gpt-google-drive-comments
description: "Google Docs·Sheets·Slides 문서의 댓글 읽기·검토 의견 작성·답글·해결 요청에 사용(코멘트, 피드백 남기기). 본문 수정과 댓글 작업을 구분."
---

# Drive 문서 댓글 작성·답글·해결

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

파일·댓글 읽기 및 댓글 변경 기능 필요.

## Claude 도구 대응

- Claude의 Google Drive 커넥터에서 확인된 도구: `search_files`, `list_recent_files`, `get_file_metadata`, `read_file_content`(댓글 포함 읽기 지원), `download_file_content`, `create_file`, `update_file`, `copy_file`, `share_file`, `get_file_permissions`, `trash_file`. 도구 접두어는 환경마다 다르므로 실제 목록에서 이름을 확인한다.
- 댓글 읽기는 `read_file_content`의 `includeComments`로 가능하다. 현재 커넥터에는 댓글 작성·답글·해결 도구가 없으므로, 그 기능이 있는 MCP가 연결되지 않았다면 작성할 댓글 초안(위치·인용 문구·내용)을 목록으로 제공하고 직접 게시했다고 말하지 않는다.

## 작업 지침

1. 대상 파일과 실제 본문을 먼저 확인한다.

2. 댓글은 관찰 가능한 텍스트·셀·슬라이드·위치에 근거해 작성하고, 정확한 앵커를 지원하지 않는 커넥터에서는 이를 명시한다.

3. 한 파일에서 필요한 변경을 모아 중복을 피한다.

4. 답글과 해결은 실제 스레드 ID를 확인해 수행한다.

5. 지원되는 경우 검토 대상 문구와 변경 제안을 간결하게 연결한다.

6. 파일 내용 편집과 댓글 검토를 구분하고, 요청하지 않은 본문 수정을 하지 않는다.

7. 결과는 반환된 댓글·스레드 상태로 확인한다.

## 출처

google-drive:google-drive-comments. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
