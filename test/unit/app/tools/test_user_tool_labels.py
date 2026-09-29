import json
import logging
from typing import Any
from unittest import mock

import pytest

from galaxy import model
from galaxy.model.dataset_collections.adapters import (
    PromoteCollectionElementToCollectionAdapter,
    PromoteDatasetToCollection,
)
from galaxy.tool_util_models.user_tool_labels import (
    LABEL_COLLECTION_KEYS,
    LABEL_FILE_KEYS,
    label_problems,
    lift_label,
    MAX_LABEL_LENGTH,
)
from galaxy.tool_util_models.yaml_parameters import YamlGalaxyToolParameter
from galaxy.tools.expressions import labels
from galaxy.tools.expressions.labels import render_user_tool_label
from galaxy.tools.parameters.workflow_utils import (
    ConnectedValue,
    RuntimeValue,
)


def _hda(name: str, extension: str = "txt") -> model.HistoryDatasetAssociation:
    return model.HistoryDatasetAssociation(name=name, extension=extension, create_dataset=True, flush=False)


def _collection(collection_type: str, **elements: Any) -> model.DatasetCollection:
    collection = model.DatasetCollection(collection_type=collection_type)
    for index, (identifier, element) in enumerate(elements.items()):
        model.DatasetCollectionElement(
            collection=collection, element=element, element_identifier=identifier, element_index=index
        )
    return collection


def _render(label: str, state: dict[str, Any], on_string: str = "data 1") -> str:
    return render_user_tool_label(label, state.keys(), state, on_string)


STATE: dict[str, Any] = {
    "input": _hda("reads.fastq", "fastqsanger"),
    "n": 3,
    "x": 1.5,
    "flag": True,
    "modes": ["a", "b"],
    "opt": None,
    "cond": {"select": "a", "__current_case__": 0, "value": "nested"},
    "rep": [{"__index__": 0, "v": "first"}],
}


@pytest.mark.parametrize(
    "label,expected",
    [
        ("from $(inputs.input.name) as $(inputs['input'].format)", "from reads.fastq as fastqsanger"),
        ("$(inputs.input.element_identifier)", "reads.fastq"),
        ("$(runtime.on_string) filtered", "data 1 filtered"),
        ("n=$(inputs.n) x=$(inputs.x) $(inputs.flag)", "n=3 x=1.5 true"),
        ("$(inputs.modes) $(inputs.modes[1]) $(inputs.modes.length)", '["a", "b"] b 2'),
        ("$(inputs.cond.value) $(inputs.rep[0].v) $(inputs.cond)", 'nested first {"select": "a", "value": "nested"}'),
        ("[$(inputs.opt)] [$(inputs.opt.name)]", "[] []"),
        ("\\$(inputs.n) \\${x} \\\\$(inputs.n)", "$(inputs.n) ${x} \\3"),
        (" plain text ", " plain text "),
    ],
)
def test_references_filled_in(label, expected):
    assert _render(label, STATE) == expected


def test_each_unresolved_reference_kept_as_written():
    unresolved = "$(inputs.missing) $(inputs.input.path) $(inputs.input.basename) $(inputs.n.x) $(1 + 1) ${x} $(inputs)"
    assert _render(f"n=$(inputs.n) {unresolved}", STATE) == f"n=3 {unresolved}"


def test_undeclared_state_not_readable():
    assert render_user_tool_label("$(inputs.n)", ["input"], STATE, None) == "$(inputs.n)"


def test_on_string_without_value_kept_as_written():
    assert render_user_tool_label("$(runtime.on_string) filtered", [], {}, None) == "$(runtime.on_string) filtered"


def test_long_stored_label_cut_without_filling_in():
    label = "$(inputs.n)" + "x" * MAX_LABEL_LENGTH
    assert _render(label, STATE) == label[:MAX_LABEL_LENGTH]


def test_dataset_and_collection_views():
    listed = model.HistoryDatasetCollectionAssociation(collection=_collection("list", s1=_hda("a.txt")), name="l")
    state = {"input": _hda("reads.fastq"), "listed": listed}
    dataset = json.loads(_render("$(inputs.input)", state))
    collection = json.loads(_render("$(inputs.listed)", state))
    element = json.loads(_render("$(inputs.listed.elements[0])", state))
    assert set(dataset) == set(LABEL_FILE_KEYS)
    assert set(collection) == set(LABEL_COLLECTION_KEYS) - {"elements"}
    assert set(element) == set(LABEL_FILE_KEYS)
    assert _render("$(inputs.listed.elements)", state) == "$(inputs.listed.elements)"


def test_collection_references():
    listed = model.HistoryDatasetCollectionAssociation(
        collection=_collection("list", s1=_hda("a.txt"), s2=_hda("b.txt")), name="my list"
    )
    paired = _collection("paired", forward=_hda("f.fq"), reverse=_hda("r.fq"))
    state = {"listed": listed, "paired": paired}
    label = "$(inputs.listed.name) $(inputs.listed.collection_type) $(inputs.listed.elements.length) $(inputs.listed.elements[1].element_identifier)"
    assert _render(label, state) == "my list list 2 s2"
    assert _render("$(inputs.paired.elements['reverse'].name) $(inputs.paired.elements[0].name)", state) == (
        "r.fq $(inputs.paired.elements[0].name)"
    )


