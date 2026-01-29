from dataclasses import dataclass

__all__ = ["DeleteQuotaPayload"]


@dataclass
class DeleteQuotaPayload:
    """
    DeleteQuotaPayload dataclass

    Args:
        purge (bool | None)      : Whether to also purge the Quota after deleting it.
    """

    purge: bool | None = False  # Whether to also purge the Quota after deleting it.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "purge": "purge",
        }
        key_transform_with_dump = {
            "purge": "purge",
        }
