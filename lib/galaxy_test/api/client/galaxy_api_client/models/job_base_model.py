from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_state import JobState
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobBaseModel")


@_attrs_define
class JobBaseModel:
    """
    Attributes:
        create_time (datetime.datetime): The time and date this item was created.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['Job']): The name of the database model class.
        state (JobState):
        tool_id (str): Identifier of the tool that generated this job.
        update_time (datetime.datetime): The last time and date this item was updated.
        exit_code (int | None | Unset): The exit code returned by the tool. Can be unset if the job is not completed
            yet.
        galaxy_version (None | str | Unset): The (major) version of Galaxy used to create this job.
        history_id (None | str | Unset): The encoded ID of the history associated with this item.
    """

    create_time: datetime.datetime
    id: str
    model_class: Literal["Job"]
    state: JobState
    tool_id: str
    update_time: datetime.datetime
    exit_code: int | None | Unset = UNSET
    galaxy_version: None | str | Unset = UNSET
    history_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time.isoformat()

        id = self.id

        model_class = self.model_class

        state = self.state.value

        tool_id = self.tool_id

        update_time = self.update_time.isoformat()

        exit_code: int | None | Unset
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        galaxy_version: None | str | Unset
        if isinstance(self.galaxy_version, Unset):
            galaxy_version = UNSET
        else:
            galaxy_version = self.galaxy_version

        history_id: None | str | Unset
        if isinstance(self.history_id, Unset):
            history_id = UNSET
        else:
            history_id = self.history_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_time": create_time,
                "id": id,
                "model_class": model_class,
                "state": state,
                "tool_id": tool_id,
                "update_time": update_time,
            }
        )
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if galaxy_version is not UNSET:
            field_dict["galaxy_version"] = galaxy_version
        if history_id is not UNSET:
            field_dict["history_id"] = history_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time = isoparse(d.pop("create_time"))

        id = d.pop("id")

        model_class = cast(Literal["Job"], d.pop("model_class"))
        if model_class != "Job":
            raise ValueError(f"model_class must match const 'Job', got '{model_class}'")

        state = JobState(d.pop("state"))

        tool_id = d.pop("tool_id")

        update_time = isoparse(d.pop("update_time"))

        def _parse_exit_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exit_code = _parse_exit_code(d.pop("exit_code", UNSET))

        def _parse_galaxy_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        galaxy_version = _parse_galaxy_version(d.pop("galaxy_version", UNSET))

        def _parse_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        history_id = _parse_history_id(d.pop("history_id", UNSET))

        job_base_model = cls(
            create_time=create_time,
            id=id,
            model_class=model_class,
            state=state,
            tool_id=tool_id,
            update_time=update_time,
            exit_code=exit_code,
            galaxy_version=galaxy_version,
            history_id=history_id,
        )

        job_base_model.additional_properties = d
        return job_base_model

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
