from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoOptionsParameterValidatorModel")


@_attrs_define
class NoOptionsParameterValidatorModel:
    """
    Attributes:
        implicit (bool | Unset):  Default: False.
        message (None | str | Unset):
        negate (bool | Unset):  Default: False.
        type_ (Literal['no_options'] | Unset):  Default: 'no_options'.
    """

    implicit: bool | Unset = False
    message: None | str | Unset = UNSET
    negate: bool | Unset = False
    type_: Literal["no_options"] | Unset = "no_options"

    def to_dict(self) -> dict[str, Any]:
        implicit = self.implicit

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        negate = self.negate

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        implicit = d.pop("implicit", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        negate = d.pop("negate", UNSET)

        type_ = cast(Literal["no_options"] | Unset, d.pop("type", UNSET))
        if type_ != "no_options" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'no_options', got '{type_}'")

        no_options_parameter_validator_model = cls(
            implicit=implicit,
            message=message,
            negate=negate,
            type_=type_,
        )

        return no_options_parameter_validator_model
