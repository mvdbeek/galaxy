from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.group_model import GroupModel


T = TypeVar("T", bound="GroupQuota")


@_attrs_define
class GroupQuota:
    """
    Attributes:
        group (GroupModel): User group model
        model_class (Literal['GroupQuotaAssociation']): The name of the database model class.
    """

    group: GroupModel
    model_class: Literal["GroupQuotaAssociation"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        model_class = self.model_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "model_class": model_class,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_model import GroupModel

        d = dict(src_dict)
        group = GroupModel.from_dict(d.pop("group"))

        model_class = cast(Literal["GroupQuotaAssociation"], d.pop("model_class"))
        if model_class != "GroupQuotaAssociation":
            raise ValueError(f"model_class must match const 'GroupQuotaAssociation', got '{model_class}'")

        group_quota = cls(
            group=group,
            model_class=model_class,
        )

        group_quota.additional_properties = d
        return group_quota

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
