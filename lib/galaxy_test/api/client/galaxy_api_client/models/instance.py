from typing import TypeAlias

__all__ = ["Instance"]

Instance: TypeAlias = bool | None
"""Alias for True when fetching by Workflow ID, False when fetching by StoredWorkflow ID"""
