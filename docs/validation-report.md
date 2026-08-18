# Validation Report

Date: 2026-08-18

## Summary

Current status: release candidate.

The framework has static production gates, CI configuration, Windows/Linux/macOS command wrappers, a product CLI, live Odoo smoke-test scripts, Odoo transaction tests, and multi-agent adapters. It is not yet production-certified because the live Odoo install/update smoke test could not pull required Docker images from Docker Hub in this environment.

## Passed

- `python tools/validate_framework.py`
- `powershell -ExecutionPolicy Bypass -File scripts\validate.ps1`
- `powershell -ExecutionPolicy Bypass -File scripts\test.ps1`
- `python -m odoo_architect_cli info`
- `python -m odoo_architect_cli doctor`
- `python -m odoo_architect_cli validate`
- `python -m odoo_architect_cli review examples\custom_addons\biz_bridge_pro`
- `python -m odoo_architect_cli scaffold` probe in ignored temp workspace
- `.codex/skills/odoo-architect` skill validation
- `.agents/skills/odoo-architect` skill validation
- No generated `__pycache__` directories found
- Docker and Docker Compose are installed
- Cross-platform support files are present and statically validated:
  - `scripts/validate.sh`
  - `scripts/odoo-smoke-test.sh`
  - `Makefile`
  - `.gitattributes`

## Blocked

- `scripts/odoo-smoke-test.ps1 -OdooVersion 18.0 -Database odoo_architect_test_18`
- `bash scripts/validate.sh` on this Windows machine

Docker reason:

```text
Docker Hub image downloads for postgres:16 and odoo:18.0 returned 403 Forbidden from production.cloudfront.docker.com.
```

The Docker engine is now reachable, but the external image download is blocked or denied by Docker Hub/CDN/network conditions.

Bash reason:

```text
Bash/Service/CreateInstance/E_ACCESSDENIED
```

This is a local Windows/WSL permission issue, not a Linux/macOS script syntax issue. The PowerShell validation path works on Windows.

## Next Gate

Resolve the Docker Hub image pull issue, then run:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0 -Database odoo_architect_test_18
.\scripts\odoo-smoke-test.ps1 -OdooVersion 19.0 -Database odoo_architect_test_19
```

Linux/macOS equivalents:

```bash
make smoke-test-18
make smoke-test-19
```

If both pass, update this report to production-ready for the reference addon.
