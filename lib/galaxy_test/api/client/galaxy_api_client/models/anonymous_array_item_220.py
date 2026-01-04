from typing import TypeAlias

from .limited_user_model import LimitedUserModel
from .user_model import UserModel

__all__ = ["AnonymousArrayItem220"]

AnonymousArrayItem220: TypeAlias = LimitedUserModel | UserModel
