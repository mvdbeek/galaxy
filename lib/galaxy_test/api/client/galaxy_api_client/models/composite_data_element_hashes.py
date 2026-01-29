from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["CompositeDataElementHashes"]

CompositeDataElementHashes: TypeAlias = list[FetchDatasetHash] | None
