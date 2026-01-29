from typing import TypeAlias

from .user_quota_usage import UserQuotaUsage

__all__ = ["UsersUsageUsageFor200Response"]

UsersUsageUsageFor200Response: TypeAlias = UserQuotaUsage | None
