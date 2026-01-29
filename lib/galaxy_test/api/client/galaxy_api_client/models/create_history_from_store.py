from dataclasses import dataclass

from .create_history_from_store_model_store_format import CreateHistoryFromStoreModelStoreFormat
from .create_history_from_store_store_content_uri import CreateHistoryFromStoreStoreContentUri
from .create_history_from_store_store_dict import CreateHistoryFromStoreStoreDict

__all__ = ["CreateHistoryFromStore"]


@dataclass
class CreateHistoryFromStore:
    """
    CreateHistoryFromStore dataclass

    Args:
        model_store_format (CreateHistoryFromStoreModelStoreFormat | None)
                                 :
        store_content_uri (CreateHistoryFromStoreStoreContentUri | None)
                                 :
        store_dict (CreateHistoryFromStoreStoreDict | None)
                                 :
    """

    model_store_format: CreateHistoryFromStoreModelStoreFormat | None = None
    store_content_uri: CreateHistoryFromStoreStoreContentUri | None = None
    store_dict: CreateHistoryFromStoreStoreDict | None = None

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
