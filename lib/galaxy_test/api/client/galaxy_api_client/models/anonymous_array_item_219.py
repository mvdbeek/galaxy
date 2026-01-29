from typing import TypeAlias

from .limited_user_model import LimitedUserModel
from .user_model import UserModel

__all__ = ["AnonymousArrayItem219"]

AnonymousArrayItem219: TypeAlias = LimitedUserModel | UserModel
