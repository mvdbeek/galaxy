from typing import TypeAlias

__all__ = ["DatasetsShowParamLimit"]

DatasetsShowParamLimit: TypeAlias = int | None
"""Alias for Maximum number of items to return. Currently only applies to `data_type=raw_data` requests"""
