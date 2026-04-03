import random

import pytest
from sqlalchemy import inspect

from galaxy import model as m
from galaxy.model.unittest_utils.db_helpers import get_hdca_by_name
from galaxy.tools.parameters.dataset_matcher import (
    _batch_collection_summaries,
    _batch_populated_check,
    _batch_summary_query,
    _prefetch_implicitly_converted_datasets,
)
from . import MockTransaction
from .. import PRIVATE_OBJECT_STORE_ID


def test_history_update(make_history, make_hda, session):
    """
    Verify the following behavior:
    - history updated due to hda insert
    - history updated due to hda update
    - history NOT updated when hda copied
    """
    h1 = make_history()
    old_update_time = h1.update_time

    hda = make_hda(history=h1, create_dataset=True, sa_session=session)
    # history updated due to hda insert
    assert h1.update_time > old_update_time

    old_update_time = h1.update_time
    hda.name = "new name"
    session.add(hda)
    session.commit()
    # history updated due to hda update
    assert h1.update_time > old_update_time

    old_update_time = h1.update_time
    hda2 = hda.copy()
    assert hda2
    # history NOT updated when hda copied
    assert h1.update_time == old_update_time


def test_ratings(
    make_user,
    make_stored_workflow,
    make_history,
    make_page,
    make_visualization,
    make_hdca,
    make_ldca,
    make_user_item_rating_association,
):
    def _test_rating(assoc_class, item, assoc_class_item_attr_name):
        user = make_user()
        rating = random.randint(0, 100)
        rating_assoc = make_user_item_rating_association(assoc_class, user, item, rating)
        assert rating_assoc.user == user
        assert getattr(rating_assoc, assoc_class_item_attr_name) == item
        assert rating_assoc.rating == rating

    _test_rating(m.StoredWorkflowRatingAssociation, make_stored_workflow(), "stored_workflow")
    _test_rating(m.HistoryRatingAssociation, make_history(), "history")
    _test_rating(m.PageRatingAssociation, make_page(), "page")
    _test_rating(m.VisualizationRatingAssociation, make_visualization(), "visualization")
    _test_rating(m.HistoryDatasetCollectionRatingAssociation, make_hdca(), "dataset_collection")
    _test_rating(m.LibraryDatasetCollectionRatingAssociation, make_ldca(), "dataset_collection")


def test_hda_to_library_dataset_dataset_association(session, make_user, make_history, make_hda, make_library_folder):
    hda = make_hda(create_dataset=True, sa_session=session)
    target_folder = make_library_folder()
    mock_trans = MockTransaction(user=None)

    ldda = hda.to_library_dataset_dataset_association(
        trans=mock_trans,
        target_folder=target_folder,
    )
    assert target_folder.item_count == 1
    assert ldda.id
    assert ldda.library_dataset.id
    assert ldda.library_dataset.library_dataset_dataset_association.id

    new_ldda = hda.to_library_dataset_dataset_association(
        trans=mock_trans, target_folder=target_folder, replace_dataset=ldda.library_dataset
    )
    assert new_ldda.id != ldda.id
    assert new_ldda.library_dataset_id == ldda.library_dataset_id
    assert new_ldda.library_dataset.library_dataset_dataset_association_id == new_ldda.id
    assert len(new_ldda.library_dataset.expired_datasets) == 1
    assert new_ldda.library_dataset.expired_datasets[0] == ldda
    assert target_folder.item_count == 1


def test_hda_to_library_dataset_dataset_association_fails_if_private(
    session, make_user, make_history, make_hda, make_library_folder
):
    hda = make_hda(create_dataset=True, sa_session=session)
    hda.dataset.object_store_id = PRIVATE_OBJECT_STORE_ID
    target_folder = make_library_folder()
    mock_trans = MockTransaction(user=None)

    with pytest.raises(Exception) as exec_info:
        hda.to_library_dataset_dataset_association(
            trans=mock_trans,
            target_folder=target_folder,
        )
    assert m.CANNOT_SHARE_PRIVATE_DATASET_MESSAGE in str(exec_info.value)


def test_collection_get_interface(session, make_hda, make_dataset_collection):
    c = make_dataset_collection(collection_type="list")
    d = make_hda(create_dataset=True, sa_session=session)
    elements = 100
    dces = [
        m.DatasetCollectionElement(collection=c, element=d, element_identifier=f"{i}", element_index=i)
        for i in range(elements)
    ]
    for i in range(elements):
        assert c[i] == dces[i]


