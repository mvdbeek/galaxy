from dataclasses import dataclass

from .label import Label
from .uuid_ import Uuid_
from .value import Value

__all__ = ["WorkflowInput"]


@dataclass
class WorkflowInput:
    """
    WorkflowInput dataclass.

    Args:
        label (Optional[Label])  : Label of the input.
        uuid_ (Uuid_)            : Universal unique identifier of the workflow invocation.
        value (Optional[Value])  : TODO
    """

    label: Label | None  # Label of the input.
    uuid_: Uuid_  # Universal unique identifier of the workflow invocation.
    value: Value | None  # TODO
