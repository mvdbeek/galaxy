from dataclasses import dataclass

from .create_quota_result_quota_source_label import CreateQuotaResultQuotaSourceLabel

__all__ = ["CreateQuotaResult"]


@dataclass
class CreateQuotaResult:
    """
    CreateQuotaResult dataclass

    Args:
        id_ (str)                : The `encoded identifier` of the quota. (maps from 'id')
        message (str)            : Text message describing the result of the operation.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        url (str)                : The relative URL to get this particular Quota details
                                   from the rest API.
        quota_source_label (CreateQuotaResultQuotaSourceLabel | None)
                                 : Quota source label
    """

    id_: str  # The `encoded identifier` of the quota. (maps from 'id')
    message: str  # Text message describing the result of the operation.
    model_class: str  # The name of the database model class.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    url: str  # The relative URL to get this particular Quota details from the rest API.
    quota_source_label: CreateQuotaResultQuotaSourceLabel | None = None  # Quota source label

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "message": "message",
            "model_class": "model_class",
            "name": "name",
            "quota_source_label": "quota_source_label",
            "url": "url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "message": "message",
            "model_class": "model_class",
            "name": "name",
            "quota_source_label": "quota_source_label",
            "url": "url",
        }
