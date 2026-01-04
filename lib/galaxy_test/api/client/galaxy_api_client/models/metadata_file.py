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
