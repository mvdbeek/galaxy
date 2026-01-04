from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_source_transform import DatasetSourceTransform


T = TypeVar("T", bound="DatasetSource")


@_attrs_define
class DatasetSource:
    """
    Attributes:
        id (str): Encoded ID of the dataset source. Example: 0123456789ABCDEF.
        source_uri (str): The URI of the dataset source.
        extra_files_path (None | str | Unset): The path to the extra files.
        transform (list[DatasetSourceTransform] | None | Unset): The transformations applied to the dataset source.
    """

    id: str
    source_uri: str
    extra_files_path: None | str | Unset = UNSET
    transform: list[DatasetSourceTransform] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source_uri = self.source_uri

        extra_files_path: None | str | Unset
        if isinstance(self.extra_files_path, Unset):
            extra_files_path = UNSET
        else:
            extra_files_path = self.extra_files_path

        transform: list[dict[str, Any]] | None | Unset
        if isinstance(self.transform, Unset):
            transform = UNSET
        elif isinstance(self.transform, list):
            transform = []
            for transform_type_0_item_data in self.transform:
                transform_type_0_item = transform_type_0_item_data.to_dict()
                transform.append(transform_type_0_item)

        else:
            transform = self.transform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source_uri": source_uri,
            }
        )
        if extra_files_path is not UNSET:
            field_dict["extra_files_path"] = extra_files_path
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_source_transform import DatasetSourceTransform

        d = dict(src_dict)
        id = d.pop("id")

        source_uri = d.pop("source_uri")

        def _parse_extra_files_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra_files_path = _parse_extra_files_path(d.pop("extra_files_path", UNSET))

        def _parse_transform(data: object) -> list[DatasetSourceTransform] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transform_type_0 = []
                _transform_type_0 = data
                for transform_type_0_item_data in _transform_type_0:
                    transform_type_0_item = DatasetSourceTransform.from_dict(transform_type_0_item_data)

                    transform_type_0.append(transform_type_0_item)

                return transform_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatasetSourceTransform] | None | Unset, data)

        transform = _parse_transform(d.pop("transform", UNSET))

        dataset_source = cls(
            id=id,
            source_uri=source_uri,
            extra_files_path=extra_files_path,
            transform=transform,
        )

        dataset_source.additional_properties = d
        return dataset_source

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
