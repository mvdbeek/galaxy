from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId
from .label import Label

__all__ = ["JobOutput"]


@dataclass
class JobOutput:
    """
    JobOutput dataclass.

    Args:
        label (Optional[Label])  : Label of the input.
        value (EncodedDataItemSourceId)
                                 :
    """

    label: Label | None  # Label of the input.
    value: EncodedDataItemSourceId
