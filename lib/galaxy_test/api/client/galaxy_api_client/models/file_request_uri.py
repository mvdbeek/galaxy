from dataclasses import dataclass

from .create_file_landing_payload_request_state_item_class_enum import CreateFileLandingPayloadRequestStateItemClassEnum
from .file_request_uri_created_from_basename import FileRequestUriCreatedFromBasename
from .file_request_uri_hashes import FileRequestUriHashes
from .file_request_uri_info import FileRequestUriInfo
from .file_request_uri_name import FileRequestUriName
from .file_request_uri_src import FileRequestUriSrc
from .file_request_uri_tags import FileRequestUriTags

__all__ = ["FileRequestUri"]


@dataclass
class FileRequestUri:
    """
    FileRequestUri dataclass

    Args:
        class_ (CreateFileLandingPayloadRequestStateItemClassEnum)
                                 : Maps from 'class'
        ext (str)                :
        location (str)           :
        created_from_basename (FileRequestUriCreatedFromBasename | None)
                                 :
        dbkey (str | None)       :
        deferred (bool | None)   :
        hashes (FileRequestUriHashes | None)
                                 :
        info (FileRequestUriInfo | None)
                                 :
        name (FileRequestUriName | None)
                                 :
        space_to_tab (bool | None):
        src (FileRequestUriSrc | None)
                                 :
        tags (FileRequestUriTags | None)
                                 :
        to_posix_lines (bool | None)
                                 :
    """

    class_: CreateFileLandingPayloadRequestStateItemClassEnum  # Maps from 'class'
    ext: str
    location: str
    created_from_basename: FileRequestUriCreatedFromBasename | None = None
    dbkey: str | None = "?"
    deferred: bool | None = False
    hashes: FileRequestUriHashes | None = None
    info: FileRequestUriInfo | None = None
    name: FileRequestUriName | None = None
    space_to_tab: bool | None = False
    src: FileRequestUriSrc | None = None
    tags: FileRequestUriTags | None = None
    to_posix_lines: bool | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class": "class_",
            "created_from_basename": "created_from_basename",
            "dbkey": "dbkey",
            "deferred": "deferred",
            "ext": "ext",
            "hashes": "hashes",
            "info": "info",
            "location": "location",
            "name": "name",
            "space_to_tab": "space_to_tab",
            "src": "src",
            "tags": "tags",
            "to_posix_lines": "to_posix_lines",
        }
        key_transform_with_dump = {
            "class_": "class",
            "created_from_basename": "created_from_basename",
            "dbkey": "dbkey",
            "deferred": "deferred",
            "ext": "ext",
            "hashes": "hashes",
            "info": "info",
            "location": "location",
            "name": "name",
            "space_to_tab": "space_to_tab",
            "src": "src",
            "tags": "tags",
            "to_posix_lines": "to_posix_lines",
        }
