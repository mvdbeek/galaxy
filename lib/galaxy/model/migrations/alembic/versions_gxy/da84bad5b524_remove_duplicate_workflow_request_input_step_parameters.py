"""Remove duplicate rows from workflow_request_input_step_parameter

Revision ID: da84bad5b524
Revises: 04288b6a5b25
Create Date: 2026-03-06 00:00:00.000000

"""

import logging

from alembic import op
from sqlalchemy import text

from galaxy.model.migrations.util import transaction

log = logging.getLogger(__name__)

# revision identifiers, used by Alembic.
revision = "da84bad5b524"
down_revision = "04288b6a5b25"
branch_labels = None
depends_on = None

table_name = "workflow_request_input_step_parameter"
batch_size = 10000

DELETE_BATCH = text(
    f"""
DELETE FROM {table_name}
WHERE id IN (
    SELECT id FROM (
        SELECT w1.id
        FROM {table_name} w1
        WHERE EXISTS (
            SELECT 1 FROM {table_name} w2
            WHERE w2.workflow_invocation_id = w1.workflow_invocation_id
            AND w2.workflow_step_id = w1.workflow_step_id
            AND w2.id < w1.id
        )
        LIMIT :batch_size
    ) tmp
)
"""
)


def upgrade():
    connection = op.get_bind()
    total_deleted = 0
    while True:
        with transaction():
            result = connection.execute(DELETE_BATCH, {"batch_size": batch_size})
            if result.rowcount == 0:
                break
            total_deleted += result.rowcount
            log.info(f"Removed {result.rowcount} duplicate rows from {table_name} (total: {total_deleted})")
    if total_deleted:
        log.info(f"Removed {total_deleted} total duplicate rows from {table_name}")


def downgrade():
    # Data-cleaning migration; deleted duplicates cannot be restored.
    pass
