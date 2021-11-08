"""
Migration script to add a 'when_expression' column to the 'WorkflowStep' table.
"""

import logging

from sqlalchemy import Column, MetaData

from galaxy.model.custom_types import JSONType
from galaxy.model.migrate.versions.util import add_column, drop_column

log = logging.getLogger(__name__)
metadata = MetaData()

# Column to add.
when_col = Column("when_expression", JSONType, default=None)


def upgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.reflect()

    add_column(when_col, 'workflow_step', metadata)


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    metadata.reflect()

    drop_column('when_expression', 'workflow_step', metadata)
