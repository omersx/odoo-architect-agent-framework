from __future__ import annotations

import contextlib
import io
import shutil
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from odoo_architect_cli.cli import main
from odoo_architect_cli.review import review_addon
from odoo_architect_cli.scaffold import ScaffoldError, scaffold_addon

TEMP_ROOT = ROOT / "tests" / "tmp"


@contextmanager
def temporary_workspace():
    TEMP_ROOT.mkdir(exist_ok=True)
    temp_dir = TEMP_ROOT / f"case_{uuid.uuid4().hex}"
    temp_dir.mkdir(parents=True)
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        try:
            TEMP_ROOT.rmdir()
        except OSError:
            pass


class TestOdooArchitectCli(unittest.TestCase):
    def test_info_command_prints_version(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = main(["info"])

        self.assertEqual(exit_code, 0)
        self.assertIn("Odoo Architect CLI", output.getvalue())

    def test_scaffold_extension_adds_hub_dependency(self):
        with temporary_workspace() as root:
            target = scaffold_addon(
                root=root,
                name="biz_bridge_pharmacy",
                output=Path("custom_addons"),
                depends=["stock,product_expiry"],
                summary="Pharmacy extension.",
                extension=True,
            )

            manifest = (target / "__manifest__.py").read_text(encoding="utf-8")
            has_security = (target / "security" / "ir.model.access.csv").is_file()
            has_tests = (target / "tests" / "__init__.py").is_file()

        self.assertIn('"biz_bridge_pro"', manifest)
        self.assertIn('"stock"', manifest)
        self.assertIn('"product_expiry"', manifest)
        self.assertTrue(has_security)
        self.assertTrue(has_tests)

    def test_scaffold_rejects_invalid_module_name(self):
        with temporary_workspace() as root:
            with self.assertRaises(ScaffoldError):
                scaffold_addon(
                    root=root,
                    name="Bad-Name",
                    output=Path("custom_addons"),
                    depends=["base"],
                )

    def test_review_scaffolded_addon_has_no_findings(self):
        with temporary_workspace() as root:
            target = scaffold_addon(
                root=root,
                name="biz_bridge_demo",
                output=Path("custom_addons"),
                depends=["base"],
            )
            findings = review_addon(target)

        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
