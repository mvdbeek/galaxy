from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegexParameterValidatorModel")


@_attrs_define
class RegexParameterValidatorModel:
    """Check if a regular expression **matches** the value, i.e. appears
    at the beginning of the value. To enforce a match of the complete value use
    ``$`` at the end of the expression. The expression is given is the content
    of the validator tag. Note that for ``selects`` each option is checked
    separately.

        Attributes:
            expression (str):
            implicit (bool | Unset):  Default: False.
            message (None | str | Unset):
            negate (bool | Unset):  Default: False.
            type_ (Literal['regex'] | Unset):  Default: 'regex'.
    """

    expression: str
    implicit: bool | Unset = False
    message: None | str | Unset = UNSET
    negate: bool | Unset = False
    type_: Literal["regex"] | Unset = "regex"

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        implicit = self.implicit

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        negate = self.negate

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expression": expression,
            }
        )
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if message is not UNSET:
            field_dict["message"] = message
        if negate is not UNSET:
            field_dict["negate"] = negate
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expression = d.pop("expression")

        implicit = d.pop("implicit", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        negate = d.pop("negate", UNSET)

        type_ = cast(Literal["regex"] | Unset, d.pop("type", UNSET))
        if type_ != "regex" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'regex', got '{type_}'")

        regex_parameter_validator_model = cls(
            expression=expression,
            implicit=implicit,
            message=message,
            negate=negate,
            type_=type_,
        )

        return regex_parameter_validator_model
