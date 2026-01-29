from dataclasses import dataclass

from .tool_data_field_fields import ToolDataFieldFields
from .tool_data_field_files import ToolDataFieldFiles

__all__ = ["ToolDataField"]


@dataclass
class ToolDataField:
    """
    ToolDataField dataclass

    Args:
        base_dir (List[str])     : A list of directories where the data files are stored
        fields (ToolDataFieldFields)
                                 :
        files (ToolDataFieldFiles): A dictionary of file names and their size in bytes
        fingerprint (str)        : SHA1 Hash
        model_class (str)        : The name of class modelling this tool data field
        name (str)               : The name of the field
    """

    base_dir: list[str]  # A list of directories where the data files are stored
    fields: ToolDataFieldFields
    files: ToolDataFieldFiles  # A dictionary of file names and their size in bytes
    fingerprint: str  # SHA1 Hash
    model_class: str  # The name of class modelling this tool data field
    name: str  # The name of the field

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "base_dir": "base_dir",
            "fields": "fields",
            "files": "files",
            "fingerprint": "fingerprint",
            "model_class": "model_class",
            "name": "name",
        }
        key_transform_with_dump = {
            "base_dir": "base_dir",
            "fields": "fields",
            "files": "files",
            "fingerprint": "fingerprint",
            "model_class": "model_class",
            "name": "name",
        }
