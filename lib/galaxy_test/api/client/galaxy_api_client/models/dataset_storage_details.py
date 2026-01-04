from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.badge_dict import BadgeDict
    from ..models.concrete_object_store_quota_source_details import ConcreteObjectStoreQuotaSourceDetails
    from ..models.dataset_storage_details_hashes_item import DatasetStorageDetailsHashesItem
    from ..models.dataset_storage_details_sources_item import DatasetStorageDetailsSourcesItem


T = TypeVar("T", bound="DatasetStorageDetails")


@_attrs_define
class DatasetStorageDetails:
    """
    Attributes:
        badges (list[BadgeDict]): A list of badges describing object store properties for concrete object store dataset
            is stored in.
        dataset_state (str): The model state of the supplied dataset instance.
        description (None | str): A description of how this dataset is stored.
        hashes (list[DatasetStorageDetailsHashesItem]): The file contents hashes associated with the supplied dataset
            instance.
        name (None | str): The display name of the destination ObjectStore for this dataset.
        object_store_id (None | str): The identifier of the destination ObjectStore for this dataset.
        percent_used (float | None): The percentage indicating how full the store is.
        private (bool): Indicator of whether the objectstore is marked as private.
        quota (ConcreteObjectStoreQuotaSourceDetails):
        relocatable (bool): Indicator of whether the objectstore for this dataset can be switched by this user.
        shareable (bool): Is this dataset shareable.
        sources (list[DatasetStorageDetailsSourcesItem]): The file sources associated with the supplied dataset
            instance.
    """

    badges: list[BadgeDict]
    dataset_state: str
    description: None | str
    hashes: list[DatasetStorageDetailsHashesItem]
    name: None | str
    object_store_id: None | str
    percent_used: float | None
    private: bool
    quota: ConcreteObjectStoreQuotaSourceDetails
    relocatable: bool
    shareable: bool
    sources: list[DatasetStorageDetailsSourcesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badges = []
        for badges_item_data in self.badges:
            badges_item = badges_item_data.to_dict()
            badges.append(badges_item)

        dataset_state = self.dataset_state

        description: None | str
        description = self.description

        hashes = []
        for hashes_item_data in self.hashes:
            hashes_item = hashes_item_data.to_dict()
            hashes.append(hashes_item)

        name: None | str
        name = self.name

        object_store_id: None | str
        object_store_id = self.object_store_id

        percent_used: float | None
        percent_used = self.percent_used

        private = self.private

        quota = self.quota.to_dict()

        relocatable = self.relocatable

        shareable = self.shareable

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "badges": badges,
                "dataset_state": dataset_state,
                "description": description,
                "hashes": hashes,
                "name": name,
                "object_store_id": object_store_id,
                "percent_used": percent_used,
                "private": private,
                "quota": quota,
                "relocatable": relocatable,
                "shareable": shareable,
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge_dict import BadgeDict
        from ..models.concrete_object_store_quota_source_details import ConcreteObjectStoreQuotaSourceDetails
        from ..models.dataset_storage_details_hashes_item import DatasetStorageDetailsHashesItem
        from ..models.dataset_storage_details_sources_item import DatasetStorageDetailsSourcesItem

        d = dict(src_dict)
        badges = []
        _badges = d.pop("badges")
        for badges_item_data in _badges:
            badges_item = BadgeDict.from_dict(badges_item_data)

            badges.append(badges_item)

        dataset_state = d.pop("dataset_state")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        hashes = []
        _hashes = d.pop("hashes")
        for hashes_item_data in _hashes:
            hashes_item = DatasetStorageDetailsHashesItem.from_dict(hashes_item_data)

            hashes.append(hashes_item)

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_object_store_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_store_id = _parse_object_store_id(d.pop("object_store_id"))

        def _parse_percent_used(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        percent_used = _parse_percent_used(d.pop("percent_used"))

        private = d.pop("private")

        quota = ConcreteObjectStoreQuotaSourceDetails.from_dict(d.pop("quota"))

        relocatable = d.pop("relocatable")

        shareable = d.pop("shareable")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = DatasetStorageDetailsSourcesItem.from_dict(sources_item_data)

            sources.append(sources_item)

        dataset_storage_details = cls(
            badges=badges,
            dataset_state=dataset_state,
            description=description,
            hashes=hashes,
            name=name,
            object_store_id=object_store_id,
            percent_used=percent_used,
            private=private,
            quota=quota,
            relocatable=relocatable,
            shareable=shareable,
            sources=sources,
        )

        dataset_storage_details.additional_properties = d
        return dataset_storage_details

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
