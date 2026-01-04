from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composite_data_element import CompositeDataElement
    from ..models.file_data_element import FileDataElement
    from ..models.ftp_import_element import FtpImportElement
    from ..models.hdca_destination import HdcaDestination
    from ..models.nested_element import NestedElement
    from ..models.pasted_data_element import PastedDataElement
    from ..models.path_data_element import PathDataElement
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition
    from ..models.server_dir_element import ServerDirElement
    from ..models.url_data_element import UrlDataElement


T = TypeVar("T", bound="HdcaDataItemsTarget")


@_attrs_define
class HdcaDataItemsTarget:
    """
    Attributes:
        destination (HdcaDestination):
        elements (list[CompositeDataElement | FileDataElement | FtpImportElement | NestedElement | PastedDataElement |
            PathDataElement | ServerDirElement | UrlDataElement]):
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
        collection_type (None | str | Unset):
        column_definitions (list[SampleSheetColumnDefinition] | None | Unset):
        name (None | str | Unset):
        tags (list[str] | None | Unset):
    """

    destination: HdcaDestination
    elements: list[
        CompositeDataElement
        | FileDataElement
        | FtpImportElement
        | NestedElement
        | PastedDataElement
        | PathDataElement
        | ServerDirElement
        | UrlDataElement
    ]
    auto_decompress: bool | Unset = False
    collection_type: None | str | Unset = UNSET
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        destination = self.destination.to_dict()

        elements = []
        for elements_item_data in self.elements:
            elements_item: dict[str, Any]
            if isinstance(elements_item_data, FileDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PastedDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, UrlDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, PathDataElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, ServerDirElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, FtpImportElement):
                elements_item = elements_item_data.to_dict()
            elif isinstance(elements_item_data, CompositeDataElement):
                elements_item = elements_item_data.to_dict()
            else:
                elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

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
                "elements": elements,
            }
        )
        if auto_decompress is not UNSET:
            field_dict["auto_decompress"] = auto_decompress
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.hdca_destination import HdcaDestination
        from ..models.nested_element import NestedElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        d = dict(src_dict)
        destination = HdcaDestination.from_dict(d.pop("destination"))

        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:

            def _parse_elements_item(
                data: object,
            ) -> (
                CompositeDataElement
                | FileDataElement
                | FtpImportElement
                | NestedElement
                | PastedDataElement
                | PathDataElement
                | ServerDirElement
                | UrlDataElement
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_0 = FileDataElement.from_dict(data)

                    return elements_item_type_0_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_1 = PastedDataElement.from_dict(data)

                    return elements_item_type_0_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_2 = UrlDataElement.from_dict(data)

                    return elements_item_type_0_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_3 = PathDataElement.from_dict(data)

                    return elements_item_type_0_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_4 = ServerDirElement.from_dict(data)

                    return elements_item_type_0_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_5 = FtpImportElement.from_dict(data)

                    return elements_item_type_0_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0_type_6 = CompositeDataElement.from_dict(data)

                    return elements_item_type_0_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                elements_item_type_1 = NestedElement.from_dict(data)

                return elements_item_type_1

            elements_item = _parse_elements_item(elements_item_data)

            elements.append(elements_item)

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

        hdca_data_items_target = cls(
            destination=destination,
            elements=elements,
            auto_decompress=auto_decompress,
            collection_type=collection_type,
            column_definitions=column_definitions,
            name=name,
            tags=tags,
        )

        hdca_data_items_target.additional_properties = d
        return hdca_data_items_target

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
