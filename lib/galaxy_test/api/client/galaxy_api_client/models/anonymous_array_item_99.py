from typing import TypeAlias

from .exit_code_job_message import ExitCodeJobMessage
from .max_discovered_files_job_message import MaxDiscoveredFilesJobMessage
from .regex_job_message import RegexJobMessage

__all__ = ["AnonymousArrayItem99"]

AnonymousArrayItem99: TypeAlias = ExitCodeJobMessage | MaxDiscoveredFilesJobMessage | RegexJobMessage
