from dataclasses import dataclass

from .default_quota_types import DefaultQuotaTypes

__all__ = ["DefaultQuota"]


@dataclass
class DefaultQuota:
    """
    DefaultQuota dataclass

    Args:
        model_class (str)        : The name of the database model class.
        type_ (DefaultQuotaTypes): Maps from 'type'
    """

    model_class: str  # The name of the database model class.
    type_: DefaultQuotaTypes  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "model_class": "model_class",
            "type": "type_",
        }
        key_transform_with_dump = {
            "model_class": "model_class",
            "type_": "type",
        }
