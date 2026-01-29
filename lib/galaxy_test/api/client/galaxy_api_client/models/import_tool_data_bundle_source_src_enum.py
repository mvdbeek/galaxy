from enum import Enum, unique

__all__ = ["ImportToolDataBundleSourceSrcEnum"]


@unique
class ImportToolDataBundleSourceSrcEnum(str, Enum):
    """
    Discriminator enum for ImportToolDataBundleSource union types.

    Args:
        hda (str)                : Value for HDA
        ldda (str)               : Value for LDDA
        uri (str)                : Value for URI
    """

    HDA = "hda"
    LDDA = "ldda"
    URI = "uri"
