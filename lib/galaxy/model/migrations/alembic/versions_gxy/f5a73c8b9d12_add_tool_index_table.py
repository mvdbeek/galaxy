"""Add tool_index table for storing pre-computed tool index

Revision ID: f5a73c8b9d12
Revises: 98621a25ab75
Create Date: 2026-01-25 10:00:00.000000

"""

import logging

import sqlalchemy as sa

from galaxy.model.migrations.util import (
    create_table,
    drop_table,
    table_exists,
)

log = logging.getLogger(__name__)

# revision identifiers, used by Alembic.
revision = "f5a73c8b9d12"
down_revision = "98621a25ab75"
branch_labels = None
depends_on = None

TABLE_NAME = "tool_index"


def upgrade():
    """Create tool_index table for storing pre-computed tool index.

    This table stores a serialized ToolIndex object that provides
    fast access to tool metadata for API responses without loading
    full tool sources.
    """
    if not table_exists(TABLE_NAME, True):
        create_table(
            TABLE_NAME,
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("version", sa.String(64), nullable=False, unique=True),
            sa.Column("data", sa.LargeBinary, nullable=False),
            sa.Column("built_at", sa.DateTime, nullable=True),
            sa.Column("create_time", sa.DateTime, default=sa.func.now()),
            sa.Column("update_time", sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
        )
    else:
        log.info(f"Skipping revision script: table {TABLE_NAME} already exists")


def downgrade():
    drop_table(TABLE_NAME)
