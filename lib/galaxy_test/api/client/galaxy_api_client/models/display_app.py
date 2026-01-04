from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hyperlink import Hyperlink


T = TypeVar("T", bound="DisplayApp")


@_attrs_define
class DisplayApp:
    """Basic linked information about an application that can display certain datatypes.

    Attributes:
        label (str): The label or title of the Display Application.
        links (list[Hyperlink]): The collection of link details for this Display Application.
    """

    label: str
    links: list[Hyperlink]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hyperlink import Hyperlink

        d = dict(src_dict)
        label = d.pop("label")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = Hyperlink.from_dict(links_item_data)

            links.append(links_item)

        display_app = cls(
            label=label,
            links=links,
        )

        display_app.additional_properties = d
        return display_app

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
