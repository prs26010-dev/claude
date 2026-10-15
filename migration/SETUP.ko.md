# 외부 연결을 실제로 복원하는 방법

지침 파일을 읽는 것과 외부 서비스에 접근하는 것은 별도다. 이 패키지는 인증 토큰, OAuth 세션, MCP 서버 프로그램, 계정 데이터나 호스팅 자원을 복제하지 않는다. 모든 연결 설정은 아직 대기 상태다.

## Claude 웹·앱

Claude의 커넥터 메뉴에서 사용 가능한 Google Drive·GitHub 연결을 선택하고 본인 계정으로 인증한다. 제공되는 읽기·쓰기 기능을 확인한다. 검색만 되는 연결로 파일 편집까지 된다고 가정하지 않는다.

기존 법률서면 서버를 양쪽에서 그대로 쓰려면 원래 서버의 관리 화면 또는 소스에서 Claude 클라이언트용 MCP URL과 인증 지원을 확인해야 한다. 공개된 원격 MCP 주소가 있으면 사용자 커넥터로 추가한다. Claude의 클라우드에서 서버에 접근할 수 있어야 하며, 로컬 stdio 서버를 웹 채팅에서 바로 호출하는 구성으로 설명하지 않는다. 현재 GPT의 일시적인 내부 게이트웨이 주소는 재사용하지 않는다.

## Claude Code

이 패키지의 `claude-code/`에서 시작하면 로컬 스킬이 프로젝트 범위로 배치되어 있다. 기존 프로젝트로 옮기려면 아래 설치 도우미를 사용한다.

```text
python3 install.py --project /absolute/path/to/project --dry-run
python3 install.py --project /absolute/path/to/project
```

기존 `CLAUDE.md`를 유지할 때는 설치 명령에 `--skills-only`를 추가하고 지침은 직접 통합한다.

원격 MCP 서버가 실제로 준비되면 다음 형식으로 추가한다. 대괄호 부분은 실제 값으로 바꾼다. 이 문서에는 미확인 서버 주소나 인증 값을 넣지 않았다.

```text
claude mcp add --transport http --scope user [server-name] [verified-https-mcp-url]
```

서버가 제공하는 인증 절차를 따른다. Code의 `/mcp`에서 연결과 도구를 확인한다. 별도 JSON 파일을 만들어 쓸 경우 프로젝트 설정은 `.mcp.json` 형태이지만, 이 패키지는 존재하지 않는 서버 설정을 자동 생성하지 않는다.

## 기능별 필요한 것

| 기능 | 복원에 필요한 것 | 확인 방법 |
| --- | --- | --- |
| Google Drive·Docs·Sheets·Slides | 지원되는 연결·인증·해당 편집 권한 | 사용자가 지정한 시험 파일의 메타데이터와 소범위 읽기; 편집은 지정한 복사본에서만 확인 |
| GitHub | 저장소 범위를 지정한 인증된 연결 또는 git/gh | 지정 저장소와 대상 브랜치 읽기 |
| 법률서면 MCP | 기존 서버 주소·소스 또는 재배포 권한, Google/공식 법령 API 설정, HWP/HWPX/OCR 지원 | connection_status가 먼저 성공해야 함. 그 후 사용자가 지정한 사건만 열기 |
| Sites | 원본 사이트 소스와 대상 호스팅·도메인·저장소 설정 | 빌드 및 해당 배포 제공자의 성공 URL |
| Pets | 원본 스프라이트·지원 런타임·검증 계약·이미지 도구 | 프레임 구조와 실제 재생 확인. ChatGPT 컬렉션 등록은 별도 |
| 예약 | 실제 백그라운드 스케줄러와 사용자의 시간대 | 작업 ID·활성 상태·다음 실행 시각 확인 |
| 연결 문서 제어 | Claude에서 사용할 수 있는 세션 브리지/확장·MCP | 세션 열거 → 스키마 확인 → 요청 작업 실행 |
| 실행 환경 | Claude 실행 머신의 네트워크·도구·인증 구성 | 현재 상태 확인. GPT 세션의 환경 ID는 재사용하지 않음 |
| 웹 검색·이미지 제작 | 현재 Claude의 지원 기능 또는 외부 API | 실제 검색 페이지/생성 파일 확인 |

## 공식 형식 확인 근거

2026-10-15 조회. UI와 사용 가능 범위는 현재 계정·조직 정책에 따를 수 있다.

- [Claude Code 스킬 위치와 SKILL.md](https://code.claude.com/docs/en/skills)
- [사용자 스킬 ZIP 작성·업로드](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Claude 원격 MCP 커넥터](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Claude Code MCP 연결](https://code.claude.com/docs/en/mcp)

