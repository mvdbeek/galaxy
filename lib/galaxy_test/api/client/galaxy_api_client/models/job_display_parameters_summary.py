from dataclasses import dataclass

from .job_display_parameters_summary_outputs import JobDisplayParametersSummaryOutputs
from .job_parameter import JobParameter

__all__ = ["JobDisplayParametersSummary"]


@dataclass
class JobDisplayParametersSummary:
    """
    JobDisplayParametersSummary dataclass

    Args:
        has_parameter_errors (bool)
                                 : The job has parameter errors
        outputs (JobDisplayParametersSummaryOutputs)
                                 : Dictionary mapping all the tool outputs (by name) with
                                   the corresponding dataset information in a nested format.
        parameters (List[JobParameter])
                                 : The parameters of the job in a nested format.
    """

    has_parameter_errors: bool  # The job has parameter errors
    outputs: JobDisplayParametersSummaryOutputs  # Dictionary mapping all the tool outputs (by name) with the corresponding dataset information in a nested format.
    parameters: list[JobParameter]  # The parameters of the job in a nested format.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "has_parameter_errors": "has_parameter_errors",
            "outputs": "outputs",
            "parameters": "parameters",
        }
        key_transform_with_dump = {
            "has_parameter_errors": "has_parameter_errors",
            "outputs": "outputs",
            "parameters": "parameters",
        }
