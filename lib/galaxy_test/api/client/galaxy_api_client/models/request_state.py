from typing import TypeAlias

from .request_state_item import RequestStateItem

__all__ = ["RequestState"]

RequestState: TypeAlias = list[RequestStateItem]
