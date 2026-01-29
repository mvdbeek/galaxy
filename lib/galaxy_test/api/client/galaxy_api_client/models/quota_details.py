from dataclasses import dataclass, field

from .default_quota import DefaultQuota
from .group_quota import GroupQuota
from .quota_details_quota_source_label import QuotaDetailsQuotaSourceLabel
from .quota_operation import QuotaOperation
from .user_quota import UserQuota

__all__ = ["QuotaDetails"]


@dataclass
class QuotaDetails:
    """
    QuotaDetails dataclass

    Args:
        bytes_ (int)             : The amount, expressed in bytes, of this Quota. (maps from
                                   'bytes')
        description (str)        : Detailed text description for this Quota.
        display_amount (str)     : Human-readable representation of the `amount` field.
        id_ (str)                : The `encoded identifier` of the quota. (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        default (List[DefaultQuota] | None)
                                 : A list indicating which types of default user quotas, if
                                   any, are associated with this quota.
        groups (List[GroupQuota] | None)
                                 : A list of specific groups of users associated with this
                                   quota.
        operation (QuotaOperation | None)
                                 :
        quota_source_label (QuotaDetailsQuotaSourceLabel | None)
                                 : Quota source label
        users (List[UserQuota] | None)
                                 : A list of specific users associated with this quota.
    """

    bytes_: int  # The amount, expressed in bytes, of this Quota. (maps from 'bytes')
    description: str  # Detailed text description for this Quota.
    display_amount: str  # Human-readable representation of the `amount` field.
    id_: str  # The `encoded identifier` of the quota. (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    default: list[DefaultQuota] | None = field(
        default_factory=list
    )  # A list indicating which types of default user quotas, if any, are associated with this quota.
    groups: list[GroupQuota] | None = field(
        default_factory=list
    )  # A list of specific groups of users associated with this quota.
    operation: QuotaOperation | None = None
    quota_source_label: QuotaDetailsQuotaSourceLabel | None = None  # Quota source label
    users: list[UserQuota] | None = field(default_factory=list)  # A list of specific users associated with this quota.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "bytes": "bytes_",
            "default": "default",
            "description": "description",
            "display_amount": "display_amount",
            "groups": "groups",
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "operation": "operation",
            "quota_source_label": "quota_source_label",
            "users": "users",
        }
        key_transform_with_dump = {
            "bytes_": "bytes",
            "default": "default",
            "description": "description",
            "display_amount": "display_amount",
            "groups": "groups",
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "operation": "operation",
            "quota_source_label": "quota_source_label",
            "users": "users",
        }
