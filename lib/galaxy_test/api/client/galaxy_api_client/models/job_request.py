from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_request_inputs_type_0 import JobRequestInputsType0


T = TypeVar("T", bound="JobRequest")


@_attrs_define
class JobRequest:
    """
    Attributes:
        history_id (None | str | Unset): TODO
        inputs (JobRequestInputsType0 | None | Unset): TODO
        rerun_remap_job_id (None | str | Unset): TODO
        send_email_notification (bool | Unset): TODO Default: False.
        strict (bool | Unset): Turn on strict validation of the inputs that drops support for some inconsistent legacy
            behavior. Default: True.
        tool_id (None | str | Unset): TODO
        tool_uuid (None | str | Unset): TODO
        tool_version (None | str | Unset): TODO
        use_cached_jobs (bool | None | Unset):
    """

    history_id: None | str | Unset = UNSET
    inputs: JobRequestInputsType0 | None | Unset = UNSET
    rerun_remap_job_id: None | str | Unset = UNSET
    send_email_notification: bool | Unset = False
    strict: bool | Unset = True
    tool_id: None | str | Unset = UNSET
    tool_uuid: None | str | Unset = UNSET
    tool_version: None | str | Unset = UNSET
    use_cached_jobs: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_request_inputs_type_0 import JobRequestInputsType0

        history_id: None | str | Unset
        if isinstance(self.history_id, Unset):
            history_id = UNSET
        else:
            history_id = self.history_id

        inputs: dict[str, Any] | None | Unset
        if isinstance(self.inputs, Unset):
            inputs = UNSET
        elif isinstance(self.inputs, JobRequestInputsType0):
            inputs = self.inputs.to_dict()
        else:
            inputs = self.inputs

        rerun_remap_job_id: None | str | Unset
        if isinstance(self.rerun_remap_job_id, Unset):
            rerun_remap_job_id = UNSET
        else:
            rerun_remap_job_id = self.rerun_remap_job_id

        send_email_notification = self.send_email_notification

        strict = self.strict

        tool_id: None | str | Unset
        if isinstance(self.tool_id, Unset):
            tool_id = UNSET
        else:
            tool_id = self.tool_id

        tool_uuid: None | str | Unset
        if isinstance(self.tool_uuid, Unset):
            tool_uuid = UNSET
        else:
            tool_uuid = self.tool_uuid

        tool_version: None | str | Unset
        if isinstance(self.tool_version, Unset):
            tool_version = UNSET
        else:
            tool_version = self.tool_version

        use_cached_jobs: bool | None | Unset
        if isinstance(self.use_cached_jobs, Unset):
            use_cached_jobs = UNSET
        else:
            use_cached_jobs = self.use_cached_jobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if rerun_remap_job_id is not UNSET:
            field_dict["rerun_remap_job_id"] = rerun_remap_job_id
        if send_email_notification is not UNSET:
            field_dict["send_email_notification"] = send_email_notification
        if strict is not UNSET:
            field_dict["strict"] = strict
        if tool_id is not UNSET:
            field_dict["tool_id"] = tool_id
        if tool_uuid is not UNSET:
            field_dict["tool_uuid"] = tool_uuid
        if tool_version is not UNSET:
            field_dict["tool_version"] = tool_version
        if use_cached_jobs is not UNSET:
            field_dict["use_cached_jobs"] = use_cached_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_request_inputs_type_0 import JobRequestInputsType0

        d = dict(src_dict)

        def _parse_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        history_id = _parse_history_id(d.pop("history_id", UNSET))

        def _parse_inputs(data: object) -> JobRequestInputsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inputs_type_0 = JobRequestInputsType0.from_dict(data)

                return inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobRequestInputsType0 | None | Unset, data)

        inputs = _parse_inputs(d.pop("inputs", UNSET))

        def _parse_rerun_remap_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rerun_remap_job_id = _parse_rerun_remap_job_id(d.pop("rerun_remap_job_id", UNSET))

        send_email_notification = d.pop("send_email_notification", UNSET)

        strict = d.pop("strict", UNSET)

        def _parse_tool_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_id = _parse_tool_id(d.pop("tool_id", UNSET))

        def _parse_tool_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_uuid = _parse_tool_uuid(d.pop("tool_uuid", UNSET))

        def _parse_tool_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_version = _parse_tool_version(d.pop("tool_version", UNSET))

        def _parse_use_cached_jobs(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_cached_jobs = _parse_use_cached_jobs(d.pop("use_cached_jobs", UNSET))

        job_request = cls(
            history_id=history_id,
            inputs=inputs,
            rerun_remap_job_id=rerun_remap_job_id,
            send_email_notification=send_email_notification,
            strict=strict,
            tool_id=tool_id,
            tool_uuid=tool_uuid,
            tool_version=tool_version,
            use_cached_jobs=use_cached_jobs,
        )

        job_request.additional_properties = d
        return job_request

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
