"""Add collection_references column to workflow_invocation_message table

Revision ID: 4daccc7749f6
Revises: e96dd6fd5863
Create Date: 2026-09-03 10:00:00.000000
"""

import sqlalchemy as sa

from galaxy.model.migrations.util import (
    add_column,
    drop_column,
)

# revision identifiers, used by Alembic.
revision = "4daccc7749f6"
down_revision = "e96dd6fd5863"
branch_labels = None
depends_on = None

# database object names used in this revision
table_name = "workflow_invocation_message"
column_name = "collection_references"


def upgrade():
    add_column(
        table_name,
        sa.Column(
            column_name,
            sa.JSON,
            nullable=True,
        ),
    )


def downgrade():
    drop_column(
        table_name,
        column_name,
    )
