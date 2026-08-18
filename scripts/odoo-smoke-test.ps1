param(
    [string]$OdooVersion = "18.0",
    [string]$Database = "odoo_architect_test",
    [string]$Module = "biz_bridge_pro"
)

$ErrorActionPreference = "Stop"
$env:ODOO_VERSION = $OdooVersion

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Label,

        [Parameter(Mandatory = $true)]
        [string[]]$Command
    )

    Write-Host $Label
    & $Command[0] @($Command[1..($Command.Length - 1)])
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE."
    }
}

Invoke-CheckedCommand `
    -Label "Starting PostgreSQL for Odoo $OdooVersion..." `
    -Command @("docker", "compose", "-f", "compose.odoo.yml", "up", "-d", "db")

Invoke-CheckedCommand `
    -Label "Running install/update smoke test for $Module on database $Database..." `
    -Command @(
        "docker",
        "compose",
        "-f",
        "compose.odoo.yml",
        "run",
        "--rm",
        "odoo",
        "odoo",
        "-d",
        $Database,
        "-i",
        $Module,
        "--addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons",
        "--test-enable",
        "--stop-after-init",
        "--without-demo=all",
        "--log-level=test"
    )

Invoke-CheckedCommand `
    -Label "Running update smoke test for $Module on database $Database..." `
    -Command @(
        "docker",
        "compose",
        "-f",
        "compose.odoo.yml",
        "run",
        "--rm",
        "odoo",
        "odoo",
        "-d",
        $Database,
        "-u",
        $Module,
        "--addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons",
        "--test-enable",
        "--stop-after-init",
        "--log-level=test"
    )

Write-Host "Smoke test completed."
