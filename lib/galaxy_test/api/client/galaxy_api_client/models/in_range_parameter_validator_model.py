from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InRangeParameterValidatorModel")


@_attrs_define
class InRangeParameterValidatorModel:
    """
    Attributes:
        exclude_max (bool | Unset):  Default: False.
        exclude_min (bool | Unset):  Default: False.
        implicit (bool | Unset):  Default: False.
        max_ (float | int | None | Unset):
        message (None | str | Unset):
        min_ (float | int | None | Unset):
        negate (bool | Unset):  Default: False.
        type_ (Literal['in_range'] | Unset):  Default: 'in_range'.
    """

    exclude_max: bool | Unset = False
    exclude_min: bool | Unset = False
    implicit: bool | Unset = False
    max_: float | int | None | Unset = UNSET
    message: None | str | Unset = UNSET
    min_: float | int | None | Unset = UNSET
    negate: bool | Unset = False
    type_: Literal["in_range"] | Unset = "in_range"

    def to_dict(self) -> dict[str, Any]:
        exclude_max = self.exclude_max

        exclude_min = self.exclude_min

        implicit = self.implicit

        max_: float | int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        min_: float | int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        negate = self.negate

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if exclude_max is not UNSET:
            field_dict["exclude_max"] = exclude_max
        if exclude_min is not UNSET:
            field_dict["exclude_min"] = exclude_min
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if max_ is not UNSET:
            field_dict["max"] = max_
        if message is not UNSET:
            field_dict["message"] = message
        if min_ is not UNSET:
            field_dict["min"] = min_
        if negate is not UNSET:
            field_dict["negate"] = negate
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclude_max = d.pop("exclude_max", UNSET)

        exclude_min = d.pop("exclude_min", UNSET)

        implicit = d.pop("implicit", UNSET)

        def _parse_max_(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_min_(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        negate = d.pop("negate", UNSET)

        type_ = cast(Literal["in_range"] | Unset, d.pop("type", UNSET))
        if type_ != "in_range" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'in_range', got '{type_}'")

        in_range_parameter_validator_model = cls(
            exclude_max=exclude_max,
            exclude_min=exclude_min,
            implicit=implicit,
            max_=max_,
            message=message,
            min_=min_,
            negate=negate,
            type_=type_,
        )

        return in_range_parameter_validator_model
