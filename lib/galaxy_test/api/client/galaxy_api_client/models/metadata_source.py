from typing import TypeAlias

__all__ = ["MetadataSource"]

MetadataSource: TypeAlias = str | None
"""Alias for This copies the metadata information from the tool’s input dataset to serve as default for information that cannot be detected from the output. One prominent use case is interval data with a non-standard column order that cannot be deduced from a header line, but which is known to be identical in the input and output datasets."""
