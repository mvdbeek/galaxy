from dataclasses import dataclass

from .id_ import Id_

__all__ = ["InvocationOutputCollection"]


@dataclass
class InvocationOutputCollection:
    """
    InvocationOutputCollection dataclass.

    Args:
        src (str)                : Source model of the output dataset collection.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   dataset/dataset collection.
        id_ (Optional[Id_])      : The encoded ID of the dataset/dataset collection.
    """

    src: str  # Source model of the output dataset collection.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the dataset/dataset collection.
    id_: Id_ | None = None  # The encoded ID of the dataset/dataset collection.
