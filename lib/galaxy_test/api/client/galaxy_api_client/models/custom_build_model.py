from dataclasses import dataclass

from .custom_build_model_count import CustomBuildModelCount
from .custom_build_model_fasta import CustomBuildModelFasta
from .custom_build_model_linecount import CustomBuildModelLinecount

__all__ = ["CustomBuildModel"]


@dataclass
class CustomBuildModel:
    """
    CustomBuildModel dataclass

    Args:
        id_ (str)                : The ID of the custom build. (maps from 'id')
        len_ (str)               : The primary id of the len file. (maps from 'len')
        name (str)               : The name of the custom build.
        count (CustomBuildModelCount | None)
                                 : The number of chromosomes/contigs.
        fasta (CustomBuildModelFasta | None)
                                 : The primary id of the fasta file from a history.
        linecount (CustomBuildModelLinecount | None)
                                 : The primary id of a linecount dataset.
    """

    id_: str  # The ID of the custom build. (maps from 'id')
    len_: str  # The primary id of the len file. (maps from 'len')
    name: str  # The name of the custom build.
    count: CustomBuildModelCount | None = None  # The number of chromosomes/contigs.
    fasta: CustomBuildModelFasta | None = None  # The primary id of the fasta file from a history.
    linecount: CustomBuildModelLinecount | None = None  # The primary id of a linecount dataset.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "count": "count",
            "fasta": "fasta",
            "id": "id_",
            "len": "len_",
            "linecount": "linecount",
            "name": "name",
        }
        key_transform_with_dump = {
            "count": "count",
            "fasta": "fasta",
            "id_": "id",
            "len_": "len",
            "linecount": "linecount",
            "name": "name",
        }
