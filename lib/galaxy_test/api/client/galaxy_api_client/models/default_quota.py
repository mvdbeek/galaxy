from dataclasses import dataclass

from .default_quota_types import DefaultQuotaTypes

__all__ = ["DefaultQuota"]


@dataclass
class DefaultQuota:
    """
    DefaultQuota dataclass.

    Args:
        model_class (str)        : The name of the database model class.
        type_ (DefaultQuotaTypes):
    """

    model_class: str  # The name of the database model class.
    type_: DefaultQuotaTypes
