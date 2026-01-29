from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["ServerDirElementHashes"]

ServerDirElementHashes: TypeAlias = list[FetchDatasetHash] | None
