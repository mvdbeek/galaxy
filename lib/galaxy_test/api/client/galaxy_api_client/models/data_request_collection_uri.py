from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_element_collection_request_uri import CollectionElementCollectionRequestUri
    from ..models.collection_element_data_request_uri import CollectionElementDataRequestUri


T = TypeVar("T", bound="DataRequestCollectionUri")


@_attrs_define
class DataRequestCollectionUri:
    """
    Attributes:
        class_ (Literal['Collection']):
        collection_type (str):
        elements (list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]):
        deferred (bool | Unset):  Default: False.
        name (None | str | Unset):
        src (None | Unset):
    """

    class_: Literal["Collection"]
    collection_type: str
    elements: list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]
    deferred: bool | Unset = False
    name: None | str | Unset = UNSET
    src: None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.collection_element_collection_request_uri import CollectionElementCollectionRequestUri

        class_ = self.class_

        collection_type = self.collection_type

        elements = []
        for elements_item_data in self.elements:
            elements_item: dict[str, Any]
            if isinstance(elements_item_data, CollectionElementCollectionRequestUri):
                elements_item = elements_item_data.to_dict()
            else:
                elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

        deferred = self.deferred

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        src = self.src

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "class": class_,
                "collection_type": collection_type,
                "elements": elements,
            }
        )
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if name is not UNSET:
            field_dict["name"] = name
        if src is not UNSET:
            field_dict["src"] = src

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_element_collection_request_uri import CollectionElementCollectionRequestUri
        from ..models.collection_element_data_request_uri import CollectionElementDataRequestUri

        d = dict(src_dict)
        class_ = cast(Literal["Collection"], d.pop("class"))
        if class_ != "Collection":
            raise ValueError(f"class must match const 'Collection', got '{class_}'")

        collection_type = d.pop("collection_type")

        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:

            def _parse_elements_item(
                data: object,
            ) -> CollectionElementCollectionRequestUri | CollectionElementDataRequestUri:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    elements_item_type_0 = CollectionElementCollectionRequestUri.from_dict(data)

                    return elements_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                elements_item_type_1 = CollectionElementDataRequestUri.from_dict(data)

                return elements_item_type_1

            elements_item = _parse_elements_item(elements_item_data)

            elements.append(elements_item)

        deferred = d.pop("deferred", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        src = d.pop("src", UNSET)

        data_request_collection_uri = cls(
            class_=class_,
            collection_type=collection_type,
            elements=elements,
            deferred=deferred,
            name=name,
            src=src,
        )

        return data_request_collection_uri
