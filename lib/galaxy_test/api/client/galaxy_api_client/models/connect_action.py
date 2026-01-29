from dataclasses import dataclass

from .connect_action_output import ConnectActionOutput
from .input_ import Input_
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["ConnectAction"]


@dataclass
class ConnectAction:
    """
    ConnectAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        input_ (Input_)          : Maps from 'input'
        output (ConnectActionOutput)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    input_: Input_  # Maps from 'input'
    output: ConnectActionOutput

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
