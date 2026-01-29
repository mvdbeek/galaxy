from dataclasses import dataclass

from .workflow_job_metric_step_label import WorkflowJobMetricStepLabel

__all__ = ["WorkflowJobMetric"]


@dataclass
class WorkflowJobMetric:
    """
    WorkflowJobMetric dataclass

    Args:
        job_id (str)             :
        name (str)               : The name of the metric variable.
        plugin (str)             : The instrumenter plugin that generated this metric.
        raw_value (str)          : The raw value of the metric as a string.
        step_index (int)         :
        step_label (WorkflowJobMetricStepLabel)
                                 :
        title (str)              : A descriptive title for this metric.
        tool_id (str)            :
        value (str)              : The textual representation of the metric value.
    """

    job_id: str
    name: str  # The name of the metric variable.
    plugin: str  # The instrumenter plugin that generated this metric.
    raw_value: str  # The raw value of the metric as a string.
    step_index: int
    step_label: WorkflowJobMetricStepLabel
    title: str  # A descriptive title for this metric.
    tool_id: str
    value: str  # The textual representation of the metric value.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "job_id": "job_id",
            "name": "name",
            "plugin": "plugin",
            "raw_value": "raw_value",
            "step_index": "step_index",
            "step_label": "step_label",
            "title": "title",
            "tool_id": "tool_id",
            "value": "value",
        }
        key_transform_with_dump = {
            "job_id": "job_id",
            "name": "name",
            "plugin": "plugin",
            "raw_value": "raw_value",
            "step_index": "step_index",
            "step_label": "step_label",
            "title": "title",
            "tool_id": "tool_id",
            "value": "value",
        }
