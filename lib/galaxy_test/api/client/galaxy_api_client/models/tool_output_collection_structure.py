from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription
    from ..models.tool_provided_metadata_dataset_collection import ToolProvidedMetadataDatasetCollection


T = TypeVar("T", bound="ToolOutputCollectionStructure")


@_attrs_define
class ToolOutputCollectionStructure:
    """
    Attributes:
        collection_type (None | str | Unset):
        collection_type_from_rules (None | str | Unset):
        collection_type_source (None | str | Unset):
        discover_datasets (list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None
            | Unset):
        structured_like (None | str | Unset):
    """

    collection_type: None | str | Unset = UNSET
    collection_type_from_rules: None | str | Unset = UNSET
    collection_type_source: None | str | Unset = UNSET
    discover_datasets: (
        list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None | Unset
    ) = UNSET
    structured_like: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        collection_type_from_rules: None | str | Unset
        if isinstance(self.collection_type_from_rules, Unset):
            collection_type_from_rules = UNSET
        else:
            collection_type_from_rules = self.collection_type_from_rules

        collection_type_source: None | str | Unset
        if isinstance(self.collection_type_source, Unset):
            collection_type_source = UNSET
        else:
            collection_type_source = self.collection_type_source

        discover_datasets: list[dict[str, Any]] | None | Unset
        if isinstance(self.discover_datasets, Unset):
            discover_datasets = UNSET
        elif isinstance(self.discover_datasets, list):
            discover_datasets = []
            for discover_datasets_type_0_item_data in self.discover_datasets:
                discover_datasets_type_0_item: dict[str, Any]
                if isinstance(discover_datasets_type_0_item_data, FilePatternDatasetCollectionDescription):
                    discover_datasets_type_0_item = discover_datasets_type_0_item_data.to_dict()
                else:
                    discover_datasets_type_0_item = discover_datasets_type_0_item_data.to_dict()

                discover_datasets.append(discover_datasets_type_0_item)

        else:
            discover_datasets = self.discover_datasets

        structured_like: None | str | Unset
        if isinstance(self.structured_like, Unset):
            structured_like = UNSET
        else:
            structured_like = self.structured_like

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if collection_type_from_rules is not UNSET:
            field_dict["collection_type_from_rules"] = collection_type_from_rules
        if collection_type_source is not UNSET:
            field_dict["collection_type_source"] = collection_type_source
        if discover_datasets is not UNSET:
            field_dict["discover_datasets"] = discover_datasets
        if structured_like is not UNSET:
            field_dict["structured_like"] = structured_like

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription
        from ..models.tool_provided_metadata_dataset_collection import ToolProvidedMetadataDatasetCollection

        d = dict(src_dict)

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_collection_type_from_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type_from_rules = _parse_collection_type_from_rules(d.pop("collection_type_from_rules", UNSET))

        def _parse_collection_type_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type_source = _parse_collection_type_source(d.pop("collection_type_source", UNSET))

        def _parse_discover_datasets(
            data: object,
        ) -> list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                discover_datasets_type_0 = []
                _discover_datasets_type_0 = data
                for discover_datasets_type_0_item_data in _discover_datasets_type_0:

                    def _parse_discover_datasets_type_0_item(
                        data: object,
                    ) -> FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            discover_datasets_type_0_item_type_0 = FilePatternDatasetCollectionDescription.from_dict(
                                data
                            )

                            return discover_datasets_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        discover_datasets_type_0_item_type_1 = ToolProvidedMetadataDatasetCollection.from_dict(data)

                        return discover_datasets_type_0_item_type_1

                    discover_datasets_type_0_item = _parse_discover_datasets_type_0_item(
                        discover_datasets_type_0_item_data
                    )

                    discover_datasets_type_0.append(discover_datasets_type_0_item)

                return discover_datasets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None | Unset,
                data,
            )

        discover_datasets = _parse_discover_datasets(d.pop("discover_datasets", UNSET))

        def _parse_structured_like(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        structured_like = _parse_structured_like(d.pop("structured_like", UNSET))

        tool_output_collection_structure = cls(
            collection_type=collection_type,
            collection_type_from_rules=collection_type_from_rules,
            collection_type_source=collection_type_source,
            discover_datasets=discover_datasets,
            structured_like=structured_like,
        )

        tool_output_collection_structure.additional_properties = d
        return tool_output_collection_structure

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
