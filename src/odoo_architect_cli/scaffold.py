from __future__ import annotations

import re
from pathlib import Path

VALID_MODULE_RE = re.compile(r"^[a-z][a-z0-9_]*$")

ACCESS_HEADER = (
    "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n"
)


class ScaffoldError(ValueError):
    pass


def normalize_depends(depends: list[str], *, extension: bool) -> list[str]:
    normalized: list[str] = []
    for dependency in depends:
        for item in dependency.split(","):
            value = item.strip()
            if value and value not in normalized:
                normalized.append(value)

    if extension and "biz_bridge_pro" not in normalized:
        normalized.insert(0, "biz_bridge_pro")

    return normalized


def validate_module_name(name: str) -> None:
    if not VALID_MODULE_RE.fullmatch(name):
        raise ScaffoldError(
            "Module names must use lowercase letters, digits, and underscores, "
            "and must start with a letter."
        )


def title_from_module_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("_"))


def manifest_text(
    *,
    technical_name: str,
    display_name: str,
    summary: str,
    depends: list[str],
    version: str,
    license_name: str,
) -> str:
    depends_lines = "\n".join(f'        "{dependency}",' for dependency in depends)
    return f'''{{
    "name": "{display_name}",
    "version": "{version}",
    "summary": "{summary}",
    "category": "Customizations",
    "author": "Odoo Architect Agent Framework",
    "license": "{license_name}",
    "depends": [
{depends_lines}
    ],
    "data": [
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "application": False,
}}
'''


def readme_text(
    *,
    technical_name: str,
    display_name: str,
    summary: str,
    depends: list[str],
    extension: bool,
) -> str:
    dependency_lines = "\n".join(f"- `{dependency}`" for dependency in depends)
    module_type = "industry extension" if extension else "custom addon"
    return f"""# {display_name}

Technical name: `{technical_name}`

Type: {module_type}

## Summary

{summary}

## Dependencies

{dependency_lines}

## Implementation Notes

- Do not modify Odoo core.
- Use `_inherit` for existing models.
- Add access rights for every new model.
- Use XML inheritance with stable XPath targets.
- Add tests for business-critical behavior.

## Production Gate

Before release, run the framework validator and a live Odoo install/update smoke test.
"""


def scaffold_addon(
    *,
    root: Path,
    name: str,
    output: Path,
    depends: list[str],
    summary: str | None = None,
    display_name: str | None = None,
    version: str = "18.0.1.0.0",
    license_name: str = "LGPL-3",
    extension: bool = False,
    force: bool = False,
) -> Path:
    validate_module_name(name)

    target_parent = output if output.is_absolute() else root / output
    target = target_parent / name
    if target.exists() and not force:
        raise ScaffoldError(f"Target already exists: {target}")

    target.mkdir(parents=True, exist_ok=True)
    for folder in ["models", "views", "security", "tests"]:
        (target / folder).mkdir(exist_ok=True)

    normalized_depends = normalize_depends(depends, extension=extension)
    if not normalized_depends:
        normalized_depends = ["base"]

    display = display_name or title_from_module_name(name)
    module_summary = summary or f"{display} Odoo customization."

    files = {
        "__init__.py": "from . import models\n",
        "models/__init__.py": "",
        "views/.gitkeep": "",
        "tests/__init__.py": "",
        "security/ir.model.access.csv": ACCESS_HEADER,
        "__manifest__.py": manifest_text(
            technical_name=name,
            display_name=display,
            summary=module_summary,
            depends=normalized_depends,
            version=version,
            license_name=license_name,
        ),
        "README.md": readme_text(
            technical_name=name,
            display_name=display,
            summary=module_summary,
            depends=normalized_depends,
            extension=extension,
        ),
    }

    for relative_name, content in files.items():
        path = target / relative_name
        if path.exists() and not force:
            continue
        path.write_text(content, encoding="utf-8")

    return target
