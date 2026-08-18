from __future__ import annotations

import os
from pathlib import Path

MARKER_FILES = ("SYSTEM.md", "AGENTS.md")


def find_framework_root(start: Path | None = None) -> Path:
    env_root = os.environ.get("ODOO_ARCHITECT_HOME")
    if env_root:
        return Path(env_root).expanduser().resolve()

    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if all((candidate / marker).is_file() for marker in MARKER_FILES):
            return candidate

    return current


def as_posix(path: Path) -> str:
    return path.as_posix()
