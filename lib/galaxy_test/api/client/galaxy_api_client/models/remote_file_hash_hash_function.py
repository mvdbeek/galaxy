from enum import Enum, unique

__all__ = ["RemoteFileHashHashFunction"]


@unique
class RemoteFileHashHashFunction(str, Enum):
    """
    RemoteFileHashHashFunction Enum

    Args:
        MD5 (str)                : Value for MD5
        SHA-1 (str)              : Value for SHA_1
        SHA-256 (str)            : Value for SHA_256
        SHA-512 (str)            : Value for SHA_512
    """

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"
