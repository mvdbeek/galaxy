from dataclasses import dataclass

from .data_item_source_type import DataItemSourceType
from .uuid_ import Uuid_

__all__ = ["EncodedDatasetJobInfo"]


@dataclass
class EncodedDatasetJobInfo:
    """
    EncodedDatasetJobInfo dataclass.

    Args:
        id_ (str)                :
        src (DataItemSourceType) :
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    id_: str
    src: DataItemSourceType
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
