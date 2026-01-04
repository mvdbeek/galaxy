from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription
    from ..models.tool_provided_metadata_dataset_collection import ToolProvidedMetadataDatasetCollection


T = TypeVar("T", bound="IncomingToolOutputDataset")


@_attrs_define
class IncomingToolOutputDataset:
    """
    Attributes:
        type_ (Literal['data']):
        discover_datasets (list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None
            | Unset):
        format_ (None | str | Unset): The short name for the output datatype.
        format_source (None | str | Unset): This sets the data type of the output dataset(s) to be the same format as
            that of the specified tool input.
        from_work_dir (None | str | Unset): Relative path to a file produced by the tool in its working directory.
            Output’s contents are set to this file’s contents.
        hidden (bool | None | Unset): If true, the output will not be shown in the history.
        label (None | str | Unset): Output label. Will be used as dataset name in history.
        metadata_source (None | str | Unset): This copies the metadata information from the tool’s input dataset to
            serve as default for information that cannot be detected from the output. One prominent use case is interval
            data with a non-standard column order that cannot be deduced from a header line, but which is known to be
            identical in the input and output datasets.
        name (None | str | Unset): Parameter name. Used when referencing parameter in workflows.
        precreate_directory (bool | None | Unset):  Default: False.
    """

    type_: Literal["data"]
    discover_datasets: (
        list[FilePatternDatasetCollectionDescription | ToolProvidedMetadataDatasetCollection] | None | Unset
    ) = UNSET
    format_: None | str | Unset = UNSET
    format_source: None | str | Unset = UNSET
    from_work_dir: None | str | Unset = UNSET
    hidden: bool | None | Unset = UNSET
    label: None | str | Unset = UNSET
    metadata_source: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    precreate_directory: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription

        type_ = self.type_

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

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        format_source: None | str | Unset
        if isinstance(self.format_source, Unset):
            format_source = UNSET
        else:
            format_source = self.format_source

        from_work_dir: None | str | Unset
        if isinstance(self.from_work_dir, Unset):
            from_work_dir = UNSET
        else:
            from_work_dir = self.from_work_dir

        hidden: bool | None | Unset
        if isinstance(self.hidden, Unset):
            hidden = UNSET
        else:
            hidden = self.hidden

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        metadata_source: None | str | Unset
        if isinstance(self.metadata_source, Unset):
            metadata_source = UNSET
        else:
            metadata_source = self.metadata_source

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        precreate_directory: bool | None | Unset
        if isinstance(self.precreate_directory, Unset):
            precreate_directory = UNSET
        else:
            precreate_directory = self.precreate_directory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if discover_datasets is not UNSET:
            field_dict["discover_datasets"] = discover_datasets
        if format_ is not UNSET:
            field_dict["format"] = format_
        if format_source is not UNSET:
            field_dict["format_source"] = format_source
        if from_work_dir is not UNSET:
            field_dict["from_work_dir"] = from_work_dir
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if metadata_source is not UNSET:
            field_dict["metadata_source"] = metadata_source
        if name is not UNSET:
            field_dict["name"] = name
        if precreate_directory is not UNSET:
            field_dict["precreate_directory"] = precreate_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_pattern_dataset_collection_description import FilePatternDatasetCollectionDescription
        from ..models.tool_provided_metadata_dataset_collection import ToolProvidedMetadataDatasetCollection

        d = dict(src_dict)
        type_ = cast(Literal["data"], d.pop("type"))
        if type_ != "data":
            raise ValueError(f"type must match const 'data', got '{type_}'")

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

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_format_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_source = _parse_format_source(d.pop("format_source", UNSET))

        def _parse_from_work_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_work_dir = _parse_from_work_dir(d.pop("from_work_dir", UNSET))

        def _parse_hidden(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hidden = _parse_hidden(d.pop("hidden", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_metadata_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata_source = _parse_metadata_source(d.pop("metadata_source", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_precreate_directory(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        precreate_directory = _parse_precreate_directory(d.pop("precreate_directory", UNSET))

        incoming_tool_output_dataset = cls(
            type_=type_,
            discover_datasets=discover_datasets,
            format_=format_,
            format_source=format_source,
            from_work_dir=from_work_dir,
            hidden=hidden,
            label=label,
            metadata_source=metadata_source,
            name=name,
            precreate_directory=precreate_directory,
        )

        incoming_tool_output_dataset.additional_properties = d
        return incoming_tool_output_dataset

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
