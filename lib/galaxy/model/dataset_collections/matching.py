from typing import (
    Literal,
    Optional,
    TypedDict,
)

from galaxy import exceptions
from galaxy.model import DatasetCollectionElement
from galaxy.util import (
    bunch,
    shrink_string_by_size,
)
from .structure import (
    get_collection,
    get_structure,
    leaf,
)

# The rendered message is persisted in workflow_invocation_message.details, a
# TrimmedString(255). Bound every interpolated value so the whole sentence fits.
MAX_DISPLAYED_COLLECTION_NAME = 30
MAX_DISPLAYED_COLLECTION_TYPE = 20


class CollectionReference(TypedDict):
    """A structured (src, id) reference to a collection instance."""

    src: Literal["hdca", "dce"]
    id: int


class CollectionStructureMismatch(exceptions.MessageException):
    """Collections a step maps over together cannot be matched up element by element.

    ``collection_references`` identifies the mismatched collection instances in the
    order the message names them, so callers can surface the actual collections.
    """

    def __init__(
        self,
        input_name: str,
        other_input_name: str,
        message: str,
        collection_references: list[CollectionReference] | None = None,
    ) -> None:
        self.input_name = input_name
        self.other_input_name = other_input_name
        self.collection_references = collection_references or []
        super().__init__(message)


def _collection_reference(hdca) -> CollectionReference | None:
    if hdca.id is None:
        return None
    src: Literal["hdca", "dce"] = "dce" if isinstance(hdca, DatasetCollectionElement) else "hdca"
    return {"src": src, "id": hdca.id}


def _display_collection_name(hdca, input_name: str) -> str:
    if isinstance(hdca, DatasetCollectionElement):
        name = hdca.element_identifier
    else:
        name = hdca.name
    return shrink_string_by_size(name or input_name, MAX_DISPLAYED_COLLECTION_NAME)


def _element_count_description(structure) -> str:
    count = len(structure.children)
    if count == 0:
        return "no elements"
    if count == 1:
        return "1 element"
    return f"{count} elements"


def _structure_mismatch_message(name: str, structure, other_name: str, other_structure) -> str:
    """Explain in end-user terms why two collections cannot be mapped over together.

    Element counts are rendered only for the compatible-type case, where both
    structures are enumerated trees: a structure with unknown children can only
    mismatch on collection type.
    """
    type_description = structure.collection_type_description
    other_type_description = other_structure.collection_type_description
    if not type_description.compatible(other_type_description):
        collection_type = shrink_string_by_size(type_description.collection_type, MAX_DISPLAYED_COLLECTION_TYPE)
        other_collection_type = shrink_string_by_size(
            other_type_description.collection_type, MAX_DISPLAYED_COLLECTION_TYPE
        )
        return (
            f"Collections '{name}' ({collection_type}) and '{other_name}' ({other_collection_type}) have "
            "incompatible collection types. To map them together, use collections of the same type."
        )
    return (
        f"Collections '{name}' ({_element_count_description(structure)}) and "
        f"'{other_name}' ({_element_count_description(other_structure)}) have different element structures. "
        "To map them together, use collections with the same number and nesting of elements."
    )


class CollectionsToMatch:
    """Structure representing a set of collections that need to be matched up
    when running tools (possibly workflows in the future as well).
    """

    def __init__(self):
        self.collections = {}

    def add(self, input_name, hdca, subcollection_type=None, linked=True):
        self.collections[input_name] = bunch.Bunch(
            hdca=hdca,
            subcollection_type=subcollection_type,
            linked=linked,
        )

    def has_collections(self):
        return len(self.collections) > 0

    def items(self):
        return self.collections.items()


