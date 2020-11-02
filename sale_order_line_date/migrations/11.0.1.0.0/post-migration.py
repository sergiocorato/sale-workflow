# Copyright 2020 Sergio Corato <https://github.com/sergiocorato>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade
from psycopg2 import sql


def move_dates(env):
    column_name = openupgrade.get_legacy_name('data_concordata')
    if openupgrade.column_exists(env.cr, 'sale_order_line', column_name):
        openupgrade.logged_query(
            env.cr, sql.SQL(
                """
                UPDATE sale_order_line
                SET
                requested_date = {column_name};
                """
                ).format(
                    column_name=sql.Identifier(column_name),
                )
            )
    if openupgrade.column_exists(env.cr, 'sale_order', column_name):
        openupgrade.logged_query(
            env.cr, sql.SQL(
                """
                UPDATE sale_order
                SET
                requested_date = {column_name};
                """
            ).format(
                column_name=sql.Identifier(column_name),
            )
        )


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return
    move_dates(env)
