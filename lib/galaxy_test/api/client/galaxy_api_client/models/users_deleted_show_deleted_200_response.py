from typing import TypeAlias

from .anon_user_model import AnonUserModel
from .detailed_user_model import DetailedUserModel

__all__ = ["UsersDeletedShowDeleted200Response"]

UsersDeletedShowDeleted200Response: TypeAlias = DetailedUserModel | AnonUserModel
