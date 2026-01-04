from typing import TypeAlias

from .anon_user_model import AnonUserModel
from .detailed_user_model import DetailedUserModel

__all__ = ["UsersShow200Response2"]

UsersShow200Response2: TypeAlias = AnonUserModel | DetailedUserModel
