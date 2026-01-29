from dataclasses import dataclass

from .exit_code_job_message_code_desc import ExitCodeJobMessageCodeDesc
from .exit_code_job_message_desc import ExitCodeJobMessageDesc

__all__ = ["ExitCodeJobMessage"]


@dataclass
class ExitCodeJobMessage:
    """
    ExitCodeJobMessage dataclass

    Args:
        desc (ExitCodeJobMessageDesc)
                                 :
        error_level (float)      :
        exit_code (int)          :
        type_ (str)              : Maps from 'type'
        code_desc (ExitCodeJobMessageCodeDesc | None)
                                 :
    """

    desc: ExitCodeJobMessageDesc
    error_level: float
    exit_code: int
    type_: str  # Maps from 'type'
    code_desc: ExitCodeJobMessageCodeDesc | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "exit_code": "exit_code",
            "type": "type_",
        }
        key_transform_with_dump = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "exit_code": "exit_code",
            "type_": "type",
        }
