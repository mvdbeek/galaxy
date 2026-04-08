import uuid
from unittest import mock

import pytest

import galaxy.datatypes.registry as registry
import galaxy.model.mapping as mapping
from galaxy.model import (
    custom_types,
    Dataset,
    HistoryDatasetAssociation,
    set_datatypes_registry,
)
from galaxy.model.metadata import FileParameter

METADATA_LIMIT = 500


@pytest.fixture(scope="module")
def datatypes_registry():
    r = registry.Registry()
    r.load_datatypes()
    set_datatypes_registry(r)


@pytest.fixture
def sa_session(datatypes_registry):
    custom_types.MAX_METADATA_VALUE_SIZE = METADATA_LIMIT
    return mapping.init("/tmp", "sqlite:///:memory:", create_tables=True).session


def create_bed_data(sa_session, string_size):
    hda = HistoryDatasetAssociation(extension="bed")
    big_string = "0" * string_size
    sa_session.add(hda)
    hda.metadata.column_names = [big_string]
    assert hda.metadata.column_names
    sa_session.commit()
    return hda


def test_hda_below_limit(sa_session):
    hda = create_bed_data(sa_session=sa_session, string_size=1)
    assert len(hda.metadata.column_names[0]) == 1


def test_hda_above_limit(sa_session):
    hda = create_bed_data(sa_session=sa_session, string_size=1000)
    assert not hda.metadata.column_names


def test_get_if_set_returns_value_when_set(sa_session):
    hda = create_bed_data(sa_session=sa_session, string_size=1)
    assert hda.metadata.get_if_set("column_names") == ["0"]


def test_get_if_set_returns_default_when_unset(sa_session):
    hda = HistoryDatasetAssociation(extension="bed")
    sa_session.add(hda)
    sa_session.commit()
    assert hda.metadata.get_if_set("column_names") is None
    assert hda.metadata.get_if_set("column_names", []) == []


def test_get_if_set_returns_default_for_nonexistent_key(sa_session):
    hda = HistoryDatasetAssociation(extension="bed")
    sa_session.add(hda)
    sa_session.commit()
    assert hda.metadata.get_if_set("nonexistent_key") is None
    assert hda.metadata.get_if_set("nonexistent_key", "fallback") == "fallback"


def test_file_parameter_wrap_commits_pending_dataset_state(sa_session):
    # Reproduces the transitive commit inside JobWrapper.finish() that
    # powers the race in https://github.com/galaxyproject/galaxy/issues/22194:
    # mid-loop, load_metadata -> MetadataCollection.from_JSON_dict ->
    # FileParameter.wrap calls session.commit() when a referenced
    # MetadataFile uuid is not in the DB. That commit flushes *unrelated*
    # pending changes to the DB -- including the scratch dataset's
    # Dataset.state = OK that an earlier loop iteration assigned in
    # memory but has not committed yet. This is the mechanism by which
    # a concurrent workflow scheduler can observe a committed
    # Dataset.state=OK while the file is already gone.
    hda = HistoryDatasetAssociation(extension="bed", create_dataset=True, sa_session=sa_session)
    sa_session.add(hda)
    sa_session.commit()

    dataset_id = hda.dataset.id
    # Mimic JobWrapper.finish line 2199: set the scratch dataset state
    # to OK in memory only, without committing. sa_session.dirty proves
    # the change is pending (not yet committed).
    hda.dataset.state = Dataset.states.OK
    assert hda.dataset in sa_session.dirty

    # Now fire the transitive commit by calling FileParameter.wrap
    # with a uuid that will not be found in the DB. This matches the
    # wrap() else-branch at lib/galaxy/model/metadata.py:630-640.
    param = FileParameter(mock.Mock())
    with mock.patch.object(sa_session, "commit", wraps=sa_session.commit) as spy:
        result = param.wrap(str(uuid.uuid4()), sa_session)
        assert result is None, "non-existent uuid should return None"
        assert spy.called, "FileParameter.wrap must commit the session mid-call"

    # The transitive commit should have flushed the pending
    # Dataset.state = OK assignment. After commit, the dirty set is
    # empty and the state is durably set.
    assert hda.dataset not in sa_session.dirty
    sa_session.expire_all()
    reloaded = sa_session.get(Dataset, dataset_id)
    assert reloaded.state == Dataset.states.OK
