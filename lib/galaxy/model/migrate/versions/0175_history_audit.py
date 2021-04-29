"""
Add history audit table and associated triggers
"""

import datetime
import logging

from sqlalchemy import Column, DateTime, ForeignKey, Index, Integer, MetaData, Table

from galaxy.model.migrate.versions.util import (
    create_table,
    drop_table
)

log = logging.getLogger(__name__)
now = datetime.datetime.utcnow
metadata = MetaData()

AuditTable = Table(
    "history_audit",
    metadata,
    Column("history_id", Integer, ForeignKey("history.id"), nullable=False),
    Column("update_time", DateTime, default=now, nullable=False),
)

Index('ix_history_audit_history_id_update_time_desc', AuditTable.c.history_id.desc(), AuditTable.c.update_time.desc())


def upgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.reflect()

    # create table + index
    create_table(AuditTable)

    # populate with update_time from every history
    copy_update_times = """
        INSERT INTO history_audit (history_id, update_time)
        SELECT id, update_time FROM history
    """
    migrate_engine.execute(copy_update_times)

    # drop update_time from history table (later maybe?)
    # create triggers to insert rows into audit table


def downgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.reflect()

    # update history.update_time with vals from audit table
    put_em_back = """
        UPDATE history h
        SET update_time = a.max_update_time
        FROM (
            SELECT history_id, max(update_time) as max_update_time
            FROM history_audit
            GROUP BY history_id, update_time
        ) a
        WHERE h.id = a.history_id
    """
    migrate_engine.execute(put_em_back)

    drop_table(AuditTable)
