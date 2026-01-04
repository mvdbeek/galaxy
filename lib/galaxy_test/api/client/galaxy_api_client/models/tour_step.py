from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TourStep")


@_attrs_define
class TourStep:
    """
    Attributes:
        content (None | str | Unset): Text shown to the user
        element (None | str | Unset): CSS selector for the element to be described/clicked
        orphan (bool | None | Unset): If true, the step is an orphan step
        placement (None | str | Unset): Placement of the text box relative to the selected element
        postclick (bool | list[str] | None | Unset): Elements that receive a click() event after the step is shown
        preclick (bool | list[str] | None | Unset): Elements that receive a click() event before the step is shown
        textinsert (None | str | Unset): Text to insert if element is a text box (e.g. tool search or upload)
        title (None | str | Unset): Title displayed in the header of the step container
    """

    content: None | str | Unset = UNSET
    element: None | str | Unset = UNSET
    orphan: bool | None | Unset = UNSET
    placement: None | str | Unset = UNSET
    postclick: bool | list[str] | None | Unset = UNSET
    preclick: bool | list[str] | None | Unset = UNSET
    textinsert: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        element: None | str | Unset
        if isinstance(self.element, Unset):
            element = UNSET
        else:
            element = self.element

        orphan: bool | None | Unset
        if isinstance(self.orphan, Unset):
            orphan = UNSET
        else:
            orphan = self.orphan

        placement: None | str | Unset
        if isinstance(self.placement, Unset):
            placement = UNSET
        else:
            placement = self.placement

        postclick: bool | list[str] | None | Unset
        if isinstance(self.postclick, Unset):
            postclick = UNSET
        elif isinstance(self.postclick, list):
            postclick = self.postclick

        else:
            postclick = self.postclick

        preclick: bool | list[str] | None | Unset
        if isinstance(self.preclick, Unset):
            preclick = UNSET
        elif isinstance(self.preclick, list):
            preclick = self.preclick

        else:
            preclick = self.preclick

        textinsert: None | str | Unset
        if isinstance(self.textinsert, Unset):
            textinsert = UNSET
        else:
            textinsert = self.textinsert

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if element is not UNSET:
            field_dict["element"] = element
        if orphan is not UNSET:
            field_dict["orphan"] = orphan
        if placement is not UNSET:
            field_dict["placement"] = placement
        if postclick is not UNSET:
            field_dict["postclick"] = postclick
        if preclick is not UNSET:
            field_dict["preclick"] = preclick
        if textinsert is not UNSET:
            field_dict["textinsert"] = textinsert
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_element(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        element = _parse_element(d.pop("element", UNSET))

        def _parse_orphan(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        orphan = _parse_orphan(d.pop("orphan", UNSET))

        def _parse_placement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placement = _parse_placement(d.pop("placement", UNSET))

        def _parse_postclick(data: object) -> bool | list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                postclick_type_1 = cast(list[str], data)

                return postclick_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | list[str] | None | Unset, data)

        postclick = _parse_postclick(d.pop("postclick", UNSET))

        def _parse_preclick(data: object) -> bool | list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                preclick_type_1 = cast(list[str], data)

                return preclick_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | list[str] | None | Unset, data)

        preclick = _parse_preclick(d.pop("preclick", UNSET))

        def _parse_textinsert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        textinsert = _parse_textinsert(d.pop("textinsert", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        tour_step = cls(
            content=content,
            element=element,
            orphan=orphan,
            placement=placement,
            postclick=postclick,
            preclick=preclick,
            textinsert=textinsert,
            title=title,
        )

        tour_step.additional_properties = d
        return tour_step

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