def test_collections_in_histories(session, make_dataset_collection, make_dataset_collection_element, make_hdca):
    c = make_dataset_collection(collection_type="pair")
    dce1 = make_dataset_collection_element(collection=c, element_identifier="left")
    dce2 = make_dataset_collection_element(collection=c, element_identifier="right")
    make_hdca(name="foo", collection=c)
    loaded_dataset_collection = get_hdca_by_name(session, "foo").collection

    assert len(loaded_dataset_collection.elements) == 2
    assert loaded_dataset_collection.collection_type == "pair"
    assert loaded_dataset_collection["left"] == dce1
    assert loaded_dataset_collection["right"] == dce2


def test_dataset_action_tuples(
    session,
    make_user,
    make_history,
    make_hda,
    make_role,
    make_dataset_permissions,
    make_dataset_collection,
    make_dataset_collection_element,
):
    role = make_role()
    hda1 = make_hda(create_dataset=True, sa_session=session)
    hda2 = make_hda(create_dataset=True, sa_session=session)
    make_dataset_permissions(action="action1", dataset=hda1.dataset, role=role)
    make_dataset_permissions(action=None, dataset=hda1.dataset, role=role)
    make_dataset_permissions(action="action3", dataset=hda1.dataset, role=role)
    c = make_dataset_collection(collection_type="type1")
    make_dataset_collection_element(collection=c, element=hda1)
    make_dataset_collection_element(collection=c, element=hda2)
    assert c.dataset_action_tuples == [("action1", role.id), ("action3", role.id)]


def test_dataset_dbkeys_and_extensions_summary(
    session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca
):
    d1 = make_hda(extension="bam", dbkey="hg19", create_dataset=True, sa_session=session)
    d2 = make_hda(extension="txt", dbkey="hg19", create_dataset=True, sa_session=session)
    c1 = make_dataset_collection(collection_type="paired")
    make_dataset_collection_element(collection=c1, element=d1)
    make_dataset_collection_element(collection=c1, element=d2)

    hdca = make_hdca(collection=c1)
    assert hdca.dataset_dbkeys_and_extensions_summary[0] == {"hg19"}
    assert hdca.dataset_dbkeys_and_extensions_summary[1] == {"bam", "txt"}


def test_populated_optimized_ok(session, make_dataset_collection, make_dataset_collection_element, make_hda):
    c1 = make_dataset_collection(collection_type="paired")
    make_dataset_collection_element(collection=c1, element=make_hda(create_dataset=True, sa_session=session))
    make_dataset_collection_element(collection=c1, element=make_hda(create_dataset=True, sa_session=session))
    assert c1.populated
    assert c1.populated_optimized


def test_populated_optimized_empty_list_list_ok(make_dataset_collection, make_dataset_collection_element):
    c1 = make_dataset_collection(collection_type="list")
    c2 = make_dataset_collection(collection_type="list:list")
    make_dataset_collection_element(collection=c2, element=c1)
    assert c1.populated
    assert c1.populated_optimized
    assert c2.populated
    assert c2.populated_optimized


def test_populated_optimized_list_list_not_populated(make_dataset_collection, make_dataset_collection_element):
    c1 = make_dataset_collection(collection_type="list", populated=False)
    c2 = make_dataset_collection(collection_type="list:list")
    make_dataset_collection_element(collection=c2, element=c1)
    assert not c1.populated
    assert not c1.populated_optimized
    assert not c2.populated
    assert not c2.populated_optimized


def test_default_disk_usage(session, make_user):
    u = make_user()
    u.adjust_total_disk_usage(1, None)
    user_reload = session.get(m.User, u.id)
    assert user_reload.disk_usage == 1


