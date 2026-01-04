from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MessageExceptionModel")


@_attrs_define
class MessageExceptionModel:
    """
    Attributes:
        err_code (int):
        err_msg (str):
    """

    err_code: int
    err_msg: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        err_code = self.err_code

        err_msg = self.err_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "err_code": err_code,
                "err_msg": err_msg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        err_code = d.pop("err_code")

        err_msg = d.pop("err_msg")

        message_exception_model = cls(
            err_code=err_code,
            err_msg=err_msg,
        )

        message_exception_model.additional_properties = d
        return message_exception_model

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
