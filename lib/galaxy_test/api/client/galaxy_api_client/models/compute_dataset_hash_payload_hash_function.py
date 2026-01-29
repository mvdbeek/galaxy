from typing import TypeAlias

from .hash_function_name_enum import HashFunctionNameEnum

__all__ = ["ComputeDatasetHashPayloadHashFunction"]

ComputeDatasetHashPayloadHashFunction: TypeAlias = HashFunctionNameEnum | None
"""Alias for Hash function name to use to compute dataset hashes."""
