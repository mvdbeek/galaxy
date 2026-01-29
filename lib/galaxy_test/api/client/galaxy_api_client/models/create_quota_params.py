from dataclasses import dataclass

from .default_quota_values import DefaultQuotaValues
from .in_groups import InGroups
from .in_users import InUsers
from .quota_operation import QuotaOperation
from .quota_source_label import QuotaSourceLabel

__all__ = ["CreateQuotaParams"]


@dataclass
class CreateQuotaParams:
    """
    CreateQuotaParams dataclass.

    Args:
        amount (str)             : Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``,
                                   ``unlimited``)
        description (str)        : Detailed text description for this Quota.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        default (Optional[DefaultQuotaValues])
                                 :
        in_groups (Optional[InGroups])
                                 : A list of group IDs or names to associate with this
                                   quota.
        in_users (Optional[InUsers])
                                 : A list of user IDs or user emails to associate with this
                                   quota.
        operation (Optional[QuotaOperation])
                                 :
        quota_source_label (Optional[QuotaSourceLabel])
                                 : Quota source label
    """

    amount: str  # Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
    description: str  # Detailed text description for this Quota.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    default: DefaultQuotaValues | None = None
    in_groups: InGroups | None = None  # A list of group IDs or names to associate with this quota.
    in_users: InUsers | None = None  # A list of user IDs or user emails to associate with this quota.
    operation: QuotaOperation | None = None
    quota_source_label: QuotaSourceLabel | None = None  # Quota source label
