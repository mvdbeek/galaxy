from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parsed_workbook_element_element_type import ParsedWorkbookElementElementType

if TYPE_CHECKING:
    from ..models.parsed_workbook_collection import ParsedWorkbookCollection
    from ..models.parsed_workbook_hda import ParsedWorkbookHda


T = TypeVar("T", bound="ParsedWorkbookElement")


@_attrs_define
class ParsedWorkbookElement:
    """
    Attributes:
        element_identifier (str):
        element_index (int):
        element_type (ParsedWorkbookElementElementType):
        object_ (ParsedWorkbookCollection | ParsedWorkbookHda):
    """

    element_identifier: str
    element_index: int
    element_type: ParsedWorkbookElementElementType
    object_: ParsedWorkbookCollection | ParsedWorkbookHda
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.parsed_workbook_hda import ParsedWorkbookHda

        element_identifier = self.element_identifier

        element_index = self.element_index

        element_type = self.element_type.value

        object_: dict[str, Any]
        if isinstance(self.object_, ParsedWorkbookHda):
            object_ = self.object_.to_dict()
        else:
            object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_identifier": element_identifier,
                "element_index": element_index,
                "element_type": element_type,
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_workbook_collection import ParsedWorkbookCollection
        from ..models.parsed_workbook_hda import ParsedWorkbookHda

        d = dict(src_dict)
        element_identifier = d.pop("element_identifier")

        element_index = d.pop("element_index")

        element_type = ParsedWorkbookElementElementType(d.pop("element_type"))

        def _parse_object_(data: object) -> ParsedWorkbookCollection | ParsedWorkbookHda:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_0 = ParsedWorkbookHda.from_dict(data)

                return object_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            object_type_1 = ParsedWorkbookCollection.from_dict(data)

            return object_type_1

        object_ = _parse_object_(d.pop("object"))

        parsed_workbook_element = cls(
            element_identifier=element_identifier,
            element_index=element_index,
            element_type=element_type,
            object_=object_,
        )

        parsed_workbook_element.additional_properties = d
        return parsed_workbook_element

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
