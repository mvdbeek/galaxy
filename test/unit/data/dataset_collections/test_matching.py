import pytest

from galaxy.model import (
    DatasetCollection,
    DatasetCollectionElement,
)
from galaxy.model.dataset_collections import (
    matching,
    query,
    registry,
    type_description,
)

TYPE_REGISTRY = registry.DatasetCollectionTypesRegistry()
TYPE_DESCRIPTION_FACTORY = type_description.CollectionTypeDescriptionFactory(TYPE_REGISTRY)


def test_pairs_match():
    assert_can_match(pair_instance(), pair_instance())


def test_lists_of_same_cardinality_match():
    assert_can_match(list_instance(), list_instance())


def test_nested_lists_match():
    nested_list = nested_list = example_list_of_paired_datasets()
    assert_can_match(nested_list, nested_list)


def test_different_types_cannot_match():
    assert_cannot_match(list_instance(), pair_instance())
    assert_cannot_match(pair_instance(), list_instance())


def test_lists_of_different_cardinality_do_not_match():
    list_1 = list_instance(ids=["data1", "data2"])
    list_2 = list_instance(ids=["data1", "data2", "data3"])
    assert_cannot_match(list_1, list_2)
    assert_cannot_match(list_2, list_1)


def test_empty_list_does_not_match_non_empty_list_in_either_order():
    empty_list = list_instance(ids=[])
    non_empty_list = list_instance(ids=["data1", "data2"])
    assert_cannot_match(empty_list, non_empty_list)
    assert_cannot_match(non_empty_list, empty_list)


def test_empty_lists_match_each_other_and_yield_no_slices():
    matched = assert_can_match(list_instance(ids=[]), list_instance(ids=[]))
    assert list(matched.slice_collections()) == []


def test_unenumerated_structure_does_not_match_other_type_in_either_order():
    unenumerated_pair = (pair_instance(), "paired")
    assert_cannot_match(unenumerated_pair, list_instance())
    assert_cannot_match(list_instance(), unenumerated_pair)


def test_matching_prefers_enumerated_structure_regardless_of_order():
    unenumerated_pair = (pair_instance(), "paired")
    assert assert_can_match(pair_instance(), unenumerated_pair).linked_structure.children_known
    assert assert_can_match(unenumerated_pair, pair_instance()).linked_structure.children_known


def test_type_mismatch_details_describe_both_collections():
    mismatch = assert_cannot_match(list_instance(name="a list"), pair_instance(name="a pair"))
    assert str(mismatch) == (
        "Collections 'a list' (list) and 'a pair' (paired) have incompatible collection types. "
        "To map them together, use collections of the same type."
    )


def test_element_mismatch_details_describe_both_collections():
    mismatch = assert_cannot_match(list_instance(ids=[], name="empty input"), list_instance(name="populated input"))
    assert str(mismatch) == (
        "Collections 'empty input' (no elements) and 'populated input' (2 elements) have different "
        "element structures. To map them together, use collections with the same number and nesting of elements."
    )


def test_mismatch_details_fall_back_to_input_names_for_unnamed_collections():
    mismatch = assert_cannot_match(list_instance(ids=["data1"]), list_instance(ids=[]))
    assert str(mismatch).startswith("Collections 'input_0' (1 element) and 'input_1' (no elements)")


def test_mismatch_references_persisted_collections_in_message_order():
    empty_list = collection_instance(collection_type="list", elements=[], id=7)
    populated_list = collection_instance(collection_type="list", elements=[hda_element("data1")], id=11)
    mismatch = assert_cannot_match(empty_list, populated_list)
    assert mismatch.collection_references == [{"src": "hdca", "id": 7}, {"src": "hdca", "id": 11}]


def test_mismatch_references_omit_unpersisted_collections():
    persisted_list = collection_instance(collection_type="list", elements=[hda_element("data1")], id=11)
    mismatch = assert_cannot_match(list_instance(ids=[]), persisted_list)
    assert mismatch.collection_references == [{"src": "hdca", "id": 11}]


