from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hda_basic_info import HDABasicInfo


T = TypeVar("T", bound="ShareHistoryExtra")


@_attrs_define
class ShareHistoryExtra:
    """
    Attributes:
        accessible_count (int | Unset): The number of datasets in the history that are public or accessible by all the
            target users. Default: 0.
        can_change (list[HDABasicInfo] | Unset): A collection of datasets that are not accessible by one or more of the
            target users and that can be made accessible for others by the user sharing the history.
        can_share (bool | Unset): Indicates whether the resource can be directly shared or requires further actions.
            Default: False.
        cannot_change (list[HDABasicInfo] | Unset): A collection of datasets that are not accessible by one or more of
            the target users and that cannot be made accessible for others by the user sharing the history.
    """

    accessible_count: int | Unset = 0
    can_change: list[HDABasicInfo] | Unset = UNSET
    can_share: bool | Unset = False
    cannot_change: list[HDABasicInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessible_count = self.accessible_count

        can_change: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.can_change, Unset):
            can_change = []
            for can_change_item_data in self.can_change:
                can_change_item = can_change_item_data.to_dict()
                can_change.append(can_change_item)

        can_share = self.can_share

        cannot_change: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cannot_change, Unset):
            cannot_change = []
            for cannot_change_item_data in self.cannot_change:
                cannot_change_item = cannot_change_item_data.to_dict()
                cannot_change.append(cannot_change_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessible_count is not UNSET:
            field_dict["accessible_count"] = accessible_count
        if can_change is not UNSET:
            field_dict["can_change"] = can_change
        if can_share is not UNSET:
            field_dict["can_share"] = can_share
        if cannot_change is not UNSET:
            field_dict["cannot_change"] = cannot_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hda_basic_info import HDABasicInfo

        d = dict(src_dict)
        accessible_count = d.pop("accessible_count", UNSET)

        _can_change = d.pop("can_change", UNSET)
        can_change: list[HDABasicInfo] | Unset = UNSET
        if _can_change is not UNSET:
            can_change = []
            for can_change_item_data in _can_change:
                can_change_item = HDABasicInfo.from_dict(can_change_item_data)

                can_change.append(can_change_item)

        can_share = d.pop("can_share", UNSET)

        _cannot_change = d.pop("cannot_change", UNSET)
        cannot_change: list[HDABasicInfo] | Unset = UNSET
        if _cannot_change is not UNSET:
            cannot_change = []
            for cannot_change_item_data in _cannot_change:
                cannot_change_item = HDABasicInfo.from_dict(cannot_change_item_data)

                cannot_change.append(cannot_change_item)

        share_history_extra = cls(
            accessible_count=accessible_count,
            can_change=can_change,
            can_share=can_share,
            cannot_change=cannot_change,
        )

        share_history_extra.additional_properties = d
        return share_history_extra

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
