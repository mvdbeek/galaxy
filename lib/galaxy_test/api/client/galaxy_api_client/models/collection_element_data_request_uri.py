from dataclasses import dataclass

from .collection_element_data_request_uri_created_from_basename import (
    CollectionElementDataRequestUriCreatedFromBasename,
)
from .collection_element_data_request_uri_hashes import CollectionElementDataRequestUriHashes
from .collection_element_data_request_uri_info import CollectionElementDataRequestUriInfo
from .collection_element_data_request_uri_name import CollectionElementDataRequestUriName
from .collection_element_data_request_uri_src import CollectionElementDataRequestUriSrc
from .collection_element_data_request_uri_tags import CollectionElementDataRequestUriTags

__all__ = ["CollectionElementDataRequestUri"]


@dataclass
class CollectionElementDataRequestUri:
    """
    CollectionElementDataRequestUri dataclass

    Args:
        class_ (str)             : Maps from 'class'
        ext (str)                :
        identifier (str)         : A unique identifier for this element within the
                                   collection.
        location (str)           :
        created_from_basename (CollectionElementDataRequestUriCreatedFromBasename | None)
                                 :
        dbkey (str | None)       :
        deferred (bool | None)   :
        hashes (CollectionElementDataRequestUriHashes | None)
                                 :
        info (CollectionElementDataRequestUriInfo | None)
                                 :
        name (CollectionElementDataRequestUriName | None)
                                 :
        space_to_tab (bool | None):
        src (CollectionElementDataRequestUriSrc | None)
                                 :
        tags (CollectionElementDataRequestUriTags | None)
                                 :
        to_posix_lines (bool | None)
                                 :
    """

    class_: str  # Maps from 'class'
    ext: str
    identifier: str  # A unique identifier for this element within the collection.
    location: str
    created_from_basename: CollectionElementDataRequestUriCreatedFromBasename | None = None
    dbkey: str | None = "?"
    deferred: bool | None = False
    hashes: CollectionElementDataRequestUriHashes | None = None
    info: CollectionElementDataRequestUriInfo | None = None
    name: CollectionElementDataRequestUriName | None = None
    space_to_tab: bool | None = False
    src: CollectionElementDataRequestUriSrc | None = None
    tags: CollectionElementDataRequestUriTags | None = None
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
            "identifier": "identifier",
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
            "identifier": "identifier",
            "info": "info",
            "location": "location",
            "name": "name",
            "space_to_tab": "space_to_tab",
            "src": "src",
            "tags": "tags",
            "to_posix_lines": "to_posix_lines",
        }