def test_history_contents(session, make_history, make_hda):
    h1 = make_history()
    d1 = make_hda(history=h1, name="1")
    d2 = make_hda(history=h1, name="2", visible=False, create_dataset=True, sa_session=session)
    d2.dataset.object_store_id = "foobar"
    d3 = make_hda(history=h1, name="3", deleted=True, create_dataset=True, sa_session=session)
    d3.dataset.object_store_id = "three_store"
    d4 = make_hda(history=h1, name="4", visible=False, deleted=True)

    def contents_iter_names(**kwds):
        history = session.get(m.History, h1.id)
        return [h.name for h in history.contents_iter(**kwds)]

    assert contents_iter_names() == ["1", "2", "3", "4"]
    assert contents_iter_names(deleted=False) == ["1", "2"]
    assert contents_iter_names(visible=True) == ["1", "3"]
    assert contents_iter_names(visible=True, object_store_ids=["three_store"]) == ["3"]
    assert contents_iter_names(visible=False) == ["2", "4"]
    assert contents_iter_names(deleted=True, visible=False) == ["4"]
    assert contents_iter_names(deleted=False, object_store_ids=["foobar"]) == ["2"]
    assert contents_iter_names(deleted=False, object_store_ids=["foobar2"]) == []
    assert contents_iter_names(ids=[d1.id, d2.id, d3.id, d4.id]) == ["1", "2", "3", "4"]
    assert contents_iter_names(ids=[d1.id, d2.id, d3.id, d4.id], max_in_filter_length=1) == ["1", "2", "3", "4"]
    assert contents_iter_names(ids=[d1.id, d3.id]) == ["1", "3"]


def test_current_galaxy_session(make_user, make_galaxy_session):
    user = make_user()
    galaxy_session = make_galaxy_session(user=user)
    assert user.current_galaxy_session == galaxy_session
    new_galaxy_session = make_galaxy_session()
    user.galaxy_sessions.append(new_galaxy_session)
    assert user.current_galaxy_session == new_galaxy_session


def test_next_hid(make_history):
    h = make_history()
    assert h.hid_counter == 1
    h._next_hid()
    assert h.hid_counter == 2
    h._next_hid(n=3)
    assert h.hid_counter == 5


def test_history_hid_counter_is_expired_after_next_hid_call(make_history):
    h = make_history()
    state = inspect(h)
    assert h.hid_counter == 1
    assert "hid_counter" not in state.unloaded
    assert "id" not in state.unloaded

    h._next_hid()

    assert "hid_counter" in state.unloaded  # this attribute has been expired
    assert "id" not in state.unloaded  # but other attributes have NOT been expired
    assert h.hid_counter == 2  # check this last: this causes this hid_counter to be reloaded


def test_get_display_name(make_ldda, make_hda, make_history, make_library, make_library_folder):

    def assert_display_name_converts_to_unicode(item, name):
        assert isinstance(item.get_display_name(), str)
        assert item.get_display_name() == name

    ldda = make_ldda(name="ldda_name")
    assert_display_name_converts_to_unicode(ldda, "ldda_name")

    hda = make_hda(name="hda_name")
    assert_display_name_converts_to_unicode(hda, "hda_name")

    history = make_history(name="history_name")
    assert_display_name_converts_to_unicode(history, "history_name")

    library = make_library(name="library_name")
    assert_display_name_converts_to_unicode(library, "library_name")

    library_folder = make_library_folder(name="library_folder")
    assert_display_name_converts_to_unicode(library_folder, "library_folder")

    history = make_history(name="Hello₩◎ґʟⅾ")
    assert isinstance(history.name, str)
    assert isinstance(history.get_display_name(), str)
    assert history.get_display_name() == "Hello₩◎ґʟⅾ"


def test_metadata_spec(make_hda):
    metadata = dict(chromCol=1, startCol=2, endCol=3)
    d = make_hda(extension="interval", metadata=metadata)
    assert d.metadata.chromCol == 1
    assert d.metadata.anyAttribute is None
    assert "items" not in d.metadata


def test_job_metrics(make_job):
    job = make_job()
    job.add_metric("gx", "galaxy_slots", 5)
    job.add_metric("system", "system_name", "localhost")

    assert len(job.text_metrics) == 1
    assert job.text_metrics[0].plugin == "system"
    assert job.text_metrics[0].metric_name == "system_name"
    assert job.text_metrics[0].metric_value == "localhost"
    assert len(job.numeric_metrics) == 1
    assert job.numeric_metrics[0].plugin == "gx"
    assert job.numeric_metrics[0].metric_name == "galaxy_slots"
    assert job.numeric_metrics[0].metric_value == 5


def test_task_metrics(make_task):
    task = make_task()
    task.add_metric("foo", "some-name", "some-value")
    big_value = ":".join(f"{i}" for i in range(2000))
    task.add_metric("env", "BIG_PATH", big_value)

    assert len(task.text_metrics) == 2
    assert task.text_metrics[0].plugin == "foo"
    assert task.text_metrics[0].metric_name == "some-name"
    assert task.text_metrics[0].metric_value == "some-value"
    assert task.text_metrics[1].plugin == "env"
    assert task.text_metrics[1].metric_name == "BIG_PATH"
    # Ensure big values truncated
    assert len(task.text_metrics[1].metric_value) <= 1023


