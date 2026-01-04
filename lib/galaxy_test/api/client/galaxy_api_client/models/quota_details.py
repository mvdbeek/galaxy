from dataclasses import dataclass, field

from .default_quota import DefaultQuota
from .group_quota import GroupQuota
from .quota_operation import QuotaOperation
from .quota_source_label import QuotaSourceLabel
from .user_quota import UserQuota

__all__ = ["QuotaDetails"]


@dataclass
class QuotaDetails:
    """
    QuotaDetails dataclass.

    Args:
        bytes_ (int)             : The amount, expressed in bytes, of this Quota.
        description (str)        : Detailed text description for this Quota.
        display_amount (str)     : Human-readable representation of the `amount` field.
        id_ (str)                : The `encoded identifier` of the quota.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        default (Optional[List[DefaultQuota]])
                                 : A list indicating which types of default user quotas, if
                                   any, are associated with this quota.
        groups (Optional[List[GroupQuota]])
                                 : A list of specific groups of users associated with this
                                   quota.
        operation (Optional[QuotaOperation])
                                 :
        quota_source_label (Optional[QuotaSourceLabel])
                                 : Quota source label
        users (Optional[List[UserQuota]])
                                 : A list of specific users associated with this quota.
    """

    bytes_: int  # The amount, expressed in bytes, of this Quota.
    description: str  # Detailed text description for this Quota.
    display_amount: str  # Human-readable representation of the `amount` field.
    id_: str  # The `encoded identifier` of the quota.
    model_class: str  # The name of the database model class.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    default: list[DefaultQuota] | None = field(
        default_factory=list
    )  # A list indicating which types of default user quotas, if any, are associated with this quota.
    groups: list[GroupQuota] | None = field(
        default_factory=list
    )  # A list of specific groups of users associated with this quota.
    operation: QuotaOperation | None = None
    quota_source_label: QuotaSourceLabel | None = None  # Quota source label
    users: list[UserQuota] | None = field(default_factory=list)  # A list of specific users associated with this quota.
