from dataclasses import dataclass

from .quota_model_source import QuotaModelSource

__all__ = ["QuotaModel"]


@dataclass
class QuotaModel:
    """
    QuotaModel dataclass

    Args:
        enabled (bool)           :
        source (QuotaModelSource | None)
                                 :
    """

    enabled: bool
    source: QuotaModelSource | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "enabled": "enabled",
            "source": "source",
        }
        key_transform_with_dump = {
            "enabled": "enabled",
            "source": "source",
        }
