from dataclasses import dataclass

from .custom_build_len_type import CustomBuildLenType

__all__ = ["CustomBuildCreationPayload"]


@dataclass
class CustomBuildCreationPayload:
    """
    CustomBuildCreationPayload dataclass

    Args:
        len_type (CustomBuildLenType)
                                 : Maps from 'len|type'
        len_value (str)          : The content of the length file. (maps from 'len|value')
        name (str)               : The name of the custom build.
    """

    len_type: CustomBuildLenType  # Maps from 'len|type'
    len_value: str  # The content of the length file. (maps from 'len|value')
    name: str  # The name of the custom build.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "len|type": "len_type",
            "len|value": "len_value",
            "name": "name",
        }
        key_transform_with_dump = {
            "len_type": "len|type",
            "len_value": "len|value",
            "name": "name",
        }
