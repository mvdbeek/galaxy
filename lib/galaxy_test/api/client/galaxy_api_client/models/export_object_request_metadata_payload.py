from typing import TypeAlias

from .short_term_store_export_payload import ShortTermStoreExportPayload
from .write_store_to_payload import WriteStoreToPayload

__all__ = ["ExportObjectRequestMetadataPayload"]

ExportObjectRequestMetadataPayload: TypeAlias = WriteStoreToPayload | ShortTermStoreExportPayload
