from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_source_type import DatasetSourceType
from ..models.dataset_state import DatasetState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HDAObject")


@_attrs_define
class HDAObject:
    """History Dataset Association Object

    Attributes:
        history_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['HistoryDatasetAssociation']): The name of the database model class.
        purged (bool):
        state (DatasetState):
        tags (list[str]):
        accessible (bool | None | Unset):
        copied_from_ldda_id (None | str | Unset):
        hda_ldda (DatasetSourceType | Unset):
    """

    history_id: str
    id: str
    model_class: Literal["HistoryDatasetAssociation"]
    purged: bool
    state: DatasetState
    tags: list[str]
    accessible: bool | None | Unset = UNSET
    copied_from_ldda_id: None | str | Unset = UNSET
    hda_ldda: DatasetSourceType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        id = self.id

        model_class = self.model_class

        purged = self.purged

        state = self.state.value

        tags = self.tags

        accessible: bool | None | Unset
        if isinstance(self.accessible, Unset):
            accessible = UNSET
        else:
            accessible = self.accessible

        copied_from_ldda_id: None | str | Unset
        if isinstance(self.copied_from_ldda_id, Unset):
            copied_from_ldda_id = UNSET
        else:
            copied_from_ldda_id = self.copied_from_ldda_id

        hda_ldda: str | Unset = UNSET
        if not isinstance(self.hda_ldda, Unset):
            hda_ldda = self.hda_ldda.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
                "id": id,
                "model_class": model_class,
                "purged": purged,
                "state": state,
                "tags": tags,
            }
        )
        if accessible is not UNSET:
            field_dict["accessible"] = accessible
        if copied_from_ldda_id is not UNSET:
            field_dict["copied_from_ldda_id"] = copied_from_ldda_id
        if hda_ldda is not UNSET:
            field_dict["hda_ldda"] = hda_ldda

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        history_id = d.pop("history_id")

        id = d.pop("id")

        model_class = cast(Literal["HistoryDatasetAssociation"], d.pop("model_class"))
        if model_class != "HistoryDatasetAssociation":
            raise ValueError(f"model_class must match const 'HistoryDatasetAssociation', got '{model_class}'")

        purged = d.pop("purged")

        state = DatasetState(d.pop("state"))

        tags = cast(list[str], d.pop("tags"))

        def _parse_accessible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        accessible = _parse_accessible(d.pop("accessible", UNSET))

        def _parse_copied_from_ldda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_ldda_id = _parse_copied_from_ldda_id(d.pop("copied_from_ldda_id", UNSET))

        _hda_ldda = d.pop("hda_ldda", UNSET)
        hda_ldda: DatasetSourceType | Unset
        if isinstance(_hda_ldda, Unset):
            hda_ldda = UNSET
        else:
            hda_ldda = DatasetSourceType(_hda_ldda)

        hda_object = cls(
            history_id=history_id,
            id=id,
            model_class=model_class,
            purged=purged,
            state=state,
            tags=tags,
            accessible=accessible,
            copied_from_ldda_id=copied_from_ldda_id,
            hda_ldda=hda_ldda,
        )

        hda_object.additional_properties = d
        return hda_object

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
