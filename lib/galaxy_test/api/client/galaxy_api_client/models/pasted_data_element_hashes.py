from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["PastedDataElementHashes"]

PastedDataElementHashes: TypeAlias = list[FetchDatasetHash] | None
