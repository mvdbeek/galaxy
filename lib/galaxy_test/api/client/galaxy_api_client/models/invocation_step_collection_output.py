from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationStepCollectionOutput")


@_attrs_define
class InvocationStepCollectionOutput:
    """
    Attributes:
        id (str): Dataset Collection ID of the workflow step output. Example: 0123456789ABCDEF.
        src (Literal['hdca'] | Unset): The source model of the output. Default: 'hdca'.
    """

    id: str
    src: Literal["hdca"] | Unset = "hdca"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        src = self.src

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if src is not UNSET:
            field_dict["src"] = src

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        src = cast(Literal["hdca"] | Unset, d.pop("src", UNSET))
        if src != "hdca" and not isinstance(src, Unset):
            raise ValueError(f"src must match const 'hdca', got '{src}'")

        invocation_step_collection_output = cls(
            id=id,
            src=src,
        )

        invocation_step_collection_output.additional_properties = d
        return invocation_step_collection_output

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
