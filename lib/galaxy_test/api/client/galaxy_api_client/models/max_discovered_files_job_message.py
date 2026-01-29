from dataclasses import dataclass

from .max_discovered_files_job_message_code_desc import MaxDiscoveredFilesJobMessageCodeDesc
from .max_discovered_files_job_message_desc import MaxDiscoveredFilesJobMessageDesc

__all__ = ["MaxDiscoveredFilesJobMessage"]


@dataclass
class MaxDiscoveredFilesJobMessage:
    """
    MaxDiscoveredFilesJobMessage dataclass

    Args:
        desc (MaxDiscoveredFilesJobMessageDesc)
                                 :
        error_level (float)      :
        type_ (str)              : Maps from 'type'
        code_desc (MaxDiscoveredFilesJobMessageCodeDesc | None)
                                 :
    """

    desc: MaxDiscoveredFilesJobMessageDesc
    error_level: float
    type_: str  # Maps from 'type'
    code_desc: MaxDiscoveredFilesJobMessageCodeDesc | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "type": "type_",
        }
        key_transform_with_dump = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "type_": "type",
        }
