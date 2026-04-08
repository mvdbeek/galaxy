import uuid
from unittest import mock

import pytest

import galaxy.datatypes.registry as registry
import galaxy.model.mapping as mapping
from galaxy.model import (
    custom_types,
    Dataset,
    HistoryDatasetAssociation,
    MetadataFile,
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


def test_file_parameter_wrap_flushes_without_committing(sa_session):
    # Regression guard for https://github.com/galaxyproject/galaxy/issues/22194.
    #
    # Previously FileParameter.wrap called session.commit() as a last resort
    # when the MetadataFile uuid it was asked to wrap was not yet visible to
    # the session (because it had been add()-ed in a sibling code path but
    # not yet flushed). Committing leaked every other pending change in the
    # session to concurrent readers -- notably, inside JobWrapper.finish()'s
    # mid-loop load_metadata call, it committed a scratch dataset's
    # Dataset.state = OK assignment that had been set on a previous loop
    # iteration. A concurrent workflow scheduler could then see state=OK
    # while exec_after_process had already deleted the scratch file from
    # disk but not yet committed the purge/HDA swap.
    #
    # The fix replaces the commit with a flush: the pending INSERT becomes
    # visible to the retry SELECT within this session (wrap's contract is
    # preserved) without leaking any pending change to other sessions.
    hda = HistoryDatasetAssociation(extension="bed", create_dataset=True, sa_session=sa_session)
    sa_session.add(hda)
    sa_session.commit()

    dataset_id = hda.dataset.id

    # Mimic JobWrapper.finish() line 2199: set the scratch dataset state
    # to OK in memory only. sa_session.dirty proves the change is pending
    # -- this is the "poisoned" state that must NOT reach the DB mid-wrap.
    hda.dataset.state = Dataset.states.OK
    assert hda.dataset in sa_session.dirty

    # Mimic the "simultaneously copied dataset + changed datatype" scenario
    # the wrap() else-branch exists to handle: a MetadataFile has been
    # add()-ed to the session but not yet flushed, so the initial SELECT
    # returns None. wrap()'s flush must make the pending INSERT visible
    # to the retry SELECT so we still find it.
    pending_uuid = uuid.uuid4()
    pending_mf = MetadataFile(dataset=hda, name="bed_file", uuid=pending_uuid)
    sa_session.add(pending_mf)
    assert pending_mf in sa_session.new

    param = FileParameter(mock.Mock())
    with (
        mock.patch.object(sa_session, "commit", wraps=sa_session.commit) as commit_spy,
        mock.patch.object(sa_session, "flush", wraps=sa_session.flush) as flush_spy,
    ):
        result = param.wrap(str(pending_uuid), sa_session)

        # wrap() must not commit -- that is the whole bug.
        assert not commit_spy.called, "FileParameter.wrap must not commit the session"
        # wrap() must flush so the retry SELECT finds the pending MetadataFile.
        assert flush_spy.called, "FileParameter.wrap must flush the session"
        # wrap() still returns the MetadataFile (contract preserved).
        assert result is not None, "wrap() must return the pending MetadataFile"
        assert result.uuid == pending_uuid

    # The pending Dataset.state = OK must NOT have been committed: it is
    # still in the dirty set (flush sends the UPDATE into the current
    # transaction, but does not commit the transaction). From another
    # session's view under READ COMMITTED the row is still pre-OK, which
    # is the guarantee that closes the #22194 race window.
    #
    # We measure this directly by rolling back the current session's
    # transaction: the Dataset.state change must disappear because it
    # was never committed. If wrap had committed, rollback would be a
    # no-op and the assertion below would fail.
    sa_session.rollback()
    reloaded = sa_session.get(Dataset, dataset_id)
    assert reloaded.state != Dataset.states.OK, (
        "Dataset.state = OK must not survive rollback -- "
        "FileParameter.wrap must not commit pending changes"
    )
