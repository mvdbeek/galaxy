from dataclasses import dataclass

from .base_dir import BaseDir
from .fields import Fields
from .files import Files

__all__ = ["ToolDataField"]


@dataclass
class ToolDataField:
    """
    ToolDataField dataclass.

    Args:
        base_dir (BaseDir)       : A list of directories where the data files are stored
        fields (Fields)          :
        files (Files)            : A dictionary of file names and their size in bytes
        fingerprint (str)        : SHA1 Hash
        model_class (str)        : The name of class modelling this tool data field
        name (str)               : The name of the field
    """

    base_dir: BaseDir  # A list of directories where the data files are stored
    fields: Fields
    files: Files  # A dictionary of file names and their size in bytes
    fingerprint: str  # SHA1 Hash
    model_class: str  # The name of class modelling this tool data field
    name: str  # The name of the field
