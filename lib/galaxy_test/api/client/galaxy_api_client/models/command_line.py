from typing import TypeAlias

__all__ = ["CommandLine"]

CommandLine: TypeAlias = str | None
"""Alias for The command line produced by the job. Users can see this value if allowed in the configuration, administrator can always see this value."""
