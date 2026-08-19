# Publishing to GitHub

This checklist prepares the project for a public open-source GitHub release.

## 1. Validate

Run:

```bash
python tools/validate_framework.py
```

Run tests:

```bash
python -B -m unittest discover -s tests/unit -p "test_*.py"
```

## 2. Initialize Git

If this folder is not already a Git repository:

```bash
git init -b main
git add .
git commit -m "Initial public release"
```

If Git asks for identity:

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

## 3. Authenticate GitHub CLI

The GitHub CLI must be logged in:

```bash
gh auth login -h github.com
gh auth status
```

## 4. Create and Push Public Repository

Recommended repository name:

```text
odoo-architect-agent-framework
```

Create and push:

```bash
gh repo create odoo-architect-agent-framework \
  --public \
  --source=. \
  --remote=origin \
  --push \
  --description "Open-source Odoo Architect Agent Framework for production-minded Odoo addon development."
```

After pushing, replace `YOUR_USERNAME` in `README.md` and `docs/install-and-use.md` with the real GitHub owner or organization.

## 5. Repository Settings

After publishing:

- Add topics: `odoo`, `erp`, `ai-agents`, `codex`, `claude-code`, `opencode`, `antigravity`, `odoo-addons`, `python`.
- Enable issues.
- Enable discussions if you want community Q&A.
- Enable private vulnerability reporting.
- Protect `main` after the first public push.
- Require the `Validate` workflow before merging pull requests.

## 6. Optional Manual Push

If you create the GitHub repository in the browser instead of using `gh`, use:

```bash
git remote add origin https://github.com/<owner>/odoo-architect-agent-framework.git
git push -u origin main
```
