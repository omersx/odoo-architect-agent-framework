# Security Gates

Every new model needs access rights.

Review record rules when:

- The model stores sensitive customer, financial, employee, or medical data.
- Portal or public users access it.
- Data crosses company boundaries.
- Background jobs use `sudo()`.

Keep `sudo()` narrow and explain why it is necessary.