# --- Batch matching tests ---



def _make_flat_collection(session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca, history, n_elements=2, extension="txt", dbkey="hg19", state="ok"):
    """Helper: create a flat (list) collection with HDAs in a history."""
    coll = make_dataset_collection(collection_type="list")
    for _ in range(n_elements):
        hda = make_hda(extension=extension, dbkey=dbkey, history=history, create_dataset=True, sa_session=session)
        hda.dataset.state = state
        session.add(hda.dataset)
        make_dataset_collection_element(collection=coll, element=hda)
    hdca = make_hdca(collection=coll, history=history)
    session.flush()
    return hdca


def _make_nested_collection(session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca, history, n_pairs=2, extension="fastqsanger", dbkey="hg38", state="ok", populated=True):
    """Helper: create a list:paired collection."""
    outer = make_dataset_collection(collection_type="list:paired")
    for i in range(n_pairs):
        inner = make_dataset_collection(collection_type="paired", populated=populated)
        for side in ("forward", "reverse"):
            hda = make_hda(extension=extension, dbkey=dbkey, history=history, create_dataset=True, sa_session=session)
            hda.dataset.state = state
            session.add(hda.dataset)
            make_dataset_collection_element(collection=inner, element=hda, element_identifier=side)
        make_dataset_collection_element(collection=outer, element=inner, element_identifier=f"pair_{i}")
    hdca = make_hdca(collection=outer, history=history)
    session.flush()
    return hdca


def test_batch_collection_summaries_flat(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Batch summary for flat collections matches individual property calls."""
    history = make_history()
    hdcas = []
    for i in range(5):
        ext = ["txt", "bam", "bed", "vcf", "fasta"][i]
        hdca = _make_flat_collection(
            session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
            history, n_elements=2, extension=ext,
        )
        hdcas.append(hdca)

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert len(unpopulated) == 0
    assert len(summaries) == 5

    for hdca in hdcas:
        assert hdca.id in summaries
        batch_summary = summaries[hdca.id]
        individual_summary = hdca.collection.dataset_states_and_extensions_summary
        assert set(batch_summary.extensions) == set(individual_summary.extensions)
        assert batch_summary.states == individual_summary.states


def test_batch_collection_summaries_nested(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Batch summary for nested (list:paired) collections matches individual property calls."""
    history = make_history()
    hdcas = []
    for _ in range(3):
        hdca = _make_nested_collection(
            session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
            history, n_pairs=2, extension="fastqsanger",
        )
        hdcas.append(hdca)

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert len(unpopulated) == 0
    assert len(summaries) == 3

    for hdca in hdcas:
        assert hdca.id in summaries
        batch_summary = summaries[hdca.id]
        individual_summary = hdca.collection.dataset_states_and_extensions_summary
        assert set(batch_summary.extensions) == set(individual_summary.extensions)
        assert batch_summary.states == individual_summary.states


def test_batch_collection_summaries_filters_unpopulated(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Collections with populated_state != 'ok' are excluded from summaries."""
    history = make_history()

    # One populated collection
    ok_hdca = _make_flat_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history,
    )

    # One unpopulated flat collection
    coll_unpop = make_dataset_collection(collection_type="list", populated=False)
    hda = make_hda(history=history, create_dataset=True, sa_session=session)
    make_dataset_collection_element(collection=coll_unpop, element=hda)
    unpop_hdca = make_hdca(collection=coll_unpop, history=history)
    session.flush()

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert ok_hdca.id in summaries
    assert unpop_hdca.id in unpopulated
    assert unpop_hdca.id not in summaries


def test_batch_collection_summaries_filters_unpopulated_nested(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Nested collections with unpopulated sub-collections are excluded."""
    history = make_history()

    # Nested collection with unpopulated inner
    hdca = _make_nested_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history, n_pairs=2, populated=False,
    )

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert hdca.id in unpopulated
    assert hdca.id not in summaries


def test_batch_collection_summaries_state_prefilter(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Collections with datasets in invalid states are excluded from summaries."""
    history = make_history()

    # Collection with all ok datasets
    ok_hdca = _make_flat_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history, extension="txt", state="ok",
    )

    # Collection with error datasets
    error_hdca = _make_flat_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history, extension="txt", state="error",
    )

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert ok_hdca.id in summaries
    assert error_hdca.id not in summaries  # filtered by state


def test_batch_collection_summaries_empty(session, make_history):
    """Empty history returns empty results."""
    history = make_history()

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert summaries == {}
    assert unpopulated == set()


def test_batch_collection_summaries_mixed_types(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Batch handles a mix of flat and nested collection types correctly."""
    history = make_history()

    flat_hdca = _make_flat_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history, extension="bam",
    )
    nested_hdca = _make_nested_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history, extension="fastqsanger",
    )

    valid_states = m.Dataset.valid_input_states
    summaries, unpopulated = _batch_collection_summaries(session, history.id, None, valid_states)

    assert len(summaries) == 2
    assert flat_hdca.id in summaries
    assert nested_hdca.id in summaries
    assert "bam" in summaries[flat_hdca.id].extensions
    assert "fastqsanger" in summaries[nested_hdca.id].extensions


