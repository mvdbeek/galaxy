from dataclasses import dataclass

from .create_file_landing_payload_request_state_item_class_enum import CreateFileLandingPayloadRequestStateItemClassEnum
from .data_request_collection_uri_elements import DataRequestCollectionUriElements
from .data_request_collection_uri_name import DataRequestCollectionUriName
from .data_request_collection_uri_src import DataRequestCollectionUriSrc

__all__ = ["DataRequestCollectionUri"]


@dataclass
class DataRequestCollectionUri:
    """
    DataRequestCollectionUri dataclass

    Args:
        class_ (CreateFileLandingPayloadRequestStateItemClassEnum)
                                 : Maps from 'class'
        collection_type (str)    :
        elements (DataRequestCollectionUriElements)
                                 :
        deferred (bool | None)   :
        name (DataRequestCollectionUriName | None)
                                 :
        src (DataRequestCollectionUriSrc | None)
                                 :
    """

    class_: CreateFileLandingPayloadRequestStateItemClassEnum  # Maps from 'class'
    collection_type: str
    elements: DataRequestCollectionUriElements
    deferred: bool | None = False
    name: DataRequestCollectionUriName | None = None
    src: DataRequestCollectionUriSrc | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class": "class_",
            "collection_type": "collection_type",
            "deferred": "deferred",
            "elements": "elements",
            "name": "name",
            "src": "src",
        }
        key_transform_with_dump = {
            "class_": "class",
            "collection_type": "collection_type",
            "deferred": "deferred",
            "elements": "elements",
            "name": "name",
            "src": "src",
        }
