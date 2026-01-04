from typing import TypeAlias

__all__ = ["DatasetsShowParamOffset"]

DatasetsShowParamOffset: TypeAlias = int | None
"""Alias for Starts at the beginning skip the first ( offset - 1 ) items and begin returning at the Nth item. Currently only applies to `data_type=raw_data` requests"""
