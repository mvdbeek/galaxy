from dataclasses import dataclass

from .amount import Amount
from .default import Default
from .description import Description
from .in_groups import InGroups
from .in_users import InUsers
from .name import Name
from .quota_operation import QuotaOperation

__all__ = ["UpdateQuotaParams"]


@dataclass
class UpdateQuotaParams:
    """
    UpdateQuotaParams dataclass.

    Args:
        amount (Optional[Amount]): Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``,
                                   ``unlimited``)
        default (Optional[Default])
                                 : Whether or not this is a default quota. Valid values are
                                   ``no``, ``unregistered``, ``registered``. Calling this
                                   method with ``default="no"`` on a non-default quota will
                                   throw an error. Not passing this parameter is equivalent
                                   to passing ``no``.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        in_groups (Optional[InGroups])
                                 : A list of group IDs or names to associate with this
                                   quota.
        in_users (Optional[InUsers])
                                 : A list of user IDs or user emails to associate with this
                                   quota.
        name (Optional[Name])    : The name of the creator.
        operation (Optional[QuotaOperation])
                                 :
    """

    amount: Amount | None = None  # Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
    default: Default | None = (
        None  # Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.
    )
    description: Description | None = ""  # Detailed text description for this Quota.
    in_groups: InGroups | None = None  # A list of group IDs or names to associate with this quota.
    in_users: InUsers | None = None  # A list of user IDs or user emails to associate with this quota.
    name: Name | None = None  # The name of the creator.
    operation: QuotaOperation | None = None
