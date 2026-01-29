from typing import TypeAlias

__all__ = ["HistoryContentsShowLegacyParamFuzzyCount"]

HistoryContentsShowLegacyParamFuzzyCount: TypeAlias = int | None
"""Alias for This value can be used to broadly restrict the magnitude of the number of elements returned via the API for large collections. The number of actual elements returned may be "a bit" more than this number or "a lot" less - varying on the depth of nesting, balance of nesting at each level, and size of target collection. The consumer of this API should not expect a stable number or pre-calculable number of elements to be produced given this parameter - the only promise is that this API will not respond with an order of magnitude more elements estimated with this value. The UI uses this parameter to fetch a "balanced" concept of the "start" of large collections at every depth of the collection."""
