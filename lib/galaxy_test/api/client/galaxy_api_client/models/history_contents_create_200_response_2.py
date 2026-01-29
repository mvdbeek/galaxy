from typing import TypeAlias

from .anonymous_array_item_176 import AnonymousArrayItem176
from .hda_custom import HdaCustom
from .hda_detailed import HdaDetailed
from .hda_inaccessible import HdaInaccessible
from .hda_summary import HdaSummary
from .hdca_custom import HdcaCustom
from .hdca_detailed_2 import HdcaDetailed2
from .hdca_summary import HdcaSummary

__all__ = ["HistoryContentsCreate200Response2"]

HistoryContentsCreate200Response2: TypeAlias = (
    HdaCustom
    | HdaDetailed
    | HdaInaccessible
    | HdaSummary
    | HdcaCustom
    | HdcaDetailed2
    | HdcaSummary
    | list[AnonymousArrayItem176]
)
