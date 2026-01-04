from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationOutputCollection")


@_attrs_define
class InvocationOutputCollection:
    """
    Attributes:
        src (Literal['hdca']): Source model of the output dataset collection.
        workflow_step_id (str): The encoded ID of the workflow step associated with the dataset/dataset collection.
            Example: 0123456789ABCDEF.
        id (None | str | Unset): The encoded ID of the dataset/dataset collection.
    """

    src: Literal["hdca"]
    workflow_step_id: str
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src = self.src

        workflow_step_id = self.workflow_step_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src": src,
                "workflow_step_id": workflow_step_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src = cast(Literal["hdca"], d.pop("src"))
        if src != "hdca":
            raise ValueError(f"src must match const 'hdca', got '{src}'")

        workflow_step_id = d.pop("workflow_step_id")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        invocation_output_collection = cls(
            src=src,
            workflow_step_id=workflow_step_id,
            id=id,
        )

        invocation_output_collection.additional_properties = d
        return invocation_output_collection

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
