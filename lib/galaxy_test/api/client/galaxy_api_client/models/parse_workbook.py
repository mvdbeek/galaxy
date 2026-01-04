from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_workbook_collection_type import ParseWorkbookCollectionType
from ..models.parse_workbook_prefix_columns_type import ParseWorkbookPrefixColumnsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel


T = TypeVar("T", bound="ParseWorkbook")


@_attrs_define
class ParseWorkbook:
    """
    Attributes:
        collection_type (ParseWorkbookCollectionType):
        column_definitions (list[SampleSheetColumnDefinitionModel]): A description of the columns expected in the
            workbook after the first columns described by 'prefix_columns_type'
        content (str): The workbook content (the contents of the xlsx file) that have been base64 encoded.
        prefix_columns_type (ParseWorkbookPrefixColumnsType | Unset):  Default: ParseWorkbookPrefixColumnsType.URI.
    """

    collection_type: ParseWorkbookCollectionType
    column_definitions: list[SampleSheetColumnDefinitionModel]
    content: str
    prefix_columns_type: ParseWorkbookPrefixColumnsType | Unset = ParseWorkbookPrefixColumnsType.URI
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_type = self.collection_type.value

        column_definitions = []
        for column_definitions_item_data in self.column_definitions:
            column_definitions_item = column_definitions_item_data.to_dict()
            column_definitions.append(column_definitions_item)

        content = self.content

        prefix_columns_type: str | Unset = UNSET
        if not isinstance(self.prefix_columns_type, Unset):
            prefix_columns_type = self.prefix_columns_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_type": collection_type,
                "column_definitions": column_definitions,
                "content": content,
            }
        )
        if prefix_columns_type is not UNSET:
            field_dict["prefix_columns_type"] = prefix_columns_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

        d = dict(src_dict)
        collection_type = ParseWorkbookCollectionType(d.pop("collection_type"))

        column_definitions = []
        _column_definitions = d.pop("column_definitions")
        for column_definitions_item_data in _column_definitions:
            column_definitions_item = SampleSheetColumnDefinitionModel.from_dict(column_definitions_item_data)

            column_definitions.append(column_definitions_item)

        content = d.pop("content")

        _prefix_columns_type = d.pop("prefix_columns_type", UNSET)
        prefix_columns_type: ParseWorkbookPrefixColumnsType | Unset
        if isinstance(_prefix_columns_type, Unset):
            prefix_columns_type = UNSET
        else:
            prefix_columns_type = ParseWorkbookPrefixColumnsType(_prefix_columns_type)

        parse_workbook = cls(
            collection_type=collection_type,
            column_definitions=column_definitions,
            content=content,
            prefix_columns_type=prefix_columns_type,
        )

        parse_workbook.additional_properties = d
        return parse_workbook

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
