from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.classes_map import ClassesMap
    from ..models.extension_map import ExtensionMap


T = TypeVar("T", bound="DatatypesMap")


@_attrs_define
class DatatypesMap:
    """
    Attributes:
        class_to_classes (ClassesMap): Dictionary mapping datatype's classes with their base classes
        ext_to_class_name (ExtensionMap): Dictionary mapping datatype's extensions with implementation classes
    """

    class_to_classes: ClassesMap
    ext_to_class_name: ExtensionMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_to_classes = self.class_to_classes.to_dict()

        ext_to_class_name = self.ext_to_class_name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class_to_classes": class_to_classes,
                "ext_to_class_name": ext_to_class_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.classes_map import ClassesMap
        from ..models.extension_map import ExtensionMap

        d = dict(src_dict)
        class_to_classes = ClassesMap.from_dict(d.pop("class_to_classes"))

        ext_to_class_name = ExtensionMap.from_dict(d.pop("ext_to_class_name"))

        datatypes_map = cls(
            class_to_classes=class_to_classes,
            ext_to_class_name=ext_to_class_name,
        )

        datatypes_map.additional_properties = d
        return datatypes_map

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
