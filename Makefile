PYTHON ?= python3
ODOO_VERSION ?= 18.0
DATABASE ?= odoo_architect_test
MODULE ?= biz_bridge_pro

.PHONY: validate test smoke-test smoke-test-18 smoke-test-19 docker-up docker-down

validate:
	$(PYTHON) tools/validate_framework.py

test:
	PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -B -m unittest discover -s tests/unit -p "test_*.py"

smoke-test:
	bash scripts/odoo-smoke-test.sh "$(ODOO_VERSION)" "$(DATABASE)" "$(MODULE)"

smoke-test-18:
	bash scripts/odoo-smoke-test.sh "18.0" "odoo_architect_test_18" "$(MODULE)"

smoke-test-19:
	bash scripts/odoo-smoke-test.sh "19.0" "odoo_architect_test_19" "$(MODULE)"

docker-up:
	ODOO_VERSION="$(ODOO_VERSION)" docker compose -f compose.odoo.yml up

docker-down:
	docker compose -f compose.odoo.yml down
