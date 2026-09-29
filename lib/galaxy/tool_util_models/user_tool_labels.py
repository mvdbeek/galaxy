"""Output labels of user-defined tools.

A label is literal text with optional parameter references. ``$(inputs.<name>...)``
reads the tool state and ``$(runtime.on_string)`` is the description of the job's
inputs that XML tool labels get as ``on_string``. Nothing in a label is evaluated as
JavaScript or Cheetah. ``\\$(``, ``\\${`` and ``\\\\`` are a literal ``$(``, ``${`` and
``\\``, as in the expression evaluator.

This module parses labels and checks their references against a tool's declared
inputs. ``galaxy.tools.expressions.labels`` fills them in.
"""

import re
from typing import (
    Callable,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from .yaml_parameters import (
    YamlConditionalParameter,
    YamlDataCollectionParameter,
    YamlDataParameter,
    YamlGalaxyParameterT,
    YamlRepeatParameter,
    YamlSectionParameter,
    YamlSelectParameter,
)

# Applies to the label as written and as filled in; the name columns hold 255 characters.
MAX_LABEL_LENGTH = 250

# What a label sees of a dataset and of a collection.
# Labels are filled in when a job is created, before an input made by a job that has not finished
# has its file name, so no key depends on it.
LABEL_FILE_KEYS = ("name", "element_identifier", "format")
LABEL_COLLECTION_KEYS = ("name", "element_identifier", "collection_type", "elements")

_SEGMENT = r"""\.\w+|\['(?:[^'\\]|\\.)+'\]|\["(?:[^"\\]|\\.)+"\]|\[[0-9]+\]"""
_SEGMENT_RE = re.compile(_SEGMENT)
_REFERENCE_RE = re.compile(rf"\$\((\w+)((?:{_SEGMENT})*)\)")
_QUOTED_ESCAPE_RE = re.compile(r"\\(.)")

_NOT_A_REFERENCE = (
    "labels only take the parameter references $(inputs.<name>...) and $(runtime.on_string), "
    "write '\\$(' for a literal '$('"
)

Key = Union[str, int]


class LabelReference(NamedTuple):
    """A ``$(symbol...)`` parameter reference at ``label[start:end]``."""

    start: int
    end: int
    symbol: str
    keys: Tuple[Key, ...]

    @property
    def input_name(self) -> Optional[str]:
        if self.symbol == "inputs" and self.keys and isinstance(self.keys[0], str):
            return self.keys[0]
        return None

    @property
    def is_on_string(self) -> bool:
        return self.symbol == "runtime" and self.keys == ("on_string",)


class UnsupportedExpression(NamedTuple):
    """An opening ``$(`` or ``${`` at ``label[start:end]`` that starts no parameter reference."""

    start: int
    end: int


LabelPart = Union[str, LabelReference, UnsupportedExpression]


def parse_label(label: str) -> Iterator[LabelPart]:
    """Split ``label`` into literal text (with escapes applied), references and unsupported expressions."""
    text: List[str] = []
    position = 0
    while position < len(label):
        char = label[position]
        if char == "\\":
            escaped = label[position + 1 : position + 3]
            if escaped in ("$(", "${"):
                text.append(escaped)
                position += 3
            elif escaped[:1] == "\\":
                text.append("\\")
                position += 2
            else:
                text.append(label[position : position + 2])
                position += 2
        elif char == "$" and label[position + 1 : position + 2] in ("(", "{"):
            if text:
                yield "".join(text)
                text = []
            match = _REFERENCE_RE.match(label, position)
            if match:
                yield LabelReference(position, match.end(), match.group(1), _keys(match.group(2)))
                position = match.end()
            else:
                yield UnsupportedExpression(position, position + 2)
                position += 2
        else:
            text.append(char)
            position += 1
    if text:
        yield "".join(text)


def label_problems(label: str, inputs: Sequence[YamlGalaxyParameterT]) -> List[str]:
    """Describe each part of ``label`` that is not a reference to something ``inputs`` provide."""
    return [problem for _, problem in _problems(label, inputs)]


def lift_label(label: str, inputs: Sequence[YamlGalaxyParameterT]) -> str:
    """Rewrite a stored ``label`` so that ``label_problems`` reports nothing.

    The result fills in as ``label`` does, or as the start of it when escaping makes the
    result too long: each rejected part becomes literal text, and the cut falls between
    whole references and escapes.
    """
    units: List[str] = []
    if len(label) > MAX_LABEL_LENGTH:
        # A label this long is shown as its first characters, with nothing filled in.
        units.extend(_literal_units(label[:MAX_LABEL_LENGTH]))
    else:
        rejected = {start for start, _ in _problems(label, inputs)}
        for part in parse_label(label):
            if isinstance(part, str):
                units.extend(_literal_units(part))
            elif part.start in rejected or isinstance(part, UnsupportedExpression):
                units.extend(_literal_units(label[part.start : part.end]))
            else:
                units.append(label[part.start : part.end])
    lifted: List[str] = []
    length = 0
    for unit in units:
        length += len(unit)
        if length > MAX_LABEL_LENGTH:
            break
        lifted.append(unit)
    return "".join(lifted)


def _literal_units(text: str) -> Iterator[str]:
    """Label source for ``text``, in pieces that each fill in as a piece of ``text``."""
    position = 0
    while position < len(text):
        if text[position] == "\\":
            yield "\\\\"
            position += 1
        elif text[position] == "$" and text[position + 1 : position + 2] in ("(", "{"):
            yield f"\\{text[position : position + 2]}"
            position += 2
        else:
            yield text[position]
            position += 1


def _keys(segments: str) -> Tuple[Key, ...]:
    keys: List[Key] = []
    for match in _SEGMENT_RE.finditer(segments):
        segment = match.group(0)
        if segment[0] == ".":
            keys.append(segment[1:])
        elif segment[1] in "'\"":
            keys.append(_QUOTED_ESCAPE_RE.sub(r"\1", segment[2:-2]))
        else:
            keys.append(int(segment[1:-1]))
    return tuple(keys)


def _problems(label: str, inputs: Sequence[YamlGalaxyParameterT]) -> List[Tuple[int, str]]:
    problems: List[Tuple[int, str]] = []
    for part in parse_label(label):
        if isinstance(part, UnsupportedExpression):
            written = label[part.start : part.end]
            if written == "${":
                problems.append((part.start, "'${' JavaScript blocks are not allowed, write '\\${' for a literal '${'"))
            else:
                snippet = label[part.start : part.start + 40]
                problems.append((part.start, f"{snippet!r} is not allowed; {_NOT_A_REFERENCE}"))
        elif isinstance(part, LabelReference) and not part.is_on_string:
            written = label[part.start : part.end]
            if part.input_name is None:
                problems.append((part.start, f"{written!r} is not allowed; {_NOT_A_REFERENCE}"))
            elif (reason := _group_problem(inputs, part.keys)) is not None:
                problems.append((part.start, f"{written!r} does not resolve: {reason}"))
    return problems


def _group_problem(params: Sequence[YamlGalaxyParameterT], keys: Sequence[Key]) -> Optional[str]:
    if not keys:
        return None
    name = keys[0]
    # Conditional branches may declare the same name with different types; any one will do.
    problems = [_value_problem(param, keys[1:]) for param in params if param.name == name]
    if not problems:
        return f"no input named {name!r} is declared"
    return None if None in problems else problems[0]


def _value_problem(param: YamlGalaxyParameterT, keys: Sequence[Key]) -> Optional[str]:
    if isinstance(param, YamlDataParameter):
        return _list_problem(keys, _file_problem) if param.multiple else _file_problem(keys)
    if isinstance(param, YamlDataCollectionParameter):
        return _collection_problem(keys)
    if isinstance(param, YamlRepeatParameter):
        nested = [p.root for p in param.parameters]
        return _list_problem(keys, lambda rest: _group_problem(nested, rest))
    if isinstance(param, YamlSectionParameter):
        return _group_problem([p.root for p in param.parameters], keys)
    if isinstance(param, YamlConditionalParameter):
        branches = [p.root for when in param.whens for p in when.parameters]
        return _group_problem([param.test_parameter, *branches], keys)
    if isinstance(param, YamlSelectParameter) and param.multiple:
        return _list_problem(keys, _scalar_problem)
    return _scalar_problem(keys)


def _list_problem(keys: Sequence[Key], item_problem: Callable[[Sequence[Key]], Optional[str]]) -> Optional[str]:
    if not keys or tuple(keys) == ("length",):
        return None
    if isinstance(keys[0], int):
        return item_problem(keys[1:])
    return "a list is read with [<index>] or .length"


def _file_problem(keys: Sequence[Key]) -> Optional[str]:
    if not keys or (len(keys) == 1 and keys[0] in LABEL_FILE_KEYS):
        return None
    return f"a dataset only provides {', '.join(LABEL_FILE_KEYS)} to labels"


def _collection_problem(keys: Sequence[Key]) -> Optional[str]:
    if not keys or (len(keys) == 1 and keys[0] in LABEL_COLLECTION_KEYS and keys[0] != "elements"):
        return None
    if keys[0] != "elements":
        return f"a collection only provides {', '.join(LABEL_COLLECTION_KEYS)} to labels"
    if tuple(keys[1:]) == ("length",):
        return None
    if len(keys) == 1:
        return "a collection's elements are read one at a time, as elements[<index>] or elements.<identifier>"
    # Which identifiers exist, and whether an element is a dataset or a collection, depends on
    # the collection a run uses.
    element_keys = keys[2:]
    if not element_keys:
        return None
    if element_keys[0] == "elements":
        return _collection_problem(element_keys)
    if len(element_keys) == 1 and element_keys[0] in LABEL_FILE_KEYS + LABEL_COLLECTION_KEYS:
        return None
    return f"a collection element only provides {', '.join(dict.fromkeys(LABEL_FILE_KEYS + LABEL_COLLECTION_KEYS))} to labels"


def _scalar_problem(keys: Sequence[Key]) -> Optional[str]:
    if not keys:
        return None
    return "a text, number, boolean, color or select value has no attributes"
