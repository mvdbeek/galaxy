from dataclasses import dataclass

__all__ = ["MetadataFile"]


@dataclass
class MetadataFile:
    """
    Metadata file associated with a dataset.

    Args:
        download_url (str)       : The URL to download this item from the server.
        file_type (str)          : TODO
    """

    download_url: str  # The URL to download this item from the server.
    file_type: str  # TODO

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "download_url": "download_url",
            "file_type": "file_type",
        }
        key_transform_with_dump = {
            "download_url": "download_url",
            "file_type": "file_type",
        }
