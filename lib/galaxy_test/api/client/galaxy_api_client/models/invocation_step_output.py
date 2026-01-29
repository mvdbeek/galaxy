from dataclasses import dataclass

from .uuid__6 import Uuid6

__all__ = ["InvocationStepOutput"]


@dataclass
class InvocationStepOutput:
    """
    InvocationStepOutput dataclass

    Args:
        id_ (str)                : Dataset ID of the workflow step output. (maps from 'id')
        src (str | None)         : The source model of the output.
        uuid_ (Uuid6 | None)     : Universal unique identifier of the workflow step output
                                   dataset. (maps from 'uuid')
    """

    id_: str  # Dataset ID of the workflow step output. (maps from 'id')
    src: str | None = "hda"  # The source model of the output.
    uuid_: Uuid6 | None = None  # Universal unique identifier of the workflow step output dataset. (maps from 'uuid')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
            "uuid_": "uuid",
        }
