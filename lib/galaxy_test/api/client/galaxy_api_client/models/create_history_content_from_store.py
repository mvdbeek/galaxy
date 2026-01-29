from dataclasses import dataclass

from .create_history_content_from_store_model_store_format import CreateHistoryContentFromStoreModelStoreFormat
from .create_history_content_from_store_store_content_uri import CreateHistoryContentFromStoreStoreContentUri
from .create_history_content_from_store_store_dict import CreateHistoryContentFromStoreStoreDict

__all__ = ["CreateHistoryContentFromStore"]


@dataclass
class CreateHistoryContentFromStore:
    """
    CreateHistoryContentFromStore dataclass

    Args:
        model_store_format (CreateHistoryContentFromStoreModelStoreFormat | None)
                                 :
        store_content_uri (CreateHistoryContentFromStoreStoreContentUri | None)
                                 :
        store_dict (CreateHistoryContentFromStoreStoreDict | None)
                                 :
    """

    model_store_format: CreateHistoryContentFromStoreModelStoreFormat | None = None
    store_content_uri: CreateHistoryContentFromStoreStoreContentUri | None = None
    store_dict: CreateHistoryContentFromStoreStoreDict | None = None

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
