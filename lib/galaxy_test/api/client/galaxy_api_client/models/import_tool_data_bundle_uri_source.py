from dataclasses import dataclass

from .import_tool_data_bundle_source_src_enum import ImportToolDataBundleSourceSrcEnum

__all__ = ["ImportToolDataBundleUriSource"]


@dataclass
class ImportToolDataBundleUriSource:
    """
    ImportToolDataBundleUriSource dataclass

    Args:
        src (ImportToolDataBundleSourceSrcEnum)
                                 : Indicates that the tool data should be resolved by a URI.
        uri (str)                : URI to fetch tool data bundle from (file:// URIs are fine
                                   because this is an admin-only operation)
    """

    src: ImportToolDataBundleSourceSrcEnum  # Indicates that the tool data should be resolved by a URI.
    uri: str  # URI to fetch tool data bundle from (file:// URIs are fine because this is an admin-only operation)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "src": "src",
            "uri": "uri",
        }
        key_transform_with_dump = {
            "src": "src",
            "uri": "uri",
        }
