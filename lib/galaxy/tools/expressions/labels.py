"""Filling in output labels of user-defined tools.

``galaxy.tool_util_models.user_tool_labels`` defines the label syntax and which labels a
tool may be saved with. Here each ``$(inputs...)`` reference is resolved in Python by
walking a projection of the tool state, one key at a time, so only what a reference
names is looked at. Nothing is evaluated as Cheetah or JavaScript.

The projection:

- scalars are plain values, conditionals and sections are mappings, repeats and multiple
  selections are lists;
- a dataset has the keys in ``LABEL_FILE_KEYS``, where ``name`` is its name in the history;
- a collection has the keys in ``LABEL_COLLECTION_KEYS``; its ``elements`` are read one
  at a time, by position for list-like collection types and by identifier otherwise, and
  are loaded only when a reference reaches them.

``element_identifier`` is what Cheetah's ``element_identifier`` gives: the identifier of
a collection element, including the element a mapped-over job runs on, and otherwise the
name of the dataset or collection. Paths, locations, file contents and object store
details are never included.

A reference that resolves to text fills in as that text and any other value as JSON; a
reference through an optional input left empty fills in as nothing. A reference that
does not resolve is kept as written, so a label never fails a job: stored tools may
predate the label rules, and a runtime or connected value in the workflow editor has no
value yet.
"""

import json
import logging
from collections.abc import (
    Callable,
    Container,
    Mapping,
    Sequence,
)
from typing import (
    Any,
    Optional,
    Union,
)

from galaxy import model
from galaxy.model.dataset_collections.adapters import (
    CollectionAdapter,
    TransientCollectionAdapterDatasetInstanceElement,
)
from galaxy.tool_util_models.user_tool_labels import (
    Key,
    LabelReference,
    MAX_LABEL_LENGTH,
    parse_label,
)
from galaxy.tools.parameters.workflow_utils import (
    is_runtime_value,
    NoReplacement,
)
from galaxy.tools.runtime import is_list_like

log = logging.getLogger(__name__)


class _Unresolved:
    pass


_UNRESOLVED = _Unresolved()


class _Elements:
    """A collection's elements, loaded only when a reference reaches them."""

    def __init__(self, collection_type: str, elements: Callable[[], Sequence[Any]]):
        self.list_like = is_list_like(collection_type)
        self.elements = elements

    def step(self, key: Key) -> Any:
        elements = self.elements()
        if self.list_like:
            if key == "length":
                return len(elements)
            if isinstance(key, int) and key < len(elements):
                return elements[key]
            return _UNRESOLVED
        for element in elements:
            if element.element_identifier == key:
                return element
        return _UNRESOLVED


def render_user_tool_label(
    label: str, input_names: Container[str], state: Mapping[str, Any], on_string: Optional[str]
) -> str:
    """Fill in the references in ``label`` from the declared inputs of ``state``."""
    if len(label) > MAX_LABEL_LENGTH:
        # Only a tool stored before the length limit has such a label.
        return label[:MAX_LABEL_LENGTH]
    parts: list[str] = []
    length = 0
    for part in parse_label(label):
        if length >= MAX_LABEL_LENGTH:
            break
        if isinstance(part, str):
            filled = part
        else:
            written = label[part.start : part.end]
            filled = (
                _fill(part, written, input_names, state, on_string) if isinstance(part, LabelReference) else written
            )
        parts.append(filled)
        length += len(filled)
    return "".join(parts)[:MAX_LABEL_LENGTH]


def _fill(
    reference: LabelReference,
    written: str,
    input_names: Container[str],
    state: Mapping[str, Any],
    on_string: Optional[str],
) -> str:
    if reference.is_on_string:
        return written if on_string is None else on_string
    name = reference.input_name
    if name is None or name not in input_names or name not in state:
        return written
    try:
        value = _resolve(state[name], reference.keys[1:])
    except Exception:
        # Resolving only walks model objects, mappings and lists; an error is a bug, not a bad label.
        log.warning("Could not fill in output label reference %s", written, exc_info=True)
        return written
    if value is _UNRESOLVED:
        return written
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, sort_keys=True)


def _resolve(value: Any, keys: Sequence[Key]) -> Any:
    for key in keys:
        if value is None:
            return None
        value = _step(value, key)
        if value is _UNRESOLVED:
            return value
    return _project(value)


def _step(value: Any, key: Key) -> Any:
    if isinstance(value, NoReplacement) or is_runtime_value(value):
        return _UNRESOLVED
    view = _view(value)
    if isinstance(view, _Elements):
        return view.step(key)
    if isinstance(view, (list, tuple)):
        if key == "length":
            return len(view)
        if isinstance(key, int) and key < len(view):
            return view[key]
        return _UNRESOLVED
    if isinstance(view, Mapping) and isinstance(key, str) and not key.startswith("__") and key in view:
        return view[key]
    return _UNRESOLVED


def _project(value: Any) -> Any:
    if isinstance(value, NoReplacement) or is_runtime_value(value):
        return _UNRESOLVED
    view = _view(value)
    if isinstance(view, _Elements):
        # Printing every element of a collection costs a query per element; labels read them one at a time.
        return _UNRESOLVED
    if isinstance(view, (list, tuple)):
        # No more items than characters fit in a label.
        return [None if (item := _project(v)) is _UNRESOLVED else item for v in view[:MAX_LABEL_LENGTH]]
    if isinstance(view, Mapping):
        projected = {}
        for key, item in view.items():
            if isinstance(key, str) and not key.startswith("__"):
                item = _project(item)
                if item is not _UNRESOLVED:
                    projected[key] = item
        return projected
    if view is None or isinstance(view, (str, int, float, bool)):
        return view
    # Anything else is an internal object labels have no business seeing.
    return _UNRESOLVED


def _view(value: Any) -> Any:
    """Return the label view of a dataset or collection, and anything else unchanged."""
    if isinstance(value, model.HistoryDatasetCollectionAssociation):
        return _collection(value.collection, value.name)
    if isinstance(value, model.DatasetCollectionElement):
        if value.child_collection is not None:
            return _collection(value.child_collection, value.element_identifier)
        element_object = value.element_object
        assert isinstance(element_object, model.DatasetInstance)
        return _file(element_object, value.element_identifier)
    if isinstance(value, TransientCollectionAdapterDatasetInstanceElement):
        return _file(value.hda, value.element_identifier)
    if isinstance(value, model.DatasetCollection):
        return _collection(value, None)
    if isinstance(value, CollectionAdapter):
        return _collection(value, _adapter_name(value))
    if isinstance(value, model.DatasetInstance):
        return _file(value, None)
    return value


def _file(dataset: model.DatasetInstance, element_identifier: Optional[str]) -> dict[str, Any]:
    # Expanding a mapped-over collection records each element's identifier on its dataset.
    identifier = element_identifier or getattr(dataset, "element_identifier", None) or dataset.name
    return {"name": dataset.name, "element_identifier": identifier, "format": dataset.extension}


def _collection(collection: Union[model.DatasetCollection, CollectionAdapter], name: Optional[str]) -> dict[str, Any]:
    return {
        "name": name,
        "element_identifier": name,
        "collection_type": collection.collection_type,
        "elements": _Elements(collection.collection_type, lambda: collection.elements),
    }


def _adapter_name(adapter: CollectionAdapter) -> Optional[str]:
    adapting = adapter.adapting
    if isinstance(adapting, model.DatasetCollectionElement):
        return adapting.element_identifier
    if isinstance(adapting, model.DatasetInstance):
        return adapting.name
    return None
