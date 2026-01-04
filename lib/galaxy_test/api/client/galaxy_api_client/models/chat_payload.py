from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatPayload")


@_attrs_define
class ChatPayload:
    """
    Attributes:
        query (str): The query to be sent to the chatbot.
        context (None | str | Unset): The context for the chatbot. Default: ''.
        exchange_id (int | None | Unset): The ID of an existing chat exchange to continue.
    """

    query: str
    context: None | str | Unset = ""
    exchange_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        context: None | str | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        exchange_id: int | None | Unset
        if isinstance(self.exchange_id, Unset):
            exchange_id = UNSET
        else:
            exchange_id = self.exchange_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if exchange_id is not UNSET:
            field_dict["exchange_id"] = exchange_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_context(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        def _parse_exchange_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exchange_id = _parse_exchange_id(d.pop("exchange_id", UNSET))

        chat_payload = cls(
            query=query,
            context=context,
            exchange_id=exchange_id,
        )

        chat_payload.additional_properties = d
        return chat_payload

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
