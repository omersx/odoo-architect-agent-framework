# Pattern: XML Views

Use inherited views and stable XPath targets.

```xml
<record id="view_order_form_inherit_my_module" model="ir.ui.view">
    <field name="name">sale.order.form.inherit.my.module</field>
    <field name="model">sale.order</field>
    <field name="inherit_id" ref="sale.view_order_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='payment_term_id']" position="after">
            <field name="delivery_urgency"/>
        </xpath>
    </field>
</record>
```

Prefer adding near a known field. Avoid replacing broad containers.
