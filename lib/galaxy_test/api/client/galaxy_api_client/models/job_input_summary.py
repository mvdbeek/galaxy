from dataclasses import dataclass

__all__ = ["JobInputSummary"]


@dataclass
class JobInputSummary:
    """
    JobInputSummary dataclass

    Args:
        has_duplicate_inputs (bool)
                                 : Job has duplicate inputs.
        has_empty_inputs (bool)  : Job has empty inputs.
    """

    has_duplicate_inputs: bool  # Job has duplicate inputs.
    has_empty_inputs: bool  # Job has empty inputs.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "has_duplicate_inputs": "has_duplicate_inputs",
            "has_empty_inputs": "has_empty_inputs",
        }
        key_transform_with_dump = {
            "has_duplicate_inputs": "has_duplicate_inputs",
            "has_empty_inputs": "has_empty_inputs",
        }
