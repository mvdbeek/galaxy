from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExitCodeJobMessage")


@_attrs_define
class ExitCodeJobMessage:
    """
    Attributes:
        desc (None | str):
        error_level (float):
        exit_code (int):
        type_ (Literal['exit_code']):
        code_desc (None | str | Unset):
    """

    desc: None | str
    error_level: float
    exit_code: int
    type_: Literal["exit_code"]
    code_desc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desc: None | str
        desc = self.desc

        error_level = self.error_level

        exit_code = self.exit_code

        type_ = self.type_

        code_desc: None | str | Unset
        if isinstance(self.code_desc, Unset):
            code_desc = UNSET
        else:
            code_desc = self.code_desc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desc": desc,
                "error_level": error_level,
                "exit_code": exit_code,
                "type": type_,
            }
        )
        if code_desc is not UNSET:
            field_dict["code_desc"] = code_desc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_desc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        desc = _parse_desc(d.pop("desc"))

        error_level = d.pop("error_level")

        exit_code = d.pop("exit_code")

        type_ = cast(Literal["exit_code"], d.pop("type"))
        if type_ != "exit_code":
            raise ValueError(f"type must match const 'exit_code', got '{type_}'")

        def _parse_code_desc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_desc = _parse_code_desc(d.pop("code_desc", UNSET))

        exit_code_job_message = cls(
            desc=desc,
            error_level=error_level,
            exit_code=exit_code,
            type_=type_,
            code_desc=code_desc,
        )

        exit_code_job_message.additional_properties = d
        return exit_code_job_message

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
