from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_model import UserModel


T = TypeVar("T", bound="UserQuota")


@_attrs_define
class UserQuota:
    """
    Attributes:
        model_class (Literal['UserQuotaAssociation']): The name of the database model class.
        user (UserModel): User in a transaction context.
    """

    model_class: Literal["UserQuotaAssociation"]
    user: UserModel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_class = self.model_class

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_class": model_class,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_model import UserModel

        d = dict(src_dict)
        model_class = cast(Literal["UserQuotaAssociation"], d.pop("model_class"))
        if model_class != "UserQuotaAssociation":
            raise ValueError(f"model_class must match const 'UserQuotaAssociation', got '{model_class}'")

        user = UserModel.from_dict(d.pop("user"))

        user_quota = cls(
            model_class=model_class,
            user=user,
        )

        user_quota.additional_properties = d
        return user_quota

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
