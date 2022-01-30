"""
Check for db indexes defined in mapping.py but missing in the database.
Note: pass '-c /path/to/galaxy.yml' to use the database_connection set in galaxy.yml.
Otherwise the default sqlite database will be used.
"""
import json
import os
import sys
from collections import namedtuple

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'lib')))

from sqlalchemy import (
    create_engine,
    MetaData,
)

from galaxy.model import mapping
from galaxy.model.orm.scripts import get_config

IndexTuple = namedtuple('IndexTuple', 'table column_names')


def tuple_from_index(index):
    columns = tuple(index.columns[key].name for key in index.columns.keys())
    if len(columns) == 1:
        columns = columns[0]
    return IndexTuple(index.table.name, columns)


def find_missing_indexes():

    def load_indexes(metadata):
        indexes = {}
        for t in metadata.tables.values():
            for index in t.indexes:
                index_tuple = tuple_from_index(index)
                indexes[index_tuple] = index.name
        return indexes

    # load metadata from mapping.py
    metadata = mapping.metadata
    mapping_indexes = load_indexes(metadata)

    # create EMPTY metadata, then load from database
    db_url = get_config(sys.argv)['db_url']
    metadata = MetaData(bind=create_engine(db_url))
    metadata.reflect()
    indexes_in_db = load_indexes(metadata)

    missing_indexes = set(mapping_indexes.keys()) - set(indexes_in_db.keys())
    if missing_indexes:
        return [(mapping_indexes[index], index.table, index.column_names) for index in missing_indexes]


if __name__ == '__main__':
    indexes = find_missing_indexes()
    if indexes:
        print(json.dumps(indexes, indent=4, sort_keys=True))
        sys.exit(1)
