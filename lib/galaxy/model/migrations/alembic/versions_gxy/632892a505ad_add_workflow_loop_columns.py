"""Add workflow step loop settings and subworkflow invocation iterations

Revision ID: 632892a505ad
Revises: b9467a8c12de
Create Date: 2026-11-21 21:11:08.000000

"""

from sqlalchemy import (
    Column,
    Integer,
    String,
)

from galaxy.model.custom_types import JSONType
from galaxy.model.migrations.util import (
    add_column,
    create_index,
    drop_column,
    drop_index,
    index_names_on_columns,
    transaction,
)

# revision identifiers, used by Alembic.
revision = "632892a505ad"
down_revision = "b9467a8c12de"
branch_labels = None
depends_on = None

# database object names used in this revision
workflow_step_table = "workflow_step"
association_table = "workflow_invocation_to_subworkflow_invocation_association"
iteration_index = "ix_wfi_swi_wfi_ws_iteration"
# The iteration index starts with workflow_invocation_id, so it replaces the index on that column.
invocation_index = "ix_wfi_swi_wfi"


def upgrade() -> None:
    with transaction():
        add_column(workflow_step_table, Column("loop", JSONType))
        add_column(association_table, Column("iteration", Integer))
        add_column(association_table, Column("loop_outcome", String(64)))
        create_index(
            iteration_index,
            association_table,
            ["workflow_invocation_id", "workflow_step_id", "iteration"],
            unique=True,
        )
        # Its name depends on how the database was created, e.g. truncated on PostgreSQL.
        for index_name in index_names_on_columns(
            association_table, ["workflow_invocation_id"], default=[invocation_index]
        ):
            drop_index(index_name, association_table)


def downgrade() -> None:
    with transaction():
        create_index(invocation_index, association_table, ["workflow_invocation_id"])
        drop_index(iteration_index, association_table)
        drop_column(association_table, "loop_outcome")
        drop_column(association_table, "iteration")
        drop_column(workflow_step_table, "loop")
