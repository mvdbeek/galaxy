from dataclasses import dataclass

from .create_link_incoming_kwd import CreateLinkIncomingKwd

__all__ = ["CreateLinkIncoming"]


@dataclass
class CreateLinkIncoming:
    """
    CreateLinkIncoming dataclass

    Args:
        app_name (str)           :
        dataset_id (str)         :
        link_name (str)          :
        kwd (CreateLinkIncomingKwd | None)
                                 :
    """

    app_name: str
    dataset_id: str
    link_name: str
    kwd: CreateLinkIncomingKwd | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "app_name": "app_name",
            "dataset_id": "dataset_id",
            "kwd": "kwd",
            "link_name": "link_name",
        }
        key_transform_with_dump = {
            "app_name": "app_name",
            "dataset_id": "dataset_id",
            "kwd": "kwd",
            "link_name": "link_name",
        }
