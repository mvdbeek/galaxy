from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_type import CreateType
from ..models.upload_option import UploadOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_contents_folder_create_payload_extended_metadata_type_0 import (
        LibraryContentsFolderCreatePayloadExtendedMetadataType0,
    )


T = TypeVar("T", bound="LibraryContentsFolderCreatePayload")


@_attrs_define
class LibraryContentsFolderCreatePayload:
    """
    Attributes:
        create_type (CreateType):
        folder_id (str): the encoded id of the parent folder of the new item Example: 0123456789ABCDEF.
        description (str | Unset):  Default: ''.
        extended_metadata (LibraryContentsFolderCreatePayloadExtendedMetadataType0 | None | Unset): sub-dictionary
            containing any extended metadata to associate with the item
        from_hda_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDA to copy
            into the library
        from_hdca_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDCA to copy
            into the library
        ldda_message (str | Unset): the new message attribute of the LDDA created Default: ''.
        name (str | Unset):  Default: ''.
        tag_using_filenames (bool | Unset): create tags on datasets using the file's original name Default: False.
        tags (list[str] | Unset): create the given list of tags on datasets
        upload_option (UploadOption | Unset):
    """

    create_type: CreateType
    folder_id: str
    description: str | Unset = ""
    extended_metadata: LibraryContentsFolderCreatePayloadExtendedMetadataType0 | None | Unset = UNSET
    from_hda_id: None | str | Unset = UNSET
    from_hdca_id: None | str | Unset = UNSET
    ldda_message: str | Unset = ""
    name: str | Unset = ""
    tag_using_filenames: bool | Unset = False
    tags: list[str] | Unset = UNSET
    upload_option: UploadOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.library_contents_folder_create_payload_extended_metadata_type_0 import (
            LibraryContentsFolderCreatePayloadExtendedMetadataType0,
        )

        create_type = self.create_type.value

        folder_id = self.folder_id

        description = self.description

        extended_metadata: dict[str, Any] | None | Unset
        if isinstance(self.extended_metadata, Unset):
            extended_metadata = UNSET
        elif isinstance(self.extended_metadata, LibraryContentsFolderCreatePayloadExtendedMetadataType0):
            extended_metadata = self.extended_metadata.to_dict()
        else:
            extended_metadata = self.extended_metadata

        from_hda_id: None | str | Unset
        if isinstance(self.from_hda_id, Unset):
            from_hda_id = UNSET
        else:
            from_hda_id = self.from_hda_id

        from_hdca_id: None | str | Unset
        if isinstance(self.from_hdca_id, Unset):
            from_hdca_id = UNSET
        else:
            from_hdca_id = self.from_hdca_id

        ldda_message = self.ldda_message

        name = self.name

        tag_using_filenames = self.tag_using_filenames

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        upload_option: str | Unset = UNSET
        if not isinstance(self.upload_option, Unset):
            upload_option = self.upload_option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_type": create_type,
                "folder_id": folder_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if extended_metadata is not UNSET:
            field_dict["extended_metadata"] = extended_metadata
        if from_hda_id is not UNSET:
            field_dict["from_hda_id"] = from_hda_id
        if from_hdca_id is not UNSET:
            field_dict["from_hdca_id"] = from_hdca_id
        if ldda_message is not UNSET:
            field_dict["ldda_message"] = ldda_message
        if name is not UNSET:
            field_dict["name"] = name
        if tag_using_filenames is not UNSET:
            field_dict["tag_using_filenames"] = tag_using_filenames
        if tags is not UNSET:
            field_dict["tags"] = tags
        if upload_option is not UNSET:
            field_dict["upload_option"] = upload_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_contents_folder_create_payload_extended_metadata_type_0 import (
            LibraryContentsFolderCreatePayloadExtendedMetadataType0,
        )

        d = dict(src_dict)
        create_type = CreateType(d.pop("create_type"))

        folder_id = d.pop("folder_id")

        description = d.pop("description", UNSET)

        def _parse_extended_metadata(
            data: object,
        ) -> LibraryContentsFolderCreatePayloadExtendedMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extended_metadata_type_0 = LibraryContentsFolderCreatePayloadExtendedMetadataType0.from_dict(data)

                return extended_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LibraryContentsFolderCreatePayloadExtendedMetadataType0 | None | Unset, data)

        extended_metadata = _parse_extended_metadata(d.pop("extended_metadata", UNSET))

        def _parse_from_hda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hda_id = _parse_from_hda_id(d.pop("from_hda_id", UNSET))

        def _parse_from_hdca_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_hdca_id = _parse_from_hdca_id(d.pop("from_hdca_id", UNSET))

        ldda_message = d.pop("ldda_message", UNSET)

        name = d.pop("name", UNSET)

        tag_using_filenames = d.pop("tag_using_filenames", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _upload_option = d.pop("upload_option", UNSET)
        upload_option: UploadOption | Unset
        if isinstance(_upload_option, Unset):
            upload_option = UNSET
        else:
            upload_option = UploadOption(_upload_option)

        library_contents_folder_create_payload = cls(
            create_type=create_type,
            folder_id=folder_id,
            description=description,
            extended_metadata=extended_metadata,
            from_hda_id=from_hda_id,
            from_hdca_id=from_hdca_id,
            ldda_message=ldda_message,
            name=name,
            tag_using_filenames=tag_using_filenames,
            tags=tags,
            upload_option=upload_option,
        )

        library_contents_folder_create_payload.additional_properties = d
        return library_contents_folder_create_payload

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
