from typing import TypeAlias

from .dataset_inheritance_chain_entry import DatasetInheritanceChainEntry

__all__ = ["DatasetInheritanceChain"]

DatasetInheritanceChain: TypeAlias = list[DatasetInheritanceChainEntry]
