from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["UrlDataElementHashes"]

UrlDataElementHashes: TypeAlias = list[FetchDatasetHash] | None
