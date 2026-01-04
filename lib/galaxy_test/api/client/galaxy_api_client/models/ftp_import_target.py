from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elements_from_type import ElementsFromType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hdca_destination import HdcaDestination
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition


T = TypeVar("T", bound="FtpImportTarget")


@_attrs_define
class FtpImportTarget:
    """
    Attributes:
        destination (HdcaDestination):
        ftp_path (str):
        src (Literal['ftp_import']):
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
        collection_type (None | str | Unset):
        column_definitions (list[SampleSheetColumnDefinition] | None | Unset):
        items_from (ElementsFromType | None | Unset):
        name (None | str | Unset):
        tags (list[str] | None | Unset):
    """

    destination: HdcaDestination
    ftp_path: str
    src: Literal["ftp_import"]
    auto_decompress: bool | Unset = False
    collection_type: None | str | Unset = UNSET
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    items_from: ElementsFromType | None | Unset = UNSET
    name: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination.to_dict()

        ftp_path = self.ftp_path

        src = self.src

        auto_decompress = self.auto_decompress

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

        items_from: None | str | Unset
        if isinstance(self.items_from, Unset):
            items_from = UNSET
        elif isinstance(self.items_from, ElementsFromType):
            items_from = self.items_from.value
        else:
            items_from = self.items_from

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "ftp_path": ftp_path,
                "src": src,
            }
        )
        if auto_decompress is not UNSET:
            field_dict["auto_decompress"] = auto_decompress
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if items_from is not UNSET:
            field_dict["items_from"] = items_from
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hdca_destination import HdcaDestination
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition

        d = dict(src_dict)
        destination = HdcaDestination.from_dict(d.pop("destination"))

        ftp_path = d.pop("ftp_path")

        src = cast(Literal["ftp_import"], d.pop("src"))
        if src != "ftp_import":
            raise ValueError(f"src must match const 'ftp_import', got '{src}'")

        auto_decompress = d.pop("auto_decompress", UNSET)

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

        def _parse_items_from(data: object) -> ElementsFromType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                items_from_type_0 = ElementsFromType(data)

                return items_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ElementsFromType | None | Unset, data)

        items_from = _parse_items_from(d.pop("items_from", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        ftp_import_target = cls(
            destination=destination,
            ftp_path=ftp_path,
            src=src,
            auto_decompress=auto_decompress,
            collection_type=collection_type,
            column_definitions=column_definitions,
            items_from=items_from,
            name=name,
            tags=tags,
        )

        ftp_import_target.additional_properties = d
        return ftp_import_target

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
