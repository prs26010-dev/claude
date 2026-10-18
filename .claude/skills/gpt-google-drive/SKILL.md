---
name: gpt-google-drive
description: "Google Drive 파일 찾기·열기·복사·이동·이름변경·공유·삭제·내보내기·다운로드 요청에 사용(드라이브, 구글 드라이브, 폴더, 파일 링크). 내용 편집은 Docs/Sheets/Slides 스킬로 넘긴다."
---

# Drive 파일 탐색·정리·복사·이동·내보내기

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

Google Drive 커넥터/MCP/API 재연결 필요. 도구별 읽기·쓰기 범위를 확인한다.

## Claude 도구 대응

- Claude의 Google Drive 커넥터에서 확인된 도구: `search_files`, `list_recent_files`, `get_file_metadata`, `read_file_content`(댓글 포함 읽기 지원), `download_file_content`, `create_file`, `update_file`, `copy_file`, `share_file`, `get_file_permissions`, `trash_file`. 도구 접두어는 환경마다 다르므로 실제 목록에서 이름을 확인한다.
- 스키마로 확인한 제약: `update_file`은 제목·설명·부모 폴더(이동)만 바꾸며 **파일 내용은 덮어쓰지 못한다**. `create_file`은 업로드한 docx·xlsx·pptx·텍스트를 기본적으로 Google 네이티브 형식으로 변환한다(`disableConversionToGoogleType: true`면 원형 유지). `download_file_content`는 네이티브 파일을 `exportMimeType`(docx·xlsx·pptx·pdf 등)으로 내보내며 지정하지 않으면 일반 텍스트/CSV다. `revisionId`로 이전 버전을 받을 수 있다. `read_file_content`는 큰 파일에서 일부만 반환할 수 있다.
- 따라서 기존 네이티브 문서의 내용 수정 결과는 **새 파일**(원본 옆 복사본 등)로 만들어진다. 원본 대체(이름 교환·원본 휴지통 이동)는 사용자가 요청할 때만 한다.
- 이동은 `update_file`의 `parentId`로 한다(기존 부모가 교체됨). 대상 폴더 ID는 `search_files`(`mimeType = 'application/vnd.google-apps.folder'`)로 확인한다.
- 이름 변경은 `update_file`의 `title`, 폴더 만들기는 `create_file`(`application/vnd.google-apps.folder`).
- 삭제는 `trash_file`(휴지통 이동)이며 영구 삭제가 아니다. 사용자가 요청한 경우에만 실행한다.

## 작업 지침

1. 파일 URL이나 ID를 확정하고, 제목만 있으면 실제 검색으로 대상을 찾는다.

2. 파일 메타데이터의 MIME 유형을 확인해 네이티브 Docs/Sheets/Slides와 업로드된 일반 파일을 구분한다.

3. 탐색과 파일 수명주기는 Drive에서 처리하고, 내용 편집은 해당 문서 종류의 스킬로 넘긴다.

4. 이동은 확인한 대상 폴더와 현재 부모를 기준으로 수행하고 관련 없는 폴더 관계는 보존한다.

5. 템플릿은 원본 전체를 복사한 뒤 복사본을 편집한다.

6. 사용자가 기존 파일 편집을 요청했으면 제자리 수정이 가능한 도구가 있는지 확인하고, 현재 커넥터처럼 내용 덮어쓰기가 없으면 수정본을 새 파일로 만들었다는 점을 분명히 알린다.

7. 버전 비교는 실제 현재본과 해당 리비전(`download_file_content`의 `revisionId`)을 읽고 비교한다.

8. 공유 상태나 삭제는 사용자 요청 범위에서만 변경한다.

9. 내보내기와 다운로드는 연결 도구가 반환한 파일 참조로 처리하고 완료된 결과를 읽어 확인한다.

10. 출처와 산출물은 실제 확인한 링크로 표시한다.

11. ChatGPT라는 기본 폴더명은 이식하지 않으며, 사용자가 지정한 위치 또는 확인한 작업 위치를 사용한다.

## 출처

google-drive:google-drive. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
