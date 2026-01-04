from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_state import JobState
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobConsoleOutput")


@_attrs_define
class JobConsoleOutput:
    """
    Attributes:
        state (JobState | None | Unset): The current job's state
        stderr (None | str | Unset): Tool STDERR from job.
        stdout (None | str | Unset): Tool STDOUT from job.
    """

    state: JobState | None | Unset = UNSET
    stderr: None | str | Unset = UNSET
    stdout: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, JobState):
            state = self.state.value
        else:
            state = self.state

        stderr: None | str | Unset
        if isinstance(self.stderr, Unset):
            stderr = UNSET
        else:
            stderr = self.stderr

        stdout: None | str | Unset
        if isinstance(self.stdout, Unset):
            stdout = UNSET
        else:
            stdout = self.stdout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if stdout is not UNSET:
            field_dict["stdout"] = stdout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_state(data: object) -> JobState | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = JobState(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobState | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_stderr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stderr = _parse_stderr(d.pop("stderr", UNSET))

        def _parse_stdout(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stdout = _parse_stdout(d.pop("stdout", UNSET))

        job_console_output = cls(
            state=state,
            stderr=stderr,
            stdout=stdout,
        )

        job_console_output.additional_properties = d
        return job_console_output

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
