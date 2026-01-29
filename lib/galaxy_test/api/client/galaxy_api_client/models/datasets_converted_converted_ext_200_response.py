from typing import TypeAlias

from .hda_custom_2 import HdaCustom2
from .hda_detailed_2 import HdaDetailed2
from .hda_inaccessible_2 import HdaInaccessible2
from .hda_summary_2 import HdaSummary2

__all__ = ["DatasetsConvertedConvertedExt200Response"]

DatasetsConvertedConvertedExt200Response: TypeAlias = HdaCustom2 | HdaDetailed2 | HdaSummary2 | HdaInaccessible2
