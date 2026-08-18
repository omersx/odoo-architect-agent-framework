# Release Template

## Version

`[version]`

## Scope

- `[feature or fix]`

## Validation

- Static validation: `[pass/fail]`
- Odoo 18 install smoke: `[pass/fail]`
- Odoo 19 install smoke: `[pass/fail]`
- Manual functional acceptance: `[pass/fail]`
- Security review: `[pass/fail]`

## Known Risks

- `[risk]`

## Rollback

- Uninstall or disable the affected custom addon.
- Restore database backup if the release includes schema/data changes that cannot be safely reverted.
