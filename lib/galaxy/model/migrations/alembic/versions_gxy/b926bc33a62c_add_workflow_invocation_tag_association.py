"""Add workflow_invocation_tag_association table

Revision ID: b926bc33a62c
Revises: 75b461a2b24a
Create Date: 2026-01-03 12:00:00.000000

"""

import sqlalchemy as sa

from galaxy.model.custom_types import TrimmedString
from galaxy.model.migrations.util import (
    create_table,
    drop_table,
)

# revision identifiers, used by Alembic.
revision = "b926bc33a62c"
down_revision = "75b461a2b24a"
branch_labels = None
depends_on = None


def upgrade():
    create_table(
        "workflow_invocation_tag_association",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("workflow_invocation_id", sa.Integer, sa.ForeignKey("workflow_invocation.id"), index=True),
        sa.Column("tag_id", sa.Integer, sa.ForeignKey("tag.id"), index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("galaxy_user.id"), index=True),
        sa.Column("user_tname", TrimmedString(255), index=True),
        sa.Column("value", TrimmedString(255), index=True),
    )


def downgrade():
    drop_table("workflow_invocation_tag_association")
