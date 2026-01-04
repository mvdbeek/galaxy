from dataclasses import dataclass

from .extra_files_path import ExtraFilesPath
from .hash_function_name_enum import HashFunctionNameEnum

__all__ = ["DatasetHash"]


@dataclass
class DatasetHash:
    """
    DatasetHash dataclass.

    Args:
        hash_function (HashFunctionNameEnum)
                                 : Hash function names that can be used to generate
                                   checksums for files.
        hash_value (str)         : The hash value.
        id_ (str)                : Encoded ID of the dataset hash.
        model_class (str)        : The name of the database model class.
        extra_files_path (Optional[ExtraFilesPath])
                                 : The path to the extra files.
    """

    hash_function: HashFunctionNameEnum  # Hash function names that can be used to generate checksums for files.
    hash_value: str  # The hash value.
    id_: str  # Encoded ID of the dataset hash.
    model_class: str  # The name of the database model class.
    extra_files_path: ExtraFilesPath | None = None  # The path to the extra files.
