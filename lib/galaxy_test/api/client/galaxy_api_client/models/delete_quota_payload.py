from dataclasses import dataclass

__all__ = ["DeleteQuotaPayload"]


@dataclass
class DeleteQuotaPayload:
    """
    DeleteQuotaPayload dataclass.

    Args:
        purge (Optional[bool])   : Whether to also purge the Quota after deleting it.
    """

    purge: bool | None = False  # Whether to also purge the Quota after deleting it.
