from dataclasses import dataclass

__all__ = ["RemoteDirectory"]


@dataclass
class RemoteDirectory:
    """
    RemoteDirectory dataclass.

    Args:
        class_ (str)             :
        name (str)               : The name of the entry.
        path (str)               : The path of the entry.
        uri (str)                : The URI of the entry.
    """

    class_: str
    name: str  # The name of the entry.
    path: str  # The path of the entry.
    uri: str  # The URI of the entry.
