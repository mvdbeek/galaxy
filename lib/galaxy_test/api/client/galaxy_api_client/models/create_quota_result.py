from dataclasses import dataclass

from .quota_source_label import QuotaSourceLabel

__all__ = ["CreateQuotaResult"]


@dataclass
class CreateQuotaResult:
    """
    CreateQuotaResult dataclass.

    Args:
        id_ (str)                : The `encoded identifier` of the quota.
        message (str)            : Text message describing the result of the operation.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        url (str)                : The relative URL to get this particular Quota details
                                   from the rest API.
        quota_source_label (Optional[QuotaSourceLabel])
                                 : Quota source label
    """

    id_: str  # The `encoded identifier` of the quota.
    message: str  # Text message describing the result of the operation.
    model_class: str  # The name of the database model class.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    url: str  # The relative URL to get this particular Quota details from the rest API.
    quota_source_label: QuotaSourceLabel | None = None  # Quota source label
