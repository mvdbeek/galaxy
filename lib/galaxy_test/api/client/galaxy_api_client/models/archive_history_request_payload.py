from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveHistoryRequestPayload")


@_attrs_define
class ArchiveHistoryRequestPayload:
    """
    Attributes:
        archive_export_id (None | str | Unset): The encoded ID of the export record to associate with this history
            archival.This is used to be able to recover the history from the export record.
        purge_history (bool | Unset): Whether to purge the history after archiving it. It requires an
            `archive_export_id` to be set. Default: False.
    """

    archive_export_id: None | str | Unset = UNSET
    purge_history: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_export_id: None | str | Unset
        if isinstance(self.archive_export_id, Unset):
            archive_export_id = UNSET
        else:
            archive_export_id = self.archive_export_id

        purge_history = self.purge_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archive_export_id is not UNSET:
            field_dict["archive_export_id"] = archive_export_id
        if purge_history is not UNSET:
            field_dict["purge_history"] = purge_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_archive_export_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archive_export_id = _parse_archive_export_id(d.pop("archive_export_id", UNSET))

        purge_history = d.pop("purge_history", UNSET)

        archive_history_request_payload = cls(
            archive_export_id=archive_export_id,
            purge_history=purge_history,
        )

        archive_history_request_payload.additional_properties = d
        return archive_history_request_payload

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
