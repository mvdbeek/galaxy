from dataclasses import dataclass

from .import_tool_data_bundle_source import ImportToolDataBundleSource

__all__ = ["ImportToolDataBundle"]


@dataclass
class ImportToolDataBundle:
    """
    ImportToolDataBundle dataclass

    Args:
        source (ImportToolDataBundleSource)
                                 :
    """

    source: ImportToolDataBundleSource

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "source": "source",
        }
        key_transform_with_dump = {
            "source": "source",
        }
