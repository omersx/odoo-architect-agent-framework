# Module Checklist

- Manifest has correct dependencies.
- Module imports are complete.
- No Odoo core files are modified.
- Existing models are extended with `_inherit`.
- New models have access rights.
- Views use stable XPath targets.
- User-facing strings are translatable.
- Data files load in the correct order.
- Tests or a test plan are included.
- Install and upgrade steps are documented.
- `python tools/validate_framework.py` passes.
- Live Odoo install smoke test passes before production release.
