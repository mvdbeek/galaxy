from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_source_transform_action_type import DatasetSourceTransformActionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetSourceTransform")


@_attrs_define
class DatasetSourceTransform:
    """
    Attributes:
        action (DatasetSourceTransformActionType):
        datatype_ext (None | str | Unset): If action is 'datatype_groom', this is the datatype that was used to find and
            run the grooming code as part of the transform action.
    """

    action: DatasetSourceTransformActionType
    datatype_ext: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        datatype_ext: None | str | Unset
        if isinstance(self.datatype_ext, Unset):
            datatype_ext = UNSET
        else:
            datatype_ext = self.datatype_ext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if datatype_ext is not UNSET:
            field_dict["datatype_ext"] = datatype_ext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DatasetSourceTransformActionType(d.pop("action"))

        def _parse_datatype_ext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datatype_ext = _parse_datatype_ext(d.pop("datatype_ext", UNSET))

        dataset_source_transform = cls(
            action=action,
            datatype_ext=datatype_ext,
        )

        dataset_source_transform.additional_properties = d
        return dataset_source_transform

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
