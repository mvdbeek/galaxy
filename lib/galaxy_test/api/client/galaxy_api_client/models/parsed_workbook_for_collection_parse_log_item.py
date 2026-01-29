from typing import TypeAlias

from .content_type_message import ContentTypeMessage
from .csv_dialect_inference_message import CsvDialectInferenceMessage
from .inferred_column_mapping import InferredColumnMapping

__all__ = ["ParsedWorkbookForCollectionParseLogItem"]

ParsedWorkbookForCollectionParseLogItem: TypeAlias = (
    InferredColumnMapping | ContentTypeMessage | CsvDialectInferenceMessage
)
