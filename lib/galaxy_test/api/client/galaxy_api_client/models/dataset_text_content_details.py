from dataclasses import dataclass

from .item_data import ItemData

__all__ = ["DatasetTextContentDetails"]


@dataclass
class DatasetTextContentDetails:
    """
    DatasetTextContentDetails dataclass.

    Args:
        item_data (Optional[ItemData])
                                 : First chunk of text content (maximum 1MB) of the dataset.
        item_url (str)           : URL to access this dataset.
        truncated (bool)         : Whether the text in `item_data` has been truncated or
                                   contains the whole contents.
    """

    item_data: ItemData | None  # First chunk of text content (maximum 1MB) of the dataset.
    item_url: str  # URL to access this dataset.
    truncated: bool  # Whether the text in `item_data` has been truncated or contains the whole contents.
