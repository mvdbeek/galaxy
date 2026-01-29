from typing import TypeAlias

from .refactor_request_actions_item import RefactorRequestActionsItem

__all__ = ["RefactorRequestActions"]

RefactorRequestActions: TypeAlias = list[RefactorRequestActionsItem]
