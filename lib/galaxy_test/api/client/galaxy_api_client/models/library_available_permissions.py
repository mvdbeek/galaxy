from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_role_model import BasicRoleModel


T = TypeVar("T", bound="LibraryAvailablePermissions")


@_attrs_define
class LibraryAvailablePermissions:
    """
    Attributes:
        page (int): Current page.
        page_limit (int): Maximum number of items per page.
        roles (list[BasicRoleModel]): A list containing available roles that can be assigned to a particular permission.
        total (int): Total number of items
    """

    page: int
    page_limit: int
    roles: list[BasicRoleModel]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_limit = self.page_limit

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "page_limit": page_limit,
                "roles": roles,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_role_model import BasicRoleModel

        d = dict(src_dict)
        page = d.pop("page")

        page_limit = d.pop("page_limit")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = BasicRoleModel.from_dict(roles_item_data)

            roles.append(roles_item)

        total = d.pop("total")

        library_available_permissions = cls(
            page=page,
            page_limit=page_limit,
            roles=roles,
            total=total,
        )

        library_available_permissions.additional_properties = d
        return library_available_permissions

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
