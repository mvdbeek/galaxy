from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel


T = TypeVar("T", bound="ParseWorkbookForCollectionApi")


@_attrs_define
class ParseWorkbookForCollectionApi:
    """
    Attributes:
        column_definitions (list[SampleSheetColumnDefinitionModel]): A description of the columns expected in the
            workbook after the first columns described by 'prefix_columns_type'
        content (str): The workbook content (the contents of the xlsx file) that have been base64 encoded.
    """

    column_definitions: list[SampleSheetColumnDefinitionModel]
    content: str

    def to_dict(self) -> dict[str, Any]:
        column_definitions = []
        for column_definitions_item_data in self.column_definitions:
            column_definitions_item = column_definitions_item_data.to_dict()
            column_definitions.append(column_definitions_item)

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "column_definitions": column_definitions,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

        d = dict(src_dict)
        column_definitions = []
        _column_definitions = d.pop("column_definitions")
        for column_definitions_item_data in _column_definitions:
            column_definitions_item = SampleSheetColumnDefinitionModel.from_dict(column_definitions_item_data)

            column_definitions.append(column_definitions_item)

        content = d.pop("content")

        parse_workbook_for_collection_api = cls(
            column_definitions=column_definitions,
            content=content,
        )

        return parse_workbook_for_collection_api
