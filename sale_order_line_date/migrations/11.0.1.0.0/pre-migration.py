# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    if openupgrade.column_exists(cr, 'sale_order_line', 'data_concordata'):
        openupgrade.rename_columns(
            cr, {'sale_order_line': [
                ('data_concordata', None),
            ],
            }
        )
    if openupgrade.column_exists(cr, 'sale_order', 'data_concordata'):
        openupgrade.rename_columns(
            cr, {'sale_order': [
                ('data_concordata', None),
            ],
            }
        )
