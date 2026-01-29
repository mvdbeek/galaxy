from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .import_tool_data_bundle_dataset_source import ImportToolDataBundleDatasetSource
from .import_tool_data_bundle_uri_source import ImportToolDataBundleUriSource

__all__ = ["ImportToolDataBundleSource", "ImportToolDataBundleSourceDiscriminator"]


@dataclass(frozen=True)
class ImportToolDataBundleSourceDiscriminator:
    """Discriminator metadata for ImportToolDataBundleSource union."""

    property_name: str = "src"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("hda", "ImportToolDataBundleDatasetSource"),
        ("ldda", "ImportToolDataBundleDatasetSource"),
        ("uri", "ImportToolDataBundleUriSource"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .import_tool_data_bundle_dataset_source import ImportToolDataBundleDatasetSource
        from .import_tool_data_bundle_uri_source import ImportToolDataBundleUriSource

        return {
            "hda": ImportToolDataBundleDatasetSource,
            "ldda": ImportToolDataBundleDatasetSource,
            "uri": ImportToolDataBundleUriSource,
        }


ImportToolDataBundleSource: TypeAlias = Annotated[
    ImportToolDataBundleDatasetSource | ImportToolDataBundleUriSource, ImportToolDataBundleSourceDiscriminator()
]
