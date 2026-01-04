from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_link_step import CreateLinkStep


T = TypeVar("T", bound="CreateLinkFeedback")


@_attrs_define
class CreateLinkFeedback:
    """
    Attributes:
        messages (list[list[str]] | None | Unset):
        preparable_steps (list[CreateLinkStep] | None | Unset):
        refresh (bool | None | Unset):  Default: False.
        resource (None | str | Unset):
    """

    messages: list[list[str]] | None | Unset = UNSET
    preparable_steps: list[CreateLinkStep] | None | Unset = UNSET
    refresh: bool | None | Unset = False
    resource: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages: list[list[str]] | None | Unset
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = []
            for messages_type_0_item_data in self.messages:
                messages_type_0_item = []
                for messages_type_0_item_item_data in messages_type_0_item_data:
                    messages_type_0_item_item: str
                    messages_type_0_item_item = messages_type_0_item_item_data
                    messages_type_0_item.append(messages_type_0_item_item)

                messages.append(messages_type_0_item)

        else:
            messages = self.messages

        preparable_steps: list[dict[str, Any]] | None | Unset
        if isinstance(self.preparable_steps, Unset):
            preparable_steps = UNSET
        elif isinstance(self.preparable_steps, list):
            preparable_steps = []
            for preparable_steps_type_0_item_data in self.preparable_steps:
                preparable_steps_type_0_item = preparable_steps_type_0_item_data.to_dict()
                preparable_steps.append(preparable_steps_type_0_item)

        else:
            preparable_steps = self.preparable_steps

        refresh: bool | None | Unset
        if isinstance(self.refresh, Unset):
            refresh = UNSET
        else:
            refresh = self.refresh

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if preparable_steps is not UNSET:
            field_dict["preparable_steps"] = preparable_steps
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_link_step import CreateLinkStep

        d = dict(src_dict)

        def _parse_messages(data: object) -> list[list[str]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = []
                _messages_type_0 = data
                for messages_type_0_item_data in _messages_type_0:
                    messages_type_0_item = []
                    _messages_type_0_item = messages_type_0_item_data
                    for messages_type_0_item_item_data in _messages_type_0_item:

                        def _parse_messages_type_0_item_item(data: object) -> str:
                            return cast(str, data)

                        messages_type_0_item_item = _parse_messages_type_0_item_item(messages_type_0_item_item_data)

                        messages_type_0_item.append(messages_type_0_item_item)

                    messages_type_0.append(messages_type_0_item)

                return messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[str]] | None | Unset, data)

        messages = _parse_messages(d.pop("messages", UNSET))

        def _parse_preparable_steps(data: object) -> list[CreateLinkStep] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                preparable_steps_type_0 = []
                _preparable_steps_type_0 = data
                for preparable_steps_type_0_item_data in _preparable_steps_type_0:
                    preparable_steps_type_0_item = CreateLinkStep.from_dict(preparable_steps_type_0_item_data)

                    preparable_steps_type_0.append(preparable_steps_type_0_item)

                return preparable_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateLinkStep] | None | Unset, data)

        preparable_steps = _parse_preparable_steps(d.pop("preparable_steps", UNSET))

        def _parse_refresh(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        refresh = _parse_refresh(d.pop("refresh", UNSET))

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))

        create_link_feedback = cls(
            messages=messages,
            preparable_steps=preparable_steps,
            refresh=refresh,
            resource=resource,
        )

        create_link_feedback.additional_properties = d
        return create_link_feedback

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
