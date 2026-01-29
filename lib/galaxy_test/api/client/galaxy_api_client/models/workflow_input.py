from dataclasses import dataclass

from .uuid__8 import Uuid8
from .workflow_input_label import WorkflowInputLabel
from .workflow_input_value import WorkflowInputValue

__all__ = ["WorkflowInput"]


@dataclass
class WorkflowInput:
    """
    WorkflowInput dataclass

    Args:
        label (WorkflowInputLabel): Label of the input.
        uuid_ (Uuid8 | None)     : Universal unique identifier of the input. (maps from
                                   'uuid')
        value (WorkflowInputValue): TODO
    """

    label: WorkflowInputLabel  # Label of the input.
    uuid_: Uuid8 | None  # Universal unique identifier of the input. (maps from 'uuid')
    value: WorkflowInputValue  # TODO

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "uuid": "uuid_",
            "value": "value",
        }
        key_transform_with_dump = {
            "label": "label",
            "uuid_": "uuid",
            "value": "value",
        }
