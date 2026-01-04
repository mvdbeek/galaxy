from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHistoryPayload")


@_attrs_define
class UpdateHistoryPayload:
    """
    Attributes:
        annotation (None | str | Unset):
        deleted (bool | None | Unset):
        genome_build (None | str | Unset):
        importable (bool | None | Unset):
        name (None | str | Unset):
        preferred_object_store_id (None | str | Unset):
        published (bool | None | Unset):
        purged (bool | None | Unset):
        tags (list[str] | None | Unset):
    """

    annotation: None | str | Unset = UNSET
    deleted: bool | None | Unset = UNSET
    genome_build: None | str | Unset = UNSET
    importable: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    preferred_object_store_id: None | str | Unset = UNSET
    published: bool | None | Unset = UNSET
    purged: bool | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        genome_build: None | str | Unset
        if isinstance(self.genome_build, Unset):
            genome_build = UNSET
        else:
            genome_build = self.genome_build

        importable: bool | None | Unset
        if isinstance(self.importable, Unset):
            importable = UNSET
        else:
            importable = self.importable

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        published: bool | None | Unset
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        purged: bool | None | Unset
        if isinstance(self.purged, Unset):
            purged = UNSET
        else:
            purged = self.purged

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if importable is not UNSET:
            field_dict["importable"] = importable
        if name is not UNSET:
            field_dict["name"] = name
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id
        if published is not UNSET:
            field_dict["published"] = published
        if purged is not UNSET:
            field_dict["purged"] = purged
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_genome_build(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genome_build = _parse_genome_build(d.pop("genome_build", UNSET))

        def _parse_importable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        importable = _parse_importable(d.pop("importable", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        def _parse_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published = _parse_published(d.pop("published", UNSET))

        def _parse_purged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        purged = _parse_purged(d.pop("purged", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        update_history_payload = cls(
            annotation=annotation,
            deleted=deleted,
            genome_build=genome_build,
            importable=importable,
            name=name,
            preferred_object_store_id=preferred_object_store_id,
            published=published,
            purged=purged,
            tags=tags,
        )

        update_history_payload.additional_properties = d
        return update_history_payload

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
