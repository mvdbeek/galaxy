from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_permission_action import DatasetPermissionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDatasetPermissionsPayloadAliasB")


@_attrs_define
class UpdateDatasetPermissionsPayloadAliasB:
    """
    Attributes:
        access (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have access
            permission on the dataset.
        action (DatasetPermissionAction | None | Unset): Indicates what action should be performed on the dataset.
            Default: DatasetPermissionAction.SET_PERMISSIONS.
        manage (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have manage
            permission on the dataset.
        modify (list[str] | None | str | Unset): A list of role encoded IDs defining roles that should have modify
            permission on the dataset.
    """

    access: list[str] | None | str | Unset = UNSET
    action: DatasetPermissionAction | None | Unset = DatasetPermissionAction.SET_PERMISSIONS
    manage: list[str] | None | str | Unset = UNSET
    modify: list[str] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: list[str] | None | str | Unset
        if isinstance(self.access, Unset):
            access = UNSET
        elif isinstance(self.access, list):
            access = self.access

        else:
            access = self.access

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, DatasetPermissionAction):
            action = self.action.value
        else:
            action = self.action

        manage: list[str] | None | str | Unset
        if isinstance(self.manage, Unset):
            manage = UNSET
        elif isinstance(self.manage, list):
            manage = self.manage

        else:
            manage = self.manage

        modify: list[str] | None | str | Unset
        if isinstance(self.modify, Unset):
            modify = UNSET
        elif isinstance(self.modify, list):
            modify = self.modify

        else:
            modify = self.modify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if action is not UNSET:
            field_dict["action"] = action
        if manage is not UNSET:
            field_dict["manage"] = manage
        if modify is not UNSET:
            field_dict["modify"] = modify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_type_0 = cast(list[str], data)

                return access_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        access = _parse_access(d.pop("access", UNSET))

        def _parse_action(data: object) -> DatasetPermissionAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_0 = DatasetPermissionAction(data)

                return action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetPermissionAction | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_manage(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                manage_type_0 = cast(list[str], data)

                return manage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        manage = _parse_manage(d.pop("manage", UNSET))

        def _parse_modify(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modify_type_0 = cast(list[str], data)

                return modify_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        modify = _parse_modify(d.pop("modify", UNSET))

        update_dataset_permissions_payload_alias_b = cls(
            access=access,
            action=action,
            manage=manage,
            modify=modify,
        )

        update_dataset_permissions_payload_alias_b.additional_properties = d
        return update_dataset_permissions_payload_alias_b

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
