from enum import Enum, unique

__all__ = ["CreateFileLandingPayloadRequestStateItemClassEnum"]


@unique
class CreateFileLandingPayloadRequestStateItemClassEnum(str, Enum):
    """
    Discriminator enum for CreateFileLandingPayloadRequestStateItem union types.

    Args:
        File (str)               : Value for FILE
        Collection (str)         : Value for COLLECTION
    """

    FILE = "File"
    COLLECTION = "Collection"
