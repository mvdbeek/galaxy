from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entry_point import EntryPoint
    from ..models.visualization_plugin_response_settings_type_0_item import VisualizationPluginResponseSettingsType0Item
    from ..models.visualization_plugin_response_specs_type_0 import VisualizationPluginResponseSpecsType0
    from ..models.visualization_plugin_response_tracks_type_0_item import VisualizationPluginResponseTracksType0Item


T = TypeVar("T", bound="VisualizationPluginResponse")


@_attrs_define
class VisualizationPluginResponse:
    """
    Attributes:
        description (str): The description of the plugin.
        embeddable (bool): Whether the plugin is embeddable.
        entry_point (EntryPoint): The entry point of the plugin.
        href (str): The href of the plugin.
        html (str): The HTML of the plugin.
        name (str): The name of the plugin.
        logo (None | str | Unset): The logo of the plugin.
        settings (list[VisualizationPluginResponseSettingsType0Item] | None | Unset): The settings of the plugin.
        specs (None | Unset | VisualizationPluginResponseSpecsType0): The specs of the plugin.
        title (None | str | Unset): The title of the plugin.
        tracks (list[VisualizationPluginResponseTracksType0Item] | None | Unset): The tracks of the plugin.
    """

    description: str
    embeddable: bool
    entry_point: EntryPoint
    href: str
    html: str
    name: str
    logo: None | str | Unset = UNSET
    settings: list[VisualizationPluginResponseSettingsType0Item] | None | Unset = UNSET
    specs: None | Unset | VisualizationPluginResponseSpecsType0 = UNSET
    title: None | str | Unset = UNSET
    tracks: list[VisualizationPluginResponseTracksType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.visualization_plugin_response_specs_type_0 import VisualizationPluginResponseSpecsType0

        description = self.description

        embeddable = self.embeddable

        entry_point = self.entry_point.to_dict()

        href = self.href

        html = self.html

        name = self.name

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        settings: list[dict[str, Any]] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, list):
            settings = []
            for settings_type_0_item_data in self.settings:
                settings_type_0_item = settings_type_0_item_data.to_dict()
                settings.append(settings_type_0_item)

        else:
            settings = self.settings

        specs: dict[str, Any] | None | Unset
        if isinstance(self.specs, Unset):
            specs = UNSET
        elif isinstance(self.specs, VisualizationPluginResponseSpecsType0):
            specs = self.specs.to_dict()
        else:
            specs = self.specs

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        tracks: list[dict[str, Any]] | None | Unset
        if isinstance(self.tracks, Unset):
            tracks = UNSET
        elif isinstance(self.tracks, list):
            tracks = []
            for tracks_type_0_item_data in self.tracks:
                tracks_type_0_item = tracks_type_0_item_data.to_dict()
                tracks.append(tracks_type_0_item)

        else:
            tracks = self.tracks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "embeddable": embeddable,
                "entry_point": entry_point,
                "href": href,
                "html": html,
                "name": name,
            }
        )
        if logo is not UNSET:
            field_dict["logo"] = logo
        if settings is not UNSET:
            field_dict["settings"] = settings
        if specs is not UNSET:
            field_dict["specs"] = specs
        if title is not UNSET:
            field_dict["title"] = title
        if tracks is not UNSET:
            field_dict["tracks"] = tracks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry_point import EntryPoint
        from ..models.visualization_plugin_response_settings_type_0_item import (
            VisualizationPluginResponseSettingsType0Item,
        )
        from ..models.visualization_plugin_response_specs_type_0 import VisualizationPluginResponseSpecsType0
        from ..models.visualization_plugin_response_tracks_type_0_item import VisualizationPluginResponseTracksType0Item

        d = dict(src_dict)
        description = d.pop("description")

        embeddable = d.pop("embeddable")

        entry_point = EntryPoint.from_dict(d.pop("entry_point"))

        href = d.pop("href")

        html = d.pop("html")

        name = d.pop("name")

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_settings(data: object) -> list[VisualizationPluginResponseSettingsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                settings_type_0 = []
                _settings_type_0 = data
                for settings_type_0_item_data in _settings_type_0:
                    settings_type_0_item = VisualizationPluginResponseSettingsType0Item.from_dict(
                        settings_type_0_item_data
                    )

                    settings_type_0.append(settings_type_0_item)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VisualizationPluginResponseSettingsType0Item] | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_specs(data: object) -> None | Unset | VisualizationPluginResponseSpecsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                specs_type_0 = VisualizationPluginResponseSpecsType0.from_dict(data)

                return specs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VisualizationPluginResponseSpecsType0, data)

        specs = _parse_specs(d.pop("specs", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_tracks(data: object) -> list[VisualizationPluginResponseTracksType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tracks_type_0 = []
                _tracks_type_0 = data
                for tracks_type_0_item_data in _tracks_type_0:
                    tracks_type_0_item = VisualizationPluginResponseTracksType0Item.from_dict(tracks_type_0_item_data)

                    tracks_type_0.append(tracks_type_0_item)

                return tracks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VisualizationPluginResponseTracksType0Item] | None | Unset, data)

        tracks = _parse_tracks(d.pop("tracks", UNSET))

        visualization_plugin_response = cls(
            description=description,
            embeddable=embeddable,
            entry_point=entry_point,
            href=href,
            html=html,
            name=name,
            logo=logo,
            settings=settings,
            specs=specs,
            title=title,
            tracks=tracks,
        )

        visualization_plugin_response.additional_properties = d
        return visualization_plugin_response

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
