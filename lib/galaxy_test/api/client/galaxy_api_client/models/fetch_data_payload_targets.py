from typing import TypeAlias

from .fetch_data_payload_targets_item import FetchDataPayloadTargetsItem

__all__ = ["FetchDataPayloadTargets"]

FetchDataPayloadTargets: TypeAlias = list[FetchDataPayloadTargetsItem]
