$ErrorActionPreference = "Stop"

python tools/validate_framework.py
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
