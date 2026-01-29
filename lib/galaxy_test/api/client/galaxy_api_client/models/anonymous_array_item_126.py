from typing import TypeAlias

from .limited_user_model import LimitedUserModel
from .user_model import UserModel

__all__ = ["AnonymousArrayItem126"]

AnonymousArrayItem126: TypeAlias = UserModel | LimitedUserModel
