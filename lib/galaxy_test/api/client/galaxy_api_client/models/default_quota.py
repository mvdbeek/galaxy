from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.default_quota_types import DefaultQuotaTypes

T = TypeVar("T", bound="DefaultQuota")


@_attrs_define
class DefaultQuota:
    """
    Attributes:
        model_class (Literal['DefaultQuotaAssociation']): The name of the database model class.
        type_ (DefaultQuotaTypes):
    """

    model_class: Literal["DefaultQuotaAssociation"]
    type_: DefaultQuotaTypes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_class = self.model_class

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_class": model_class,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_class = cast(Literal["DefaultQuotaAssociation"], d.pop("model_class"))
        if model_class != "DefaultQuotaAssociation":
            raise ValueError(f"model_class must match const 'DefaultQuotaAssociation', got '{model_class}'")

        type_ = DefaultQuotaTypes(d.pop("type"))

        default_quota = cls(
            model_class=model_class,
            type_=type_,
        )

        default_quota.additional_properties = d
        return default_quota

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
