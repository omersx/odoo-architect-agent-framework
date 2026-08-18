#!/usr/bin/env bash
set -Eeuo pipefail

python_bin="${PYTHON:-python3}"

if ! command -v "$python_bin" >/dev/null 2>&1; then
    python_bin="python"
fi

"$python_bin" tools/validate_framework.py
