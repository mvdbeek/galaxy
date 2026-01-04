from dataclasses import dataclass

from .from_order_index import FromOrderIndex
from .from_step_label import FromStepLabel
from .input_name import InputName
from .order_index import OrderIndex
from .output_label import OutputLabel
from .output_name import OutputName
from .refactor_action_execution_message_type_enum import RefactorActionExecutionMessageTypeEnum
from .step_label import StepLabel

__all__ = ["RefactorActionExecutionMessage"]


@dataclass
class RefactorActionExecutionMessage:
    """
    RefactorActionExecutionMessage dataclass.

    Args:
        message (str)            :
        message_type (RefactorActionExecutionMessageTypeEnum)
                                 :
        from_order_index (Optional[FromOrderIndex])
                                 : For dropped connections these optional attributes refer
                                   to the output side of the connection that was dropped.
        from_step_label (Optional[FromStepLabel])
                                 : For dropped connections these optional attributes refer
                                   to the output side of the connection that was dropped.
        input_name (Optional[InputName])
                                 : If this message is about an input to a step, this field
                                   describes the target input name. $The input name as
                                   defined by the workflow module corresponding to the step
                                   being referenced. For Galaxy tool steps these inputs
                                   should be normalized using '|' (e.g.
                                   'cond|repeat_0|input').
        order_index (Optional[OrderIndex])
                                 : Reference to the step the message refers to. $  Messages
                                   don't have to be bound to a step, but if they are they
                                   will have a step_label and order_index included in the
                                   execution message. These are the label and order_index
                                   before applying the refactoring, the result of applying
                                   the action may change one or both of these. If
                                   connections are dropped this step reference will refer to
                                   the step with the previously connected input.
        output_label (Optional[OutputLabel])
                                 : If the message_type is workflow_output_drop_forced, this
                                   is the output label dropped.
        output_name (Optional[OutputName])
                                 : If this message is about an output to a step, this field
                                   describes the target output name. The output name as
                                   defined by the workflow module corresponding to the step
                                   being referenced.
        step_label (Optional[StepLabel])
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
    from_order_index: FromOrderIndex | None = (
        None  # For dropped connections these optional attributes refer to the output side of the connection that was dropped.
    )
    from_step_label: FromStepLabel | None = (
        None  # For dropped connections these optional attributes refer to the output side of the connection that was dropped.
    )
    input_name: InputName | None = (
        None  # If this message is about an input to a step, this field describes the target input name. $The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').
    )
    order_index: OrderIndex | None = (
        None  # Reference to the step the message refers to. $  Messages don't have to be bound to a step, but if they are they will have a step_label and order_index included in the execution message. These are the label and order_index before applying the refactoring, the result of applying the action may change one or both of these. If connections are dropped this step reference will refer to the step with the previously connected input.
    )
    output_label: OutputLabel | None = (
        None  # If the message_type is workflow_output_drop_forced, this is the output label dropped.
    )
    output_name: OutputName | None = (
        "output"  # If this message is about an output to a step, this field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.
    )
    step_label: StepLabel | None = (
        None  # Reference to the step the message refers to. $  Messages don't have to be bound to a step, but if they are they will have a step_label and order_index included in the execution message. These are the label and order_index before applying the refactoring, the result of applying the action may change one or both of these. If connections are dropped this step reference will refer to the step with the previously connected input.
    )
