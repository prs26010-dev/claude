---
name: gpt-connected-document-control
description: "Codex의 '연결된 문서 세션'을 조작하던 작업을 다시 하려는 요청에서 /gpt-connected-document-control 로만 실행. 일반 Google 문서·Office 파일 작업에는 사용하지 않음."
disable-model-invocation: true
---

# 연결된 문서 세션 탐색·지원 작업 실행

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

Codex 문서 세션은 Claude 세션으로 자동 연결되지 않음. 대응 MCP/확장 기능 필요.

## Claude 도구 대응

- Claude에는 Codex 문서 세션 브리지가 없다. 일반 문서는 `gpt-google-docs`/`gpt-google-sheets`/`gpt-google-slides` 또는 docx·xlsx·pptx 스킬로 처리한다.

## 작업 지침

1. 현재 연결된 문서 세션을 실제로 열거하고 대상을 고른다.

2. 선택한 세션이 제공하는 도구 스키마를 조회한 뒤 그 스키마에 맞춰 인자를 구성한다.

3. 실행에 안정적인 idempotency_key를 사용하고 결과가 불확실하면 중복 실행 전 상태를 확인한다.

4. 연결된 세션이 없으면 일반 Google 문서나 로컬 Office 파일을 연결 세션처럼 취급하지 않는다.

5. 일반 문서 작업은 해당 Drive/Docs/Sheets/Slides 또는 로컬 문서 작성 기능으로 처리한다.

## 출처

추가 문서 제어 도구 3개에서 재구성. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
