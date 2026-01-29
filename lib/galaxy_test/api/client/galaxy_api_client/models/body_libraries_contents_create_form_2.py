from dataclasses import dataclass

from .create_type import CreateType
from .dbkey import Dbkey
from .extended_metadata import ExtendedMetadata
from .file_type import FileType
from .files import Files
from .filesystem_paths import FilesystemPaths
from .folder_id import FolderId
from .from_hda_id import FromHdaId
from .from_hdca_id import FromHdcaId
from .ldda_message import LddaMessage
from .link_data_only import LinkDataOnly
from .roles import Roles
from .server_dir import ServerDir
from .tag_using_filenames import TagUsingFilenames
from .tags import Tags
from .upload_files import UploadFiles
from .upload_option import UploadOption
from .uuid_ import Uuid_

__all__ = ["BodyLibrariesContentsCreateForm2"]


@dataclass
class BodyLibrariesContentsCreateForm2:
    """
    BodyLibrariesContentsCreateForm2 dataclass.

    Args:
        create_type (CreateType) :
        folder_id (FolderId)     : The ID of the library folder that will contain the
                                   collection. Required if `instance_type=library`.
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        extended_metadata (Optional[ExtendedMetadata])
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        file_type (Optional[FileType])
                                 :
        files (Optional[Files])  :
        filesystem_paths (Optional[FilesystemPaths])
                                 :
        from_hda_id (Optional[FromHdaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (Optional[FromHdcaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (Optional[LddaMessage])
                                 : The new message attribute of the LDDA created.
        link_data_only (Optional[LinkDataOnly])
                                 :
        roles (Optional[Roles])  :
        server_dir (Optional[ServerDir])
                                 :
        tag_using_filenames (Optional[TagUsingFilenames])
                                 :
        tags (Optional[Tags])    : The collection of tags associated with an item.
        upload_files (Optional[UploadFiles])
                                 :
        upload_option (Optional[UploadOption])
                                 :
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    create_type: CreateType
    folder_id: (
        FolderId  # The ID of the library folder that will contain the collection. Required if `instance_type=library`.
    )
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    extended_metadata: ExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    file_type: FileType | None = None
    files: Files | None = None
    filesystem_paths: FilesystemPaths | None = ""
    from_hda_id: FromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: FromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: LddaMessage | None = ""  # The new message attribute of the LDDA created.
    link_data_only: LinkDataOnly | None = "copy_files"
    roles: Roles | None = ""
    server_dir: ServerDir | None = ""
    tag_using_filenames: TagUsingFilenames | None = False
    tags: Tags | None = None  # The collection of tags associated with an item.
    upload_files: UploadFiles | None = None
    upload_option: UploadOption | None = "upload_file"
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
