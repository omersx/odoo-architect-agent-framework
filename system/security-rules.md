# Security Rules

Security is part of the design, not a final cleanup step.

## Access Rights

- Every new model requires an `ir.model.access.csv` row.
- Inherited standard models usually keep existing access rights unless a new access pattern is introduced.
- Do not grant broad manager rights to solve ordinary user access errors.

## Record Rules

Review record rules when:

- A new model stores customer, financial, employee, medical, or government data.
- Data crosses company boundaries.
- Portal or website users can access records.
- Automated jobs use elevated privileges.

## Elevated Access

- Use `sudo()` only for a specific reason.
- Keep `sudo()` scopes small.
- Never use `sudo()` to bypass business permissions without documenting the reason.
