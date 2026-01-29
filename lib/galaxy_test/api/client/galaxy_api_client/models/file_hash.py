from dataclasses import dataclass

from .file_hash_hash_function import FileHashHashFunction

__all__ = ["FileHash"]


@dataclass
class FileHash:
    """
    FileHash dataclass

    Args:
        hash_function (FileHashHashFunction)
                                 :
        hash_value (str)         :
    """

    hash_function: FileHashHashFunction
    hash_value: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "hash_function": "hash_function",
            "hash_value": "hash_value",
        }
        key_transform_with_dump = {
            "hash_function": "hash_function",
            "hash_value": "hash_value",
        }
