"""Add workflow_invocation_input_dependency table

Revision ID: ef59b94d69c4
Revises: 9930b68c85af
Create Date: 2026-02-04 10:00:00.000000

This table tracks dependencies between workflow invocations where one
invocation uses outputs from another (potentially still running) invocation
as inputs.
"""

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from galaxy.model.migrations.util import (
    create_table,
    drop_table,
)

# revision identifiers, used by Alembic.
revision = "ef59b94d69c4"
down_revision = "9930b68c85af"
branch_labels = None
depends_on = None


table_name = "workflow_invocation_input_dependency"


def upgrade():
    create_table(
        table_name,
        Column("id", Integer, primary_key=True),
        # The invocation that is waiting for input
        Column(
            "workflow_invocation_id",
            Integer,
            ForeignKey("workflow_invocation.id", onupdate="CASCADE", ondelete="CASCADE"),
            index=True,
            nullable=False,
        ),
        # The workflow step that needs the input
        Column(
            "workflow_step_id",
            Integer,
            ForeignKey("workflow_step.id", onupdate="CASCADE", ondelete="CASCADE"),
            index=True,
            nullable=False,
        ),
        # Input name on the step
        Column("input_name", String(255), nullable=False),
        # The source invocation providing the output
        Column(
            "source_invocation_id",
            Integer,
            ForeignKey("workflow_invocation.id", onupdate="CASCADE", ondelete="CASCADE"),
            index=True,
            nullable=False,
        ),
        # The workflow output ID (if referencing labeled output)
        Column(
            "source_workflow_output_id",
            Integer,
            ForeignKey("workflow_output.id", onupdate="CASCADE", ondelete="SET NULL"),
            index=True,
            nullable=True,
        ),
        # Alternative: reference step output directly
        Column(
            "source_step_id",
            Integer,
            ForeignKey("workflow_step.id", onupdate="CASCADE", ondelete="SET NULL"),
            index=True,
            nullable=True,
        ),
        Column("source_output_name", String(255), nullable=True),
        # Resolved dataset/collection when available
        Column(
            "resolved_dataset_id",
            Integer,
            ForeignKey("history_dataset_association.id", onupdate="CASCADE", ondelete="SET NULL"),
            index=True,
            nullable=True,
        ),
        Column(
            "resolved_collection_id",
            Integer,
            ForeignKey("history_dataset_collection_association.id", onupdate="CASCADE", ondelete="SET NULL"),
            index=True,
            nullable=True,
        ),
        # Timestamps
        Column("create_time", DateTime),
        Column("update_time", DateTime),
    )


def downgrade():
    drop_table(table_name)
