"""
Replace in-place timestamp triggers with history update time audit table triggers.
"""

import logging

from sqlalchemy import MetaData


from galaxy.model.triggers import (
    drop_in_place_timestamp_triggers,
    install_in_place_timestamp_triggers,
)

log = logging.getLogger(__name__)
metadata = MetaData()


def upgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.reflect()
    drop_in_place_timestamp_triggers(migrate_engine)


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    metadata.reflect()
    install_in_place_timestamp_triggers(migrate_engine)
