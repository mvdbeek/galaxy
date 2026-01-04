from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowInput")


@_attrs_define
class WorkflowInput:
    """
    Attributes:
        label (None | str): Label of the input.
        uuid (None | str): Universal unique identifier of the input.
        value (Any | None): TODO
    """

    label: None | str
    uuid: None | str
    value: Any | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: None | str
        label = self.label

        uuid: None | str
        uuid = self.uuid

        value: Any | None
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "uuid": uuid,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        def _parse_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        def _parse_value(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        value = _parse_value(d.pop("value"))

        workflow_input = cls(
            label=label,
            uuid=uuid,
            value=value,
        )

        workflow_input.additional_properties = d
        return workflow_input

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
