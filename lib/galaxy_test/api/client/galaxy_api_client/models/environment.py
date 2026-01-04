from typing import TypeAlias

__all__ = ["Environment"]

Environment: TypeAlias = str | None
"""Alias for Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced."""
