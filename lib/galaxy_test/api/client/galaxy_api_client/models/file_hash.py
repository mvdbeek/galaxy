from dataclasses import dataclass

from .hash_function import HashFunction

__all__ = ["FileHash"]


@dataclass
class FileHash:
    """
    FileHash dataclass.

    Args:
        hash_function (HashFunction)
                                 : Hash function name to use to compute dataset hashes.
        hash_value (str)         :
    """

    hash_function: HashFunction  # Hash function name to use to compute dataset hashes.
    hash_value: str