def test_mismatch_references_identify_collection_elements():
    dce = DatasetCollectionElement(
        collection=DatasetCollection(collection_type="list"),
        element=DatasetCollection(collection_type="list"),
        element_identifier="outer element",
    )
    dce.id = 13
    persisted_list = collection_instance(collection_type="list", elements=[hda_element("data1")], id=11)
    mismatch = assert_cannot_match(dce, persisted_list)
    assert str(mismatch).startswith("Collections 'outer element' (no elements) and 'input_1' (1 element)")
    assert mismatch.collection_references == [{"src": "dce", "id": 13}, {"src": "hdca", "id": 11}]


# "list" mismatches on element count, "paired" on collection type - the two
# message shapes have different lengths and both must fit the details column.
@pytest.mark.parametrize("other_collection_type", ["list", "paired"])
def test_structure_mismatch_identifies_inputs_with_persistable_details(other_collection_type):
    input_name = f"input_{'a' * 100}"
    other_input_name = f"input_{'b' * 100}"
    to_match = matching.CollectionsToMatch()
    to_match.add(input_name, list_instance(ids=["data1", "data2"], name="c" * 300))
    to_match.add(
        other_input_name, collection_instance(collection_type=other_collection_type, elements=[], name="d" * 300)
    )

    with pytest.raises(matching.CollectionStructureMismatch) as exc_info:
        matching.MatchingCollections.for_collections(to_match, TYPE_DESCRIPTION_FACTORY)

    assert exc_info.value.input_name == other_input_name
    assert exc_info.value.other_input_name == input_name
    assert len(str(exc_info.value)) <= 255


def test_valid_collection_subcollection_matching():
    flat_list = list_instance(ids=["data1", "data2", "data3"])
    nested_list = example_list_of_paired_datasets()
    assert_cannot_match(flat_list, nested_list)
    assert_cannot_match(nested_list, flat_list)
    assert_can_match((nested_list, "paired"), flat_list)


# Sibling matching is symmetric: paired and paired_or_unpaired can be
# zipped under a common map-over regardless of arrival order. The
# substitution-rejection sentiment (paired_or_unpaired cannot be
# substituted *where paired is required*) is a connection-time concern
# tested in test_type_descriptions.py::test_paired_accepts_relation.
def test_paired_and_paired_or_unpaired_match_symmetric():
    paired = pair_instance()
    optional_paired = paired_or_unpaired_pair_instance()
    assert_can_match(optional_paired, paired)
    assert_can_match(paired, optional_paired)


def test_paired_or_unpaired_with_one_element_rejected_against_paired():
    """Cardinality safety: 1-element paired_or_unpaired cannot zip with 2-element paired."""
    paired = pair_instance()
    one_element_optional = collection_instance(
        collection_type="paired_or_unpaired",
        elements=[hda_element("unpaired")],
    )
    assert_cannot_match(paired, one_element_optional)
    assert_cannot_match(one_element_optional, paired)


