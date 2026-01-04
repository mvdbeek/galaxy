from typing import TypeAlias

from .actions_item import ActionsItem

__all__ = ["Actions"]

Actions: TypeAlias = list[ActionsItem]
