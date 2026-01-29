from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["FileDataElementHashes"]

FileDataElementHashes: TypeAlias = list[FetchDatasetHash] | None
