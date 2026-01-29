from typing import TypeAlias

from .fetch_dataset_hash import FetchDatasetHash

__all__ = ["FtpImportElementHashes"]

FtpImportElementHashes: TypeAlias = list[FetchDatasetHash] | None
