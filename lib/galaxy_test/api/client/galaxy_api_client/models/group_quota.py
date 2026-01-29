from dataclasses import dataclass

from .group_model import GroupModel

__all__ = ["GroupQuota"]


@dataclass
class GroupQuota:
    """
    GroupQuota dataclass

    Args:
        group (GroupModel)       : User group model
        model_class (str)        : The name of the database model class.
    """

    group: GroupModel  # User group model
    model_class: str  # The name of the database model class.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "group": "group",
            "model_class": "model_class",
        }
        key_transform_with_dump = {
            "group": "group",
            "model_class": "model_class",
        }
