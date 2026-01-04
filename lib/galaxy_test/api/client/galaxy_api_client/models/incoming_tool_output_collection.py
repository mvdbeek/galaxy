from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_output_collection_structure import ToolOutputCollectionStructure


T = TypeVar("T", bound="IncomingToolOutputCollection")


@_attrs_define
class IncomingToolOutputCollection:
    """
    Attributes:
        structure (ToolOutputCollectionStructure):
        type_ (Literal['collection']):
        hidden (bool | None | Unset): If true, the output will not be shown in the history.
        label (None | str | Unset): Output label. Will be used as dataset name in history.
        name (None | str | Unset): Parameter name. Used when referencing parameter in workflows.
    """

    structure: ToolOutputCollectionStructure
    type_: Literal["collection"]
    hidden: bool | None | Unset = UNSET
    label: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structure = self.structure.to_dict()

        type_ = self.type_

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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structure": structure,
                "type": type_,
            }
        )
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_output_collection_structure import ToolOutputCollectionStructure

        d = dict(src_dict)
        structure = ToolOutputCollectionStructure.from_dict(d.pop("structure"))

        type_ = cast(Literal["collection"], d.pop("type"))
        if type_ != "collection":
            raise ValueError(f"type must match const 'collection', got '{type_}'")

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        incoming_tool_output_collection = cls(
            structure=structure,
            type_=type_,
            hidden=hidden,
            label=label,
            name=name,
        )

        incoming_tool_output_collection.additional_properties = d
        return incoming_tool_output_collection

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
