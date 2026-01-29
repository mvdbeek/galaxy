from typing import TypeAlias

__all__ = ["InvokeWorkflowPayloadInstance"]

InvokeWorkflowPayloadInstance: TypeAlias = bool | None
"""Alias for True when fetching by Workflow ID, False when fetching by StoredWorkflow ID"""
