---
name: gpt-cloud-environment-runtime
description: "실행 환경·네트워크·프록시·Docker·클라우드 인증(gcloud·aws 등) 점검이나 '왜 접속이 안 되지' 같은 환경 문제 진단 요청에 사용. 토큰·환경변수 값은 출력하지 않음."
---

# 실행 환경·네트워크·Docker·클라우드 인증 점검

이 문서는 GPT의 스킬과 노출 도구를 바탕으로 Claude용으로 새로 작성한 이식 지침이다. 원문 보관본이나 과거 사용자 메모리가 아니다. 여기 언급된 도구는 현재 Claude의 연결 목록과 스키마에서 실제 지원 여부를 확인한 뒤 사용한다. 없는 기능의 실행·연결·게시 성공을 주장하지 않는다.

## 연결 전제

Claude가 사용하는 실제 머신/컨테이너 정책에 맞게 재설정 필요.

## Claude 도구 대응

- Claude Code 클라우드 세션: 네트워크 정책·환경변수·설정 스크립트는 claude.ai의 환경 설정에서 바꾼다. 막히거나 사용자가 설정 방법을 물으면 `read_documentation`(주제: `environment.network`, `environment.secrets`, `environment.setup_script`, `environment.dependencies`, `github.access`, `connectors.add`, `session.resources`)으로 현재 절차를 확인한다. 이 도구는 사용자에게 설정 화면 버튼도 보여 준다.
- 클라우드 세션의 외부 HTTPS는 에이전트 프록시를 거친다. TLS 오류·403/407·전송 끊김이면 `/root/.ccr/README.md`와 `curl -sS "$HTTPS_PROXY/__agentproxy/status"`로 원인을 확인하고, 필요하면 CA 번들 `/root/.ccr/ca-bundle.crt`를 도구에 지정한다. TLS 검증을 끄거나 `HTTPS_PROXY`를 해제하지 않는다.
- 클라우드 세션의 디스크는 세션별 할당량이다. `df`의 Avail이 0이면 할당량 소진이므로 빌드 산출물·캐시를 지워 확보한다.
- Claude Code 로컬: 사용자의 셸 환경과 `settings.json`(`update-config` 스킬)을 따른다.

## 작업 지침

1. 작업할 환경의 현재 경로, 도구, 쓰기 가능 위치와 네트워크 정책을 확인한다.

2. 토큰 값이나 전체 환경 변수, 인증 파일 내용을 출력하지 않는다.

3. 원문에 나온 Codex 환경 ID와 /etc/codex 경로, 프록시·CA·클라우드 인증 주입이 Claude에도 있다고 가정하지 않는다.

4. Docker 실행 시 실제 환경이 요구하는 프록시와 CA 신뢰를 컨테이너 안에도 적용한다.

5. 클라우드 계정은 별칭과 프로필을 확인해 선택하고 임의의 다른 계정을 쓰지 않는다.

6. 설정 존재, 현재 준비 상태, 개별 API 요청 성공을 구분한다.

7. VPN 설정 여부와 실제 연결 건강 상태도 구분한다.

8. 환경 설정 변경이 필요하면 현재 Claude 환경의 지원 절차를 따른다.

## 출처

cloud-environment:cloud-environment-runtime. 기존 도구명과 GPT 전용 문법은 그대로 실행하지 않고 현재 도구에 대응시킨다.
