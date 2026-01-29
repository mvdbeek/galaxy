from typing import TypeAlias

from .input_reference_by_label import InputReferenceByLabel
from .input_reference_by_order_index import InputReferenceByOrderIndex

__all__ = ["Input2"]

Input2: TypeAlias = InputReferenceByOrderIndex | InputReferenceByLabel
