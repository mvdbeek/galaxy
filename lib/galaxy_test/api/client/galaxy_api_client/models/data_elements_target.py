from dataclasses import dataclass

from .data_elements_target_destination import DataElementsTargetDestination
from .data_elements_target_elements import DataElementsTargetElements

__all__ = ["DataElementsTarget"]


@dataclass
class DataElementsTarget:
    """
    DataElementsTarget dataclass

    Args:
        destination (DataElementsTargetDestination)
                                 :
        elements (DataElementsTargetElements)
                                 :
        auto_decompress (bool | None)
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
    """

    destination: DataElementsTargetDestination
    elements: DataElementsTargetElements
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "auto_decompress": "auto_decompress",
            "destination": "destination",
            "elements": "elements",
        }
        key_transform_with_dump = {
            "auto_decompress": "auto_decompress",
            "destination": "destination",
            "elements": "elements",
        }
