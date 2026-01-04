from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_type_message import ContentTypeMessage
    from ..models.csv_dialect_inference_message import CsvDialectInferenceMessage
    from ..models.inferred_column_mapping import InferredColumnMapping
    from ..models.parsed_column import ParsedColumn
    from ..models.parsed_workbook_element import ParsedWorkbookElement
    from ..models.parsed_workbook_for_collection_rows_item import ParsedWorkbookForCollectionRowsItem


T = TypeVar("T", bound="ParsedWorkbookForCollection")


@_attrs_define
class ParsedWorkbookForCollection:
    """
    Attributes:
        elements (list[ParsedWorkbookElement]):
        extra_columns (list[ParsedColumn]):
        parse_log (list[ContentTypeMessage | CsvDialectInferenceMessage | InferredColumnMapping]):
        rows (list[ParsedWorkbookForCollectionRowsItem]):
    """

    elements: list[ParsedWorkbookElement]
    extra_columns: list[ParsedColumn]
    parse_log: list[ContentTypeMessage | CsvDialectInferenceMessage | InferredColumnMapping]
    rows: list[ParsedWorkbookForCollectionRowsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_type_message import ContentTypeMessage
        from ..models.inferred_column_mapping import InferredColumnMapping

        elements = []
        for elements_item_data in self.elements:
            elements_item = elements_item_data.to_dict()
            elements.append(elements_item)

        extra_columns = []
        for extra_columns_item_data in self.extra_columns:
            extra_columns_item = extra_columns_item_data.to_dict()
            extra_columns.append(extra_columns_item)

        parse_log = []
        for parse_log_item_data in self.parse_log:
            parse_log_item: dict[str, Any]
            if isinstance(parse_log_item_data, InferredColumnMapping):
                parse_log_item = parse_log_item_data.to_dict()
            elif isinstance(parse_log_item_data, ContentTypeMessage):
                parse_log_item = parse_log_item_data.to_dict()
            else:
                parse_log_item = parse_log_item_data.to_dict()

            parse_log.append(parse_log_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
                "extra_columns": extra_columns,
                "parse_log": parse_log,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_type_message import ContentTypeMessage
        from ..models.csv_dialect_inference_message import CsvDialectInferenceMessage
        from ..models.inferred_column_mapping import InferredColumnMapping
        from ..models.parsed_column import ParsedColumn
        from ..models.parsed_workbook_element import ParsedWorkbookElement
        from ..models.parsed_workbook_for_collection_rows_item import ParsedWorkbookForCollectionRowsItem

        d = dict(src_dict)
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:
            elements_item = ParsedWorkbookElement.from_dict(elements_item_data)

            elements.append(elements_item)

        extra_columns = []
        _extra_columns = d.pop("extra_columns")
        for extra_columns_item_data in _extra_columns:
            extra_columns_item = ParsedColumn.from_dict(extra_columns_item_data)

            extra_columns.append(extra_columns_item)

        parse_log = []
        _parse_log = d.pop("parse_log")
        for parse_log_item_data in _parse_log:

            def _parse_parse_log_item(
                data: object,
            ) -> ContentTypeMessage | CsvDialectInferenceMessage | InferredColumnMapping:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_0 = InferredColumnMapping.from_dict(data)

                    return parse_log_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_1 = ContentTypeMessage.from_dict(data)

                    return parse_log_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                parse_log_item_type_2 = CsvDialectInferenceMessage.from_dict(data)

                return parse_log_item_type_2

            parse_log_item = _parse_parse_log_item(parse_log_item_data)

            parse_log.append(parse_log_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ParsedWorkbookForCollectionRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        parsed_workbook_for_collection = cls(
            elements=elements,
            extra_columns=extra_columns,
            parse_log=parse_log,
            rows=rows,
        )

        parsed_workbook_for_collection.additional_properties = d
        return parsed_workbook_for_collection

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
