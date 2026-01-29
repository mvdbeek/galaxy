from dataclasses import dataclass

__all__ = ["InputReferenceByLabel"]


@dataclass
class InputReferenceByLabel:
    """
    InputReferenceByLabel dataclass

    Args:
        input_name (str)         : The input name as defined by the workflow module
                                   corresponding to the step being referenced. For Galaxy
                                   tool steps these inputs should be normalized using '|'
                                   (e.g. 'cond|repeat_0|input').
        label (str)              : The unique label of the step being referenced.
    """

    input_name: str  # The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').
    label: str  # The unique label of the step being referenced.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "input_name": "input_name",
            "label": "label",
        }
        key_transform_with_dump = {
            "input_name": "input_name",
            "label": "label",
        }
