from dataclasses import dataclass

__all__ = ["InvocationStepCollectionOutput"]


@dataclass
class InvocationStepCollectionOutput:
    """
    InvocationStepCollectionOutput dataclass.

    Args:
        id_ (str)                : Dataset Collection ID of the workflow step output.
        src (Optional[str])      : The source model of the output.
    """

    id_: str  # Dataset Collection ID of the workflow step output.
    src: str | None = "hdca"  # The source model of the output.
