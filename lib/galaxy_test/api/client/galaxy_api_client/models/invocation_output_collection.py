from dataclasses import dataclass

from .id__6 import Id6

__all__ = ["InvocationOutputCollection"]


@dataclass
class InvocationOutputCollection:
    """
    InvocationOutputCollection dataclass

    Args:
        src (str)                : Source model of the output dataset collection.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   dataset/dataset collection.
        id_ (Id6 | None)         : The encoded ID of the dataset/dataset collection. (maps
                                   from 'id')
    """

    src: str  # Source model of the output dataset collection.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the dataset/dataset collection.
    id_: Id6 | None = None  # The encoded ID of the dataset/dataset collection. (maps from 'id')

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
