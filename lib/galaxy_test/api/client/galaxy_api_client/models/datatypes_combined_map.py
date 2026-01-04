from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.datatypes_map import DatatypesMap


T = TypeVar("T", bound="DatatypesCombinedMap")


@_attrs_define
class DatatypesCombinedMap:
    """
    Attributes:
        datatypes (list[str]): List of datatypes extensions
        datatypes_mapping (DatatypesMap):
    """

    datatypes: list[str]
    datatypes_mapping: DatatypesMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datatypes = self.datatypes

        datatypes_mapping = self.datatypes_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datatypes": datatypes,
                "datatypes_mapping": datatypes_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datatypes_map import DatatypesMap

        d = dict(src_dict)
        datatypes = cast(list[str], d.pop("datatypes"))

        datatypes_mapping = DatatypesMap.from_dict(d.pop("datatypes_mapping"))

        datatypes_combined_map = cls(
            datatypes=datatypes,
            datatypes_mapping=datatypes_mapping,
        )

        datatypes_combined_map.additional_properties = d
        return datatypes_combined_map

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
