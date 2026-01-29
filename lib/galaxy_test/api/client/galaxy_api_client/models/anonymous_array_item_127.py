from typing import TypeAlias

from .limited_user_model import LimitedUserModel
from .user_model import UserModel

__all__ = ["AnonymousArrayItem127"]

AnonymousArrayItem127: TypeAlias = UserModel | LimitedUserModel
