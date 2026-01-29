from dataclasses import dataclass, field

from .create_type import CreateType
from .library_contents_file_create_payload_dbkey import LibraryContentsFileCreatePayloadDbkey
from .library_contents_file_create_payload_extended_metadata import LibraryContentsFileCreatePayloadExtendedMetadata
from .library_contents_file_create_payload_file_type import LibraryContentsFileCreatePayloadFileType
from .library_contents_file_create_payload_from_hda_id import LibraryContentsFileCreatePayloadFromHdaId
from .library_contents_file_create_payload_from_hdca_id import LibraryContentsFileCreatePayloadFromHdcaId
from .library_contents_file_create_payload_upload_files import LibraryContentsFileCreatePayloadUploadFiles
from .link_data_only import LinkDataOnly
from .upload_option import UploadOption
from .uuid__7 import Uuid7

__all__ = ["LibraryContentsFileCreatePayload"]


@dataclass
class LibraryContentsFileCreatePayload:
    """
    LibraryContentsFileCreatePayload dataclass

    Args:
        create_type (CreateType) :
        folder_id (str)          : the encoded id of the parent folder of the new item
        dbkey (LibraryContentsFileCreatePayloadDbkey | None)
                                 :
        extended_metadata (LibraryContentsFileCreatePayloadExtendedMetadata | None)
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        file_type (LibraryContentsFileCreatePayloadFileType | None)
                                 :
        filesystem_paths (str | None)
                                 : (only if upload_option is 'upload_paths' and the user is
                                   an admin) file paths on the Galaxy server to upload to
                                   the library, one file per line
        from_hda_id (LibraryContentsFileCreatePayloadFromHdaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (LibraryContentsFileCreatePayloadFromHdcaId | None)
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (str | None): the new message attribute of the LDDA created
        link_data_only (LinkDataOnly | None)
                                 :
        roles (str | None)       :
        server_dir (str | None)  : (only if upload_option is 'upload_directory') relative
                                   path of the subdirectory of Galaxy ``library_import_dir``
                                   (if admin) or ``user_library_import_dir`` (if non-admin)
                                   to upload. All and only the files (i.e. no
                                   subdirectories) contained in the specified directory will
                                   be uploaded.
        tag_using_filenames (bool | None)
                                 : create tags on datasets using the file's original name
        tags (List[str] | None)  : create the given list of tags on datasets
        upload_files (LibraryContentsFileCreatePayloadUploadFiles | None)
                                 :
        upload_option (UploadOption | None)
                                 :
        uuid_ (Uuid7 | None)     : Maps from 'uuid'
    """

    create_type: CreateType
    folder_id: str  # the encoded id of the parent folder of the new item
    dbkey: LibraryContentsFileCreatePayloadDbkey | None = "?"
    extended_metadata: LibraryContentsFileCreatePayloadExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    file_type: LibraryContentsFileCreatePayloadFileType | None = None
    filesystem_paths: str | None = (
        ""  # (only if upload_option is 'upload_paths' and the user is an admin) file paths on the Galaxy server to upload to the library, one file per line
    )
    from_hda_id: LibraryContentsFileCreatePayloadFromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: LibraryContentsFileCreatePayloadFromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    link_data_only: LinkDataOnly | None = None
    roles: str | None = ""
    server_dir: str | None = (
        ""  # (only if upload_option is 'upload_directory') relative path of the subdirectory of Galaxy ``library_import_dir`` (if admin) or ``user_library_import_dir`` (if non-admin) to upload. All and only the files (i.e. no subdirectories) contained in the specified directory will be uploaded.
    )
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: list[str] | None = field(default_factory=list)  # create the given list of tags on datasets
    upload_files: LibraryContentsFileCreatePayloadUploadFiles | None = None
    upload_option: UploadOption | None = None
    uuid_: Uuid7 | None = None  # Maps from 'uuid'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_type": "create_type",
            "dbkey": "dbkey",
            "extended_metadata": "extended_metadata",
            "file_type": "file_type",
            "filesystem_paths": "filesystem_paths",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
            "link_data_only": "link_data_only",
            "roles": "roles",
            "server_dir": "server_dir",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_files": "upload_files",
            "upload_option": "upload_option",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "create_type": "create_type",
            "dbkey": "dbkey",
            "extended_metadata": "extended_metadata",
            "file_type": "file_type",
            "filesystem_paths": "filesystem_paths",
            "folder_id": "folder_id",
            "from_hda_id": "from_hda_id",
            "from_hdca_id": "from_hdca_id",
            "ldda_message": "ldda_message",
            "link_data_only": "link_data_only",
            "roles": "roles",
            "server_dir": "server_dir",
            "tag_using_filenames": "tag_using_filenames",
            "tags": "tags",
            "upload_files": "upload_files",
            "upload_option": "upload_option",
            "uuid_": "uuid",
        }
