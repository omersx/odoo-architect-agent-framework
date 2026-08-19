# Install and Use

This guide shows how to install and use the Odoo Architect Agent Framework after cloning it from GitHub.

## Requirements

- Python 3.10 or newer.
- Git.
- Docker and Docker Compose v2 for live Odoo smoke tests.
- Windows, Linux, or macOS.

## 1. Clone

```bash
git clone https://github.com/omersx/odoo-architect-agent-framework.git
cd odoo-architect-agent-framework
```

## 2. Install the CLI

```bash
python -m pip install -e .
```

## 3. Check the Installation

```bash
odoo-architect info
odoo-architect doctor
odoo-architect validate
```

Expected result:

```text
Production validation passed.
```

## 4. Use Without Installing

Linux/macOS:

```bash
PYTHONPATH=src python -m odoo_architect_cli info
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m odoo_architect_cli info
```

## 5. Create an Odoo Addon

Create a normal addon:

```bash
odoo-architect scaffold my_custom_addon --depends sale_management,stock
```

Create an industry extension that depends on `biz_bridge_pro`:

```bash
odoo-architect scaffold biz_bridge_pharmacy --extension --depends stock,product_expiry,point_of_sale
```

By default, generated addons are created under:

```text
examples/custom_addons
```

## 6. Review an Addon

```bash
odoo-architect review examples/custom_addons/biz_bridge_pro
```

## 7. Run Local Tests

Windows:

```powershell
.\scripts\test.ps1
.\scripts\validate.ps1
```

Linux/macOS:

```bash
bash scripts/test.sh
bash scripts/validate.sh
```

or:

```bash
make test
make validate
```

## 8. Run Live Odoo Smoke Tests

Start Docker first.

Windows:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0 -Database odoo_architect_test_18
```

Linux/macOS:

```bash
make smoke-test-18
```

Repeat for Odoo 19 before calling the reference addon production-ready.

## 9. Use With AI Coding Tools

Use these files as tool adapters:

- Codex: `.codex/skills/odoo-architect/SKILL.md`
- Claude Code: `CLAUDE.md`
- Antigravity: `.agents/`
- OpenCode: `.opencode/agents/odoo-architect.md`
- Copencode-style tools: `COPENCODE.md`
- Generic tools: `SYSTEM.md` and `AGENTS.md`
