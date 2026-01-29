from typing import TypeAlias

__all__ = ["RefactorActionExecutionMessageStepLabel"]

RefactorActionExecutionMessageStepLabel: TypeAlias = str | None
"""Alias for Reference to the step the message refers to. $

Messages don't have to be bound to a step, but if they are they will
have a step_label and order_index included in the execution message.
These are the label and order_index before applying the refactoring,
the result of applying the action may change one or both of these.
If connections are dropped this step reference will refer to the
step with the previously connected input.
"""
