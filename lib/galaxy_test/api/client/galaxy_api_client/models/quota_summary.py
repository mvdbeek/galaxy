from dataclasses import dataclass

from .quota_summary_quota_source_label import QuotaSummaryQuotaSourceLabel

__all__ = ["QuotaSummary"]


@dataclass
class QuotaSummary:
    """
    Contains basic information about a Quota

    Args:
        id_ (str)                : The `encoded identifier` of the quota. (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        url (str)                : The relative URL to get this particular Quota details
                                   from the rest API.
        quota_source_label (QuotaSummaryQuotaSourceLabel | None)
                                 : Quota source label
    """

    id_: str  # The `encoded identifier` of the quota. (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    url: str  # The relative URL to get this particular Quota details from the rest API.
    quota_source_label: QuotaSummaryQuotaSourceLabel | None = None  # Quota source label

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "quota_source_label": "quota_source_label",
            "url": "url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "quota_source_label": "quota_source_label",
            "url": "url",
        }
