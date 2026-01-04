from dataclasses import dataclass

from .model_store_format import ModelStoreFormat

__all__ = ["StoreExportPayload"]


@dataclass
class StoreExportPayload:
    """
    StoreExportPayload dataclass.

    Args:
        include_deleted (Optional[bool])
                                 : Include file contents for deleted datasets (if
                                   include_files is True).
        include_files (Optional[bool])
                                 : include materialized files in export when available
        include_hidden (Optional[bool])
                                 : Include file contents for hidden datasets (if
                                   include_files is True).
        model_store_format (Optional[ModelStoreFormat])
                                 :
    """

    include_deleted: bool | None = False  # Include file contents for deleted datasets (if include_files is True).
    include_files: bool | None = True  # include materialized files in export when available
    include_hidden: bool | None = False  # Include file contents for hidden datasets (if include_files is True).
    model_store_format: ModelStoreFormat | None = None
