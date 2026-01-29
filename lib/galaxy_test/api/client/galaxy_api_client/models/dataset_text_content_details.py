from dataclasses import dataclass

from .dataset_text_content_details_item_data import DatasetTextContentDetailsItemData

__all__ = ["DatasetTextContentDetails"]


@dataclass
class DatasetTextContentDetails:
    """
    DatasetTextContentDetails dataclass

    Args:
        item_data (DatasetTextContentDetailsItemData)
                                 : First chunk of text content (maximum 1MB) of the dataset.
        item_url (str)           : URL to access this dataset.
        truncated (bool)         : Whether the text in `item_data` has been truncated or
                                   contains the whole contents.
    """

    item_data: DatasetTextContentDetailsItemData  # First chunk of text content (maximum 1MB) of the dataset.
    item_url: str  # URL to access this dataset.
    truncated: bool  # Whether the text in `item_data` has been truncated or contains the whole contents.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "item_data": "item_data",
            "item_url": "item_url",
            "truncated": "truncated",
        }
        key_transform_with_dump = {
            "item_data": "item_data",
            "item_url": "item_url",
            "truncated": "truncated",
        }
