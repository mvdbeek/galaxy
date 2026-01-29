from dataclasses import dataclass

__all__ = ["FileDefaultsAction"]


@dataclass
class FileDefaultsAction:
    """
    FileDefaultsAction dataclass.

    Args:
        action_type (str)        :
    """

    action_type: str
