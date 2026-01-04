from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.plugin_aspect_status_state import PluginAspectStatusState

T = TypeVar("T", bound="PluginAspectStatus")


@_attrs_define
class PluginAspectStatus:
    """
    Attributes:
        message (str):
        state (PluginAspectStatusState):
    """

    message: str
    state: PluginAspectStatusState

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        state = self.state.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        state = PluginAspectStatusState(d.pop("state"))

        plugin_aspect_status = cls(
            message=message,
            state=state,
        )

        return plugin_aspect_status
