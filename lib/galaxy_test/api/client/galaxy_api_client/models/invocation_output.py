from dataclasses import dataclass

from .id__5 import Id5

__all__ = ["InvocationOutput"]


@dataclass
class InvocationOutput:
    """
    InvocationOutput dataclass

    Args:
        src (str)                : Source model of the output dataset.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   dataset/dataset collection.
        id_ (Id5 | None)         : The encoded ID of the dataset/dataset collection. (maps
                                   from 'id')
    """

    src: str  # Source model of the output dataset.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the dataset/dataset collection.
    id_: Id5 | None = None  # The encoded ID of the dataset/dataset collection. (maps from 'id')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
            "workflow_step_id": "workflow_step_id",
        }
