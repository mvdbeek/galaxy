from typing import TypeAlias

__all__ = ["OutputName"]

OutputName: TypeAlias = str | None
"""Alias for If this message is about an output to a step,
this field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.
"""
