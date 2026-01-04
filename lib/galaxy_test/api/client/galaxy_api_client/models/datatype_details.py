from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.composite_file_info import CompositeFileInfo


T = TypeVar("T", bound="DatatypeDetails")


@_attrs_define
class DatatypeDetails:
    """
    Attributes:
        description (None | str): A summary description for this data type
        description_url (None | str): The URL to a detailed description for this datatype
        extension (str): The data type’s Dataset file extension
        composite_files (list[CompositeFileInfo] | None | Unset): A collection of files composing this data type
        display_behavior (None | str | Unset): How this datatype behaves when displayed with preview=True: 'inline' (can
            be displayed in browser) or 'download' (triggers download)
        display_in_upload (bool | Unset): If True, the associated file extension will be displayed in the `File Format`
            select list in the `Upload File from your computer` tool in the `Get Data` tool section of the tool panel
            Default: False.
        upload_warning (None | str | Unset): End-user information regarding potential pitfalls with this upload type.
    """

    description: None | str
    description_url: None | str
    extension: str
    composite_files: list[CompositeFileInfo] | None | Unset = UNSET
    display_behavior: None | str | Unset = UNSET
    display_in_upload: bool | Unset = False
    upload_warning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str
        description = self.description

        description_url: None | str
        description_url = self.description_url

        extension = self.extension

        composite_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.composite_files, Unset):
            composite_files = UNSET
        elif isinstance(self.composite_files, list):
            composite_files = []
            for composite_files_type_0_item_data in self.composite_files:
                composite_files_type_0_item = composite_files_type_0_item_data.to_dict()
                composite_files.append(composite_files_type_0_item)

        else:
            composite_files = self.composite_files

        display_behavior: None | str | Unset
        if isinstance(self.display_behavior, Unset):
            display_behavior = UNSET
        else:
            display_behavior = self.display_behavior

        display_in_upload = self.display_in_upload

        upload_warning: None | str | Unset
        if isinstance(self.upload_warning, Unset):
            upload_warning = UNSET
        else:
            upload_warning = self.upload_warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "description_url": description_url,
                "extension": extension,
            }
        )
        if composite_files is not UNSET:
            field_dict["composite_files"] = composite_files
        if display_behavior is not UNSET:
            field_dict["display_behavior"] = display_behavior
        if display_in_upload is not UNSET:
            field_dict["display_in_upload"] = display_in_upload
        if upload_warning is not UNSET:
            field_dict["upload_warning"] = upload_warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.composite_file_info import CompositeFileInfo

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_description_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description_url = _parse_description_url(d.pop("description_url"))

        extension = d.pop("extension")

        def _parse_composite_files(data: object) -> list[CompositeFileInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                composite_files_type_0 = []
                _composite_files_type_0 = data
                for composite_files_type_0_item_data in _composite_files_type_0:
                    composite_files_type_0_item = CompositeFileInfo.from_dict(composite_files_type_0_item_data)

                    composite_files_type_0.append(composite_files_type_0_item)

                return composite_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompositeFileInfo] | None | Unset, data)

        composite_files = _parse_composite_files(d.pop("composite_files", UNSET))

        def _parse_display_behavior(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_behavior = _parse_display_behavior(d.pop("display_behavior", UNSET))

        display_in_upload = d.pop("display_in_upload", UNSET)

        def _parse_upload_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_warning = _parse_upload_warning(d.pop("upload_warning", UNSET))

        datatype_details = cls(
            description=description,
            description_url=description_url,
            extension=extension,
            composite_files=composite_files,
            display_behavior=display_behavior,
            display_in_upload=display_in_upload,
            upload_warning=upload_warning,
        )

        datatype_details.additional_properties = d
        return datatype_details

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
