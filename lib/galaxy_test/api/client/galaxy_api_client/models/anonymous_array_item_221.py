from typing import TypeAlias

from .limited_user_model import LimitedUserModel
from .user_model import UserModel

__all__ = ["AnonymousArrayItem221"]

AnonymousArrayItem221: TypeAlias = LimitedUserModel | UserModel
