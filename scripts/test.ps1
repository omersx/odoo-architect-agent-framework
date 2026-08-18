$ErrorActionPreference = "Stop"

$env:PYTHONPATH = "src"
$env:PYTHONDONTWRITEBYTECODE = "1"
python -B -m unittest discover -s tests/unit -p "test_*.py"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
