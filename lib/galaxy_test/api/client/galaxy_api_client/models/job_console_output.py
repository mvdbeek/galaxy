from dataclasses import dataclass

from .job_console_output_state import JobConsoleOutputState
from .job_console_output_stderr import JobConsoleOutputStderr
from .job_console_output_stdout import JobConsoleOutputStdout

__all__ = ["JobConsoleOutput"]


@dataclass
class JobConsoleOutput:
    """
    JobConsoleOutput dataclass

    Args:
        state (JobConsoleOutputState | None)
                                 : The current job's state
        stderr (JobConsoleOutputStderr | None)
                                 : Tool STDERR from job.
        stdout (JobConsoleOutputStdout | None)
                                 : Tool STDOUT from job.
    """

    state: JobConsoleOutputState | None = None  # The current job's state
    stderr: JobConsoleOutputStderr | None = None  # Tool STDERR from job.
    stdout: JobConsoleOutputStdout | None = None  # Tool STDOUT from job.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "state": "state",
            "stderr": "stderr",
            "stdout": "stdout",
        }
        key_transform_with_dump = {
            "state": "state",
            "stderr": "stderr",
            "stdout": "stdout",
        }
