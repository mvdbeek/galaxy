from dataclasses import dataclass

from .job_parameter_notes import JobParameterNotes
from .job_parameter_value import JobParameterValue

__all__ = ["JobParameter"]


@dataclass
class JobParameter:
    """
    JobParameter dataclass

    Args:
        depth (int)              : The depth of the job parameter.
        text (str)               : Text associated with the job parameter.
        notes (JobParameterNotes | None)
                                 : Notes associated with the job parameter.
        value (JobParameterValue | None)
                                 : The values of the job parameter
    """

    depth: int  # The depth of the job parameter.
    text: str  # Text associated with the job parameter.
    notes: JobParameterNotes | None = None  # Notes associated with the job parameter.
    value: JobParameterValue | None = None  # The values of the job parameter

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "depth": "depth",
            "notes": "notes",
            "text": "text",
            "value": "value",
        }
        key_transform_with_dump = {
            "depth": "depth",
            "notes": "notes",
            "text": "text",
            "value": "value",
        }
