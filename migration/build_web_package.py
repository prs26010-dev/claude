#!/usr/bin/env python3
"""Regenerate skill-zips/*.zip and WORKFLOWS.ko.md from ../.claude/skills/gpt-*/SKILL.md.

Usage: python3 migration/build_web_package.py [--check]
--check exits non-zero if the generated files differ from what is committed.
"""
import io
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILLS = ROOT.parent / ".claude" / "skills"
ZIPS = ROOT / "skill-zips"
WORKFLOWS = ROOT / "WORKFLOWS.ko.md"
# Fixed timestamp keeps zip bytes stable across rebuilds.
ZIP_TIME = (2026, 1, 1, 0, 0, 0)

HEADER = """# Claude용 업무 지침 16개 (개선판)

웹·앱 프로젝트 참고 파일용. 내용은 `skill-zips/`의 SKILL.md와 같다. `build_web_package.py`로 생성하므로 직접 고치지 않는다.
"""


def web_skill_text(text):
    # claude.ai skill upload does not use the Claude Code-only invocation flag.
    return re.sub(r"^disable-model-invocation: true\n", "", text, flags=re.M)


def zip_bytes(name, text):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        info = zipfile.ZipInfo(f"{name}/SKILL.md", ZIP_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, text)
    return buf.getvalue()


def workflow_section(name, text):
    body = text.split("---\n", 2)[2].strip()
    title, rest = body.split("\n", 1)
    # Nest every heading one level under the per-skill "##" title.
    rest = re.sub(r"^(#{2,5}) ", r"#\1 ", rest, flags=re.M)
    return f"## {name} — {title.lstrip('# ').strip()}\n{rest.rstrip()}\n"


def build():
    outputs = {}
    sections = []
    for skill in sorted(SKILLS.glob("gpt-*/SKILL.md")):
        name = skill.parent.name
        text = web_skill_text(skill.read_text(encoding="utf-8"))
        outputs[ZIPS / f"{name}.zip"] = zip_bytes(name, text)
        sections.append(workflow_section(name, text))
    outputs[WORKFLOWS] = (HEADER + "\n---\n\n" + "\n---\n\n".join(sections)).encode("utf-8")
    return outputs


def main():
    check = "--check" in sys.argv
    stale = []
    for path, data in build().items():
        if path.exists() and path.read_bytes() == data:
            continue
        stale.append(path)
        if not check:
            path.write_bytes(data)
    for path in stale:
        print(("stale: " if check else "wrote: ") + str(path.relative_to(ROOT.parent)))
    sys.exit(1 if check and stale else 0)


if __name__ == "__main__":
    main()