class MatchingCollections:
    """Structure holding the result of matching a list of collections
    together. This class being different than the class above and being
    created in the DatasetCollectionManager layer may seem like
    overkill but I suspect in the future plugins will be subtypable for
    instance so matching collections will need to make heavy use of the
    dataset collection type registry managed by the dataset collections
    service - hence the complexity now.
    """

    def __init__(self):
        self.linked_structure = None
        self.linked_input_name: str | None = None
        self.unlinked_structures = []
        self.collections = {}
        self.subcollection_types = {}
        self.action_tuples = {}
        self.when_values = None

    def __attempt_add_to_linked_match(
        self, input_name, hdca, child_collection, collection_type_description, subcollection_type
    ):
        structure = get_structure(
            child_collection, collection_type_description, leaf_subcollection_type=subcollection_type
        )
        linked_structure = self.linked_structure
        linked_input_name = self.linked_input_name
        if (
            linked_structure is not None
            and linked_input_name is not None
            and not linked_structure.compatible_shape(structure)
        ):
            linked_hdca = self.collections[linked_input_name]
            collection_references = [
                reference
                for reference in (_collection_reference(linked_hdca), _collection_reference(hdca))
                if reference is not None
            ]
            raise CollectionStructureMismatch(
                input_name,
                linked_input_name,
                _structure_mismatch_message(
                    _display_collection_name(linked_hdca, linked_input_name),
                    linked_structure,
                    _display_collection_name(hdca, input_name),
                    structure,
                ),
                collection_references=collection_references,
            )
        # The reference structure drives slicing, which needs enumerated children;
        # an unenumerated structure only vouches for its collection type. Prefer
        # enumerated structures so the choice is independent of input-name order.
        if linked_structure is None or (structure.children_known and not linked_structure.children_known):
            self.linked_structure = structure
            self.linked_input_name = input_name
        self.collections[input_name] = hdca
        self.subcollection_types[input_name] = subcollection_type

    def slice_collections(self):
        self.linked_structure.when_values = self.when_values
        return self.linked_structure.walk_collections({k: get_collection(v) for k, v in self.collections.items()})

    def subcollection_mapping_type(self, input_name):
        return self.subcollection_types[input_name]

    @property
    def structure(self):
        """Yield cross product of all unlinked collections structures to linked collection structure."""
        effective_structure = leaf
        for unlinked_structure in self.unlinked_structures:
            effective_structure = effective_structure.multiply(unlinked_structure)
        linked_structure = self.linked_structure
        if linked_structure is None:
            linked_structure = leaf
        effective_structure = effective_structure.multiply(linked_structure)
        effective_structure.when_values = self.when_values
        return None if effective_structure.is_leaf else effective_structure

    def map_over_action_tuples(self, input_name):
        if input_name not in self.action_tuples:
            collection_instance = self.collections[input_name]
            self.action_tuples[input_name] = get_collection(collection_instance).dataset_action_tuples
        return self.action_tuples[input_name]

    def is_mapped_over(self, input_name):
        return input_name in self.collections

    @staticmethod
    def for_collections(collections_to_match, collection_type_descriptions) -> Optional["MatchingCollections"]:
        if not collections_to_match.has_collections():
            return None

        matching_collections = MatchingCollections()
        for input_key, to_match in sorted(collections_to_match.items()):
            hdca = to_match.hdca
            # Resolve the contained collection: for an HDCA this is
            # hdca.collection; for a DCE it is dce.child_collection
            # (not dce.collection which is the *parent*).
            # Both collection_type_description and get_structure must
            # use the same collection so the type and elements agree.
            child_collection = get_collection(hdca)
            collection_type_description = collection_type_descriptions.for_collection_type(
                child_collection.collection_type
            )
            subcollection_type = to_match.subcollection_type

            if to_match.linked:
                matching_collections.__attempt_add_to_linked_match(
                    input_key, hdca, child_collection, collection_type_description, subcollection_type
                )
            else:
                structure = get_structure(
                    child_collection,
                    collection_type_description,
                    leaf_subcollection_type=subcollection_type,
                )
                matching_collections.unlinked_structures.append(structure)

        return matching_collections
