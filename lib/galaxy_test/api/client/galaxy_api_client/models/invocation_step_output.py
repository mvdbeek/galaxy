from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvocationStepOutput")


@_attrs_define
class InvocationStepOutput:
    """
    Attributes:
        id (str): Dataset ID of the workflow step output. Example: 0123456789ABCDEF.
        src (Literal['hda'] | Unset): The source model of the output. Default: 'hda'.
        uuid (None | str | Unset): Universal unique identifier of the workflow step output dataset.
    """

    id: str
    src: Literal["hda"] | Unset = "hda"
    uuid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        src = self.src

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if src is not UNSET:
            field_dict["src"] = src
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        src = cast(Literal["hda"] | Unset, d.pop("src", UNSET))
        if src != "hda" and not isinstance(src, Unset):
            raise ValueError(f"src must match const 'hda', got '{src}'")

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        invocation_step_output = cls(
            id=id,
            src=src,
            uuid=uuid,
        )

        invocation_step_output.additional_properties = d
        return invocation_step_output

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
