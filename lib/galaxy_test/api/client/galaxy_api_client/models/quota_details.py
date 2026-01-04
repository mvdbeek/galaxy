from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quota_operation import QuotaOperation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.default_quota import DefaultQuota
    from ..models.group_quota import GroupQuota
    from ..models.user_quota import UserQuota


T = TypeVar("T", bound="QuotaDetails")


@_attrs_define
class QuotaDetails:
    """
    Attributes:
        bytes_ (int): The amount, expressed in bytes, of this Quota.
        description (str): Detailed text description for this Quota.
        display_amount (str): Human-readable representation of the `amount` field.
        id (str): The `encoded identifier` of the quota. Example: 0123456789ABCDEF.
        model_class (Literal['Quota']): The name of the database model class.
        name (str): The name of the quota. This must be unique within a Galaxy instance.
        default (list[DefaultQuota] | Unset): A list indicating which types of default user quotas, if any, are
            associated with this quota.
        groups (list[GroupQuota] | Unset): A list of specific groups of users associated with this quota.
        operation (QuotaOperation | Unset):
        quota_source_label (None | str | Unset): Quota source label
        users (list[UserQuota] | Unset): A list of specific users associated with this quota.
    """

    bytes_: int
    description: str
    display_amount: str
    id: str
    model_class: Literal["Quota"]
    name: str
    default: list[DefaultQuota] | Unset = UNSET
    groups: list[GroupQuota] | Unset = UNSET
    operation: QuotaOperation | Unset = UNSET
    quota_source_label: None | str | Unset = UNSET
    users: list[UserQuota] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_ = self.bytes_

        description = self.description

        display_amount = self.display_amount

        id = self.id

        model_class = self.model_class

        name = self.name

        default: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = []
            for default_item_data in self.default:
                default_item = default_item_data.to_dict()
                default.append(default_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        quota_source_label: None | str | Unset
        if isinstance(self.quota_source_label, Unset):
            quota_source_label = UNSET
        else:
            quota_source_label = self.quota_source_label

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bytes": bytes_,
                "description": description,
                "display_amount": display_amount,
                "id": id,
                "model_class": model_class,
                "name": name,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if groups is not UNSET:
            field_dict["groups"] = groups
        if operation is not UNSET:
            field_dict["operation"] = operation
        if quota_source_label is not UNSET:
            field_dict["quota_source_label"] = quota_source_label
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.default_quota import DefaultQuota
        from ..models.group_quota import GroupQuota
        from ..models.user_quota import UserQuota

        d = dict(src_dict)
        bytes_ = d.pop("bytes")

        description = d.pop("description")

        display_amount = d.pop("display_amount")

        id = d.pop("id")

        model_class = cast(Literal["Quota"], d.pop("model_class"))
        if model_class != "Quota":
            raise ValueError(f"model_class must match const 'Quota', got '{model_class}'")

        name = d.pop("name")

        _default = d.pop("default", UNSET)
        default: list[DefaultQuota] | Unset = UNSET
        if _default is not UNSET:
            default = []
            for default_item_data in _default:
                default_item = DefaultQuota.from_dict(default_item_data)

                default.append(default_item)

        _groups = d.pop("groups", UNSET)
        groups: list[GroupQuota] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GroupQuota.from_dict(groups_item_data)

                groups.append(groups_item)

        _operation = d.pop("operation", UNSET)
        operation: QuotaOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = QuotaOperation(_operation)

        def _parse_quota_source_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota_source_label = _parse_quota_source_label(d.pop("quota_source_label", UNSET))

        _users = d.pop("users", UNSET)
        users: list[UserQuota] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserQuota.from_dict(users_item_data)

                users.append(users_item)

        quota_details = cls(
            bytes_=bytes_,
            description=description,
            display_amount=display_amount,
            id=id,
            model_class=model_class,
            name=name,
            default=default,
            groups=groups,
            operation=operation,
            quota_source_label=quota_source_label,
            users=users,
        )

        quota_details.additional_properties = d
        return quota_details

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
