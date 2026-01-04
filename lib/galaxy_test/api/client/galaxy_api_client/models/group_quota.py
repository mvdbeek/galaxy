from dataclasses import dataclass

from .group_model import GroupModel

__all__ = ["GroupQuota"]


@dataclass
class GroupQuota:
    """
    GroupQuota dataclass.

    Args:
        group (GroupModel)       : User group model
        model_class (str)        : The name of the database model class.
    """

    group: GroupModel  # User group model
    model_class: str  # The name of the database model class.
