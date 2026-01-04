from typing import TypeAlias

from .output_reference_by_label import OutputReferenceByLabel
from .output_reference_by_order_index import OutputReferenceByOrderIndex

__all__ = ["Output"]

Output: TypeAlias = OutputReferenceByLabel | OutputReferenceByOrderIndex
