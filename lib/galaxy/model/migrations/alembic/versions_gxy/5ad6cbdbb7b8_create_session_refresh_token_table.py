"""create session_refresh_token table

Revision ID: 5ad6cbdbb7b8
Revises: eee9229a9765
Create Date: 2026-04-01 16:00:00.000000

"""

import sqlalchemy as sa

from galaxy.model.migrations.util import (
    create_table,
    drop_table,
)

# revision identifiers, used by Alembic.
revision = "5ad6cbdbb7b8"
down_revision = "9930b68c85af"
branch_labels = None
depends_on = None

table_name = "session_refresh_token"


def upgrade():
    create_table(
        table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("galaxy_user.id"), nullable=False, index=True),
        sa.Column("token_hash", sa.String(64), nullable=False, unique=True, index=True),
        sa.Column("created_at", sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column("expires_at", sa.DateTime, nullable=False),
        sa.Column("is_valid", sa.Boolean, nullable=False, server_default=sa.true()),
    )


def downgrade():
    drop_table(table_name)
