from typing import TypeAlias

__all__ = ["ExitCode"]

ExitCode: TypeAlias = int | None
"""Alias for The exit code returned by the tool. Can be unset if the job is not completed yet."""
