from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composite_data_element import CompositeDataElement
    from ..models.file_data_element import FileDataElement
    from ..models.ftp_import_element import FtpImportElement
    from ..models.hda_destination import HdaDestination
    from ..models.library_destination import LibraryDestination
    from ..models.library_folder_destination import LibraryFolderDestination
    from ..models.nested_element import NestedElement
    from ..models.pasted_data_element import PastedDataElement
    from ..models.path_data_element import PathDataElement
    from ..models.server_dir_element import ServerDirElement
    from ..models.url_data_element import UrlDataElement


T = TypeVar("T", bound="DataElementsTarget")


@_attrs_define
class DataElementsTarget:
    """
    Attributes:
        destination (HdaDestination | LibraryDestination | LibraryFolderDestination):
        elements (list[CompositeDataElement | FileDataElement | FtpImportElement | NestedElement | PastedDataElement |
            PathDataElement | ServerDirElement | UrlDataElement]):
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
    """

    destination: HdaDestination | LibraryDestination | LibraryFolderDestination
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.hda_destination import HdaDestination
        from ..models.library_folder_destination import LibraryFolderDestination
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        destination: dict[str, Any]
        if isinstance(self.destination, HdaDestination):
            destination = self.destination.to_dict()
        elif isinstance(self.destination, LibraryFolderDestination):
            destination = self.destination.to_dict()
        else:
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composite_data_element import CompositeDataElement
        from ..models.file_data_element import FileDataElement
        from ..models.ftp_import_element import FtpImportElement
        from ..models.hda_destination import HdaDestination
        from ..models.library_destination import LibraryDestination
        from ..models.library_folder_destination import LibraryFolderDestination
        from ..models.nested_element import NestedElement
        from ..models.pasted_data_element import PastedDataElement
        from ..models.path_data_element import PathDataElement
        from ..models.server_dir_element import ServerDirElement
        from ..models.url_data_element import UrlDataElement

        d = dict(src_dict)

        def _parse_destination(data: object) -> HdaDestination | LibraryDestination | LibraryFolderDestination:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = HdaDestination.from_dict(data)

                return destination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_1 = LibraryFolderDestination.from_dict(data)

                return destination_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_2 = LibraryDestination.from_dict(data)

            return destination_type_2

        destination = _parse_destination(d.pop("destination"))

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

        data_elements_target = cls(
            destination=destination,
            elements=elements,
            auto_decompress=auto_decompress,
        )

        data_elements_target.additional_properties = d
        return data_elements_target

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
