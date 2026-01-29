from typing import TypeAlias

from .anon_user_model import AnonUserModel
from .detailed_user_model import DetailedUserModel

__all__ = ["UsersShow200Response"]

UsersShow200Response: TypeAlias = DetailedUserModel | AnonUserModel
