from dataclasses import dataclass

from .custom_build_len_type import CustomBuildLenType

__all__ = ["CustomBuildCreationPayload"]


@dataclass
class CustomBuildCreationPayload:
    """
    CustomBuildCreationPayload dataclass.

    Args:
        len_type (CustomBuildLenType)
                                 :
        len_value (str)          : The content of the length file.
        name (str)               : The name of the custom build.
    """

    len_type: CustomBuildLenType
    len_value: str  # The content of the length file.
    name: str  # The name of the custom build.
