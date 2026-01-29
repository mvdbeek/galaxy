from dataclasses import dataclass

from .dataset_hash_extra_files_path import DatasetHashExtraFilesPath
from .hash_function_name_enum import HashFunctionNameEnum

__all__ = ["DatasetHash"]


@dataclass
class DatasetHash:
    """
    DatasetHash dataclass

    Args:
        hash_function (HashFunctionNameEnum)
                                 : Hash function names that can be used to generate
                                   checksums for files.
        hash_value (str)         : The hash value.
        id_ (str)                : Encoded ID of the dataset hash. (maps from 'id')
        model_class (str)        : The name of the database model class.
        extra_files_path (DatasetHashExtraFilesPath | None)
                                 : The path to the extra files used to generate the hash.
    """

    hash_function: HashFunctionNameEnum  # Hash function names that can be used to generate checksums for files.
    hash_value: str  # The hash value.
    id_: str  # Encoded ID of the dataset hash. (maps from 'id')
    model_class: str  # The name of the database model class.
    extra_files_path: DatasetHashExtraFilesPath | None = None  # The path to the extra files used to generate the hash.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "extra_files_path": "extra_files_path",
            "hash_function": "hash_function",
            "hash_value": "hash_value",
            "id": "id_",
            "model_class": "model_class",
        }
        key_transform_with_dump = {
            "extra_files_path": "extra_files_path",
            "hash_function": "hash_function",
            "hash_value": "hash_value",
            "id_": "id",
            "model_class": "model_class",
        }
