from typing import TypeAlias

from .hda_custom import HdaCustom
from .hda_detailed import HdaDetailed
from .hda_inaccessible import HdaInaccessible
from .hda_summary import HdaSummary

__all__ = ["DatasetsConvertedConvertedExt200Response2"]

DatasetsConvertedConvertedExt200Response2: TypeAlias = HdaCustom | HdaDetailed | HdaInaccessible | HdaSummary
