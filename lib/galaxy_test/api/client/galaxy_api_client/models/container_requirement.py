from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.container import Container


T = TypeVar("T", bound="ContainerRequirement")


@_attrs_define
class ContainerRequirement:
    """
    Attributes:
        container (Container):
        type_ (Literal['container']):
    """

    container: Container
    type_: Literal["container"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container = self.container.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container": container,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.container import Container

        d = dict(src_dict)
        container = Container.from_dict(d.pop("container"))

        type_ = cast(Literal["container"], d.pop("type"))
        if type_ != "container":
            raise ValueError(f"type must match const 'container', got '{type_}'")

        container_requirement = cls(
            container=container,
            type_=type_,
        )

        container_requirement.additional_properties = d
        return container_requirement

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
