from dataclasses import dataclass

from .export_object_type import ExportObjectType
from .payload import Payload
from .user_id import UserId

__all__ = ["ExportObjectRequestMetadata"]


@dataclass
class ExportObjectRequestMetadata:
    """
    ExportObjectRequestMetadata dataclass.

    Args:
        object_id (str)          :
        object_type (ExportObjectType)
                                 : Types of objects that can be exported.
        payload (Payload)        :
        user_id (Optional[UserId]): User ID of user that ran this job
    """

    object_id: str
    object_type: ExportObjectType  # Types of objects that can be exported.
    payload: Payload
    user_id: UserId | None = None  # User ID of user that ran this job
