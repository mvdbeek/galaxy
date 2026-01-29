from dataclasses import dataclass

from .extra_files_fuzzy_root import ExtraFilesFuzzyRoot
from .extra_files_items_from import ExtraFilesItemsFrom
from .src import Src

__all__ = ["ExtraFiles"]


@dataclass
class ExtraFiles:
    """
    ExtraFiles dataclass

    Args:
        src (Src)                :
        fuzzy_root (ExtraFilesFuzzyRoot | None)
                                 : Prevent Galaxy from checking for a single file in a
                                   directory and re-interpreting the archive
        items_from (ExtraFilesItemsFrom | None)
                                 :
    """

    src: Src
    fuzzy_root: ExtraFilesFuzzyRoot | None = (
        True  # Prevent Galaxy from checking for a single file in a directory and re-interpreting the archive
    )
    items_from: ExtraFilesItemsFrom | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "fuzzy_root": "fuzzy_root",
            "items_from": "items_from",
            "src": "src",
        }
        key_transform_with_dump = {
            "fuzzy_root": "fuzzy_root",
            "items_from": "items_from",
            "src": "src",
        }
