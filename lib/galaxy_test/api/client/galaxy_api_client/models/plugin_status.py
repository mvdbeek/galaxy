from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_aspect_status import PluginAspectStatus


T = TypeVar("T", bound="PluginStatus")


@_attrs_define
class PluginStatus:
    """
    Attributes:
        template_definition (PluginAspectStatus):
        connection (None | PluginAspectStatus | Unset):
        oauth2_access_token_generation (None | PluginAspectStatus | Unset):
        template_settings (None | PluginAspectStatus | Unset):
    """

    template_definition: PluginAspectStatus
    connection: None | PluginAspectStatus | Unset = UNSET
    oauth2_access_token_generation: None | PluginAspectStatus | Unset = UNSET
    template_settings: None | PluginAspectStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_aspect_status import PluginAspectStatus

        template_definition = self.template_definition.to_dict()

        connection: dict[str, Any] | None | Unset
        if isinstance(self.connection, Unset):
            connection = UNSET
        elif isinstance(self.connection, PluginAspectStatus):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

        oauth2_access_token_generation: dict[str, Any] | None | Unset
        if isinstance(self.oauth2_access_token_generation, Unset):
            oauth2_access_token_generation = UNSET
        elif isinstance(self.oauth2_access_token_generation, PluginAspectStatus):
            oauth2_access_token_generation = self.oauth2_access_token_generation.to_dict()
        else:
            oauth2_access_token_generation = self.oauth2_access_token_generation

        template_settings: dict[str, Any] | None | Unset
        if isinstance(self.template_settings, Unset):
            template_settings = UNSET
        elif isinstance(self.template_settings, PluginAspectStatus):
            template_settings = self.template_settings.to_dict()
        else:
            template_settings = self.template_settings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "template_definition": template_definition,
            }
        )
        if connection is not UNSET:
            field_dict["connection"] = connection
        if oauth2_access_token_generation is not UNSET:
            field_dict["oauth2_access_token_generation"] = oauth2_access_token_generation
        if template_settings is not UNSET:
            field_dict["template_settings"] = template_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_aspect_status import PluginAspectStatus

        d = dict(src_dict)
        template_definition = PluginAspectStatus.from_dict(d.pop("template_definition"))

        def _parse_connection(data: object) -> None | PluginAspectStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_0 = PluginAspectStatus.from_dict(data)

                return connection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PluginAspectStatus | Unset, data)

        connection = _parse_connection(d.pop("connection", UNSET))

        def _parse_oauth2_access_token_generation(data: object) -> None | PluginAspectStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth2_access_token_generation_type_0 = PluginAspectStatus.from_dict(data)

                return oauth2_access_token_generation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PluginAspectStatus | Unset, data)

        oauth2_access_token_generation = _parse_oauth2_access_token_generation(
            d.pop("oauth2_access_token_generation", UNSET)
        )

        def _parse_template_settings(data: object) -> None | PluginAspectStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_settings_type_0 = PluginAspectStatus.from_dict(data)

                return template_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PluginAspectStatus | Unset, data)

        template_settings = _parse_template_settings(d.pop("template_settings", UNSET))

        plugin_status = cls(
            template_definition=template_definition,
            connection=connection,
            oauth2_access_token_generation=oauth2_access_token_generation,
            template_settings=template_settings,
        )

        return plugin_status
