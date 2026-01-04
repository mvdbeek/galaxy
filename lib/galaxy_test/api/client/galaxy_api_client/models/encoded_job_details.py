from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_state import JobState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inputs import Inputs
    from ..models.output_collections import OutputCollections
    from ..models.outputs import Outputs


T = TypeVar("T", bound="EncodedJobDetails")


@_attrs_define
class EncodedJobDetails:
    """
    Attributes:
        create_time (datetime.datetime): The time and date this item was created.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['Job']): The name of the database model class.
        params (Any): Object containing all the parameters of the tool associated with this job. The specific parameters
            depend on the tool itself.
        state (JobState):
        tool_id (str): Identifier of the tool that generated this job.
        update_time (datetime.datetime): The last time and date this item was updated.
        command_line (None | str | Unset): The command line produced by the job. Users can see this value if allowed in
            the configuration, administrator can always see this value.
        command_version (None | str | Unset): Tool version indicated during job execution.
        copied_from_job_id (None | str | Unset): Reference to cached job if job execution was cached.
        exit_code (int | None | Unset): The exit code returned by the tool. Can be unset if the job is not completed
            yet.
        external_id (None | str | Unset): The job id used by the external job runner (Condor, Pulsar, etc.). Only
            administrator can see this value.
        galaxy_version (None | str | Unset): The (major) version of Galaxy used to create this job.
        handler (None | str | Unset): The job handler process assigned to handle this job. Only administrator can see
            this value.
        history_id (None | str | Unset): The encoded ID of the history associated with this item.
        inputs (Inputs | Unset): Dictionary mapping all the tool inputs (by name) to the corresponding data references.
        job_runner_name (None | str | Unset): Name of the job runner plugin that handles this job. Only administrator
            can see this value.
        output_collections (OutputCollections | Unset):
        outputs (Outputs | Unset): Dictionary mapping all the tool outputs (by name) to the corresponding data
            references.
        user_email (None | str | Unset): The email of the user that owns this job. Only the owner of the job and
            administrators can see this value.
        user_id (None | str | Unset): User ID of user that ran this job
    """

    create_time: datetime.datetime
    id: str
    model_class: Literal["Job"]
    params: Any
    state: JobState
    tool_id: str
    update_time: datetime.datetime
    command_line: None | str | Unset = UNSET
    command_version: None | str | Unset = UNSET
    copied_from_job_id: None | str | Unset = UNSET
    exit_code: int | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    galaxy_version: None | str | Unset = UNSET
    handler: None | str | Unset = UNSET
    history_id: None | str | Unset = UNSET
    inputs: Inputs | Unset = UNSET
    job_runner_name: None | str | Unset = UNSET
    output_collections: OutputCollections | Unset = UNSET
    outputs: Outputs | Unset = UNSET
    user_email: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time.isoformat()

        id = self.id

        model_class = self.model_class

        params = self.params

        state = self.state.value

        tool_id = self.tool_id

        update_time = self.update_time.isoformat()

        command_line: None | str | Unset
        if isinstance(self.command_line, Unset):
            command_line = UNSET
        else:
            command_line = self.command_line

        command_version: None | str | Unset
        if isinstance(self.command_version, Unset):
            command_version = UNSET
        else:
            command_version = self.command_version

        copied_from_job_id: None | str | Unset
        if isinstance(self.copied_from_job_id, Unset):
            copied_from_job_id = UNSET
        else:
            copied_from_job_id = self.copied_from_job_id

        exit_code: int | None | Unset
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        galaxy_version: None | str | Unset
        if isinstance(self.galaxy_version, Unset):
            galaxy_version = UNSET
        else:
            galaxy_version = self.galaxy_version

        handler: None | str | Unset
        if isinstance(self.handler, Unset):
            handler = UNSET
        else:
            handler = self.handler

        history_id: None | str | Unset
        if isinstance(self.history_id, Unset):
            history_id = UNSET
        else:
            history_id = self.history_id

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        job_runner_name: None | str | Unset
        if isinstance(self.job_runner_name, Unset):
            job_runner_name = UNSET
        else:
            job_runner_name = self.job_runner_name

        output_collections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_collections, Unset):
            output_collections = self.output_collections.to_dict()

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_time": create_time,
                "id": id,
                "model_class": model_class,
                "params": params,
                "state": state,
                "tool_id": tool_id,
                "update_time": update_time,
            }
        )
        if command_line is not UNSET:
            field_dict["command_line"] = command_line
        if command_version is not UNSET:
            field_dict["command_version"] = command_version
        if copied_from_job_id is not UNSET:
            field_dict["copied_from_job_id"] = copied_from_job_id
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if galaxy_version is not UNSET:
            field_dict["galaxy_version"] = galaxy_version
        if handler is not UNSET:
            field_dict["handler"] = handler
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if job_runner_name is not UNSET:
            field_dict["job_runner_name"] = job_runner_name
        if output_collections is not UNSET:
            field_dict["output_collections"] = output_collections
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inputs import Inputs
        from ..models.output_collections import OutputCollections
        from ..models.outputs import Outputs

        d = dict(src_dict)
        create_time = isoparse(d.pop("create_time"))

        id = d.pop("id")

        model_class = cast(Literal["Job"], d.pop("model_class"))
        if model_class != "Job":
            raise ValueError(f"model_class must match const 'Job', got '{model_class}'")

        params = d.pop("params")

        state = JobState(d.pop("state"))

        tool_id = d.pop("tool_id")

        update_time = isoparse(d.pop("update_time"))

        def _parse_command_line(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_line = _parse_command_line(d.pop("command_line", UNSET))

        def _parse_command_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command_version = _parse_command_version(d.pop("command_version", UNSET))

        def _parse_copied_from_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_job_id = _parse_copied_from_job_id(d.pop("copied_from_job_id", UNSET))

        def _parse_exit_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exit_code = _parse_exit_code(d.pop("exit_code", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_galaxy_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        galaxy_version = _parse_galaxy_version(d.pop("galaxy_version", UNSET))

        def _parse_handler(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handler = _parse_handler(d.pop("handler", UNSET))

        def _parse_history_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        history_id = _parse_history_id(d.pop("history_id", UNSET))

        _inputs = d.pop("inputs", UNSET)
        inputs: Inputs | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = Inputs.from_dict(_inputs)

        def _parse_job_runner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_runner_name = _parse_job_runner_name(d.pop("job_runner_name", UNSET))

        _output_collections = d.pop("output_collections", UNSET)
        output_collections: OutputCollections | Unset
        if isinstance(_output_collections, Unset):
            output_collections = UNSET
        else:
            output_collections = OutputCollections.from_dict(_output_collections)

        _outputs = d.pop("outputs", UNSET)
        outputs: Outputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = Outputs.from_dict(_outputs)

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        encoded_job_details = cls(
            create_time=create_time,
            id=id,
            model_class=model_class,
            params=params,
            state=state,
            tool_id=tool_id,
            update_time=update_time,
            command_line=command_line,
            command_version=command_version,
            copied_from_job_id=copied_from_job_id,
            exit_code=exit_code,
            external_id=external_id,
            galaxy_version=galaxy_version,
            handler=handler,
            history_id=history_id,
            inputs=inputs,
            job_runner_name=job_runner_name,
            output_collections=output_collections,
            outputs=outputs,
            user_email=user_email,
            user_id=user_id,
        )

        encoded_job_details.additional_properties = d
        return encoded_job_details

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
