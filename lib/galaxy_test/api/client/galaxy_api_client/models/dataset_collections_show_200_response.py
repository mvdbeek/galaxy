from typing import TypeAlias

from .hdca_custom_2 import HdcaCustom2
from .hdca_detailed_2 import HdcaDetailed2
from .hdca_summary_2 import HdcaSummary2

__all__ = ["DatasetCollectionsShow200Response"]

DatasetCollectionsShow200Response: TypeAlias = HdcaCustom2 | HdcaDetailed2 | HdcaSummary2
