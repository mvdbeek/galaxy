from typing import TypeAlias

from .request_data_type import RequestDataType

__all__ = ["DatasetsShowParamDataType"]

DatasetsShowParamDataType: TypeAlias = RequestDataType | None
"""Alias for The type of information about the dataset to be requested. Each of these values may require additional parameters in the request and may return different responses."""
