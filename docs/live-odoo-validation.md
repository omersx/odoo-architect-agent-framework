# Live Odoo Validation

Static checks are useful, but Odoo modules become trustworthy only after installation in a real Odoo database.

## Local Docker Smoke Test

Prerequisites:

- Docker Desktop.
- Docker Desktop Linux engine running.
- Docker Compose plugin.

Run:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0
```

On Linux or macOS:

```bash
bash scripts/odoo-smoke-test.sh 18.0 odoo_architect_test_18
```

or:

```bash
make smoke-test-18
```

If Docker reports that `dockerDesktopLinuxEngine` cannot be found, start Docker Desktop and wait until it says the engine is running, then rerun the command.

Then run:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 19.0 -Database odoo_architect_test_19
```

On Linux or macOS:

```bash
bash scripts/odoo-smoke-test.sh 19.0 odoo_architect_test_19
```

## Manual Browser Check

Start Odoo:

```powershell
$env:ODOO_VERSION = "18.0"
docker compose -f compose.odoo.yml up
```

Open:

```text
http://localhost:8069
```

Create a database, install `biz_bridge_pro`, and run the acceptance flow in `docs/production-readiness.md`.

## CI

`.github/workflows/validate.yml` runs static validation on push and pull request.

The Odoo install smoke test is manual through `workflow_dispatch` because it pulls Odoo and PostgreSQL images and can take longer than ordinary static checks.

The smoke script runs both:

- Install: `-i biz_bridge_pro`
- Update: `-u biz_bridge_pro`
