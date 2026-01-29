from dataclasses import dataclass

from .compute_dataset_hash_payload_extra_files_path import ComputeDatasetHashPayloadExtraFilesPath
from .compute_dataset_hash_payload_hash_function import ComputeDatasetHashPayloadHashFunction

__all__ = ["ComputeDatasetHashPayload"]


@dataclass
class ComputeDatasetHashPayload:
    """
    ComputeDatasetHashPayload dataclass

    Args:
        extra_files_path (ComputeDatasetHashPayloadExtraFilesPath | None)
                                 : If set, extra files path to compute a hash for.
        hash_function (ComputeDatasetHashPayloadHashFunction | None)
                                 : Hash function name to use to compute dataset hashes.
    """

    extra_files_path: ComputeDatasetHashPayloadExtraFilesPath | None = (
        None  # If set, extra files path to compute a hash for.
    )
    hash_function: ComputeDatasetHashPayloadHashFunction | None = (
        "MD5"  # Hash function name to use to compute dataset hashes.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "extra_files_path": "extra_files_path",
            "hash_function": "hash_function",
        }
        key_transform_with_dump = {
            "extra_files_path": "extra_files_path",
            "hash_function": "hash_function",
        }
