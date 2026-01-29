from dataclasses import dataclass

from .create_libraries_from_store_model_store_format import CreateLibrariesFromStoreModelStoreFormat
from .create_libraries_from_store_store_content_uri import CreateLibrariesFromStoreStoreContentUri
from .create_libraries_from_store_store_dict import CreateLibrariesFromStoreStoreDict

__all__ = ["CreateLibrariesFromStore"]


@dataclass
class CreateLibrariesFromStore:
    """
    CreateLibrariesFromStore dataclass

    Args:
        model_store_format (CreateLibrariesFromStoreModelStoreFormat | None)
                                 :
        store_content_uri (CreateLibrariesFromStoreStoreContentUri | None)
                                 :
        store_dict (CreateLibrariesFromStoreStoreDict | None)
                                 :
    """

    model_store_format: CreateLibrariesFromStoreModelStoreFormat | None = None
    store_content_uri: CreateLibrariesFromStoreStoreContentUri | None = None
    store_dict: CreateLibrariesFromStoreStoreDict | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "model_store_format": "model_store_format",
            "store_content_uri": "store_content_uri",
            "store_dict": "store_dict",
        }
        key_transform_with_dump = {
            "model_store_format": "model_store_format",
            "store_content_uri": "store_content_uri",
            "store_dict": "store_dict",
        }
