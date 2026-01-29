from dataclasses import dataclass

from .id_ import Id_
from .label import Label
from .src import Src

__all__ = ["InvocationInput"]


@dataclass
class InvocationInput:
    """
    InvocationInput dataclass.

    Args:
        src (Src)                : Source type of the input dataset/dataset collection.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   dataset/dataset collection.
        id_ (Optional[Id_])      : The encoded ID of the dataset/dataset collection.
        label (Optional[Label])  : Label of the input.
    """

    src: Src  # Source type of the input dataset/dataset collection.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the dataset/dataset collection.
    id_: Id_ | None = None  # The encoded ID of the dataset/dataset collection.
    label: Label | None = None  # Label of the input.
