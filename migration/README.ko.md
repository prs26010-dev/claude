# GPT → Claude 이식 (개선판)

Google Drive의 `GPT-to-Claude-migration-full.zip`(SHA-256 `e37cae26…8a59b4`, 체크섬 65개 일치 확인)을 바탕으로 변환 스킬 15개를 고친 결과다. 공개 저장소이므로 GPT 원문 스킬(`source-skills/`)과 도구 명세(`tools/`)는 올리지 않았다. 원본 ZIP은 Drive에 그대로 있다.

## 고친 점

| 문제 | 수정 |
| --- | --- |
| description이 "관련 요청에서 GPT 업무 흐름을 재현할 때"뿐이라 Claude가 언제 쓸지 판단하기 어려움 | 15개 모두 실제 요청 표현(구글 시트, 준비서면, 예약, PR 등)과 사용하지 않을 경우를 넣어 다시 씀 |
| description에 GPT 세션의 일시적 결과("최초 429, 재확인 404")가 들어 있음 | description에서 빼고 본문에 이식 당시 기록으로만 남김 |
| 스킬이 Claude에 없는 기능(Docs batchUpdate, Sheets 범위 쓰기, 댓글 작성, Slides 편집)을 전제로 함 | 각 스킬에 **Claude 도구 대응** 절 추가. Claude Google Drive 커넥터의 실제 도구(11개)와, 없는 기능은 docx·xlsx·pptx 스킬 경유 또는 초안 제공으로 대체 |
| Pets 3개·연결 문서 제어는 Claude에 백엔드가 없는데 자동 실행될 수 있음 | Claude Code판에 `disable-model-invocation: true` 추가(`/이름`으로만 실행). 웹판은 description에 명시 |
| 법률서면 스킬에 대체 경로가 없음 | 법률 MCP 미연결 시 Drive 커넥터로 사건자료 읽기, 한국 법령 MCP(`search_law` 등) 또는 law.go.kr로 법령 확인, 인용 대조표 제공 |
| 예약 스킬에 Claude 쪽 수단이 없음 | 클라우드 세션 예약 작업, `/loop`, OS cron + `claude -p`, .ics 대체 경로 추가. 시간대 `CRON_TZ=Asia/Seoul` 명시 |
| CLAUDE.md·프로젝트 지침이 설치 위치에 없는 "SETUP 문서"를 참조 | 스킬의 대응 절과 `migration/SETUP.ko.md`를 가리키도록 수정 |

## Claude Code

이 저장소에는 이미 설치되어 있다: `CLAUDE.md`, `.claude/skills/gpt-*` 15개. 저장소를 열고 `claude`를 실행하면 `/gpt-google-drive`처럼 쓸 수 있다.

다른 프로젝트나 모든 프로젝트에 쓰려면:

```text
cp -r .claude/skills/gpt-* /path/to/project/.claude/skills/   # 해당 프로젝트만
cp -r .claude/skills/gpt-* ~/.claude/skills/                    # 모든 프로젝트
```

## Claude 웹·앱

1. 설정 → 기능 → 스킬에서 `migration/skill-zips/`의 ZIP을 하나씩 업로드하고 켠다(각 ZIP은 `gpt-이름/SKILL.md` 한 폴더).
2. 또는 프로젝트를 만들어 `PROJECT_INSTRUCTIONS.ko.md`를 지침에 붙여 넣고 `WORKFLOWS.ko.md`를 참고 파일로 올린다.
3. 첫 메시지로 `START_PROMPT.ko.md`를 사용한다.
4. 연결 복원은 `SETUP.ko.md`를 따른다.
