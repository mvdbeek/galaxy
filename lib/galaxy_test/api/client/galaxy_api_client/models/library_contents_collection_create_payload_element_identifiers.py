from typing import TypeAlias

from .library_contents_collection_create_payload_element_identifiers_item import (
    LibraryContentsCollectionCreatePayloadElementIdentifiersItem,
)

__all__ = ["LibraryContentsCollectionCreatePayloadElementIdentifiers"]

LibraryContentsCollectionCreatePayloadElementIdentifiers: TypeAlias = list[
    LibraryContentsCollectionCreatePayloadElementIdentifiersItem
]
