from dataclasses import dataclass

from .refactor_action_execution_message_from_order_index import RefactorActionExecutionMessageFromOrderIndex
from .refactor_action_execution_message_from_step_label import RefactorActionExecutionMessageFromStepLabel
from .refactor_action_execution_message_input_name import RefactorActionExecutionMessageInputName
from .refactor_action_execution_message_order_index import RefactorActionExecutionMessageOrderIndex
from .refactor_action_execution_message_output_label import RefactorActionExecutionMessageOutputLabel
from .refactor_action_execution_message_output_name import RefactorActionExecutionMessageOutputName
from .refactor_action_execution_message_step_label import RefactorActionExecutionMessageStepLabel
from .refactor_action_execution_message_type_enum import RefactorActionExecutionMessageTypeEnum

__all__ = ["RefactorActionExecutionMessage"]


@dataclass
class RefactorActionExecutionMessage:
    """
    RefactorActionExecutionMessage dataclass

    Args:
        message (str)            :
        message_type (RefactorActionExecutionMessageTypeEnum)
                                 :
        from_order_index (RefactorActionExecutionMessageFromOrderIndex | None)
                                 : For dropped connections these optional attributes refer
                                   to the output side of the connection that was dropped.
        from_step_label (RefactorActionExecutionMessageFromStepLabel | None)
                                 : For dropped connections these optional attributes refer
                                   to the output side of the connection that was dropped.
        input_name (RefactorActionExecutionMessageInputName | None)
                                 : If this message is about an input to a step, this field
                                   describes the target input name. $The input name as
                                   defined by the workflow module corresponding to the step
                                   being referenced. For Galaxy tool steps these inputs
                                   should be normalized using '|' (e.g.
                                   'cond|repeat_0|input').
        order_index (RefactorActionExecutionMessageOrderIndex | None)
                                 : Reference to the step the message refers to. $  Messages
                                   don't have to be bound to a step, but if they are they
                                   will have a step_label and order_index included in the
                                   execution message. These are the label and order_index
                                   before applying the refactoring, the result of applying
                                   the action may change one or both of these. If
                                   connections are dropped this step reference will refer to
                                   the step with the previously connected input.
        output_label (RefactorActionExecutionMessageOutputLabel | None)
                                 : If the message_type is workflow_output_drop_forced, this
                                   is the output label dropped.
        output_name (RefactorActionExecutionMessageOutputName | None)
                                 : If this message is about an output to a step, this field
                                   describes the target output name. The output name as
                                   defined by the workflow module corresponding to the step
                                   being referenced.
        step_label (RefactorActionExecutionMessageStepLabel | None)
                                 : Reference to the step the message refers to. $  Messages
                                   don't have to be bound to a step, but if they are they
                                   will have a step_label and order_index included in the
                                   execution message. These are the label and order_index
                                   before applying the refactoring, the result of applying
                                   the action may change one or both of these. If
                                   connections are dropped this step reference will refer to
                                   the step with the previously connected input.
    """

    message: str
    message_type: RefactorActionExecutionMessageTypeEnum
    from_order_index: RefactorActionExecutionMessageFromOrderIndex | None = (
        None  # For dropped connections these optional attributes refer to the output side of the connection that was dropped.
    )
    from_step_label: RefactorActionExecutionMessageFromStepLabel | None = (
        None  # For dropped connections these optional attributes refer to the output side of the connection that was dropped.
    )
    input_name: RefactorActionExecutionMessageInputName | None = (
        None  # If this message is about an input to a step, this field describes the target input name. $The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').
    )
    order_index: RefactorActionExecutionMessageOrderIndex | None = (
        None  # Reference to the step the message refers to. $  Messages don't have to be bound to a step, but if they are they will have a step_label and order_index included in the execution message. These are the label and order_index before applying the refactoring, the result of applying the action may change one or both of these. If connections are dropped this step reference will refer to the step with the previously connected input.
    )
    output_label: RefactorActionExecutionMessageOutputLabel | None = (
        None  # If the message_type is workflow_output_drop_forced, this is the output label dropped.
    )
    output_name: RefactorActionExecutionMessageOutputName | None = (
        None  # If this message is about an output to a step, this field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.
    )
    step_label: RefactorActionExecutionMessageStepLabel | None = (
        None  # Reference to the step the message refers to. $  Messages don't have to be bound to a step, but if they are they will have a step_label and order_index included in the execution message. These are the label and order_index before applying the refactoring, the result of applying the action may change one or both of these. If connections are dropped this step reference will refer to the step with the previously connected input.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "from_order_index": "from_order_index",
            "from_step_label": "from_step_label",
            "input_name": "input_name",
            "message": "message",
            "message_type": "message_type",
            "order_index": "order_index",
            "output_label": "output_label",
            "output_name": "output_name",
            "step_label": "step_label",
        }
        key_transform_with_dump = {
            "from_order_index": "from_order_index",
            "from_step_label": "from_step_label",
            "input_name": "input_name",
            "message": "message",
            "message_type": "message_type",
            "order_index": "order_index",
            "output_label": "output_label",
            "output_name": "output_name",
            "step_label": "step_label",
        }
