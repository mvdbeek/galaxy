from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_new_collection_payload_instance_type_type_0 import CreateNewCollectionPayloadInstanceTypeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_element_identifier import CollectionElementIdentifier
    from ..models.create_new_collection_payload_rows_type_0 import CreateNewCollectionPayloadRowsType0
    from ..models.field_dict import FieldDict
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition


T = TypeVar("T", bound="CreateNewCollectionPayload")


@_attrs_define
class CreateNewCollectionPayload:
    """
    Attributes:
        collection_type (None | str | Unset): The type of the collection, can be `list`, `paired`, or define
            subcollections using `:` as separator like `list:paired` or `list:list`.
        column_definitions (list[SampleSheetColumnDefinition] | None | Unset): Specify definitions for row data if
            collection_type is sample_sheet
        copy_elements (bool | None | Unset): Whether to create a copy of the source HDAs for the new collection.
            Default: True.
        element_identifiers (list[CollectionElementIdentifier] | None | Unset): List of elements that should be in the
            new collection.
        fields (list[FieldDict] | None | str | Unset): List of fields to create for this collection. Set to 'auto' to
            guess fields from identifiers. Default: '[]'.
        folder_id (None | str | Unset): The ID of the library folder that will contain the collection. Required if
            `instance_type=library`.
        hide_source_items (bool | None | Unset): Whether to mark the original HDAs as hidden. Default: False.
        history_id (None | str | Unset): The ID of the history that will contain the collection. Required if
            `instance_type=history`.
        instance_type (CreateNewCollectionPayloadInstanceTypeType0 | None | Unset): The type of the instance, either
            `history` (default) or `library`. Default: CreateNewCollectionPayloadInstanceTypeType0.HISTORY.
        name (None | str | Unset): The name of the new collection.
        rows (CreateNewCollectionPayloadRowsType0 | None | Unset): Specify rows of metadata data corresponding to an
            identifier if collection_type is sample_sheet
    """

    collection_type: None | str | Unset = UNSET
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    copy_elements: bool | None | Unset = True
    element_identifiers: list[CollectionElementIdentifier] | None | Unset = UNSET
    fields: list[FieldDict] | None | str | Unset = "[]"
    folder_id: None | str | Unset = UNSET
    hide_source_items: bool | None | Unset = False
    history_id: None | str | Unset = UNSET
    instance_type: CreateNewCollectionPayloadInstanceTypeType0 | None | Unset = (
        CreateNewCollectionPayloadInstanceTypeType0.HISTORY
    )
    name: None | str | Unset = UNSET
    rows: CreateNewCollectionPayloadRowsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_new_collection_payload_rows_type_0 import CreateNewCollectionPayloadRowsType0

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        column_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.column_definitions, Unset):
            column_definitions = UNSET
        elif isinstance(self.column_definitions, list):
            column_definitions = []
            for column_definitions_type_0_item_data in self.column_definitions:
                column_definitions_type_0_item = column_definitions_type_0_item_data.to_dict()
                column_definitions.append(column_definitions_type_0_item)

        else:
            column_definitions = self.column_definitions

        copy_elements: bool | None | Unset
        if isinstance(self.copy_elements, Unset):
            copy_elements = UNSET
        else:
            copy_elements = self.copy_elements

        element_identifiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.element_identifiers, Unset):
            element_identifiers = UNSET
        elif isinstance(self.element_identifiers, list):
            element_identifiers = []
            for element_identifiers_type_0_item_data in self.element_identifiers:
                element_identifiers_type_0_item = element_identifiers_type_0_item_data.to_dict()
                element_identifiers.append(element_identifiers_type_0_item)

        else:
            element_identifiers = self.element_identifiers

        fields: list[dict[str, Any]] | None | str | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_1_item_data in self.fields:
                fields_type_1_item = fields_type_1_item_data.to_dict()
                fields.append(fields_type_1_item)

        else:
            fields = self.fields

        folder_id: None | str | Unset
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        hide_source_items: bool | None | Unset
        if isinstance(self.hide_source_items, Unset):
            hide_source_items = UNSET
        else:
            hide_source_items = self.hide_source_items

        history_id: None | str | Unset
        if isinstance(self.history_id, Unset):
            history_id = UNSET
        else:
            history_id = self.history_id

        instance_type: None | str | Unset
        if isinstance(self.instance_type, Unset):
            instance_type = UNSET
        elif isinstance(self.instance_type, CreateNewCollectionPayloadInstanceTypeType0):
            instance_type = self.instance_type.value
        else:
            instance_type = self.instance_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        rows: dict[str, Any] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, CreateNewCollectionPayloadRowsType0):
            rows = self.rows.to_dict()
        else:
            rows = self.rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if copy_elements is not UNSET:
            field_dict["copy_elements"] = copy_elements
        if element_identifiers is not UNSET:
            field_dict["element_identifiers"] = element_identifiers
        if fields is not UNSET:
            field_dict["fields"] = fields
        if folder_id is not UNSET:
            field_dict["folder_id"] = folder_id
        if hide_source_items is not UNSET:
            field_dict["hide_source_items"] = hide_source_items
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if name is not UNSET:
            field_dict["name"] = name
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_element_identifier import CollectionElementIdentifier
        from ..models.create_new_collection_payload_rows_type_0 import CreateNewCollectionPayloadRowsType0
        from ..models.field_dict import FieldDict
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition

        d = dict(src_dict)

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_column_definitions(data: object) -> list[SampleSheetColumnDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                column_definitions_type_0 = []
                _column_definitions_type_0 = data
                for column_definitions_type_0_item_data in _column_definitions_type_0:
                    column_definitions_type_0_item = SampleSheetColumnDefinition.from_dict(
                        column_definitions_type_0_item_data
                    )

                    column_definitions_type_0.append(column_definitions_type_0_item)

                return column_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SampleSheetColumnDefinition] | None | Unset, data)

        column_definitions = _parse_column_definitions(d.pop("column_definitions", UNSET))

        def _parse_copy_elements(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_elements = _parse_copy_elements(d.pop("copy_elements", UNSET))

        def _parse_element_identifiers(data: object) -> list[CollectionElementIdentifier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                element_identifiers_type_0 = []
                _element_identifiers_type_0 = data
                for element_identifiers_type_0_item_data in _element_identifiers_type_0:
                    element_identifiers_type_0_item = CollectionElementIdentifier.from_dict(
                        element_identifiers_type_0_item_data
                    )

                    element_identifiers_type_0.append(element_identifiers_type_0_item)

                return element_identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CollectionElementIdentifier] | None | Unset, data)

        element_identifiers = _parse_element_identifiers(d.pop("element_identifiers", UNSET))

        def _parse_fields(data: object) -> list[FieldDict] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_1 = []
                _fields_type_1 = data
                for fields_type_1_item_data in _fields_type_1:
                    fields_type_1_item = FieldDict.from_dict(fields_type_1_item_data)

                    fields_type_1.append(fields_type_1_item)

                return fields_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FieldDict] | None | str | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_folder_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_id = _parse_folder_id(d.pop("folder_id", UNSET))

        def _parse_hide_source_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_source_items = _parse_hide_source_items(d.pop("hide_source_items", UNSET))

        def _parse_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        history_id = _parse_history_id(d.pop("history_id", UNSET))

        def _parse_instance_type(data: object) -> CreateNewCollectionPayloadInstanceTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                instance_type_type_0 = CreateNewCollectionPayloadInstanceTypeType0(data)

                return instance_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateNewCollectionPayloadInstanceTypeType0 | None | Unset, data)

        instance_type = _parse_instance_type(d.pop("instance_type", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_rows(data: object) -> CreateNewCollectionPayloadRowsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rows_type_0 = CreateNewCollectionPayloadRowsType0.from_dict(data)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateNewCollectionPayloadRowsType0 | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))

        create_new_collection_payload = cls(
            collection_type=collection_type,
            column_definitions=column_definitions,
            copy_elements=copy_elements,
            element_identifiers=element_identifiers,
            fields=fields,
            folder_id=folder_id,
            hide_source_items=hide_source_items,
            history_id=history_id,
            instance_type=instance_type,
            name=name,
            rows=rows,
        )

        create_new_collection_payload.additional_properties = d
        return create_new_collection_payload

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
