from dataclasses import dataclass

from .user_model import UserModel

__all__ = ["UserQuota"]


@dataclass
class UserQuota:
    """
    UserQuota dataclass

    Args:
        model_class (str)        : The name of the database model class.
        user (UserModel)         : User in a transaction context.
    """

    model_class: str  # The name of the database model class.
    user: UserModel  # User in a transaction context.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "model_class": "model_class",
            "user": "user",
        }
        key_transform_with_dump = {
            "model_class": "model_class",
            "user": "user",
        }
