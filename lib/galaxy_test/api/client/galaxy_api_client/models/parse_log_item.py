from typing import TypeAlias

from .content_type_message import ContentTypeMessage
from .csv_dialect_inference_message import CsvDialectInferenceMessage
from .inferred_collection_type_log_entry import InferredCollectionTypeLogEntry
from .inferred_column_mapping import InferredColumnMapping
from .split_up_paired_data_log_entry import SplitUpPairedDataLogEntry

__all__ = ["ParseLogItem"]

ParseLogItem: TypeAlias = (
    ContentTypeMessage
    | CsvDialectInferenceMessage
    | InferredCollectionTypeLogEntry
    | InferredColumnMapping
    | SplitUpPairedDataLogEntry
)
