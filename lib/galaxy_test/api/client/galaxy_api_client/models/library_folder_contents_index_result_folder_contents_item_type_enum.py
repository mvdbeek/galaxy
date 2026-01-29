from enum import Enum, unique

__all__ = ["LibraryFolderContentsIndexResultFolderContentsItemTypeEnum"]


@unique
class LibraryFolderContentsIndexResultFolderContentsItemTypeEnum(str, Enum):
    """
    Discriminator enum for LibraryFolderContentsIndexResultFolderContentsItem union types.

    Args:
        file (str)               : Value for FILE
        folder (str)             : Value for FOLDER
    """

    FILE = "file"
    FOLDER = "folder"
