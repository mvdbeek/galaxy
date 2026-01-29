from dataclasses import dataclass

__all__ = ["InvocationStepCollectionOutput"]


@dataclass
class InvocationStepCollectionOutput:
    """
    InvocationStepCollectionOutput dataclass

    Args:
        id_ (str)                : Dataset Collection ID of the workflow step output. (maps
                                   from 'id')
        src (str | None)         : The source model of the output.
    """

    id_: str  # Dataset Collection ID of the workflow step output. (maps from 'id')
    src: str | None = "hdca"  # The source model of the output.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
        }
