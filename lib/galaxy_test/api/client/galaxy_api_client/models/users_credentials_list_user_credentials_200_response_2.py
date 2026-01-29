from typing import TypeAlias

from .extended_user_credentials_list_response import ExtendedUserCredentialsListResponse
from .user_service_credentials_list_response import UserServiceCredentialsListResponse

__all__ = ["UsersCredentialsListUserCredentials200Response2"]

UsersCredentialsListUserCredentials200Response2: TypeAlias = (
    ExtendedUserCredentialsListResponse | UserServiceCredentialsListResponse
)
