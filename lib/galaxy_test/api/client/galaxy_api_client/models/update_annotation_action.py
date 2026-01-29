from dataclasses import dataclass

__all__ = ["UpdateAnnotationAction"]


@dataclass
class UpdateAnnotationAction:
    """
    UpdateAnnotationAction dataclass.

    Args:
        action_type (str)        :
        annotation (str)         :
    """

    action_type: str
    annotation: str
