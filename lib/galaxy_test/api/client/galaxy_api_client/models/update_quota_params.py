from dataclasses import dataclass

from .quota_operation import QuotaOperation
from .update_quota_params_amount import UpdateQuotaParamsAmount
from .update_quota_params_default import UpdateQuotaParamsDefault
from .update_quota_params_description import UpdateQuotaParamsDescription
from .update_quota_params_in_groups import UpdateQuotaParamsInGroups
from .update_quota_params_in_users import UpdateQuotaParamsInUsers
from .update_quota_params_name import UpdateQuotaParamsName

__all__ = ["UpdateQuotaParams"]


@dataclass
class UpdateQuotaParams:
    """
    UpdateQuotaParams dataclass

    Args:
        amount (UpdateQuotaParamsAmount | None)
                                 : Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``,
                                   ``unlimited``)
        default (UpdateQuotaParamsDefault | None)
                                 : Whether or not this is a default quota. Valid values are
                                   ``no``, ``unregistered``, ``registered``. Calling this
                                   method with ``default="no"`` on a non-default quota will
                                   throw an error. Not passing this parameter is equivalent
                                   to passing ``no``.
        description (UpdateQuotaParamsDescription | None)
                                 : Detailed text description for this Quota.
        in_groups (UpdateQuotaParamsInGroups | None)
                                 : A list of group IDs or names to associate with this
                                   quota.
        in_users (UpdateQuotaParamsInUsers | None)
                                 : A list of user IDs or user emails to associate with this
                                   quota.
        name (UpdateQuotaParamsName | None)
                                 : The new name of the quota. This must be unique within a
                                   Galaxy instance.
        operation (QuotaOperation | None)
                                 :
    """

    amount: UpdateQuotaParamsAmount | None = None  # Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
    default: UpdateQuotaParamsDefault | None = (
        None  # Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.
    )
    description: UpdateQuotaParamsDescription | None = None  # Detailed text description for this Quota.
    in_groups: UpdateQuotaParamsInGroups | None = None  # A list of group IDs or names to associate with this quota.
    in_users: UpdateQuotaParamsInUsers | None = None  # A list of user IDs or user emails to associate with this quota.
    name: UpdateQuotaParamsName | None = (
        None  # The new name of the quota. This must be unique within a Galaxy instance.
    )
    operation: QuotaOperation | None = None

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
        }
        key_transform_with_dump = {
            "amount": "amount",
            "default": "default",
            "description": "description",
            "in_groups": "in_groups",
            "in_users": "in_users",
            "name": "name",
            "operation": "operation",
        }
