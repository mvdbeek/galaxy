from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.installed_repository_tool_shed_status import InstalledRepositoryToolShedStatus


T = TypeVar("T", bound="InstalledToolShedRepository")


@_attrs_define
class InstalledToolShedRepository:
    """
    Attributes:
        changeset_revision (str): Changeset revision of the repository - a mercurial commit hash
        ctx_rev (None | str): The linearized 0-based index of the changeset on the tool shed (0, 1, 2,...)
        deleted (bool):
        dist_to_shed (bool):
        id (str): Encoded ID of the install tool shed repository. Example: 0123456789ABCDEF.
        installed_changeset_revision (str): Initially installed changeset revision. Used to construct path to repository
            within Galaxies filesystem. Does not change if a repository is updated.
        model_class (Literal['ToolShedRepository']): The name of the database model class.
        name (str): Name of repository
        owner (str): Owner of repository
        status (str):
        tool_shed (str): Hostname of the tool shed this was installed from
        uninstalled (bool):
        error_message (str | Unset):  Default: 'Installation error message, the empty string means no error was
            recorded'.
        tool_shed_status (InstalledRepositoryToolShedStatus | None | Unset):
    """

    changeset_revision: str
    ctx_rev: None | str
    deleted: bool
    dist_to_shed: bool
    id: str
    installed_changeset_revision: str
    model_class: Literal["ToolShedRepository"]
    name: str
    owner: str
    status: str
    tool_shed: str
    uninstalled: bool
    error_message: str | Unset = "Installation error message, the empty string means no error was recorded"
    tool_shed_status: InstalledRepositoryToolShedStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installed_repository_tool_shed_status import InstalledRepositoryToolShedStatus

        changeset_revision = self.changeset_revision

        ctx_rev: None | str
        ctx_rev = self.ctx_rev

        deleted = self.deleted

        dist_to_shed = self.dist_to_shed

        id = self.id

        installed_changeset_revision = self.installed_changeset_revision

        model_class = self.model_class

        name = self.name

        owner = self.owner

        status = self.status

        tool_shed = self.tool_shed

        uninstalled = self.uninstalled

        error_message = self.error_message

        tool_shed_status: dict[str, Any] | None | Unset
        if isinstance(self.tool_shed_status, Unset):
            tool_shed_status = UNSET
        elif isinstance(self.tool_shed_status, InstalledRepositoryToolShedStatus):
            tool_shed_status = self.tool_shed_status.to_dict()
        else:
            tool_shed_status = self.tool_shed_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeset_revision": changeset_revision,
                "ctx_rev": ctx_rev,
                "deleted": deleted,
                "dist_to_shed": dist_to_shed,
                "id": id,
                "installed_changeset_revision": installed_changeset_revision,
                "model_class": model_class,
                "name": name,
                "owner": owner,
                "status": status,
                "tool_shed": tool_shed,
                "uninstalled": uninstalled,
            }
        )
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if tool_shed_status is not UNSET:
            field_dict["tool_shed_status"] = tool_shed_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installed_repository_tool_shed_status import InstalledRepositoryToolShedStatus

        d = dict(src_dict)
        changeset_revision = d.pop("changeset_revision")

        def _parse_ctx_rev(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ctx_rev = _parse_ctx_rev(d.pop("ctx_rev"))

        deleted = d.pop("deleted")

        dist_to_shed = d.pop("dist_to_shed")

        id = d.pop("id")

        installed_changeset_revision = d.pop("installed_changeset_revision")

        model_class = cast(Literal["ToolShedRepository"], d.pop("model_class"))
        if model_class != "ToolShedRepository":
            raise ValueError(f"model_class must match const 'ToolShedRepository', got '{model_class}'")

        name = d.pop("name")

        owner = d.pop("owner")

        status = d.pop("status")

        tool_shed = d.pop("tool_shed")

        uninstalled = d.pop("uninstalled")

        error_message = d.pop("error_message", UNSET)

        def _parse_tool_shed_status(data: object) -> InstalledRepositoryToolShedStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_shed_status_type_0 = InstalledRepositoryToolShedStatus.from_dict(data)

                return tool_shed_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstalledRepositoryToolShedStatus | None | Unset, data)

        tool_shed_status = _parse_tool_shed_status(d.pop("tool_shed_status", UNSET))

        installed_tool_shed_repository = cls(
            changeset_revision=changeset_revision,
            ctx_rev=ctx_rev,
            deleted=deleted,
            dist_to_shed=dist_to_shed,
            id=id,
            installed_changeset_revision=installed_changeset_revision,
            model_class=model_class,
            name=name,
            owner=owner,
            status=status,
            tool_shed=tool_shed,
            uninstalled=uninstalled,
            error_message=error_message,
            tool_shed_status=tool_shed_status,
        )

        installed_tool_shed_repository.additional_properties = d
        return installed_tool_shed_repository

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
