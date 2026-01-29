from dataclasses import dataclass

__all__ = ["ToolRequestImplicitCollectionReference"]


@dataclass
class ToolRequestImplicitCollectionReference:
    """
    ToolRequestImplicitCollectionReference dataclass.

    Args:
        id_ (str)                :
        output_name (str)        :
        src (str)                :
    """

    id_: str
    output_name: str
    src: str
