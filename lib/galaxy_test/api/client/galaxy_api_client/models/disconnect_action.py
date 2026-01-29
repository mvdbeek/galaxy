from dataclasses import dataclass

from .disconnect_action_output import DisconnectActionOutput
from .input__2 import Input2
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["DisconnectAction"]


@dataclass
class DisconnectAction:
    """
    DisconnectAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        input_ (Input2)          : Maps from 'input'
        output (DisconnectActionOutput)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    input_: Input2  # Maps from 'input'
    output: DisconnectActionOutput

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "input": "input_",
            "output": "output",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "input_": "input",
            "output": "output",
        }
