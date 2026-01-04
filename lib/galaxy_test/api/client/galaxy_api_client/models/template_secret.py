from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateSecret")


@_attrs_define
class TemplateSecret:
    """
    Attributes:
        help_ (None | str):
        name (str):
        label (None | str | Unset):
    """

    help_: None | str
    name: str
    label: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        help_: None | str
        help_ = self.help_

        name = self.name

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "help": help_,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_help_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        help_ = _parse_help_(d.pop("help"))

        name = d.pop("name")

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        template_secret = cls(
            help_=help_,
            name=name,
            label=label,
        )

        return template_secret
