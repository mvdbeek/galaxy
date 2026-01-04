from typing import TypeAlias

__all__ = ["CreatedAt"]

CreatedAt: TypeAlias = str | None
"""Alias for Timestamp describing when the service was first deployed and available (RFC 3339 format)"""
