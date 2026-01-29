from dataclasses import dataclass

from .dataset_source_transform_action_type import DatasetSourceTransformActionType
from .datatype_ext import DatatypeExt

__all__ = ["DatasetSourceTransform"]


@dataclass
class DatasetSourceTransform:
    """
    DatasetSourceTransform dataclass.

    Args:
        action (DatasetSourceTransformActionType)
                                 :
        datatype_ext (Optional[DatatypeExt])
                                 : If action is 'datatype_groom', this is the datatype that
                                   was used to find and run the grooming code as part of the
                                   transform action.
    """

    action: DatasetSourceTransformActionType
    datatype_ext: DatatypeExt | None = (
        None  # If action is 'datatype_groom', this is the datatype that was used to find and run the grooming code as part of the transform action.
    )
