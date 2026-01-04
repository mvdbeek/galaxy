from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_source_type import CollectionSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionElementIdentifier")


@_attrs_define
class CollectionElementIdentifier:
    """
    Attributes:
        src (CollectionSourceType):
        collection_type (None | str | Unset): The type of the collection, can be `list`, `paired`, or define
            subcollections using `:` as separator like `list:paired` or `list:list`.
        element_identifiers (list[CollectionElementIdentifier] | None | Unset): List of elements that should be in the
            new sub-collection.
        id (None | str | Unset): The encoded ID of the element.
        name (None | str | Unset): The name of the element.
        tags (list[str] | None | Unset): The list of tags associated with the element.
    """

    src: CollectionSourceType
    collection_type: None | str | Unset = UNSET
    element_identifiers: list[CollectionElementIdentifier] | None | Unset = UNSET
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src.value

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        element_identifiers: list[dict[str, Any]] | None | Unset
        if isinstance(self.element_identifiers, Unset):
            element_identifiers = UNSET
        elif isinstance(self.element_identifiers, list):
            element_identifiers = []
            for element_identifiers_type_0_item_data in self.element_identifiers:
                element_identifiers_type_0_item = element_identifiers_type_0_item_data.to_dict()
                element_identifiers.append(element_identifiers_type_0_item)

        else:
            element_identifiers = self.element_identifiers

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
            }
        )
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if element_identifiers is not UNSET:
            field_dict["element_identifiers"] = element_identifiers
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = CollectionSourceType(d.pop("src"))

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_element_identifiers(data: object) -> list[CollectionElementIdentifier] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                element_identifiers_type_0 = []
                _element_identifiers_type_0 = data
                for element_identifiers_type_0_item_data in _element_identifiers_type_0:
                    element_identifiers_type_0_item = CollectionElementIdentifier.from_dict(
                        element_identifiers_type_0_item_data
                    )

                    element_identifiers_type_0.append(element_identifiers_type_0_item)

                return element_identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CollectionElementIdentifier] | None | Unset, data)

        element_identifiers = _parse_element_identifiers(d.pop("element_identifiers", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        collection_element_identifier = cls(
            src=src,
            collection_type=collection_type,
            element_identifiers=element_identifiers,
            id=id,
            name=name,
            tags=tags,
        )

        collection_element_identifier.additional_properties = d
        return collection_element_identifier

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
