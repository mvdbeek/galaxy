from dataclasses import dataclass

from .discover_datasets import DiscoverDatasets
from .format_ import Format_
from .format_source import FormatSource
from .from_work_dir import FromWorkDir
from .hidden import Hidden
from .label import Label
from .metadata_source import MetadataSource
from .name import Name
from .precreate_directory import PrecreateDirectory

__all__ = ["IncomingToolOutputDataset"]


@dataclass
class IncomingToolOutputDataset:
    """
    IncomingToolOutputDataset dataclass.

    Args:
        type_ (str)              :
        discover_datasets (Optional[DiscoverDatasets])
                                 :
        format_ (Optional[Format_])
                                 : The short name for the output datatype.
        format_source (Optional[FormatSource])
                                 : This sets the data type of the output dataset(s) to be
                                   the same format as that of the specified tool input.
        from_work_dir (Optional[FromWorkDir])
                                 : Relative path to a file produced by the tool in its
                                   working directory. Output’s contents are set to this
                                   file’s contents.
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        label (Optional[Label])  : Label of the input.
        metadata_source (Optional[MetadataSource])
                                 : This copies the metadata information from the tool’s
                                   input dataset to serve as default for information that
                                   cannot be detected from the output. One prominent use
                                   case is interval data with a non-standard column order
                                   that cannot be deduced from a header line, but which is
                                   known to be identical in the input and output datasets.
        name (Optional[Name])    : The name of the creator.
        precreate_directory (Optional[PrecreateDirectory])
                                 :
    """

    type_: str
    discover_datasets: DiscoverDatasets | None = None
    format_: Format_ | None = None  # The short name for the output datatype.
    format_source: FormatSource | None = (
        None  # This sets the data type of the output dataset(s) to be the same format as that of the specified tool input.
    )
    from_work_dir: FromWorkDir | None = (
        None  # Relative path to a file produced by the tool in its working directory. Output’s contents are set to this file’s contents.
    )
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    label: Label | None = None  # Label of the input.
    metadata_source: MetadataSource | None = (
        None  # This copies the metadata information from the tool’s input dataset to serve as default for information that cannot be detected from the output. One prominent use case is interval data with a non-standard column order that cannot be deduced from a header line, but which is known to be identical in the input and output datasets.
    )
    name: Name | None = None  # The name of the creator.
    precreate_directory: PrecreateDirectory | None = False
