from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from . import __version__
from .paths import find_framework_root
from .review import review_addon
from .scaffold import ScaffoldError, scaffold_addon


def run(command: list[str], *, cwd: Path) -> int:
    completed = subprocess.run(command, cwd=str(cwd), check=False)
    return completed.returncode


def command_info(args: argparse.Namespace) -> int:
    root = find_framework_root()
    print(f"Odoo Architect CLI {__version__}")
    print(f"Framework root: {root}")
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print("Commands: info, doctor, validate, scaffold, review, smoke-test")
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    root = find_framework_root()
    print(f"Framework root: {root}")

    checks = [
        ("SYSTEM.md", (root / "SYSTEM.md").is_file()),
        ("AGENTS.md", (root / "AGENTS.md").is_file()),
        ("tools/validate_framework.py", (root / "tools/validate_framework.py").is_file()),
        ("compose.odoo.yml", (root / "compose.odoo.yml").is_file()),
        ("Docker", shutil.which("docker") is not None),
    ]

    if shutil.which("docker") is not None:
        docker_compose = subprocess.run(
            ["docker", "compose", "version"],
            cwd=str(root),
            check=False,
            capture_output=True,
            text=True,
        )
        checks.append(("Docker Compose", docker_compose.returncode == 0))
    else:
        checks.append(("Docker Compose", False))

    failed = False
    for label, ok in checks:
        status = "ok" if ok else "missing"
        print(f"{status:8} {label}")
        failed = failed or not ok

    return 1 if failed and args.strict else 0


def command_validate(args: argparse.Namespace) -> int:
    root = find_framework_root()
    validator = root / "tools" / "validate_framework.py"
    if not validator.is_file():
        print(f"Validator not found: {validator}", file=sys.stderr)
        return 1
    return run([sys.executable, str(validator)], cwd=root)


def command_scaffold(args: argparse.Namespace) -> int:
    root = find_framework_root()
    try:
        target = scaffold_addon(
            root=root,
            name=args.name,
            output=Path(args.output),
            depends=args.depends,
            summary=args.summary,
            display_name=args.display_name,
            version=args.version,
            license_name=args.license,
            extension=args.extension,
            force=args.force,
        )
    except ScaffoldError as exc:
        print(f"Scaffold failed: {exc}", file=sys.stderr)
        return 1

    print(f"Created addon: {target}")
    return 0


def command_review(args: argparse.Namespace) -> int:
    findings = review_addon(Path(args.path))
    if not findings:
        print("No static review findings.")
        return 0

    failed = False
    for finding in findings:
        print(f"[{finding.severity}] {finding.message}")
        failed = failed or finding.severity == "error"

    return 1 if failed else 0


def command_smoke_test(args: argparse.Namespace) -> int:
    root = find_framework_root()
    addons_path = "/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons"
    env = dict(**os_environ_with_odoo_version(args.odoo_version))

    compose = ["docker", "compose", "-f", "compose.odoo.yml"]
    commands = [
        compose + ["up", "-d", "db"],
        compose
        + [
            "run",
            "--rm",
            "odoo",
            "odoo",
            "-d",
            args.database,
            "-i",
            args.module,
            f"--addons-path={addons_path}",
            "--test-enable",
            "--stop-after-init",
            "--without-demo=all",
            "--log-level=test",
        ],
        compose
        + [
            "run",
            "--rm",
            "odoo",
            "odoo",
            "-d",
            args.database,
            "-u",
            args.module,
            f"--addons-path={addons_path}",
            "--test-enable",
            "--stop-after-init",
            "--log-level=test",
        ],
    ]

    for command in commands:
        completed = subprocess.run(command, cwd=str(root), env=env, check=False)
        if completed.returncode != 0:
            return completed.returncode
    return 0


def os_environ_with_odoo_version(odoo_version: str) -> dict[str, str]:
    import os

    env = os.environ.copy()
    env["ODOO_VERSION"] = odoo_version
    return env


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="odoo-architect",
        description="CLI for the Odoo Architect Agent Framework.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    info = subparsers.add_parser("info", help="Show framework and CLI information.")
    info.set_defaults(func=command_info)

    doctor = subparsers.add_parser("doctor", help="Check local tooling.")
    doctor.add_argument("--strict", action="store_true", help="Fail on missing optional tools.")
    doctor.set_defaults(func=command_doctor)

    validate = subparsers.add_parser("validate", help="Run production static validation.")
    validate.set_defaults(func=command_validate)

    scaffold = subparsers.add_parser("scaffold", help="Create a new Odoo addon skeleton.")
    scaffold.add_argument("name", help="Technical module name, e.g. biz_bridge_pharmacy.")
    scaffold.add_argument(
        "--output",
        default="examples/custom_addons",
        help="Output directory for the addon parent.",
    )
    scaffold.add_argument(
        "--depends",
        action="append",
        default=[],
        help="Dependency or comma-separated dependency list. Can be repeated.",
    )
    scaffold.add_argument("--summary", help="Manifest summary.")
    scaffold.add_argument("--display-name", help="Human-readable module name.")
    scaffold.add_argument("--version", default="18.0.1.0.0")
    scaffold.add_argument("--license", default="LGPL-3")
    scaffold.add_argument(
        "--extension",
        action="store_true",
        help="Create a biz_bridge_pro extension and add dependency automatically.",
    )
    scaffold.add_argument("--force", action="store_true", help="Allow writing into existing folder.")
    scaffold.set_defaults(func=command_scaffold)

    review = subparsers.add_parser("review", help="Run lightweight static addon review.")
    review.add_argument("path", help="Path to an Odoo addon.")
    review.set_defaults(func=command_review)

    smoke = subparsers.add_parser("smoke-test", help="Run live Odoo install/update smoke test.")
    smoke.add_argument("--odoo-version", default="18.0")
    smoke.add_argument("--database", default="odoo_architect_test")
    smoke.add_argument("--module", default="biz_bridge_pro")
    smoke.set_defaults(func=command_smoke_test)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)
