from typing import TypeAlias

from .input_reference_by_label import InputReferenceByLabel
from .input_reference_by_order_index import InputReferenceByOrderIndex

__all__ = ["Input3"]

Input3: TypeAlias = InputReferenceByOrderIndex | InputReferenceByLabel
