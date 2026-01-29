from typing import TypeAlias

from .hda_custom_2 import HdaCustom2
from .hda_detailed_2 import HdaDetailed2
from .hda_inaccessible_2 import HdaInaccessible2
from .hda_summary_2 import HdaSummary2
from .hdca_custom_2 import HdcaCustom2
from .hdca_detailed_2 import HdcaDetailed2
from .hdca_summary_2 import HdcaSummary2

__all__ = ["AnonymousArrayItem85"]

AnonymousArrayItem85: TypeAlias = (
    HdaCustom2 | HdaDetailed2 | HdaSummary2 | HdaInaccessible2 | HdcaCustom2 | HdcaDetailed2 | HdcaSummary2
)