def test_batch_collection_summaries_type_filter(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca):
    """Collection type filter restricts which types are returned."""
    history = make_history()

    flat_hdca = _make_flat_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history,
    )
    nested_hdca = _make_nested_collection(
        session, make_hda, make_dataset_collection, make_dataset_collection_element, make_hdca,
        history,
    )

    valid_states = m.Dataset.valid_input_states

    # Only flat
    summaries, _ = _batch_collection_summaries(session, history.id, {"list"}, valid_states)
    assert flat_hdca.id in summaries
    assert nested_hdca.id not in summaries

    # Only nested
    summaries, _ = _batch_collection_summaries(session, history.id, {"list:paired"}, valid_states)
    assert flat_hdca.id not in summaries
    assert nested_hdca.id in summaries


def test_prefetch_implicitly_converted_datasets(session, make_history, make_hda):
    """Batch-loading implicitly_converted_datasets populates the relationship."""
    history = make_history()
    hdas = []
    for _ in range(5):
        hda = make_hda(history=history, create_dataset=True, sa_session=session)
        hdas.append(hda)
    session.flush()

    # Create some implicit conversions for the first 2 HDAs
    for hda in hdas[:2]:
        converted = make_hda(history=history, create_dataset=True, sa_session=session)
        assoc = m.ImplicitlyConvertedDatasetAssociation(
            dataset=converted, parent=hda, file_type="bed"
        )
        session.add(assoc)
    session.flush()

    # Clear caches by expunging and re-loading
    for hda in hdas:
        session.expire(hda)

    _prefetch_implicitly_converted_datasets(hdas)

    # Verify the relationship is populated without extra queries
    for hda in hdas[:2]:
        assert "implicitly_converted_datasets" in hda.__dict__
        assert len(hda.implicitly_converted_datasets) == 1
    for hda in hdas[2:]:
        assert "implicitly_converted_datasets" in hda.__dict__
        assert len(hda.implicitly_converted_datasets) == 0


def test_batch_populated_check_empty(session):
    """Empty collection_ids returns empty set."""
    result = _batch_populated_check(session, "list:paired", [], False)
    assert result == set()


def test_batch_summary_query_empty(session):
    """Empty collection_ids returns empty dict."""
    result = _batch_summary_query(session, "list", [], False)
    assert result == {}


def test_batch_summary_query_flat(session, make_history, make_hda, make_dataset_collection, make_dataset_collection_element):
    """Batch summary query for flat collections returns correct data."""
    history = make_history()
    coll = make_dataset_collection(collection_type="list")
    hda1 = make_hda(extension="bam", dbkey="hg19", history=history, create_dataset=True, sa_session=session)
    hda1.dataset.state = "ok"
    session.add(hda1.dataset)
    hda2 = make_hda(extension="txt", dbkey="hg38", history=history, create_dataset=True, sa_session=session)
    hda2.dataset.state = "ok"
    session.add(hda2.dataset)
    make_dataset_collection_element(collection=coll, element=hda1)
    make_dataset_collection_element(collection=coll, element=hda2)
    session.flush()

    result = _batch_summary_query(session, "list", [coll.id], False)
    assert coll.id in result
    summary = result[coll.id]
    assert set(summary.extensions) == {"bam", "txt"}
    assert summary.states == {"ok": 2}
