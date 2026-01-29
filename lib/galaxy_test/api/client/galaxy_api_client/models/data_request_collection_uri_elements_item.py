from typing import TypeAlias

from .collection_element_collection_request_uri import CollectionElementCollectionRequestUri
from .collection_element_data_request_uri import CollectionElementDataRequestUri

__all__ = ["DataRequestCollectionUriElementsItem"]

DataRequestCollectionUriElementsItem: TypeAlias = (
    CollectionElementCollectionRequestUri | CollectionElementDataRequestUri
)
