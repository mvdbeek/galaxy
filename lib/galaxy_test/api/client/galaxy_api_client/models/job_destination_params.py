from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobDestinationParams")


@_attrs_define
class JobDestinationParams:
    """
    Attributes:
        handler (None | str | Unset): Name of the process that handled the job.
        runner (None | str | Unset): Job runner class
        runner_job_id (None | str | Unset): ID assigned to submitted job by external job running system
    """

    handler: None | str | Unset = UNSET
    runner: None | str | Unset = UNSET
    runner_job_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handler: None | str | Unset
        if isinstance(self.handler, Unset):
            handler = UNSET
        else:
            handler = self.handler

        runner: None | str | Unset
        if isinstance(self.runner, Unset):
            runner = UNSET
        else:
            runner = self.runner

        runner_job_id: None | str | Unset
        if isinstance(self.runner_job_id, Unset):
            runner_job_id = UNSET
        else:
            runner_job_id = self.runner_job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handler is not UNSET:
            field_dict["Handler"] = handler
        if runner is not UNSET:
            field_dict["Runner"] = runner
        if runner_job_id is not UNSET:
            field_dict["Runner Job ID"] = runner_job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_handler(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handler = _parse_handler(d.pop("Handler", UNSET))

        def _parse_runner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        runner = _parse_runner(d.pop("Runner", UNSET))

        def _parse_runner_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        runner_job_id = _parse_runner_job_id(d.pop("Runner Job ID", UNSET))

        job_destination_params = cls(
            handler=handler,
            runner=runner,
            runner_job_id=runner_job_id,
        )

        job_destination_params.additional_properties = d
        return job_destination_params

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
