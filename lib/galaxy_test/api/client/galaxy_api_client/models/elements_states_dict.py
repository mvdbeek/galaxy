from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ElementsStatesDict")


@_attrs_define
class ElementsStatesDict:
    """
    Attributes:
        deferred (int | Unset):
        discarded (int | Unset):
        empty (int | Unset):
        error (int | Unset):
        failed_metadata (int | Unset):
        new (int | Unset):
        ok (int | Unset):
        paused (int | Unset):
        queued (int | Unset):
        running (int | Unset):
        setting_metadata (int | Unset):
        upload (int | Unset):
    """

    deferred: int | Unset = UNSET
    discarded: int | Unset = UNSET
    empty: int | Unset = UNSET
    error: int | Unset = UNSET
    failed_metadata: int | Unset = UNSET
    new: int | Unset = UNSET
    ok: int | Unset = UNSET
    paused: int | Unset = UNSET
    queued: int | Unset = UNSET
    running: int | Unset = UNSET
    setting_metadata: int | Unset = UNSET
    upload: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deferred = self.deferred

        discarded = self.discarded

        empty = self.empty

        error = self.error

        failed_metadata = self.failed_metadata

        new = self.new

        ok = self.ok

        paused = self.paused

        queued = self.queued

        running = self.running

        setting_metadata = self.setting_metadata

        upload = self.upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if discarded is not UNSET:
            field_dict["discarded"] = discarded
        if empty is not UNSET:
            field_dict["empty"] = empty
        if error is not UNSET:
            field_dict["error"] = error
        if failed_metadata is not UNSET:
            field_dict["failed_metadata"] = failed_metadata
        if new is not UNSET:
            field_dict["new"] = new
        if ok is not UNSET:
            field_dict["ok"] = ok
        if paused is not UNSET:
            field_dict["paused"] = paused
        if queued is not UNSET:
            field_dict["queued"] = queued
        if running is not UNSET:
            field_dict["running"] = running
        if setting_metadata is not UNSET:
            field_dict["setting_metadata"] = setting_metadata
        if upload is not UNSET:
            field_dict["upload"] = upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deferred = d.pop("deferred", UNSET)

        discarded = d.pop("discarded", UNSET)

        empty = d.pop("empty", UNSET)

        error = d.pop("error", UNSET)

        failed_metadata = d.pop("failed_metadata", UNSET)

        new = d.pop("new", UNSET)

        ok = d.pop("ok", UNSET)

        paused = d.pop("paused", UNSET)

        queued = d.pop("queued", UNSET)

        running = d.pop("running", UNSET)

        setting_metadata = d.pop("setting_metadata", UNSET)

        upload = d.pop("upload", UNSET)

        elements_states_dict = cls(
            deferred=deferred,
            discarded=discarded,
            empty=empty,
            error=error,
            failed_metadata=failed_metadata,
            new=new,
            ok=ok,
            paused=paused,
            queued=queued,
            running=running,
            setting_metadata=setting_metadata,
            upload=upload,
        )

        elements_states_dict.additional_properties = d
        return elements_states_dict

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
