from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["PathDataElementHashes"]

PathDataElementHashes: TypeAlias = list[FetchDatasetHash] | None
