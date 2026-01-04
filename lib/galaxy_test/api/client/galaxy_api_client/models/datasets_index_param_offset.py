from typing import TypeAlias

__all__ = ["DatasetsIndexParamOffset"]

DatasetsIndexParamOffset: TypeAlias = int | None
"""Alias for Starts at the beginning skip the first ( offset - 1 ) items and begin returning at the Nth item"""
