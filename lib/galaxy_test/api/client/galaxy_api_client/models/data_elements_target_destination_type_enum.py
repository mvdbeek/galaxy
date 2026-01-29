from enum import Enum, unique

__all__ = ["DataElementsTargetDestinationTypeEnum"]


@unique
class DataElementsTargetDestinationTypeEnum(str, Enum):
    """
    Discriminator enum for DataElementsTargetDestination union types.

    Args:
        hdas (str)               : Value for HDAS
        library_folder (str)     : Value for LIBRARY_FOLDER
        library (str)            : Value for LIBRARY
    """

    HDAS = "hdas"
    LIBRARY_FOLDER = "library_folder"
    LIBRARY = "library"
