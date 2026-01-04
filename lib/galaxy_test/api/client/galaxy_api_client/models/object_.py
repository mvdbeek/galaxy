from typing import TypeAlias

from .dc_object import DcObject
from .hda_detailed import HdaDetailed
from .hda_object import HdaObject

__all__ = ["Object_"]

Object_: TypeAlias = DcObject | HdaDetailed | HdaObject | None
"""Alias for The element's specific data depending on the value of `element_type`."""
