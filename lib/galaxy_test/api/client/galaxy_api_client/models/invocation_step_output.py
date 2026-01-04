from dataclasses import dataclass

from .uuid_ import Uuid_

__all__ = ["InvocationStepOutput"]


@dataclass
class InvocationStepOutput:
    """
    InvocationStepOutput dataclass.

    Args:
        id_ (str)                : Dataset ID of the workflow step output.
        src (Optional[str])      : The source model of the output.
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    id_: str  # Dataset ID of the workflow step output.
    src: str | None = "hda"  # The source model of the output.
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
