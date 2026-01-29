from dataclasses import dataclass

from .create_type import CreateType
from .dbkey import Dbkey
from .extended_metadata import ExtendedMetadata
from .file_type import FileType
from .from_hda_id import FromHdaId
from .from_hdca_id import FromHdcaId
from .link_data_only import LinkDataOnly
from .tags import Tags
from .upload_files import UploadFiles
from .upload_option import UploadOption
from .uuid_ import Uuid_

__all__ = ["LibraryContentsFileCreatePayload"]


@dataclass
class LibraryContentsFileCreatePayload:
    """
    LibraryContentsFileCreatePayload dataclass.

    Args:
        create_type (CreateType) :
        folder_id (str)          : the encoded id of the parent folder of the new item
        dbkey (Optional[Dbkey])  : The database key of the visualization.
        extended_metadata (Optional[ExtendedMetadata])
                                 : sub-dictionary containing any extended metadata to
                                   associate with the item
        file_type (Optional[FileType])
                                 :
        filesystem_paths (Optional[str])
                                 : (only if upload_option is 'upload_paths' and the user is
                                   an admin) file paths on the Galaxy server to upload to
                                   the library, one file per line
        from_hda_id (Optional[FromHdaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDA to copy into the library
        from_hdca_id (Optional[FromHdcaId])
                                 : (only if create_type is 'file') the encoded id of an
                                   accessible HDCA to copy into the library
        ldda_message (Optional[str])
                                 : the new message attribute of the LDDA created
        link_data_only (Optional[LinkDataOnly])
                                 :
        roles (Optional[str])    :
        server_dir (Optional[str]): (only if upload_option is 'upload_directory') relative
                                    path of the subdirectory of Galaxy
                                    ``library_import_dir`` (if admin) or
                                    ``user_library_import_dir`` (if non-admin) to upload.
                                    All and only the files (i.e. no subdirectories)
                                    contained in the specified directory will be uploaded.
        tag_using_filenames (Optional[bool])
                                 : create tags on datasets using the file's original name
        tags (Optional[Tags])    : create the given list of tags on datasets
        upload_files (Optional[UploadFiles])
                                 :
        upload_option (Optional[UploadOption])
                                 :
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    create_type: CreateType
    folder_id: str  # the encoded id of the parent folder of the new item
    dbkey: Dbkey | None = "?"  # The database key of the visualization.
    extended_metadata: ExtendedMetadata | None = (
        None  # sub-dictionary containing any extended metadata to associate with the item
    )
    file_type: FileType | None = None
    filesystem_paths: str | None = (
        ""  # (only if upload_option is 'upload_paths' and the user is an admin) file paths on the Galaxy server to upload to the library, one file per line
    )
    from_hda_id: FromHdaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDA to copy into the library
    )
    from_hdca_id: FromHdcaId | None = (
        None  # (only if create_type is 'file') the encoded id of an accessible HDCA to copy into the library
    )
    ldda_message: str | None = ""  # the new message attribute of the LDDA created
    link_data_only: LinkDataOnly | None = "copy_files"
    roles: str | None = ""
    server_dir: str | None = (
        ""  # (only if upload_option is 'upload_directory') relative path of the subdirectory of Galaxy ``library_import_dir`` (if admin) or ``user_library_import_dir`` (if non-admin) to upload. All and only the files (i.e. no subdirectories) contained in the specified directory will be uploaded.
    )
    tag_using_filenames: bool | None = False  # create tags on datasets using the file's original name
    tags: Tags | None = None  # create the given list of tags on datasets
    upload_files: UploadFiles | None = None
    upload_option: UploadOption | None = "upload_file"
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
