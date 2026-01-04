from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReloadFeedback")


@_attrs_define
class ReloadFeedback:
    """
    Attributes:
        failed (list[None | str]):
        message (str):
        reloaded (list[None | str]):
    """

    failed: list[None | str]
    message: str
    reloaded: list[None | str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed = []
        for failed_item_data in self.failed:
            failed_item: None | str
            failed_item = failed_item_data
            failed.append(failed_item)

        message = self.message

        reloaded = []
        for reloaded_item_data in self.reloaded:
            reloaded_item: None | str
            reloaded_item = reloaded_item_data
            reloaded.append(reloaded_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed": failed,
                "message": message,
                "reloaded": reloaded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:

            def _parse_failed_item(data: object) -> None | str:
                if data is None:
                    return data
                return cast(None | str, data)

            failed_item = _parse_failed_item(failed_item_data)

            failed.append(failed_item)

        message = d.pop("message")

        reloaded = []
        _reloaded = d.pop("reloaded")
        for reloaded_item_data in _reloaded:

            def _parse_reloaded_item(data: object) -> None | str:
                if data is None:
                    return data
                return cast(None | str, data)

            reloaded_item = _parse_reloaded_item(reloaded_item_data)

            reloaded.append(reloaded_item)

        reload_feedback = cls(
            failed=failed,
            message=message,
            reloaded=reloaded,
        )

        reload_feedback.additional_properties = d
        return reload_feedback

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
