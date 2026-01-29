from dataclasses import dataclass

from .fetch_dataset_hash_hash_function import FetchDatasetHashHashFunction

__all__ = ["FetchDatasetHash"]


@dataclass
class FetchDatasetHash:
    """
    FetchDatasetHash dataclass

    Args:
        hash_function (FetchDatasetHashHashFunction)
                                 :
        hash_value (str)         :
    """

    hash_function: FetchDatasetHashHashFunction
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
