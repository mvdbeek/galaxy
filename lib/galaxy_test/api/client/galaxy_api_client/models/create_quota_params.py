from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.default_quota_values import DefaultQuotaValues
from ..models.quota_operation import QuotaOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateQuotaParams")


@_attrs_define
class CreateQuotaParams:
    """
    Attributes:
        amount (str): Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
        description (str): Detailed text description for this Quota.
        name (str): The name of the quota. This must be unique within a Galaxy instance.
        default (DefaultQuotaValues | Unset):
        in_groups (list[str] | None | Unset): A list of group IDs or names to associate with this quota.
        in_users (list[str] | None | Unset): A list of user IDs or user emails to associate with this quota.
        operation (QuotaOperation | Unset):
        quota_source_label (None | str | Unset): If set, quota source label to apply this quota operation to. Otherwise,
            the default quota is used.
    """

    amount: str
    description: str
    name: str
    default: DefaultQuotaValues | Unset = UNSET
    in_groups: list[str] | None | Unset = UNSET
    in_users: list[str] | None | Unset = UNSET
    operation: QuotaOperation | Unset = UNSET
    quota_source_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        description = self.description

        name = self.name

        default: str | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.value

        in_groups: list[str] | None | Unset
        if isinstance(self.in_groups, Unset):
            in_groups = UNSET
        elif isinstance(self.in_groups, list):
            in_groups = self.in_groups

        else:
            in_groups = self.in_groups

        in_users: list[str] | None | Unset
        if isinstance(self.in_users, Unset):
            in_users = UNSET
        elif isinstance(self.in_users, list):
            in_users = self.in_users

        else:
            in_users = self.in_users

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        quota_source_label: None | str | Unset
        if isinstance(self.quota_source_label, Unset):
            quota_source_label = UNSET
        else:
            quota_source_label = self.quota_source_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "description": description,
                "name": name,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if in_groups is not UNSET:
            field_dict["in_groups"] = in_groups
        if in_users is not UNSET:
            field_dict["in_users"] = in_users
        if operation is not UNSET:
            field_dict["operation"] = operation
        if quota_source_label is not UNSET:
            field_dict["quota_source_label"] = quota_source_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        description = d.pop("description")

        name = d.pop("name")

        _default = d.pop("default", UNSET)
        default: DefaultQuotaValues | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = DefaultQuotaValues(_default)

        def _parse_in_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_groups_type_0 = cast(list[str], data)

                return in_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        in_groups = _parse_in_groups(d.pop("in_groups", UNSET))

        def _parse_in_users(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_users_type_0 = cast(list[str], data)

                return in_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        in_users = _parse_in_users(d.pop("in_users", UNSET))

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

        create_quota_params = cls(
            amount=amount,
            description=description,
            name=name,
            default=default,
            in_groups=in_groups,
            in_users=in_users,
            operation=operation,
            quota_source_label=quota_source_label,
        )

        create_quota_params.additional_properties = d
        return create_quota_params

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
