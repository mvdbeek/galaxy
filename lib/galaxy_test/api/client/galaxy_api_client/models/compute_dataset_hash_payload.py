from dataclasses import dataclass

from .extra_files_path import ExtraFilesPath
from .hash_function import HashFunction

__all__ = ["ComputeDatasetHashPayload"]


@dataclass
class ComputeDatasetHashPayload:
    """
    ComputeDatasetHashPayload dataclass.

    Args:
        extra_files_path (Optional[ExtraFilesPath])
                                 : The path to the extra files.
        hash_function (Optional[HashFunction])
                                 : Hash function name to use to compute dataset hashes.
    """

    extra_files_path: ExtraFilesPath | None = None  # The path to the extra files.
    hash_function: HashFunction | None = "MD5"  # Hash function name to use to compute dataset hashes.
