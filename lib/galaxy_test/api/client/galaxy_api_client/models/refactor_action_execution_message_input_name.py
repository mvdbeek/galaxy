from typing import TypeAlias

__all__ = ["RefactorActionExecutionMessageInputName"]

RefactorActionExecutionMessageInputName: TypeAlias = str | None
"""Alias for If this message is about an input to a step,
this field describes the target input name. $The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input')."""