def test_query_can_match_list_to_list():
    flat_list = list_instance(ids=["data1", "data2", "data3"])
    q = query.HistoryQuery.from_collection_types(["list"], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(flat_list) is False
    assert q.direct_match(flat_list) is True


def test_query_can_match_list_of_paireds_to_paired():
    list_of_paired_datasets = example_list_of_paired_datasets()
    q = query.HistoryQuery.from_collection_types(["paired"], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(list_of_paired_datasets).collection_type == "paired"


def test_query_can_match_list_of_lists_to_paired():
    list_of_lists = example_list_of_lists()
    q = query.HistoryQuery.from_collection_types(["paired"], TYPE_DESCRIPTION_FACTORY)
    assert not q.can_map_over(list_of_lists)
    assert not q.direct_match(list_of_lists)


def test_query_can_match_list_of_lists_to_list():
    list_of_lists = example_list_of_lists()
    q = query.HistoryQuery.from_collection_types(["list"], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(list_of_lists).collection_type == "list"
    assert not q.direct_match(list_of_lists)


def test_query_can_match_list_of_paireds_to_list_or_paired():
    list_of_paired_datasets = example_list_of_paired_datasets()
    q = query.HistoryQuery.from_collection_types(["list", "paired"], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(list_of_paired_datasets).collection_type == "paired"
    assert q.direct_match(list_of_paired_datasets) is False


def test_query_can_match_list_of_lists_to_list_or_paired():
    list_of_lists = example_list_of_lists()
    q = query.HistoryQuery.from_collection_types(["list", "paired"], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(list_of_lists).collection_type == "list"
    assert q.direct_match(list_of_lists) is False


def test_query_always_direct_match_if_no_collection_type_on_input_specified():
    list_of_lists = example_list_of_lists()
    q = query.HistoryQuery.from_collection_types([], TYPE_DESCRIPTION_FACTORY)
    assert q.can_map_over(list_of_lists) is False
    assert q.direct_match(list_of_lists) is True


def assert_can_match(*items) -> matching.MatchingCollections:
    to_match = build_collections_to_match(*items)
    matched = matching.MatchingCollections.for_collections(to_match, TYPE_DESCRIPTION_FACTORY)
    assert matched is not None
    return matched


def assert_cannot_match(*items) -> matching.CollectionStructureMismatch:
    to_match = build_collections_to_match(*items)
    with pytest.raises(matching.CollectionStructureMismatch) as exc_info:
        matching.MatchingCollections.for_collections(to_match, TYPE_DESCRIPTION_FACTORY)
    return exc_info.value


def build_collections_to_match(*items):
    to_match = matching.CollectionsToMatch()

    for i, item in enumerate(items):
        if isinstance(item, tuple):
            collection_instance, subcollection_type = item
        else:
            collection_instance, subcollection_type = item, None
        to_match.add(f"input_{i}", collection_instance, subcollection_type)
    return to_match


def example_list_of_paired_datasets():
    return list_instance(
        elements=[
            pair_element("data1"),
            pair_element("data2"),
            pair_element("data3"),
        ],
        collection_type="list:paired",
    )


def example_list_of_lists():
    return list_instance(
        elements=[
            list_instance(),
            list_instance(),
        ],
        collection_type="list:list",
    )


def pair_element(element_identifier):
    return collection_element(element_identifier, pair_instance().collection)


def list_element(element_identifier, list_collection=None):
    return collection_element(element_identifier, list_collection or list_instance().collection)


def list_of_lists_instance():
    return list_instance(
        elements=[
            list_element("outer1"),
            list_element("outer2"),
        ]
    )


def pair_instance(name=None):
    paired_collection_instance = collection_instance(
        collection_type="paired",
        elements=[
            hda_element("left"),
            hda_element("right"),
        ],
        name=name,
    )
    return paired_collection_instance


def list_paired_instance():
    return list_instance(
        elements=[
            pair_element("data1"),
            pair_element("data2"),
            pair_element("data3"),
        ],
        collection_type="list:paired",
    )


def list_of_paired_and_unpaired_instance():
    return collection_instance(
        collection_type="list:paired_or_unpaired",
        elements=[
            collection_element(
                "el1",
                collection(
                    "paired_or_unpaired",
                    [
                        hda_element("forward"),
                        hda_element("reverse"),
                    ],
                ),
            ),
            collection_element(
                "el2",
                collection(
                    "paired_or_unpaired",
                    [
                        hda_element("unpaired"),
                    ],
                ),
            ),
        ],
    )


def paired_or_unpaired_pair_instance():
    paired_collection_instance = collection_instance(
        collection_type="paired_or_unpaired",
        elements=[
            hda_element("forward"),
            hda_element("reverse"),
        ],
    )
    return paired_collection_instance


def list_instance(collection_type="list", elements=None, ids=None, name=None):
    if not elements:
        if ids is None:
            ids = ["data1", "data2"]
        elements = [hda_element(_) for _ in ids]
    list_collection_instance = collection_instance(collection_type=collection_type, elements=elements, name=name)
    return list_collection_instance


class MockCollectionInstance:
    def __init__(self, collection_type, elements, name=None, id=None):
        self.collection = MockCollection(collection_type, elements)
        self.name = name
        self.id = id


class MockCollection:
    def __init__(self, collection_type, elements):
        self.collection_type = collection_type
        self.elements = elements
        self.populated = True
        self.column_definitions = None


class MockCollectionElement:
    def __init__(self, element_identifier, collection):
        self.element_identifier = element_identifier
        self.child_collection = collection
        self.hda = None
        self.columns = None


class MockHDAElement:
    def __init__(self, element_identifier):
        self.element_identifier = element_identifier
        self.child_collection = False
        self.hda = object()
        self.columns = None


collection_instance = MockCollectionInstance
collection = MockCollection
collection_element = MockCollectionElement
hda_element = MockHDAElement
