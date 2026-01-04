from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_workbook_request_collection_type import CreateWorkbookRequestCollectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel


T = TypeVar("T", bound="CreateWorkbookRequest")


@_attrs_define
class CreateWorkbookRequest:
    """
    Attributes:
        collection_type (CreateWorkbookRequestCollectionType):
        column_definitions (list[SampleSheetColumnDefinitionModel]): A description of the columns expected in the
            workbook after the first columns described by 'prefix_columns_type'
        prefix_columns_type (Literal['URI'] | Unset):  Default: 'URI'.
        prefix_values (list[list[bool | float | int | None | str]] | None | Unset):
        title (str | Unset): A short title to give the workbook. Default: 'Sample Sheet for Galaxy'.
    """

    collection_type: CreateWorkbookRequestCollectionType
    column_definitions: list[SampleSheetColumnDefinitionModel]
    prefix_columns_type: Literal["URI"] | Unset = "URI"
    prefix_values: list[list[bool | float | int | None | str]] | None | Unset = UNSET
    title: str | Unset = "Sample Sheet for Galaxy"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_type = self.collection_type.value

        column_definitions = []
        for column_definitions_item_data in self.column_definitions:
            column_definitions_item = column_definitions_item_data.to_dict()
            column_definitions.append(column_definitions_item)

        prefix_columns_type = self.prefix_columns_type

        prefix_values: list[list[bool | float | int | None | str]] | None | Unset
        if isinstance(self.prefix_values, Unset):
            prefix_values = UNSET
        elif isinstance(self.prefix_values, list):
            prefix_values = []
            for prefix_values_type_0_item_data in self.prefix_values:
                prefix_values_type_0_item = []
                for prefix_values_type_0_item_item_data in prefix_values_type_0_item_data:
                    prefix_values_type_0_item_item: bool | float | int | None | str
                    prefix_values_type_0_item_item = prefix_values_type_0_item_item_data
                    prefix_values_type_0_item.append(prefix_values_type_0_item_item)

                prefix_values.append(prefix_values_type_0_item)

        else:
            prefix_values = self.prefix_values

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_type": collection_type,
                "column_definitions": column_definitions,
            }
        )
        if prefix_columns_type is not UNSET:
            field_dict["prefix_columns_type"] = prefix_columns_type
        if prefix_values is not UNSET:
            field_dict["prefix_values"] = prefix_values
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

        d = dict(src_dict)
        collection_type = CreateWorkbookRequestCollectionType(d.pop("collection_type"))

        column_definitions = []
        _column_definitions = d.pop("column_definitions")
        for column_definitions_item_data in _column_definitions:
            column_definitions_item = SampleSheetColumnDefinitionModel.from_dict(column_definitions_item_data)

            column_definitions.append(column_definitions_item)

        prefix_columns_type = cast(Literal["URI"] | Unset, d.pop("prefix_columns_type", UNSET))
        if prefix_columns_type != "URI" and not isinstance(prefix_columns_type, Unset):
            raise ValueError(f"prefix_columns_type must match const 'URI', got '{prefix_columns_type}'")

        def _parse_prefix_values(data: object) -> list[list[bool | float | int | None | str]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prefix_values_type_0 = []
                _prefix_values_type_0 = data
                for prefix_values_type_0_item_data in _prefix_values_type_0:
                    prefix_values_type_0_item = []
                    _prefix_values_type_0_item = prefix_values_type_0_item_data
                    for prefix_values_type_0_item_item_data in _prefix_values_type_0_item:

                        def _parse_prefix_values_type_0_item_item(data: object) -> bool | float | int | None | str:
                            if data is None:
                                return data
                            return cast(bool | float | int | None | str, data)

                        prefix_values_type_0_item_item = _parse_prefix_values_type_0_item_item(
                            prefix_values_type_0_item_item_data
                        )

                        prefix_values_type_0_item.append(prefix_values_type_0_item_item)

                    prefix_values_type_0.append(prefix_values_type_0_item)

                return prefix_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[bool | float | int | None | str]] | None | Unset, data)

        prefix_values = _parse_prefix_values(d.pop("prefix_values", UNSET))

        title = d.pop("title", UNSET)

        create_workbook_request = cls(
            collection_type=collection_type,
            column_definitions=column_definitions,
            prefix_columns_type=prefix_columns_type,
            prefix_values=prefix_values,
            title=title,
        )

        create_workbook_request.additional_properties = d
        return create_workbook_request

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
