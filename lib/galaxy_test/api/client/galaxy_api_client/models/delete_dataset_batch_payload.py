from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_source_id import DatasetSourceId


T = TypeVar("T", bound="DeleteDatasetBatchPayload")


@_attrs_define
class DeleteDatasetBatchPayload:
    """
    Attributes:
        datasets (list[DatasetSourceId]): The list of datasets IDs with their sources to be deleted/purged.
        purge (bool | None | Unset): Whether to permanently delete from disk the specified datasets. *Warning*: this is
            a destructive operation. Default: False.
    """

    datasets: list[DatasetSourceId]
    purge: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasets = []
        for datasets_item_data in self.datasets:
            datasets_item = datasets_item_data.to_dict()
            datasets.append(datasets_item)

        purge: bool | None | Unset
        if isinstance(self.purge, Unset):
            purge = UNSET
        else:
            purge = self.purge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasets": datasets,
            }
        )
        if purge is not UNSET:
            field_dict["purge"] = purge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_source_id import DatasetSourceId

        d = dict(src_dict)
        datasets = []
        _datasets = d.pop("datasets")
        for datasets_item_data in _datasets:
            datasets_item = DatasetSourceId.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        def _parse_purge(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        purge = _parse_purge(d.pop("purge", UNSET))

        delete_dataset_batch_payload = cls(
            datasets=datasets,
            purge=purge,
        )

        delete_dataset_batch_payload.additional_properties = d
        return delete_dataset_batch_payload

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
