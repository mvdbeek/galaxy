from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvocationCancellationHistoryDeletedResponse")


@_attrs_define
class InvocationCancellationHistoryDeletedResponse:
    """
    Attributes:
        history_id (str): History ID of history that was deleted. Example: 0123456789ABCDEF.
        reason (Literal['history_deleted']):
    """

    history_id: str
    reason: Literal["history_deleted"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        history_id = d.pop("history_id")

        reason = cast(Literal["history_deleted"], d.pop("reason"))
        if reason != "history_deleted":
            raise ValueError(f"reason must match const 'history_deleted', got '{reason}'")

        invocation_cancellation_history_deleted_response = cls(
            history_id=history_id,
            reason=reason,
        )

        invocation_cancellation_history_deleted_response.additional_properties = d
        return invocation_cancellation_history_deleted_response

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
