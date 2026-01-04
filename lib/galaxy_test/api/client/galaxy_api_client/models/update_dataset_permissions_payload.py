from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_permission_action import DatasetPermissionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDatasetPermissionsPayload")


@_attrs_define
class UpdateDatasetPermissionsPayload:
    """
    Attributes:
        access_ids (list[str] | None | str | Unset):
        action (DatasetPermissionAction | None | Unset): Indicates what action should be performed on the dataset.
            Default: DatasetPermissionAction.SET_PERMISSIONS.
        manage_ids (list[str] | None | str | Unset):
        modify_ids (list[str] | None | str | Unset):
    """

    access_ids: list[str] | None | str | Unset = UNSET
    action: DatasetPermissionAction | None | Unset = DatasetPermissionAction.SET_PERMISSIONS
    manage_ids: list[str] | None | str | Unset = UNSET
    modify_ids: list[str] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_ids: list[str] | None | str | Unset
        if isinstance(self.access_ids, Unset):
            access_ids = UNSET
        elif isinstance(self.access_ids, list):
            access_ids = self.access_ids

        else:
            access_ids = self.access_ids

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, DatasetPermissionAction):
            action = self.action.value
        else:
            action = self.action

        manage_ids: list[str] | None | str | Unset
        if isinstance(self.manage_ids, Unset):
            manage_ids = UNSET
        elif isinstance(self.manage_ids, list):
            manage_ids = self.manage_ids

        else:
            manage_ids = self.manage_ids

        modify_ids: list[str] | None | str | Unset
        if isinstance(self.modify_ids, Unset):
            modify_ids = UNSET
        elif isinstance(self.modify_ids, list):
            modify_ids = self.modify_ids

        else:
            modify_ids = self.modify_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_ids is not UNSET:
            field_dict["access_ids[]"] = access_ids
        if action is not UNSET:
            field_dict["action"] = action
        if manage_ids is not UNSET:
            field_dict["manage_ids[]"] = manage_ids
        if modify_ids is not UNSET:
            field_dict["modify_ids[]"] = modify_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access_ids(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_ids_type_0 = cast(list[str], data)

                return access_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        access_ids = _parse_access_ids(d.pop("access_ids[]", UNSET))

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

        def _parse_manage_ids(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                manage_ids_type_0 = cast(list[str], data)

                return manage_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        manage_ids = _parse_manage_ids(d.pop("manage_ids[]", UNSET))

        def _parse_modify_ids(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modify_ids_type_0 = cast(list[str], data)

                return modify_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        modify_ids = _parse_modify_ids(d.pop("modify_ids[]", UNSET))

        update_dataset_permissions_payload = cls(
            access_ids=access_ids,
            action=action,
            manage_ids=manage_ids,
            modify_ids=modify_ids,
        )

        update_dataset_permissions_payload.additional_properties = d
        return update_dataset_permissions_payload

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
