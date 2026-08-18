#!/usr/bin/env bash
set -Eeuo pipefail

odoo_version="${1:-18.0}"
database="${2:-odoo_architect_test}"
module="${3:-biz_bridge_pro}"

export ODOO_VERSION="$odoo_version"

run_checked() {
    local label="$1"
    shift

    echo "$label"
    "$@"
}

compose=(docker compose -f compose.odoo.yml)
addons_path="/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons"

run_checked "Starting PostgreSQL for Odoo ${odoo_version}..." \
    "${compose[@]}" up -d db

run_checked "Running install smoke test for ${module} on database ${database}..." \
    "${compose[@]}" run --rm odoo odoo \
        -d "$database" \
        -i "$module" \
        "--addons-path=${addons_path}" \
        --test-enable \
        --stop-after-init \
        --without-demo=all \
        --log-level=test

run_checked "Running update smoke test for ${module} on database ${database}..." \
    "${compose[@]}" run --rm odoo odoo \
        -d "$database" \
        -u "$module" \
        "--addons-path=${addons_path}" \
        --test-enable \
        --stop-after-init \
        --log-level=test

echo "Smoke test completed."
