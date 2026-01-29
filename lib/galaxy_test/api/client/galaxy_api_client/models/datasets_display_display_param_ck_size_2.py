from typing import TypeAlias

__all__ = ["DatasetsDisplayDisplayParamCkSize2"]

DatasetsDisplayDisplayParamCkSize2: TypeAlias = int | None
"""Alias for If offset is set, this recommends 'how large' the next chunk should be. This is not respected or interpreted uniformly and should be interpreted as a very loose recommendation. Different datatypes interpret 'largeness' differently - for bam datasets this is a number of lines whereas for tabular datatypes this is interpreted as a number of bytes. """
