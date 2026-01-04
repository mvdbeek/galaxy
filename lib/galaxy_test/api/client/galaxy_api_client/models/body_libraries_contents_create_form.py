from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BodyLibrariesContentsCreateForm")


@_attrs_define
class BodyLibrariesContentsCreateForm:
    """
    Attributes:
        create_type (Any):
        folder_id (Any):
        dbkey (Any | Unset):  Default: '?'.
        extended_metadata (Any | Unset):
        file_type (Any | Unset):
        files (list[File] | None | Unset):
        filesystem_paths (Any | Unset):  Default: ''.
        from_hda_id (Any | Unset):
        from_hdca_id (Any | Unset):
        ldda_message (Any | Unset):  Default: ''.
        link_data_only (Any | Unset):  Default: 'copy_files'.
        roles (Any | Unset):  Default: ''.
        server_dir (Any | Unset):  Default: ''.
        tag_using_filenames (Any | Unset):  Default: False.
        tags (Any | Unset):  Default: [].
        upload_files (Any | Unset):
        upload_option (Any | Unset):  Default: 'upload_file'.
        uuid (Any | Unset):
    """

    create_type: Any
    folder_id: Any
    dbkey: Any | Unset = "?"
    extended_metadata: Any | Unset = UNSET
    file_type: Any | Unset = UNSET
    files: list[File] | None | Unset = UNSET
    filesystem_paths: Any | Unset = ""
    from_hda_id: Any | Unset = UNSET
    from_hdca_id: Any | Unset = UNSET
    ldda_message: Any | Unset = ""
    link_data_only: Any | Unset = "copy_files"
    roles: Any | Unset = ""
    server_dir: Any | Unset = ""
    tag_using_filenames: Any | Unset = False
    tags: Any | Unset = []
    upload_files: Any | Unset = UNSET
    upload_option: Any | Unset = "upload_file"
    uuid: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_type = self.create_type

        folder_id = self.folder_id

        dbkey = self.dbkey

        extended_metadata = self.extended_metadata

        file_type = self.file_type

        files: list[FileTypes] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_tuple()

                files.append(files_type_0_item)

        else:
            files = self.files

        filesystem_paths = self.filesystem_paths

        from_hda_id = self.from_hda_id

        from_hdca_id = self.from_hdca_id

        ldda_message = self.ldda_message

        link_data_only = self.link_data_only

        roles = self.roles

        server_dir = self.server_dir

        tag_using_filenames = self.tag_using_filenames

        tags = self.tags

        upload_files = self.upload_files

        upload_option = self.upload_option

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
        if files is not UNSET:
            field_dict["files"] = files
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("create_type", (None, str(self.create_type).encode(), "text/plain")))

        files.append(("folder_id", (None, str(self.folder_id).encode(), "text/plain")))

        if not isinstance(self.dbkey, Unset):
            files.append(("dbkey", (None, str(self.dbkey).encode(), "text/plain")))

        if not isinstance(self.extended_metadata, Unset):
            files.append(("extended_metadata", (None, str(self.extended_metadata).encode(), "text/plain")))

        if not isinstance(self.file_type, Unset):
            files.append(("file_type", (None, str(self.file_type).encode(), "text/plain")))

        if not isinstance(self.files, Unset):
            if isinstance(self.files, list):
                for files_type_0_item_element in self.files:
                    files.append(("files", files_type_0_item_element.to_tuple()))
            else:
                files.append(("files", (None, str(self.files).encode(), "text/plain")))

        if not isinstance(self.filesystem_paths, Unset):
            files.append(("filesystem_paths", (None, str(self.filesystem_paths).encode(), "text/plain")))

        if not isinstance(self.from_hda_id, Unset):
            files.append(("from_hda_id", (None, str(self.from_hda_id).encode(), "text/plain")))

        if not isinstance(self.from_hdca_id, Unset):
            files.append(("from_hdca_id", (None, str(self.from_hdca_id).encode(), "text/plain")))

        if not isinstance(self.ldda_message, Unset):
            files.append(("ldda_message", (None, str(self.ldda_message).encode(), "text/plain")))

        if not isinstance(self.link_data_only, Unset):
            files.append(("link_data_only", (None, str(self.link_data_only).encode(), "text/plain")))

        if not isinstance(self.roles, Unset):
            files.append(("roles", (None, str(self.roles).encode(), "text/plain")))

        if not isinstance(self.server_dir, Unset):
            files.append(("server_dir", (None, str(self.server_dir).encode(), "text/plain")))

        if not isinstance(self.tag_using_filenames, Unset):
            files.append(("tag_using_filenames", (None, str(self.tag_using_filenames).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            files.append(("tags", (None, str(self.tags).encode(), "text/plain")))

        if not isinstance(self.upload_files, Unset):
            files.append(("upload_files", (None, str(self.upload_files).encode(), "text/plain")))

        if not isinstance(self.upload_option, Unset):
            files.append(("upload_option", (None, str(self.upload_option).encode(), "text/plain")))

        if not isinstance(self.uuid, Unset):
            files.append(("uuid", (None, str(self.uuid).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_type = d.pop("create_type")

        folder_id = d.pop("folder_id")

        dbkey = d.pop("dbkey", UNSET)

        extended_metadata = d.pop("extended_metadata", UNSET)

        file_type = d.pop("file_type", UNSET)

        def _parse_files(data: object) -> list[File] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in _files_type_0:
                    files_type_0_item = File(payload=BytesIO(files_type_0_item_data))

                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[File] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))

        filesystem_paths = d.pop("filesystem_paths", UNSET)

        from_hda_id = d.pop("from_hda_id", UNSET)

        from_hdca_id = d.pop("from_hdca_id", UNSET)

        ldda_message = d.pop("ldda_message", UNSET)

        link_data_only = d.pop("link_data_only", UNSET)

        roles = d.pop("roles", UNSET)

        server_dir = d.pop("server_dir", UNSET)

        tag_using_filenames = d.pop("tag_using_filenames", UNSET)

        tags = d.pop("tags", UNSET)

        upload_files = d.pop("upload_files", UNSET)

        upload_option = d.pop("upload_option", UNSET)

        uuid = d.pop("uuid", UNSET)

        body_libraries_contents_create_form = cls(
            create_type=create_type,
            folder_id=folder_id,
            dbkey=dbkey,
            extended_metadata=extended_metadata,
            file_type=file_type,
            files=files,
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

        body_libraries_contents_create_form.additional_properties = d
        return body_libraries_contents_create_form

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
