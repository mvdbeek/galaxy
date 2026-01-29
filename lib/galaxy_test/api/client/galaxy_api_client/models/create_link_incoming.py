from dataclasses import dataclass

from .kwd import Kwd

__all__ = ["CreateLinkIncoming"]


@dataclass
class CreateLinkIncoming:
    """
    CreateLinkIncoming dataclass.

    Args:
        app_name (str)           :
        dataset_id (str)         :
        link_name (str)          :
        kwd (Optional[Kwd])      :
    """

    app_name: str
    dataset_id: str
    link_name: str
    kwd: Kwd | None = None
