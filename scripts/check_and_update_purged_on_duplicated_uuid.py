"""
This script will inspect non-purged datasets that have been re-assigned to HDAs following the duplicate uuid bug.
If the file does not exist on disk anymore we mark the dataset and corresponding HDAs as deleted and purged.
Activate Galaxy's virtualenv and run this script from galaxy's root directory with
`GALAXY_CONFIG_FILE=path/to/galaxy.yml python scripts/check_and_update_purged_on_duplicated_uuid.py`
"""

import logging
import os
import sys

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "lib")))

WARNING_MODULES = ["parso", "asyncio", "galaxy.datatypes"]
for mod in WARNING_MODULES:
    logger = logging.getLogger(mod)
    logger.setLevel("WARNING")

log = logging.getLogger(__name__)

from sqlalchemy import text

from galaxy.celery import build_app
from galaxy.model import Dataset
from galaxy.model.orm.scripts import get_config
from galaxy.objectstore import ObjectStore

if __name__ == "__main__":

    from galaxy.celery import tasks  # noqa: F401

    config = get_config(sys.argv)
    os.environ["GALAXY_CONFIG_FILE"] = os.environ.get("GALAXY_CONFIG_FILE", config["config_file"])
    app = build_app()
    session = app.model.session
    object_store: ObjectStore = app.object_store
    SQL = """
SELECT distinct d.id FROM hda_dataset_mapping_pre_uuid_condense as hda_pre_condense
  JOIN history_dataset_association as hda on hda.id=hda_pre_condense.id
  JOIN dataset as d on hda.dataset_id = d.id;
"""

    updated_hda_ids = []
    r = session.execute(text(SQL))
    for i, (row) in enumerate(r):
        dataset_id = row[0]
        d = session.query(Dataset).where(Dataset.id == dataset_id).one()
        if not object_store.exists(d):
            d.deleted = True
            d.purged = True
            for dataset_instance in d.active_history_associations:
                dataset_instance.deleted = True
                dataset_instance.purged = True
                updated_hda_ids.append(dataset_instance.id)
        if i % 100:
            session.commit()
    session.commit()
    if updated_hda_ids:
        log.warning(
            "The following history dataset associations could not be found on disk and were marked as deleted and purged: %s",
            updated_hda_ids,
        )
