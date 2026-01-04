from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_type import CreateType
from ..models.link_data_only import LinkDataOnly
from ..models.upload_option import UploadOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_contents_file_create_payload_extended_metadata_type_0 import (
        LibraryContentsFileCreatePayloadExtendedMetadataType0,
    )
    from ..models.library_contents_file_create_payload_upload_files_type_0_item import (
        LibraryContentsFileCreatePayloadUploadFilesType0Item,
    )


T = TypeVar("T", bound="LibraryContentsFileCreatePayload")


@_attrs_define
class LibraryContentsFileCreatePayload:
    """
    Attributes:
        create_type (CreateType):
        folder_id (str): the encoded id of the parent folder of the new item Example: 0123456789ABCDEF.
        dbkey (list[Any] | str | Unset):  Default: '?'.
        extended_metadata (LibraryContentsFileCreatePayloadExtendedMetadataType0 | None | Unset): sub-dictionary
            containing any extended metadata to associate with the item
        file_type (None | str | Unset):
        filesystem_paths (str | Unset): (only if upload_option is 'upload_paths' and the user is an admin) file paths on
            the Galaxy server to upload to the library, one file per line Default: ''.
        from_hda_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDA to copy
            into the library
        from_hdca_id (None | str | Unset): (only if create_type is 'file') the encoded id of an accessible HDCA to copy
            into the library
        ldda_message (str | Unset): the new message attribute of the LDDA created Default: ''.
        link_data_only (LinkDataOnly | Unset):
        roles (str | Unset):  Default: ''.
        server_dir (str | Unset): (only if upload_option is 'upload_directory') relative path of the subdirectory of
            Galaxy ``library_import_dir`` (if admin) or ``user_library_import_dir`` (if non-admin) to upload. All and only
            the files (i.e. no subdirectories) contained in the specified directory will be uploaded. Default: ''.
        tag_using_filenames (bool | Unset): create tags on datasets using the file's original name Default: False.
        tags (list[str] | Unset): create the given list of tags on datasets
        upload_files (list[LibraryContentsFileCreatePayloadUploadFilesType0Item] | None | Unset):
        upload_option (UploadOption | Unset):
        uuid (None | str | Unset):
    """

    create_type: CreateType
    folder_id: str
    dbkey: list[Any] | str | Unset = "?"
    extended_metadata: LibraryContentsFileCreatePayloadExtendedMetadataType0 | None | Unset = UNSET
    file_type: None | str | Unset = UNSET
    filesystem_paths: str | Unset = ""
    from_hda_id: None | str | Unset = UNSET
    from_hdca_id: None | str | Unset = UNSET
    ldda_message: str | Unset = ""
    link_data_only: LinkDataOnly | Unset = UNSET
    roles: str | Unset = ""
    server_dir: str | Unset = ""
    tag_using_filenames: bool | Unset = False
    tags: list[str] | Unset = UNSET
    upload_files: list[LibraryContentsFileCreatePayloadUploadFilesType0Item] | None | Unset = UNSET
    upload_option: UploadOption | Unset = UNSET
    uuid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.library_contents_file_create_payload_extended_metadata_type_0 import (
            LibraryContentsFileCreatePayloadExtendedMetadataType0,
        )

        create_type = self.create_type.value

        folder_id = self.folder_id

        dbkey: list[Any] | str | Unset
        if isinstance(self.dbkey, Unset):
            dbkey = UNSET
        elif isinstance(self.dbkey, list):
            dbkey = self.dbkey

        else:
            dbkey = self.dbkey

        extended_metadata: dict[str, Any] | None | Unset
        if isinstance(self.extended_metadata, Unset):
            extended_metadata = UNSET
        elif isinstance(self.extended_metadata, LibraryContentsFileCreatePayloadExtendedMetadataType0):
            extended_metadata = self.extended_metadata.to_dict()
        else:
            extended_metadata = self.extended_metadata

        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        else:
            file_type = self.file_type

        filesystem_paths = self.filesystem_paths

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

        link_data_only: str | Unset = UNSET
        if not isinstance(self.link_data_only, Unset):
            link_data_only = self.link_data_only.value

        roles = self.roles

        server_dir = self.server_dir

        tag_using_filenames = self.tag_using_filenames

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        upload_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.upload_files, Unset):
            upload_files = UNSET
        elif isinstance(self.upload_files, list):
            upload_files = []
            for upload_files_type_0_item_data in self.upload_files:
                upload_files_type_0_item = upload_files_type_0_item_data.to_dict()
                upload_files.append(upload_files_type_0_item)

        else:
            upload_files = self.upload_files

        upload_option: str | Unset = UNSET
        if not isinstance(self.upload_option, Unset):
            upload_option = self.upload_option.value

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_type": create_type,
                "folder_id": folder_id,
            }
        )
        if dbkey is not UNSET:
            field_dict["dbkey"] = dbkey
        if extended_metadata is not UNSET:
            field_dict["extended_metadata"] = extended_metadata
        if file_type is not UNSET:
            field_dict["file_type"] = file_type
        if filesystem_paths is not UNSET:
            field_dict["filesystem_paths"] = filesystem_paths
        if from_hda_id is not UNSET:
            field_dict["from_hda_id"] = from_hda_id
        if from_hdca_id is not UNSET:
            field_dict["from_hdca_id"] = from_hdca_id
        if ldda_message is not UNSET:
            field_dict["ldda_message"] = ldda_message
        if link_data_only is not UNSET:
            field_dict["link_data_only"] = link_data_only
        if roles is not UNSET:
            field_dict["roles"] = roles
        if server_dir is not UNSET:
            field_dict["server_dir"] = server_dir
        if tag_using_filenames is not UNSET:
            field_dict["tag_using_filenames"] = tag_using_filenames
        if tags is not UNSET:
            field_dict["tags"] = tags
        if upload_files is not UNSET:
            field_dict["upload_files"] = upload_files
        if upload_option is not UNSET:
            field_dict["upload_option"] = upload_option
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_contents_file_create_payload_extended_metadata_type_0 import (
            LibraryContentsFileCreatePayloadExtendedMetadataType0,
        )
        from ..models.library_contents_file_create_payload_upload_files_type_0_item import (
            LibraryContentsFileCreatePayloadUploadFilesType0Item,
        )

        d = dict(src_dict)
        create_type = CreateType(d.pop("create_type"))

        folder_id = d.pop("folder_id")

        def _parse_dbkey(data: object) -> list[Any] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dbkey_type_1 = cast(list[Any], data)

                return dbkey_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | str | Unset, data)

        dbkey = _parse_dbkey(d.pop("dbkey", UNSET))

        def _parse_extended_metadata(
            data: object,
        ) -> LibraryContentsFileCreatePayloadExtendedMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extended_metadata_type_0 = LibraryContentsFileCreatePayloadExtendedMetadataType0.from_dict(data)

                return extended_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LibraryContentsFileCreatePayloadExtendedMetadataType0 | None | Unset, data)

        extended_metadata = _parse_extended_metadata(d.pop("extended_metadata", UNSET))

        def _parse_file_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_type = _parse_file_type(d.pop("file_type", UNSET))

        filesystem_paths = d.pop("filesystem_paths", UNSET)

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

        _link_data_only = d.pop("link_data_only", UNSET)
        link_data_only: LinkDataOnly | Unset
        if isinstance(_link_data_only, Unset):
            link_data_only = UNSET
        else:
            link_data_only = LinkDataOnly(_link_data_only)

        roles = d.pop("roles", UNSET)

        server_dir = d.pop("server_dir", UNSET)

        tag_using_filenames = d.pop("tag_using_filenames", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_upload_files(
            data: object,
        ) -> list[LibraryContentsFileCreatePayloadUploadFilesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                upload_files_type_0 = []
                _upload_files_type_0 = data
                for upload_files_type_0_item_data in _upload_files_type_0:
                    upload_files_type_0_item = LibraryContentsFileCreatePayloadUploadFilesType0Item.from_dict(
                        upload_files_type_0_item_data
                    )

                    upload_files_type_0.append(upload_files_type_0_item)

                return upload_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LibraryContentsFileCreatePayloadUploadFilesType0Item] | None | Unset, data)

        upload_files = _parse_upload_files(d.pop("upload_files", UNSET))

        _upload_option = d.pop("upload_option", UNSET)
        upload_option: UploadOption | Unset
        if isinstance(_upload_option, Unset):
            upload_option = UNSET
        else:
            upload_option = UploadOption(_upload_option)

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        library_contents_file_create_payload = cls(
            create_type=create_type,
            folder_id=folder_id,
            dbkey=dbkey,
            extended_metadata=extended_metadata,
            file_type=file_type,
            filesystem_paths=filesystem_paths,
            from_hda_id=from_hda_id,
            from_hdca_id=from_hdca_id,
            ldda_message=ldda_message,
            link_data_only=link_data_only,
            roles=roles,
            server_dir=server_dir,
            tag_using_filenames=tag_using_filenames,
            tags=tags,
            upload_files=upload_files,
            upload_option=upload_option,
            uuid=uuid,
        )

        library_contents_file_create_payload.additional_properties = d
        return library_contents_file_create_payload

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
