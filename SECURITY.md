# Security Policy

## Supported Versions

The current public development line is supported.

## Reporting a Vulnerability

Please do not open public issues for vulnerabilities.

Use GitHub private vulnerability reporting if enabled on the repository, or contact the maintainer privately through the repository owner profile.

After publishing, enable private vulnerability reporting in the GitHub repository settings.

## Security Expectations

For Odoo code and examples:

- Add access rights for every new model.
- Review record rules for sensitive or multi-company data.
- Keep `sudo()` usage narrow and justified.
- Validate portal, public website, and controller access carefully.
- Do not commit credentials, database dumps, customer data, logs, or production config.
