from dataclasses import dataclass

from .update_history_payload_annotation import UpdateHistoryPayloadAnnotation
from .update_history_payload_deleted import UpdateHistoryPayloadDeleted
from .update_history_payload_genome_build import UpdateHistoryPayloadGenomeBuild
from .update_history_payload_importable import UpdateHistoryPayloadImportable
from .update_history_payload_name import UpdateHistoryPayloadName
from .update_history_payload_preferred_object_store_id import UpdateHistoryPayloadPreferredObjectStoreId
from .update_history_payload_published import UpdateHistoryPayloadPublished
from .update_history_payload_purged import UpdateHistoryPayloadPurged
from .update_history_payload_tags import UpdateHistoryPayloadTags

__all__ = ["UpdateHistoryPayload"]


@dataclass
class UpdateHistoryPayload:
    """
    UpdateHistoryPayload dataclass

    Args:
        annotation (UpdateHistoryPayloadAnnotation | None)
                                 :
        deleted (UpdateHistoryPayloadDeleted | None)
                                 :
        genome_build (UpdateHistoryPayloadGenomeBuild | None)
                                 :
        importable (UpdateHistoryPayloadImportable | None)
                                 :
        name (UpdateHistoryPayloadName | None)
                                 :
        preferred_object_store_id (UpdateHistoryPayloadPreferredObjectStoreId | None)
                                 :
        published (UpdateHistoryPayloadPublished | None)
                                 :
        purged (UpdateHistoryPayloadPurged | None)
                                 :
        tags (UpdateHistoryPayloadTags | None)
                                 :
    """

    annotation: UpdateHistoryPayloadAnnotation | None = None
    deleted: UpdateHistoryPayloadDeleted | None = None
    genome_build: UpdateHistoryPayloadGenomeBuild | None = None
    importable: UpdateHistoryPayloadImportable | None = None
    name: UpdateHistoryPayloadName | None = None
    preferred_object_store_id: UpdateHistoryPayloadPreferredObjectStoreId | None = None
    published: UpdateHistoryPayloadPublished | None = None
    purged: UpdateHistoryPayloadPurged | None = None
    tags: UpdateHistoryPayloadTags | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "deleted": "deleted",
            "genome_build": "genome_build",
            "importable": "importable",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "deleted": "deleted",
            "genome_build": "genome_build",
            "importable": "importable",
            "name": "name",
            "preferred_object_store_id": "preferred_object_store_id",
            "published": "published",
            "purged": "purged",
            "tags": "tags",
        }
