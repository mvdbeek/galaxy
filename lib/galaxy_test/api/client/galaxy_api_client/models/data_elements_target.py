from dataclasses import dataclass

from .destination import Destination
from .elements import Elements

__all__ = ["DataElementsTarget"]


@dataclass
class DataElementsTarget:
    """
    DataElementsTarget dataclass.

    Args:
        destination (Destination):
        elements (Elements)      :
        auto_decompress (Optional[bool])
                                 : This is a boolean value that indicates whether the
                                   dataset should be automatically decompressed if it is
                                   compressed. If set to true, Galaxy will attempt to
                                   decompress the dataset if it is compressed and it is not
                                   explicitly set to a compressed datatype.
    """

    destination: Destination
    elements: Elements
    auto_decompress: bool | None = (
        False  # This is a boolean value that indicates whether the dataset should be automatically decompressed if it is compressed. If set to true, Galaxy will attempt to decompress the dataset if it is compressed and it is not explicitly set to a compressed datatype.
    )
