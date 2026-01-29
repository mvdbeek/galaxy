from typing import Any, TypeAlias

__all__ = ["AgentQueryResponseRoutingInfo"]

AgentQueryResponseRoutingInfo: TypeAlias = dict[str, Any] | None
"""Alias for Information about how the query was routed"""
