from dataclasses import dataclass

__all__ = ["ToolRequestJobReference"]


@dataclass
class ToolRequestJobReference:
    """
    ToolRequestJobReference dataclass.

    Args:
        id_ (str)                :
        src (str)                :
    """

    id_: str
    src: str
