from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.default_quota_values import DefaultQuotaValues
from ..models.quota_operation import QuotaOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateQuotaParams")


@_attrs_define
class UpdateQuotaParams:
    """
    Attributes:
        amount (None | str | Unset): Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)
        default (DefaultQuotaValues | None | Unset): Whether or not this is a default quota. Valid values are ``no``,
            ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an
            error. Not passing this parameter is equivalent to passing ``no``.
        description (None | str | Unset): Detailed text description for this Quota.
        in_groups (list[str] | None | Unset): A list of group IDs or names to associate with this quota.
        in_users (list[str] | None | Unset): A list of user IDs or user emails to associate with this quota.
        name (None | str | Unset): The new name of the quota. This must be unique within a Galaxy instance.
        operation (QuotaOperation | Unset):
    """

    amount: None | str | Unset = UNSET
    default: DefaultQuotaValues | None | Unset = UNSET
    description: None | str | Unset = UNSET
    in_groups: list[str] | None | Unset = UNSET
    in_users: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    operation: QuotaOperation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        default: None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        elif isinstance(self.default, DefaultQuotaValues):
            default = self.default.value
        else:
            default = self.default

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if in_groups is not UNSET:
            field_dict["in_groups"] = in_groups
        if in_users is not UNSET:
            field_dict["in_users"] = in_users
        if name is not UNSET:
            field_dict["name"] = name
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_default(data: object) -> DefaultQuotaValues | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_type_0 = DefaultQuotaValues(data)

                return default_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DefaultQuotaValues | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _operation = d.pop("operation", UNSET)
        operation: QuotaOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = QuotaOperation(_operation)

        update_quota_params = cls(
            amount=amount,
            default=default,
            description=description,
            in_groups=in_groups,
            in_users=in_users,
            name=name,
            operation=operation,
        )

        update_quota_params.additional_properties = d
        return update_quota_params

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
