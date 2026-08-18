{
    "name": "Integrated Business Bridge",
    "version": "18.0.1.0.0",
    "summary": "Connect CRM, Sales, Inventory, and Accounting with shared delivery urgency.",
    "category": "Sales",
    "author": "Odoo Architect Agent Framework",
    "license": "LGPL-3",
    "depends": [
        "crm",
        "sale_management",
        "sale_crm",
        "stock",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": False,
}
