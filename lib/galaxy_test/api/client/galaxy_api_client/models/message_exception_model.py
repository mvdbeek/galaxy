from dataclasses import dataclass

__all__ = ["MessageExceptionModel"]


@dataclass
class MessageExceptionModel:
    """
    MessageExceptionModel dataclass

    Args:
        err_code (int)           :
        err_msg (str)            :
    """

    err_code: int
    err_msg: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "err_code": "err_code",
            "err_msg": "err_msg",
        }
        key_transform_with_dump = {
            "err_code": "err_code",
            "err_msg": "err_msg",
        }
