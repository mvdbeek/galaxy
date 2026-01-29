from dataclasses import dataclass

from .job_parameter import JobParameter
from .outputs import Outputs

__all__ = ["JobDisplayParametersSummary"]


@dataclass
class JobDisplayParametersSummary:
    """
    JobDisplayParametersSummary dataclass.

    Args:
        has_parameter_errors (bool)
                                 : The job has parameter errors
        outputs (Outputs)        : Dictionary mapping all the tool outputs (by name) with
                                   the corresponding dataset information in a nested format.
        parameters (List[JobParameter])
                                 : The parameters of the job in a nested format.
    """

    has_parameter_errors: bool  # The job has parameter errors
    outputs: Outputs  # Dictionary mapping all the tool outputs (by name) with the corresponding dataset information in a nested format.
    parameters: list[JobParameter]  # The parameters of the job in a nested format.
