from typing import TypeAlias

from .exit_code_job_message import ExitCodeJobMessage
from .max_discovered_files_job_message import MaxDiscoveredFilesJobMessage
from .regex_job_message import RegexJobMessage

__all__ = ["AnonymousArrayItem98"]

AnonymousArrayItem98: TypeAlias = ExitCodeJobMessage | MaxDiscoveredFilesJobMessage | RegexJobMessage
