from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dce_type import DCEType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dc_object import DCObject
    from ..models.hda_detailed import HDADetailed
    from ..models.hda_object import HDAObject


T = TypeVar("T", bound="DCESummary")


@_attrs_define
class DCESummary:
    """Dataset Collection Element summary information.

    Attributes:
        element_identifier (str): The actual name of this element.
        element_index (int): The position index of this element inside the collection.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['DatasetCollectionElement']): The name of the database model class.
        columns (list[bool | float | int | None | str] | None | Unset): A row (or list of columns) of data associated
            with this element
        element_type (DCEType | None | Unset): The type of the element. Used to interpret the `object` field.
        object_ (DCObject | HDADetailed | HDAObject | None | Unset): The element's specific data depending on the value
            of `element_type`.
    """

    element_identifier: str
    element_index: int
    id: str
    model_class: Literal["DatasetCollectionElement"]
    columns: list[bool | float | int | None | str] | None | Unset = UNSET
    element_type: DCEType | None | Unset = UNSET
    object_: DCObject | HDADetailed | HDAObject | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dc_object import DCObject
        from ..models.hda_detailed import HDADetailed
        from ..models.hda_object import HDAObject

        element_identifier = self.element_identifier

        element_index = self.element_index

        id = self.id

        model_class = self.model_class

        columns: list[bool | float | int | None | str] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = []
            for columns_type_0_item_data in self.columns:
                columns_type_0_item: bool | float | int | None | str
                columns_type_0_item = columns_type_0_item_data
                columns.append(columns_type_0_item)

        else:
            columns = self.columns

        element_type: None | str | Unset
        if isinstance(self.element_type, Unset):
            element_type = UNSET
        elif isinstance(self.element_type, DCEType):
            element_type = self.element_type.value
        else:
            element_type = self.element_type

        object_: dict[str, Any] | None | Unset
        if isinstance(self.object_, Unset):
            object_ = UNSET
        elif isinstance(self.object_, HDAObject):
            object_ = self.object_.to_dict()
        elif isinstance(self.object_, HDADetailed):
            object_ = self.object_.to_dict()
        elif isinstance(self.object_, DCObject):
            object_ = self.object_.to_dict()
        else:
            object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_identifier": element_identifier,
                "element_index": element_index,
                "id": id,
                "model_class": model_class,
            }
        )
        if columns is not UNSET:
            field_dict["columns"] = columns
        if element_type is not UNSET:
            field_dict["element_type"] = element_type
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dc_object import DCObject
        from ..models.hda_detailed import HDADetailed
        from ..models.hda_object import HDAObject

        d = dict(src_dict)
        element_identifier = d.pop("element_identifier")

        element_index = d.pop("element_index")

        id = d.pop("id")

        model_class = cast(Literal["DatasetCollectionElement"], d.pop("model_class"))
        if model_class != "DatasetCollectionElement":
            raise ValueError(f"model_class must match const 'DatasetCollectionElement', got '{model_class}'")

        def _parse_columns(data: object) -> list[bool | float | int | None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = []
                _columns_type_0 = data
                for columns_type_0_item_data in _columns_type_0:

                    def _parse_columns_type_0_item(data: object) -> bool | float | int | None | str:
                        if data is None:
                            return data
                        return cast(bool | float | int | None | str, data)

                    columns_type_0_item = _parse_columns_type_0_item(columns_type_0_item_data)

                    columns_type_0.append(columns_type_0_item)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool | float | int | None | str] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_element_type(data: object) -> DCEType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                element_type_type_0 = DCEType(data)

                return element_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DCEType | None | Unset, data)

        element_type = _parse_element_type(d.pop("element_type", UNSET))

        def _parse_object_(data: object) -> DCObject | HDADetailed | HDAObject | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_0 = HDAObject.from_dict(data)

                return object_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_1 = HDADetailed.from_dict(data)

                return object_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_type_2 = DCObject.from_dict(data)

                return object_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DCObject | HDADetailed | HDAObject | None | Unset, data)

        object_ = _parse_object_(d.pop("object", UNSET))

        dce_summary = cls(
            element_identifier=element_identifier,
            element_index=element_index,
            id=id,
            model_class=model_class,
            columns=columns,
            element_type=element_type,
            object_=object_,
        )

        dce_summary.additional_properties = d
        return dce_summary

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
