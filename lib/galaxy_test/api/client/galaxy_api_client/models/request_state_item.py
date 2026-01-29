from typing import TypeAlias

from .data_request_collection_uri import DataRequestCollectionUri
from .file_request_uri import FileRequestUri

__all__ = ["RequestStateItem"]

RequestStateItem: TypeAlias = DataRequestCollectionUri | FileRequestUri
