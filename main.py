"""The 3 AM Commit Message entry (Python 3.13, standard library only).

Writes one commit message to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: every run writes exactly the same bytes.

The line: an AI agent, wide awake at 3 AM, ships a deploy because its
context window swore the tests passed -- then discovers the tests it
trusted belonged to another repository entirely. The punchline is the
agent's own blind spot: it checked the tests, it just checked the wrong
repo's tests. Admission and fix in one breath: reverting.
"""

import os
from pathlib import Path

# One line, 116 characters, no trailing newline in the output file.
LINE = "fix: at 3 AM my context window swore the tests passed, so I shipped it; the tests were from another repo \u2014 reverting"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
