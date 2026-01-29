from dataclasses import dataclass

from .id__4 import Id4
from .invocation_input_label import InvocationInputLabel
from .invocation_input_src import InvocationInputSrc

__all__ = ["InvocationInput"]


@dataclass
class InvocationInput:
    """
    InvocationInput dataclass

    Args:
        src (InvocationInputSrc) : Source type of the input dataset/dataset collection.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   dataset/dataset collection.
        id_ (Id4 | None)         : The encoded ID of the dataset/dataset collection. (maps
                                   from 'id')
        label (InvocationInputLabel | None)
                                 : Label of the workflow step associated with the input
                                   dataset/dataset collection.
    """

    src: InvocationInputSrc  # Source type of the input dataset/dataset collection.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the dataset/dataset collection.
    id_: Id4 | None = None  # The encoded ID of the dataset/dataset collection. (maps from 'id')
    label: InvocationInputLabel | None = (
        None  # Label of the workflow step associated with the input dataset/dataset collection.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "label": "label",
            "src": "src",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "id_": "id",
            "label": "label",
            "src": "src",
            "workflow_step_id": "workflow_step_id",
        }