def test_references_project_only_what_they_name():
    listed = model.HistoryDatasetCollectionAssociation(
        collection=_collection("list", s1=_hda("a.txt"), s2=_hda("b.txt"), s3=_hda("c.txt")), name="l"
    )
    elements = listed.collection.elements
    with mock.patch.object(
        model.DatasetCollection, "elements", new_callable=mock.PropertyMock, return_value=elements
    ) as loaded:
        assert _render("$(inputs.listed.name) $(inputs.listed.collection_type)", {"listed": listed}) == "l list"
        assert not loaded.called
    with mock.patch.object(labels, "_file", wraps=labels._file) as file_view:
        assert _render("literal $(inputs.listed.name)", {"listed": listed}) == "literal l"
        assert file_view.call_count == 0
        assert _render("$(inputs.listed.elements[1].name)", {"listed": listed}) == "b.txt"
        assert file_view.call_count == 1


def test_element_identifier_of_nested_element():
    nested = model.DatasetCollection(collection_type="list:paired")
    element = model.DatasetCollectionElement(
        collection=nested, element=_collection("paired", forward=_hda("f.fq")), element_identifier="sample1"
    )
    label = "$(inputs.pair.name) $(inputs.pair.elements.forward.element_identifier)"
    assert _render(label, {"pair": element}) == "sample1 forward"


def test_collection_adapters():
    listed = _collection("list", s1=_hda("a.txt"))
    state = {
        "promoted": PromoteDatasetToCollection(_hda("reads.txt"), "paired_or_unpaired"),
        "element": PromoteCollectionElementToCollectionAdapter(listed.elements[0]),
    }
    label = "$(inputs.promoted.name) $(inputs.promoted.elements.unpaired.name) $(inputs.element.name)"
    assert _render(label, state) == "reads.txt reads.txt s1"


def test_runtime_values_kept_as_written():
    state = {"input": ConnectedValue(), "n": RuntimeValue(), "cond": {"inner": {"__class__": "ConnectedValue"}}}
    label = "$(inputs.input.name) $(inputs.n) $(inputs.cond.inner) $(inputs.cond)"
    assert _render(label, state) == "$(inputs.input.name) $(inputs.n) $(inputs.cond.inner) {}"


def test_error_while_resolving_keeps_reference_and_warns(caplog):
    with mock.patch.object(labels, "_step", side_effect=RuntimeError("boom")):
        with caplog.at_level(logging.WARNING, logger=labels.__name__):
            assert _render("n=$(inputs.cond.value)", STATE) == "n=$(inputs.cond.value)"
    assert "$(inputs.cond.value)" in caplog.text


def test_internal_keys_not_readable():
    assert _render("$(inputs.cond.__current_case__) $(inputs.rep[0].__index__)", STATE) == (
        "$(inputs.cond.__current_case__) $(inputs.rep[0].__index__)"
    )


def test_filling_in_stops_once_the_label_is_full():
    state = {"v": "x" * MAX_LABEL_LENGTH, "n": 3}
    with mock.patch.object(labels, "_resolve", wraps=labels._resolve) as resolve:
        assert _render("$(inputs.v) $(inputs.n)", state) == "x" * MAX_LABEL_LENGTH
    assert resolve.call_count == 1


def test_long_list_printed_as_far_as_it_fits():
    numbers = list(range(1000))
    assert _render("$(inputs.numbers)", {"numbers": numbers}) == json.dumps(numbers)[:MAX_LABEL_LENGTH]


LIFT_INPUTS = [
    YamlGalaxyToolParameter.model_validate(param).root
    for param in ({"type": "integer", "name": "n"}, {"type": "data", "name": "input"})
]
LIFT_STATE = {"n": 7, "input": _hda("reads.fastq")}


@pytest.mark.parametrize(
    "stored",
    [
        "$(inputs.missing['$(inputs.n)'])",
        "$(inputs.missing['${x}'])",
        "${on_string} from $(inputs.input.name)",
        "\\\\$(inputs.missing) \\a$(inputs.n) $$(inputs.n) \\",
        "$(inputs.input.path) $(1 + 1) ${x} \\$(inputs.n)",
        "${x}" + "a" * 235 + "$(inputs.n)",
        "x" * 249 + "${",
        "x" * 240 + "$(inputs.n)",
        "$(inputs.n)" + "x" * MAX_LABEL_LENGTH,
        "\\$(inputs.n)" + "x" * MAX_LABEL_LENGTH,
        "$(inputs.n[" + "1" * 5000 + "])",
    ],
)
def test_lifted_label_fills_in_as_the_stored_one(stored):
    lifted = lift_label(stored, LIFT_INPUTS)
    assert len(lifted) <= MAX_LABEL_LENGTH
    assert label_problems(lifted, LIFT_INPUTS) == []
    rendered = render_user_tool_label(lifted, ["n", "input"], LIFT_STATE, None)
    expected = render_user_tool_label(stored, ["n", "input"], LIFT_STATE, None)
    assert rendered and expected.startswith(rendered)
    if len(stored) + stored.count("$") + stored.count("\\") <= MAX_LABEL_LENGTH:
        assert rendered == expected
