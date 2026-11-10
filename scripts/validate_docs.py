#!/usr/bin/env python3
"""Validate repository Markdown structure using only the Python standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CONFLICT_MARKERS = ("<<<<<<< ", "=======", ">>>>>>> ")


def validate_markdown(path: Path) -> list[str]:
    """Check UTF-8, balanced fenced blocks and merge-conflict markers."""
    errors: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path.relative_to(ROOT)}: invalid UTF-8: {exc}"]

    active_char: str | None = None
    active_length = 0
    opening_line = 0

    for line_number, line in enumerate(content.splitlines(), start=1):
        if active_char is None:
            match = FENCE_OPEN.match(line)
            if match:
                fence = match.group(1)
                active_char = fence[0]
                active_length = len(fence)
                opening_line = line_number
                # CommonMark forbids backticks in a backtick fence's info string.
                if active_char == "`" and "`" in match.group(2):
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        "backtick fence info string contains a backtick"
                    )
                continue

            if line.startswith(CONFLICT_MARKERS):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    "possible unresolved merge-conflict marker"
                )
            continue

        stripped = line.lstrip(" ")
        if len(line) - len(stripped) > 3:
            continue
        if stripped and stripped[0] == active_char:
            run_length = len(stripped) - len(stripped.lstrip(active_char))
            remainder = stripped[run_length:]
            if run_length >= active_length and not remainder.strip():
                active_char = None
                active_length = 0
                opening_line = 0

    if active_char is not None:
        errors.append(
            f"{path.relative_to(ROOT)}:{opening_line}: "
            f"unclosed {active_char * active_length} fenced block"
        )
    return errors


def main() -> int:
    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    if not markdown_files:
        print("ERROR: no Markdown documents found")
        return 1

    errors = [
        error
        for path in markdown_files
        for error in validate_markdown(path)
    ]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"FAILED: {len(errors)} issue(s) across {len(markdown_files)} Markdown files")
        return 1

    print(f"PASS: validated UTF-8, fenced blocks and conflict markers in {len(markdown_files)} Markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
