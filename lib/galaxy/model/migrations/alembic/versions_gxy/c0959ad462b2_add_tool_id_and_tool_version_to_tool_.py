"""Add tool_id and tool_version to tool_landing_request table

Revision ID: c0959ad462b2
Revises: 3af58c192752
Create Date: 2025-08-20 10:04:05.044610

"""

from sqlalchemy import (
    Column,
    String,
)

from galaxy.model.migrations.util import (
    add_column,
    column_exists,
    drop_column,
    transaction,
)

# revision identifiers, used by Alembic.
revision = "c0959ad462b2"
down_revision = "3af58c192752"
branch_labels = None
depends_on = None

# database object names used in this revision
table_name = "tool_landing_request"
tool_id_column = "tool_id"
tool_version_column = "tool_version"


def add_column_if_not_exists(table: str, column_name: str, column: Column):
    if not column_exists(table, column_name, True):
        add_column(table, column)


def upgrade():
    with transaction():
        add_column_if_not_exists(table_name, tool_id_column, Column(tool_id_column, String(255), nullable=False))
        add_column_if_not_exists(table_name, tool_version_column, Column(tool_version_column, String(255), nullable=True))


def downgrade():
    with transaction():
        drop_column(table_name, tool_version_column)
        drop_column(table_name, tool_id_column)
