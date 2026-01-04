from dataclasses import dataclass

from .step_label import StepLabel

__all__ = ["WorkflowJobMetric"]


@dataclass
class WorkflowJobMetric:
    """
    WorkflowJobMetric dataclass.

    Args:
        job_id (str)             :
        name (str)               : The name of the metric variable.
        plugin (str)             : The instrumenter plugin that generated this metric.
        raw_value (str)          : The raw value of the metric as a string.
        step_index (int)         :
        step_label (Optional[StepLabel])
                                 : Reference to the step the message refers to. $  Messages
                                   don't have to be bound to a step, but if they are they
                                   will have a step_label and order_index included in the
                                   execution message. These are the label and order_index
                                   before applying the refactoring, the result of applying
                                   the action may change one or both of these. If
                                   connections are dropped this step reference will refer to
                                   the step with the previously connected input.
        title (str)              : A descriptive title for this metric.
        tool_id (str)            :
        value (str)              : The textual representation of the metric value.
    """

    job_id: str
    name: str  # The name of the metric variable.
    plugin: str  # The instrumenter plugin that generated this metric.
    raw_value: str  # The raw value of the metric as a string.
    step_index: int
    step_label: (
        StepLabel | None
    )  # Reference to the step the message refers to. $  Messages don't have to be bound to a step, but if they are they will have a step_label and order_index included in the execution message. These are the label and order_index before applying the refactoring, the result of applying the action may change one or both of these. If connections are dropped this step reference will refer to the step with the previously connected input.
    title: str  # A descriptive title for this metric.
    tool_id: str
    value: str  # The textual representation of the metric value.
