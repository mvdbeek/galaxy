from typing import TypeAlias

from .custom_build_model import CustomBuildModel

__all__ = ["CustomBuildsCollection"]

CustomBuildsCollection: TypeAlias = list[CustomBuildModel]
"""Alias for The custom builds associated with the user."""
