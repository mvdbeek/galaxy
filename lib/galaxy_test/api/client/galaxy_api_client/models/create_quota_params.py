from dataclasses import dataclass

from .create_quota_params_in_groups import CreateQuotaParamsInGroups
from .create_quota_params_in_users import CreateQuotaParamsInUsers
from .create_quota_params_quota_source_label import CreateQuotaParamsQuotaSourceLabel
from .default_quota_values import DefaultQuotaValues
from .quota_operation import QuotaOperation

__all__ = ["CreateQuotaParams"]


@dataclass
class CreateQuotaParams:
    """
    CreateQuotaParams dataclass

    Args:
        amount (str)             : Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``,
                                   ``unlimited``)
        description (str)        : Detailed text description for this Quota.
        name (str)               : The name of the quota. This must be unique within a
                                   Galaxy instance.
        default (DefaultQuotaValues | None)
                                 :
        in_groups (CreateQuotaParamsInGroups | None)
                                 : A list of group IDs or names to associate with this
                                   quota.
        in_users (CreateQuotaParamsInUsers | None)
                                 : A list of user IDs or user emails to associate with this
                                   quota.
        operation (QuotaOperation | None)
                                 :
        quota_source_label (CreateQuotaParamsQuotaSourceLabel | None)
                                 : If set, quota source label to apply this quota operation
                                   to. Otherwise, the default quota is used.
    """

    amount: str  # Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
    description: str  # Detailed text description for this Quota.
    name: str  # The name of the quota. This must be unique within a Galaxy instance.
    default: DefaultQuotaValues | None = None
    in_groups: CreateQuotaParamsInGroups | None = None  # A list of group IDs or names to associate with this quota.
    in_users: CreateQuotaParamsInUsers | None = None  # A list of user IDs or user emails to associate with this quota.
    operation: QuotaOperation | None = None
    quota_source_label: CreateQuotaParamsQuotaSourceLabel | None = (
        None  # If set, quota source label to apply this quota operation to. Otherwise, the default quota is used.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "amount": "amount",
            "default": "default",
            "description": "description",
            "in_groups": "in_groups",
            "in_users": "in_users",
            "name": "name",
            "operation": "operation",
            "quota_source_label": "quota_source_label",
        }
        key_transform_with_dump = {
            "amount": "amount",
            "default": "default",
            "description": "description",
            "in_groups": "in_groups",
            "in_users": "in_users",
            "name": "name",
            "operation": "operation",
            "quota_source_label": "quota_source_label",
        }
