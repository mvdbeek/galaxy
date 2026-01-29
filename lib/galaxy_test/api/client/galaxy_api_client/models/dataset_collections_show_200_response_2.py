from typing import TypeAlias

from .hdca_custom import HdcaCustom
from .hdca_detailed_2 import HdcaDetailed2
from .hdca_summary import HdcaSummary

__all__ = ["DatasetCollectionsShow200Response2"]

DatasetCollectionsShow200Response2: TypeAlias = HdcaCustom | HdcaDetailed2 | HdcaSummary
