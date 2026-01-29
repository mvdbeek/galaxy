from dataclasses import dataclass

from .regex_job_message_code_desc import RegexJobMessageCodeDesc
from .regex_job_message_desc import RegexJobMessageDesc
from .regex_job_message_match import RegexJobMessageMatch
from .regex_job_message_stream import RegexJobMessageStream

__all__ = ["RegexJobMessage"]


@dataclass
class RegexJobMessage:
    """
    RegexJobMessage dataclass

    Args:
        desc (RegexJobMessageDesc):
        error_level (float)      :
        match (RegexJobMessageMatch)
                                 :
        stream (RegexJobMessageStream)
                                 :
        type_ (str)              : Maps from 'type'
        code_desc (RegexJobMessageCodeDesc | None)
                                 :
    """

    desc: RegexJobMessageDesc
    error_level: float
    match: RegexJobMessageMatch
    stream: RegexJobMessageStream
    type_: str  # Maps from 'type'
    code_desc: RegexJobMessageCodeDesc | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "match": "match",
            "stream": "stream",
            "type": "type_",
        }
        key_transform_with_dump = {
            "code_desc": "code_desc",
            "desc": "desc",
            "error_level": "error_level",
            "match": "match",
            "stream": "stream",
            "type_": "type",
        }
