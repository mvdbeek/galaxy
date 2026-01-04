from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_tool_data_bundle_dataset_source import ImportToolDataBundleDatasetSource
    from ..models.import_tool_data_bundle_uri_source import ImportToolDataBundleUriSource


T = TypeVar("T", bound="ImportToolDataBundle")


@_attrs_define
class ImportToolDataBundle:
    """
    Attributes:
        source (ImportToolDataBundleDatasetSource | ImportToolDataBundleUriSource):
    """

    source: ImportToolDataBundleDatasetSource | ImportToolDataBundleUriSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_tool_data_bundle_dataset_source import ImportToolDataBundleDatasetSource

        source: dict[str, Any]
        if isinstance(self.source, ImportToolDataBundleDatasetSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_tool_data_bundle_dataset_source import ImportToolDataBundleDatasetSource
        from ..models.import_tool_data_bundle_uri_source import ImportToolDataBundleUriSource

        d = dict(src_dict)

        def _parse_source(data: object) -> ImportToolDataBundleDatasetSource | ImportToolDataBundleUriSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = ImportToolDataBundleDatasetSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_1 = ImportToolDataBundleUriSource.from_dict(data)

            return source_type_1

        source = _parse_source(d.pop("source"))

        import_tool_data_bundle = cls(
            source=source,
        )

        import_tool_data_bundle.additional_properties = d
        return import_tool_data_bundle

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
