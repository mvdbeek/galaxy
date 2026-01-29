from dataclasses import dataclass

from .model_store_format import ModelStoreFormat
from .store_content_uri import StoreContentUri
from .store_dict import StoreDict

__all__ = ["CreateHistoryFromStore"]


@dataclass
class CreateHistoryFromStore:
    """
    CreateHistoryFromStore dataclass.

    Args:
        model_store_format (Optional[ModelStoreFormat])
                                 :
        store_content_uri (Optional[StoreContentUri])
                                 :
        store_dict (Optional[StoreDict])
                                 :
    """

    model_store_format: ModelStoreFormat | None = None
    store_content_uri: StoreContentUri | None = None
    store_dict: StoreDict | None = None
