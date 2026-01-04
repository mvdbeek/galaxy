from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collection_element_data_request_uri import CollectionElementDataRequestUri


T = TypeVar("T", bound="CollectionElementCollectionRequestUri")


@_attrs_define
class CollectionElementCollectionRequestUri:
    """
    Attributes:
        class_ (Literal['Collection']):
        collection_type (str):
        elements (list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]):
        identifier (str): A unique identifier for this element within the collection.
    """

    class_: Literal["Collection"]
    collection_type: str
    elements: list[CollectionElementCollectionRequestUri | CollectionElementDataRequestUri]
    identifier: str

    def to_dict(self) -> dict[str, Any]:
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

        identifier = self.identifier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "class": class_,
                "collection_type": collection_type,
                "elements": elements,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        identifier = d.pop("identifier")

        collection_element_collection_request_uri = cls(
            class_=class_,
            collection_type=collection_type,
            elements=elements,
            identifier=identifier,
        )

        return collection_element_collection_request_uri
