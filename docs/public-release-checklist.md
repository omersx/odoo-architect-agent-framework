# Public Release Checklist

Use this before the first GitHub push.

## Repository Hygiene

- [ ] README explains the project clearly.
- [ ] README shows clone, install, and first-use commands.
- [ ] `docs/install-and-use.md` is up to date.
- [ ] License is present.
- [ ] Contributing guide is present.
- [ ] Security policy is present.
- [ ] Code of conduct is present.
- [ ] Support policy is present.
- [ ] Issue templates are present.
- [ ] Pull request template is present.
- [ ] CI workflow is present.
- [ ] Raw private draft notes are ignored.

## Validation

- [ ] CLI unit tests pass.
- [ ] Static production validator passes.
- [ ] Skill validation passes.
- [ ] No secrets are present.
- [ ] No absolute local paths are present.
- [ ] No generated cache files are present.

## GitHub Setup

- [ ] Create public repository.
- [ ] Add topics.
- [ ] Enable issues.
- [ ] Enable discussions if desired.
- [ ] Enable private vulnerability reporting.
- [ ] Protect `main` after first push.
- [ ] Require the `Validate` workflow on pull requests.

## First Push

Recommended:

```bash
git init -b main
git add .
git commit -m "Initial public release"
git remote add origin https://github.com/<owner>/odoo-architect-agent-framework.git
git push -u origin main
```
