---
name: gpt-plugin-management
description: "어떤 커넥터·MCP·플러그인·스킬이 연결돼 있는지, 무엇을 추가·인증해야 하는지 묻는 요청에 사용. 목록 표시·설치·인증·실제 호출 성공을 구분해 보고."
---

# 연결 도구 탐색·상태·권한 관리

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

Claude 커넥터/MCP 관리로 대응. ChatGPT 플러그인 설치 상태는 복사되지 않음.

## Claude 도구 대응

- Claude 웹·앱: 설정 → 커넥터에서 연결·인증한다. 사용자 스킬은 설정 → 기능(Capabilities) → 스킬에서 ZIP 업로드.
- Claude Code: `/mcp`로 MCP 연결 확인, `claude mcp add --transport http <이름> <URL>`로 원격 MCP 추가, 스킬은 `.claude/skills/` 또는 `~/.claude/skills/`.
- 계정 상태 조회 도구(있으면 사용): `ListConnectors`(커넥터의 `connected`·`enabledInChat`), `ListSkills`(claude.ai에 올린 스킬), `ListPlugins`. 새로 연결할 후보는 `SearchMcpRegistry` → `SuggestConnectors`. 이 도구들은 조회·제안만 하며 연결 자체는 사용자가 claude.ai에서 한다.
- `connected: true`인데 `enabledInChat: false`면 인증은 됐지만 이 대화에서 꺼진 상태다. 대화의 커넥터 설정에서 켜도록 안내한다. `connected: null`은 알 수 없음이다.
- 실제 호출 성공 여부는 해당 도구를 가벼운 읽기(예: Drive `list_recent_files`)로 한 번 호출해 확인한다.
- ChatGPT 플러그인 ID(`plugin://`, `mcp__codex_apps__*`)는 Claude에서 쓸 수 없다.

## 작업 지침

1. 요청한 일을 수행할 현재 도구가 있는지 먼저 확인한다.

2. 외부 서비스가 필요하면 이미 연결된 해당 커넥터/MCP의 실제 기능을 확인하고 없는 경우에만 추가 연결 대상을 찾는다.

3. 목록에 이름이 있는 상태, 설치 상태, 인증 완료, 실제 읽기/쓰기 성공을 구분한다.

4. 지원 여부나 권한 범위를 추측하지 않는다.

5. 설치·권한 변경·제거를 했다고 말할 때는 실제 반환 상태가 있어야 한다.

6. 이식 목록은 참고 자료이며 현재 Claude의 설치 목록이 아니다.

7. 다른 서비스의 이름이나 ChatGPT 전용 식별자를 Claude의 MCP 서버 주소로 사용하지 않는다.

## 출처

plugin-management:plugin-management. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
