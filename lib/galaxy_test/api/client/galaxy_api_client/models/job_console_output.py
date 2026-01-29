from dataclasses import dataclass

from .state import State
from .stderr import Stderr
from .stdout import Stdout

__all__ = ["JobConsoleOutput"]


@dataclass
class JobConsoleOutput:
    """
    JobConsoleOutput dataclass.

    Args:
        state (Optional[State])  : Current state of the job.
        stderr (Optional[Stderr]): Combined tool and job standard error streams.
        stdout (Optional[Stdout]): Combined tool and job standard output streams.
    """

    state: State | None = None  # Current state of the job.
    stderr: Stderr | None = None  # Combined tool and job standard error streams.
    stdout: Stdout | None = None  # Combined tool and job standard output streams.
