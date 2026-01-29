from dataclasses import dataclass

from .src import Src

__all__ = ["ImportToolDataBundleDatasetSource"]


@dataclass
class ImportToolDataBundleDatasetSource:
    """
    ImportToolDataBundleDatasetSource dataclass.

    Args:
        id_ (str)                :
        src (Src)                : Source type of the input dataset/dataset collection.
    """

    id_: str
    src: Src  # Source type of the input dataset/dataset collection.
