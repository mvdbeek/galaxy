from dataclasses import dataclass

from .export_object_request_metadata_payload import ExportObjectRequestMetadataPayload
from .export_object_request_metadata_user_id import ExportObjectRequestMetadataUserId
from .export_object_type import ExportObjectType

__all__ = ["ExportObjectRequestMetadata"]


@dataclass
class ExportObjectRequestMetadata:
    """
    ExportObjectRequestMetadata dataclass

    Args:
        object_id (str)          :
        object_type (ExportObjectType)
                                 : Types of objects that can be exported.
        payload (ExportObjectRequestMetadataPayload)
                                 :
        user_id (ExportObjectRequestMetadataUserId | None)
                                 :
    """

    object_id: str
    object_type: ExportObjectType  # Types of objects that can be exported.
    payload: ExportObjectRequestMetadataPayload
    user_id: ExportObjectRequestMetadataUserId | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "object_id": "object_id",
            "object_type": "object_type",
            "payload": "payload",
            "user_id": "user_id",
        }
        key_transform_with_dump = {
            "object_id": "object_id",
            "object_type": "object_type",
            "payload": "payload",
            "user_id": "user_id",
        }
