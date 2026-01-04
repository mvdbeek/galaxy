from dataclasses import dataclass

__all__ = ["MessageExceptionModel"]


@dataclass
class MessageExceptionModel:
    """
    MessageExceptionModel dataclass.

    Args:
        err_code (int)           :
        err_msg (str)            :
    """

    err_code: int
    err_msg: str
