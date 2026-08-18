# Workflow: Extend Module

Use this for industry spokes such as `biz_bridge_pharmacy` or `biz_bridge_construct`.

1. Depend on the hub module.
2. Reuse hub fields and hooks.
3. Add only industry-specific data and behavior.
4. Avoid duplicating hub views or methods.
5. Pass data through standard Odoo hooks.
6. Add industry-specific security and tests.
7. Document what the extension assumes about the hub.

## Rule

If a behavior is useful across several industries, move it to the hub. If it is specific to one industry, keep it in the spoke.
