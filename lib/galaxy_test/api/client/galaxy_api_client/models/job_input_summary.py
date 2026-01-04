from dataclasses import dataclass

__all__ = ["JobInputSummary"]


@dataclass
class JobInputSummary:
    """
    JobInputSummary dataclass.

    Args:
        has_duplicate_inputs (bool)
                                 : Job has duplicate inputs.
        has_empty_inputs (bool)  : Job has empty inputs.
    """

    has_duplicate_inputs: bool  # Job has duplicate inputs.
    has_empty_inputs: bool  # Job has empty inputs.
