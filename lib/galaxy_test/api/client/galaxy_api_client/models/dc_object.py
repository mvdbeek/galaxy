from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dce_summary import DCESummary
    from ..models.elements_states_dict import ElementsStatesDict
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition


T = TypeVar("T", bound="DCObject")


@_attrs_define
class DCObject:
    """Dataset Collection Object

    Attributes:
        collection_type (str): The type of the collection, can be `list`, `paired`, or define subcollections using `:`
            as separator like `list:paired` or `list:list`.
        elements_datatypes (list[str]): A set containing all the different element datatypes in the collection.
        elements_deleted (int): The number of elements in the collection that are marked as deleted.
        elements_states (ElementsStatesDict):
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['DatasetCollection']): The name of the database model class.
        column_definitions (list[SampleSheetColumnDefinition] | None | Unset): Column definitions for sample sheet
            collections.
        contents_url (None | str | Unset):
        element_count (int | None | Unset): The number of elements contained in the dataset collection. It may be None
            or undefined if the collection could not be populated.
        elements (list[DCESummary] | Unset): The summary information of each of the elements inside the dataset
            collection.
        populated (bool | Unset): Whether the dataset collection elements (and any subcollections elements) were
            successfully populated.
    """

    collection_type: str
    elements_datatypes: list[str]
    elements_deleted: int
    elements_states: ElementsStatesDict
    id: str
    model_class: Literal["DatasetCollection"]
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    contents_url: None | str | Unset = UNSET
    element_count: int | None | Unset = UNSET
    elements: list[DCESummary] | Unset = UNSET
    populated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_type = self.collection_type

        elements_datatypes = self.elements_datatypes

        elements_deleted = self.elements_deleted

        elements_states = self.elements_states.to_dict()

        id = self.id

        model_class = self.model_class

        column_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.column_definitions, Unset):
            column_definitions = UNSET
        elif isinstance(self.column_definitions, list):
            column_definitions = []
            for column_definitions_type_0_item_data in self.column_definitions:
                column_definitions_type_0_item = column_definitions_type_0_item_data.to_dict()
                column_definitions.append(column_definitions_type_0_item)

        else:
            column_definitions = self.column_definitions

        contents_url: None | str | Unset
        if isinstance(self.contents_url, Unset):
            contents_url = UNSET
        else:
            contents_url = self.contents_url

        element_count: int | None | Unset
        if isinstance(self.element_count, Unset):
            element_count = UNSET
        else:
            element_count = self.element_count

        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        populated = self.populated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_type": collection_type,
                "elements_datatypes": elements_datatypes,
                "elements_deleted": elements_deleted,
                "elements_states": elements_states,
                "id": id,
                "model_class": model_class,
            }
        )
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if contents_url is not UNSET:
            field_dict["contents_url"] = contents_url
        if element_count is not UNSET:
            field_dict["element_count"] = element_count
        if elements is not UNSET:
            field_dict["elements"] = elements
        if populated is not UNSET:
            field_dict["populated"] = populated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dce_summary import DCESummary
        from ..models.elements_states_dict import ElementsStatesDict
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition

        d = dict(src_dict)
        collection_type = d.pop("collection_type")

        elements_datatypes = cast(list[str], d.pop("elements_datatypes"))

        elements_deleted = d.pop("elements_deleted")

        elements_states = ElementsStatesDict.from_dict(d.pop("elements_states"))

        id = d.pop("id")

        model_class = cast(Literal["DatasetCollection"], d.pop("model_class"))
        if model_class != "DatasetCollection":
            raise ValueError(f"model_class must match const 'DatasetCollection', got '{model_class}'")

        def _parse_column_definitions(data: object) -> list[SampleSheetColumnDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                column_definitions_type_0 = []
                _column_definitions_type_0 = data
                for column_definitions_type_0_item_data in _column_definitions_type_0:
                    column_definitions_type_0_item = SampleSheetColumnDefinition.from_dict(
                        column_definitions_type_0_item_data
                    )

                    column_definitions_type_0.append(column_definitions_type_0_item)

                return column_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SampleSheetColumnDefinition] | None | Unset, data)

        column_definitions = _parse_column_definitions(d.pop("column_definitions", UNSET))

        def _parse_contents_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_url = _parse_contents_url(d.pop("contents_url", UNSET))

        def _parse_element_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        element_count = _parse_element_count(d.pop("element_count", UNSET))

        _elements = d.pop("elements", UNSET)
        elements: list[DCESummary] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = DCESummary.from_dict(elements_item_data)

                elements.append(elements_item)

        populated = d.pop("populated", UNSET)

        dc_object = cls(
            collection_type=collection_type,
            elements_datatypes=elements_datatypes,
            elements_deleted=elements_deleted,
            elements_states=elements_states,
            id=id,
            model_class=model_class,
            column_definitions=column_definitions,
            contents_url=contents_url,
            element_count=element_count,
            elements=elements,
            populated=populated,
        )

        dc_object.additional_properties = d
        return dc_object

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
