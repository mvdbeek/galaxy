from typing import TypeAlias

__all__ = ["CreateQuotaParamsInUsers"]

CreateQuotaParamsInUsers: TypeAlias = list[str] | None
"""Alias for A list of user IDs or user emails to associate with this quota."""
