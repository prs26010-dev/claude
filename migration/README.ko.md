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

## 2차 보완 (2026-10-18)

이 세션에 실제 연결된 도구의 스키마(Google Drive 커넥터, 한국 법령 MCP `법령mcp`, 예약 작업·커넥터 조회 도구)를 읽고 스킬을 대조했다.

| 부족했던 점 | 보완 |
| --- | --- |
| 법률서면: "인용 검증 도구 없음"으로 적혀 있었으나 법령 MCP에 `legal_analysis`(인용 실존 검증·판례 변경 확인·행위시법)와 `get_annexes`·`legal_research`가 있음 | 도구 대응표 추가, 초안 전체 인용 검증·인용 대조표 절차를 작업 지침에 넣음 |
| 법률서면: 기존 MCP 전용 지침(case_handle, refresh_case 등)이 공통 지침과 섞여 미연결 시 혼란 | "기존 MCP 연결 시에만" 절로 분리 |
| 법률서면: HWP를 커넥터가 읽는다고 가정 | `read_file_content` 지원 형식에 HWP가 없음을 명시, 다운로드 후 로컬 변환 또는 변환본 요청 |
| 변호인의견서 전용 스킬과의 역할 구분 없음 | `draft-investigation-opinions`로 넘기는 경우 명시 |
| Drive 계열: `update_file`이 내용을 바꿀 수 있는지 불명확, "제자리 수정" 지침과 충돌 | 제목·설명·이동만 가능함을 명시, 수정본은 새 파일로 만들고 원본 대체는 요청 시만 |
| Drive: 이동 지원 여부를 "먼저 확인"하라고만 함 | `parentId`로 이동 가능함을 확인해 반영 |
| Sheets: CSV 내보내기가 첫 탭만 담고 수식이 사라지는 점 누락 | xlsx 내보내기로 탭·수식 확인하도록 수정 |
| Docs·Slides: 내보내기 MIME, 업로드 시 네이티브 변환, PDF 렌더링 확인 방법 없음 | 구체 절차 추가 |
| 예약: 도구 이름만 나열, cron 기본 UTC·세션 한정 cron 7일 만료·커넥터 지정 누락 | 실행 방식별 차이와 확인 절차 추가 |
| GitHub: 저장소에 없는 `tools/catalog.json` 참조, 클라우드 세션 저장소 범위·`gh` 부재 미반영 | 참조 삭제, `list_repos`/`add_repo`·PR 구독 절차 추가 |
| 실행 환경: 클라우드 프록시·CA·디스크 할당량 진단 방법 없음 | 확인 명령과 금지 사항(TLS 끄기 등) 추가 |
| 연결 관리: 커넥터·스킬 상태를 조회하는 실제 도구 미반영 | `ListConnectors`·`ListSkills`·`SearchMcpRegistry` 등과 `enabledInChat` 해석 추가 |
| Sites: Artifact 게시 경로 미반영 | claude.ai 비공개 게시 가능·자체 도메인 아님을 명시 |
| SETUP 문서가 저장소에 없는 `install.py`·`claude-code/`를 안내 | 복사 명령으로 교체, 한국 법령 MCP 행 추가 |
| ZIP·WORKFLOWS를 손으로 맞춰 SKILL.md와 어긋날 위험 | `build_web_package.py`로 생성, `--check`로 동기 확인 |

스킬을 고친 뒤에는 `python3 migration/build_web_package.py`를 실행하고, 바뀐 ZIP을 claude.ai 설정 → 기능 → 스킬에서 다시 올린다.

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
