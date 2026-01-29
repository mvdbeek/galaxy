from dataclasses import dataclass

from .body_libraries_contents_create_form_create_type import BodyLibrariesContentsCreateFormCreateType
from .body_libraries_contents_create_form_dbkey import BodyLibrariesContentsCreateFormDbkey
from .body_libraries_contents_create_form_extended_metadata import BodyLibrariesContentsCreateFormExtendedMetadata
from .body_libraries_contents_create_form_file_type import BodyLibrariesContentsCreateFormFileType
from .body_libraries_contents_create_form_files import BodyLibrariesContentsCreateFormFiles
from .body_libraries_contents_create_form_filesystem_paths import BodyLibrariesContentsCreateFormFilesystemPaths
from .body_libraries_contents_create_form_folder_id import BodyLibrariesContentsCreateFormFolderId
from .body_libraries_contents_create_form_from_hda_id import BodyLibrariesContentsCreateFormFromHdaId
from .body_libraries_contents_create_form_from_hdca_id import BodyLibrariesContentsCreateFormFromHdcaId
from .body_libraries_contents_create_form_ldda_message import BodyLibrariesContentsCreateFormLddaMessage
from .body_libraries_contents_create_form_link_data_only import BodyLibrariesContentsCreateFormLinkDataOnly
from .body_libraries_contents_create_form_roles import BodyLibrariesContentsCreateFormRoles
from .body_libraries_contents_create_form_server_dir import BodyLibrariesContentsCreateFormServerDir
from .body_libraries_contents_create_form_tag_using_filenames import BodyLibrariesContentsCreateFormTagUsingFilenames
from .body_libraries_contents_create_form_tags import BodyLibrariesContentsCreateFormTags
from .body_libraries_contents_create_form_upload_files import BodyLibrariesContentsCreateFormUploadFiles
from .body_libraries_contents_create_form_upload_option import BodyLibrariesContentsCreateFormUploadOption
from .uuid__11 import Uuid11

__all__ = ["BodyLibrariesContentsCreateForm2"]


@dataclass
class BodyLibrariesContentsCreateForm2:
    """
    BodyLibrariesContentsCreateForm2 dataclass

    Args:
        create_type (BodyLibrariesContentsCreateFormCreateType)
                                 :
        folder_id (BodyLibrariesContentsCreateFormFolderId)
                                 :
        dbkey (BodyLibrariesContentsCreateFormDbkey | None)
                                 :
        extended_metadata (BodyLibrariesContentsCreateFormExtendedMetadata | None)
                                 :
        file_type (BodyLibrariesContentsCreateFormFileType | None)
                                 :
        files (BodyLibrariesContentsCreateFormFiles | None)
                                 :
        filesystem_paths (BodyLibrariesContentsCreateFormFilesystemPaths | None)
                                 :
        from_hda_id (BodyLibrariesContentsCreateFormFromHdaId | None)
                                 :
        from_hdca_id (BodyLibrariesContentsCreateFormFromHdcaId | None)
                                 :
        ldda_message (BodyLibrariesContentsCreateFormLddaMessage | None)
                                 :
        link_data_only (BodyLibrariesContentsCreateFormLinkDataOnly | None)
                                 :
        roles (BodyLibrariesContentsCreateFormRoles | None)
                                 :
        server_dir (BodyLibrariesContentsCreateFormServerDir | None)
                                 :
        tag_using_filenames (BodyLibrariesContentsCreateFormTagUsingFilenames | None)
                                 :
        tags (BodyLibrariesContentsCreateFormTags | None)
                                 :
        upload_files (BodyLibrariesContentsCreateFormUploadFiles | None)
                                 :
        upload_option (BodyLibrariesContentsCreateFormUploadOption | None)
                                 :
        uuid_ (Uuid11 | None)    : Maps from 'uuid'
    """

    create_type: BodyLibrariesContentsCreateFormCreateType
    folder_id: BodyLibrariesContentsCreateFormFolderId
    dbkey: BodyLibrariesContentsCreateFormDbkey | None = "?"
    extended_metadata: BodyLibrariesContentsCreateFormExtendedMetadata | None = None
    file_type: BodyLibrariesContentsCreateFormFileType | None = None
    files: BodyLibrariesContentsCreateFormFiles | None = None
    filesystem_paths: BodyLibrariesContentsCreateFormFilesystemPaths | None = ""
    from_hda_id: BodyLibrariesContentsCreateFormFromHdaId | None = None
    from_hdca_id: BodyLibrariesContentsCreateFormFromHdcaId | None = None
    ldda_message: BodyLibrariesContentsCreateFormLddaMessage | None = ""
    link_data_only: BodyLibrariesContentsCreateFormLinkDataOnly | None = "copy_files"
    roles: BodyLibrariesContentsCreateFormRoles | None = ""
    server_dir: BodyLibrariesContentsCreateFormServerDir | None = ""
    tag_using_filenames: BodyLibrariesContentsCreateFormTagUsingFilenames | None = False
    tags: BodyLibrariesContentsCreateFormTags | None = None
    upload_files: BodyLibrariesContentsCreateFormUploadFiles | None = None
    upload_option: BodyLibrariesContentsCreateFormUploadOption | None = "upload_file"
    uuid_: Uuid11 | None = None  # Maps from 'uuid'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_type": "create_type",
            "dbkey": "dbkey",
            "extended_metadata": "extended_metadata",
            "file_type": "file_type",
            "files": "files",
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
            "files": "files",
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
