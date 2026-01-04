from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elements_from_type import ElementsFromType
from ..models.items_from_src import ItemsFromSrc
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hdca_destination import HdcaDestination
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition


T = TypeVar("T", bound="HdcaDataItemsFromTarget")


@_attrs_define
class HdcaDataItemsFromTarget:
    """
    Attributes:
        destination (HdcaDestination):
        items_from (ElementsFromType):
        src (ItemsFromSrc):
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
        collection_type (None | str | Unset):
        column_definitions (list[SampleSheetColumnDefinition] | None | Unset):
        ftp_path (None | str | Unset):
        name (None | str | Unset):
        path (None | str | Unset):
        server_dir (None | str | Unset):
        tags (list[str] | None | Unset):
        url (None | str | Unset):
    """

    destination: HdcaDestination
    items_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | Unset = False
    collection_type: None | str | Unset = UNSET
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    ftp_path: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    server_dir: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination.to_dict()

        items_from = self.items_from.value

        src = self.src.value

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

        ftp_path: None | str | Unset
        if isinstance(self.ftp_path, Unset):
            ftp_path = UNSET
        else:
            ftp_path = self.ftp_path

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        server_dir: None | str | Unset
        if isinstance(self.server_dir, Unset):
            server_dir = UNSET
        else:
            server_dir = self.server_dir

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "items_from": items_from,
                "src": src,
            }
        )
        if auto_decompress is not UNSET:
            field_dict["auto_decompress"] = auto_decompress
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if ftp_path is not UNSET:
            field_dict["ftp_path"] = ftp_path
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if server_dir is not UNSET:
            field_dict["server_dir"] = server_dir
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hdca_destination import HdcaDestination
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition

        d = dict(src_dict)
        destination = HdcaDestination.from_dict(d.pop("destination"))

        items_from = ElementsFromType(d.pop("items_from"))

        src = ItemsFromSrc(d.pop("src"))

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

        def _parse_ftp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ftp_path = _parse_ftp_path(d.pop("ftp_path", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_server_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_dir = _parse_server_dir(d.pop("server_dir", UNSET))

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

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        hdca_data_items_from_target = cls(
            destination=destination,
            items_from=items_from,
            src=src,
            auto_decompress=auto_decompress,
            collection_type=collection_type,
            column_definitions=column_definitions,
            ftp_path=ftp_path,
            name=name,
            path=path,
            server_dir=server_dir,
            tags=tags,
            url=url,
        )

        hdca_data_items_from_target.additional_properties = d
        return hdca_data_items_from_target

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
