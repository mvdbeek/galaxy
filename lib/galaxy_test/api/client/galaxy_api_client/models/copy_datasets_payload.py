from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_datasets_payload_source_entry import CopyDatasetsPayloadSourceEntry


T = TypeVar("T", bound="CopyDatasetsPayload")


@_attrs_define
class CopyDatasetsPayload:
    """
    Attributes:
        source_content (list[CopyDatasetsPayloadSourceEntry]):
        target_history_ids (list[str] | None | Unset):
        target_history_name (None | str | Unset):
    """

    source_content: list[CopyDatasetsPayloadSourceEntry]
    target_history_ids: list[str] | None | Unset = UNSET
    target_history_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_content = []
        for source_content_item_data in self.source_content:
            source_content_item = source_content_item_data.to_dict()
            source_content.append(source_content_item)

        target_history_ids: list[str] | None | Unset
        if isinstance(self.target_history_ids, Unset):
            target_history_ids = UNSET
        elif isinstance(self.target_history_ids, list):
            target_history_ids = self.target_history_ids

        else:
            target_history_ids = self.target_history_ids

        target_history_name: None | str | Unset
        if isinstance(self.target_history_name, Unset):
            target_history_name = UNSET
        else:
            target_history_name = self.target_history_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_content": source_content,
            }
        )
        if target_history_ids is not UNSET:
            field_dict["target_history_ids"] = target_history_ids
        if target_history_name is not UNSET:
            field_dict["target_history_name"] = target_history_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.copy_datasets_payload_source_entry import CopyDatasetsPayloadSourceEntry

        d = dict(src_dict)
        source_content = []
        _source_content = d.pop("source_content")
        for source_content_item_data in _source_content:
            source_content_item = CopyDatasetsPayloadSourceEntry.from_dict(source_content_item_data)

            source_content.append(source_content_item)

        def _parse_target_history_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                target_history_ids_type_0 = cast(list[str], data)

                return target_history_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        target_history_ids = _parse_target_history_ids(d.pop("target_history_ids", UNSET))

        def _parse_target_history_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_history_name = _parse_target_history_name(d.pop("target_history_name", UNSET))

        copy_datasets_payload = cls(
            source_content=source_content,
            target_history_ids=target_history_ids,
            target_history_name=target_history_name,
        )

        copy_datasets_payload.additional_properties = d
        return copy_datasets_payload

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
