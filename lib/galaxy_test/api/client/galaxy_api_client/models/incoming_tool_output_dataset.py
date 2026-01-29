from dataclasses import dataclass

from .format__4 import Format4
from .incoming_tool_output_dataset_discover_datasets import IncomingToolOutputDatasetDiscoverDatasets
from .incoming_tool_output_dataset_format_source import IncomingToolOutputDatasetFormatSource
from .incoming_tool_output_dataset_from_work_dir import IncomingToolOutputDatasetFromWorkDir
from .incoming_tool_output_dataset_hidden import IncomingToolOutputDatasetHidden
from .incoming_tool_output_dataset_label import IncomingToolOutputDatasetLabel
from .incoming_tool_output_dataset_metadata_source import IncomingToolOutputDatasetMetadataSource
from .incoming_tool_output_dataset_name import IncomingToolOutputDatasetName
from .incoming_tool_output_dataset_precreate_directory import IncomingToolOutputDatasetPrecreateDirectory
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["IncomingToolOutputDataset"]


@dataclass
class IncomingToolOutputDataset:
    """
    IncomingToolOutputDataset dataclass

    Args:
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        discover_datasets (IncomingToolOutputDatasetDiscoverDatasets | None)
                                 :
        format_ (Format4 | None) : The short name for the output datatype. (maps from
                                   'format')
        format_source (IncomingToolOutputDatasetFormatSource | None)
                                 : This sets the data type of the output dataset(s) to be
                                   the same format as that of the specified tool input.
        from_work_dir (IncomingToolOutputDatasetFromWorkDir | None)
                                 : Relative path to a file produced by the tool in its
                                   working directory. Output’s contents are set to this
                                   file’s contents.
        hidden (IncomingToolOutputDatasetHidden | None)
                                 : If true, the output will not be shown in the history.
        label (IncomingToolOutputDatasetLabel | None)
                                 : Output label. Will be used as dataset name in history.
        metadata_source (IncomingToolOutputDatasetMetadataSource | None)
                                 : This copies the metadata information from the tool’s
                                   input dataset to serve as default for information that
                                   cannot be detected from the output. One prominent use
                                   case is interval data with a non-standard column order
                                   that cannot be deduced from a header line, but which is
                                   known to be identical in the input and output datasets.
        name (IncomingToolOutputDatasetName | None)
                                 : Parameter name. Used when referencing parameter in
                                   workflows.
        precreate_directory (IncomingToolOutputDatasetPrecreateDirectory | None)
                                 :
    """

    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    discover_datasets: IncomingToolOutputDatasetDiscoverDatasets | None = None
    format_: Format4 | None = None  # The short name for the output datatype. (maps from 'format')
    format_source: IncomingToolOutputDatasetFormatSource | None = (
        None  # This sets the data type of the output dataset(s) to be the same format as that of the specified tool input.
    )
    from_work_dir: IncomingToolOutputDatasetFromWorkDir | None = (
        None  # Relative path to a file produced by the tool in its working directory. Output’s contents are set to this file’s contents.
    )
    hidden: IncomingToolOutputDatasetHidden | None = None  # If true, the output will not be shown in the history.
    label: IncomingToolOutputDatasetLabel | None = None  # Output label. Will be used as dataset name in history.
    metadata_source: IncomingToolOutputDatasetMetadataSource | None = (
        None  # This copies the metadata information from the tool’s input dataset to serve as default for information that cannot be detected from the output. One prominent use case is interval data with a non-standard column order that cannot be deduced from a header line, but which is known to be identical in the input and output datasets.
    )
    name: IncomingToolOutputDatasetName | None = None  # Parameter name. Used when referencing parameter in workflows.
    precreate_directory: IncomingToolOutputDatasetPrecreateDirectory | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "discover_datasets": "discover_datasets",
            "format": "format_",
            "format_source": "format_source",
            "from_work_dir": "from_work_dir",
            "hidden": "hidden",
            "label": "label",
            "metadata_source": "metadata_source",
            "name": "name",
            "precreate_directory": "precreate_directory",
            "type": "type_",
        }
        key_transform_with_dump = {
            "discover_datasets": "discover_datasets",
            "format_": "format",
            "format_source": "format_source",
            "from_work_dir": "from_work_dir",
            "hidden": "hidden",
            "label": "label",
            "metadata_source": "metadata_source",
            "name": "name",
            "precreate_directory": "precreate_directory",
            "type_": "type",
        }
