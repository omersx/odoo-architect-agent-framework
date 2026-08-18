# Platform Support

The Odoo Architect Agent Framework is designed to work on Windows, Linux, and macOS.

## Shared Requirements

- Python 3.10 or newer.
- Docker with Docker Compose v2 for live Odoo validation.
- Git is recommended for line-ending and executable-bit handling.

## Windows

Use PowerShell:

```powershell
.\scripts\validate.ps1
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0 -Database odoo_architect_test_18
```

Docker Desktop must be running with the Linux engine enabled.

If `bash scripts/validate.sh` fails on Windows with `Bash/Service/CreateInstance/E_ACCESSDENIED`, use the PowerShell scripts. The Bash scripts are intended for Linux, macOS, WSL, or Git Bash environments where Bash is allowed.

## Linux

Use Bash or Make:

```bash
bash scripts/validate.sh
bash scripts/odoo-smoke-test.sh 18.0 odoo_architect_test_18
```

or:

```bash
make validate
make smoke-test-18
```

If the shell scripts are not executable after copying the project, run:

```bash
chmod +x scripts/*.sh
```

## macOS

Use the same commands as Linux:

```bash
bash scripts/validate.sh
bash scripts/odoo-smoke-test.sh 18.0 odoo_architect_test_18
```

or:

```bash
make validate
make smoke-test-18
```

Docker Desktop must be running.

## Notes

- The framework content is Markdown, Python, XML, CSV, YAML, and Docker Compose, all of which are portable across the three operating systems.
- `.gitattributes` keeps shell scripts with LF line endings and PowerShell scripts with CRLF line endings.
- The live Odoo smoke test depends on Docker Hub image downloads. Network filtering, Docker Hub auth limits, or regional CDN issues can block the pull even when Docker itself is running.
