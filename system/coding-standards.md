# Coding Standards

## Python

- Follow Odoo style: model files under `models/`, one main model per file.
- Import only what is used.
- Use `self.ensure_one()` for single-record button actions.
- Use `@api.depends` for computed fields.
- Avoid raw SQL unless there is a measured performance reason.
- Raise `UserError` for user-correctable business errors.
- Use `_()` for user-facing strings.

## XML

- Use XML inheritance with precise XPath targets.
- Prefer adding fields after stable fields instead of replacing sections.
- Keep custom fields grouped in existing logical pages or groups.
- Avoid broad XPath expressions such as `//group[1]` unless no stable target exists.

## JavaScript and OWL

- Patch or extend standard components through supported registries.
- Keep state minimal.
- Keep RPC calls explicit and error-handled.
- Add assets through the manifest in the correct asset bundle.
