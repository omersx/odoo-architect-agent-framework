# Security Checklist

- Every new model has access rights.
- Sensitive fields have group restrictions when needed.
- Record rules are reviewed for new models.
- Multi-company access is reviewed.
- Portal and public routes validate ownership.
- `sudo()` usage is minimal and documented.
- Automated jobs do not leak or mutate unrelated company data.
