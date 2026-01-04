from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elements_from_type import ElementsFromType
from ..models.items_from_src import ItemsFromSrc
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hda_destination import HdaDestination
    from ..models.library_destination import LibraryDestination
    from ..models.library_folder_destination import LibraryFolderDestination


T = TypeVar("T", bound="DataElementsFromTarget")


@_attrs_define
class DataElementsFromTarget:
    """
    Attributes:
        destination (HdaDestination | LibraryDestination | LibraryFolderDestination):
        elements_from (ElementsFromType):
        src (ItemsFromSrc):
        auto_decompress (bool | Unset): This is a boolean value that indicates whether the dataset should be
            automatically decompressed if it is
            compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not
            explicitly set to a compressed datatype.
             Default: False.
        ftp_path (None | str | Unset):
        path (None | str | Unset):
        server_dir (None | str | Unset):
        url (None | str | Unset):
    """

    destination: HdaDestination | LibraryDestination | LibraryFolderDestination
    elements_from: ElementsFromType
    src: ItemsFromSrc
    auto_decompress: bool | Unset = False
    ftp_path: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    server_dir: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hda_destination import HdaDestination
        from ..models.library_folder_destination import LibraryFolderDestination

        destination: dict[str, Any]
        if isinstance(self.destination, HdaDestination):
            destination = self.destination.to_dict()
        elif isinstance(self.destination, LibraryFolderDestination):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        elements_from = self.elements_from.value

        src = self.src.value

        auto_decompress = self.auto_decompress

        ftp_path: None | str | Unset
        if isinstance(self.ftp_path, Unset):
            ftp_path = UNSET
        else:
            ftp_path = self.ftp_path

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
                "elements_from": elements_from,
                "src": src,
            }
        )
        if auto_decompress is not UNSET:
            field_dict["auto_decompress"] = auto_decompress
        if ftp_path is not UNSET:
            field_dict["ftp_path"] = ftp_path
        if path is not UNSET:
            field_dict["path"] = path
        if server_dir is not UNSET:
            field_dict["server_dir"] = server_dir
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hda_destination import HdaDestination
        from ..models.library_destination import LibraryDestination
        from ..models.library_folder_destination import LibraryFolderDestination

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

        elements_from = ElementsFromType(d.pop("elements_from"))

        src = ItemsFromSrc(d.pop("src"))

        auto_decompress = d.pop("auto_decompress", UNSET)

        def _parse_ftp_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ftp_path = _parse_ftp_path(d.pop("ftp_path", UNSET))

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

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        data_elements_from_target = cls(
            destination=destination,
            elements_from=elements_from,
            src=src,
            auto_decompress=auto_decompress,
            ftp_path=ftp_path,
            path=path,
            server_dir=server_dir,
            url=url,
        )

        data_elements_from_target.additional_properties = d
        return data_elements_from_target

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
