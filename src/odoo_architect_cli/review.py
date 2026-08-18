from __future__ import annotations

import ast
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ReviewFinding:
    severity: str
    message: str


def _read_manifest(path: Path) -> dict:
    try:
        return ast.literal_eval(path.read_text(encoding="utf-8"))
    except (SyntaxError, ValueError):
        return {}


def review_addon(path: Path) -> list[ReviewFinding]:
    addon = path.resolve()
    findings: list[ReviewFinding] = []

    manifest_path = addon / "__manifest__.py"
    if not manifest_path.is_file():
        return [ReviewFinding("error", "Missing __manifest__.py")]

    manifest = _read_manifest(manifest_path)
    if not manifest:
        findings.append(ReviewFinding("error", "Manifest is not a valid literal dict"))
        return findings

    for key in ["name", "version", "depends", "data", "license", "installable"]:
        if key not in manifest:
            findings.append(ReviewFinding("error", f"Manifest missing key: {key}"))

    data_files = manifest.get("data", [])
    if not isinstance(data_files, list):
        findings.append(ReviewFinding("error", "Manifest data must be a list"))
        data_files = []

    for data_file in data_files:
        if not (addon / data_file).is_file():
            findings.append(ReviewFinding("error", f"Missing data file: {data_file}"))

    if "security/ir.model.access.csv" not in data_files:
        findings.append(
            ReviewFinding("warning", "security/ir.model.access.csv is not loaded")
        )

    access_path = addon / "security" / "ir.model.access.csv"
    if access_path.is_file():
        with access_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
            if header != [
                "id",
                "name",
                "model_id:id",
                "group_id:id",
                "perm_read",
                "perm_write",
                "perm_create",
                "perm_unlink",
            ]:
                findings.append(
                    ReviewFinding("error", "ir.model.access.csv has invalid header")
                )

    if not (addon / "README.md").is_file():
        findings.append(ReviewFinding("warning", "Missing addon README.md"))

    if any(addon.rglob("*.py")) and not (addon / "tests" / "__init__.py").is_file():
        findings.append(ReviewFinding("warning", "Python addon lacks tests package"))

    return findings
