from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parsed_fetch_workbook_for_datasets_workbook_type import ParsedFetchWorkbookForDatasetsWorkbookType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_type_message import ContentTypeMessage
    from ..models.csv_dialect_inference_message import CsvDialectInferenceMessage
    from ..models.inferred_collection_type_log_entry import InferredCollectionTypeLogEntry
    from ..models.inferred_column_mapping import InferredColumnMapping
    from ..models.parsed_column import ParsedColumn
    from ..models.parsed_fetch_workbook_for_datasets_rows_item import ParsedFetchWorkbookForDatasetsRowsItem
    from ..models.split_up_paired_data_log_entry import SplitUpPairedDataLogEntry


T = TypeVar("T", bound="ParsedFetchWorkbookForDatasets")


@_attrs_define
class ParsedFetchWorkbookForDatasets:
    """
    Attributes:
        columns (list[ParsedColumn]):
        parse_log (list[ContentTypeMessage | CsvDialectInferenceMessage | InferredCollectionTypeLogEntry |
            InferredColumnMapping | SplitUpPairedDataLogEntry]):
        rows (list[ParsedFetchWorkbookForDatasetsRowsItem]):
        workbook_type (ParsedFetchWorkbookForDatasetsWorkbookType | Unset):  Default:
            ParsedFetchWorkbookForDatasetsWorkbookType.DATASETS.
    """

    columns: list[ParsedColumn]
    parse_log: list[
        ContentTypeMessage
        | CsvDialectInferenceMessage
        | InferredCollectionTypeLogEntry
        | InferredColumnMapping
        | SplitUpPairedDataLogEntry
    ]
    rows: list[ParsedFetchWorkbookForDatasetsRowsItem]
    workbook_type: ParsedFetchWorkbookForDatasetsWorkbookType | Unset = (
        ParsedFetchWorkbookForDatasetsWorkbookType.DATASETS
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_type_message import ContentTypeMessage
        from ..models.inferred_collection_type_log_entry import InferredCollectionTypeLogEntry
        from ..models.inferred_column_mapping import InferredColumnMapping
        from ..models.split_up_paired_data_log_entry import SplitUpPairedDataLogEntry

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        parse_log = []
        for parse_log_item_data in self.parse_log:
            parse_log_item: dict[str, Any]
            if isinstance(parse_log_item_data, SplitUpPairedDataLogEntry):
                parse_log_item = parse_log_item_data.to_dict()
            elif isinstance(parse_log_item_data, InferredCollectionTypeLogEntry):
                parse_log_item = parse_log_item_data.to_dict()
            elif isinstance(parse_log_item_data, InferredColumnMapping):
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

        workbook_type: str | Unset = UNSET
        if not isinstance(self.workbook_type, Unset):
            workbook_type = self.workbook_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "parse_log": parse_log,
                "rows": rows,
            }
        )
        if workbook_type is not UNSET:
            field_dict["workbook_type"] = workbook_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_type_message import ContentTypeMessage
        from ..models.csv_dialect_inference_message import CsvDialectInferenceMessage
        from ..models.inferred_collection_type_log_entry import InferredCollectionTypeLogEntry
        from ..models.inferred_column_mapping import InferredColumnMapping
        from ..models.parsed_column import ParsedColumn
        from ..models.parsed_fetch_workbook_for_datasets_rows_item import ParsedFetchWorkbookForDatasetsRowsItem
        from ..models.split_up_paired_data_log_entry import SplitUpPairedDataLogEntry

        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ParsedColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        parse_log = []
        _parse_log = d.pop("parse_log")
        for parse_log_item_data in _parse_log:

            def _parse_parse_log_item(
                data: object,
            ) -> (
                ContentTypeMessage
                | CsvDialectInferenceMessage
                | InferredCollectionTypeLogEntry
                | InferredColumnMapping
                | SplitUpPairedDataLogEntry
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_0 = SplitUpPairedDataLogEntry.from_dict(data)

                    return parse_log_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_1 = InferredCollectionTypeLogEntry.from_dict(data)

                    return parse_log_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_2 = InferredColumnMapping.from_dict(data)

                    return parse_log_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parse_log_item_type_3 = ContentTypeMessage.from_dict(data)

                    return parse_log_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                parse_log_item_type_4 = CsvDialectInferenceMessage.from_dict(data)

                return parse_log_item_type_4

            parse_log_item = _parse_parse_log_item(parse_log_item_data)

            parse_log.append(parse_log_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = ParsedFetchWorkbookForDatasetsRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        _workbook_type = d.pop("workbook_type", UNSET)
        workbook_type: ParsedFetchWorkbookForDatasetsWorkbookType | Unset
        if isinstance(_workbook_type, Unset):
            workbook_type = UNSET
        else:
            workbook_type = ParsedFetchWorkbookForDatasetsWorkbookType(_workbook_type)

        parsed_fetch_workbook_for_datasets = cls(
            columns=columns,
            parse_log=parse_log,
            rows=rows,
            workbook_type=workbook_type,
        )

        parsed_fetch_workbook_for_datasets.additional_properties = d
        return parsed_fetch_workbook_for_datasets

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
