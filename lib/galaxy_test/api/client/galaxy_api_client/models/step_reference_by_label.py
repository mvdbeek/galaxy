from dataclasses import dataclass

__all__ = ["StepReferenceByLabel"]


@dataclass
class StepReferenceByLabel:
    """
    StepReferenceByLabel dataclass

    Args:
        label (str)              : The unique label of the step being referenced.
    """

    label: str  # The unique label of the step being referenced.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
        }
        key_transform_with_dump = {
            "label": "label",
        }
