from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_for_updates_response_status import CheckForUpdatesResponseStatus

T = TypeVar("T", bound="CheckForUpdatesResponse")


@_attrs_define
class CheckForUpdatesResponse:
    """
    Attributes:
        message (str): Unstructured description of tool shed updates discovered or failure
        status (CheckForUpdatesResponseStatus): 'ok' or 'error'
    """

    message: str
    status: CheckForUpdatesResponseStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        status = CheckForUpdatesResponseStatus(d.pop("status"))

        check_for_updates_response = cls(
            message=message,
            status=status,
        )

        check_for_updates_response.additional_properties = d
        return check_for_updates_response

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
