from typing import TypeAlias

from .user_service_credentials_response import UserServiceCredentialsResponse

__all__ = ["UserServiceCredentialsListResponse"]

UserServiceCredentialsListResponse: TypeAlias = list[UserServiceCredentialsResponse]
