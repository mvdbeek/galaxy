from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invocation_state import InvocationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowInvocationCollectionView")


@_attrs_define
class WorkflowInvocationCollectionView:
    """
    Attributes:
        create_time (datetime.datetime): The time and date this item was created.
        history_id (str): The encoded ID of the history associated with the invocation. Example: 0123456789ABCDEF.
        id (str): The encoded ID of the workflow invocation. Example: 0123456789ABCDEF.
        model_class (Literal['WorkflowInvocation']): The name of the database model class.
        state (InvocationState):
        update_time (datetime.datetime): The last time and date this item was updated.
        workflow_id (str): The encoded Workflow ID associated with the invocation. Example: 0123456789ABCDEF.
        landing_uuid (None | str | Unset): The UUID of the workflow landing request associated with this invocation.
        uuid (None | str | Unset): Universal unique identifier of the workflow invocation.
    """

    create_time: datetime.datetime
    history_id: str
    id: str
    model_class: Literal["WorkflowInvocation"]
    state: InvocationState
    update_time: datetime.datetime
    workflow_id: str
    landing_uuid: None | str | Unset = UNSET
    uuid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time = self.create_time.isoformat()

        history_id = self.history_id

        id = self.id

        model_class = self.model_class

        state = self.state.value

        update_time = self.update_time.isoformat()

        workflow_id = self.workflow_id

        landing_uuid: None | str | Unset
        if isinstance(self.landing_uuid, Unset):
            landing_uuid = UNSET
        else:
            landing_uuid = self.landing_uuid

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_time": create_time,
                "history_id": history_id,
                "id": id,
                "model_class": model_class,
                "state": state,
                "update_time": update_time,
                "workflow_id": workflow_id,
            }
        )
        if landing_uuid is not UNSET:
            field_dict["landing_uuid"] = landing_uuid
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time = isoparse(d.pop("create_time"))

        history_id = d.pop("history_id")

        id = d.pop("id")

        model_class = cast(Literal["WorkflowInvocation"], d.pop("model_class"))
        if model_class != "WorkflowInvocation":
            raise ValueError(f"model_class must match const 'WorkflowInvocation', got '{model_class}'")

        state = InvocationState(d.pop("state"))

        update_time = isoparse(d.pop("update_time"))

        workflow_id = d.pop("workflow_id")

        def _parse_landing_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        landing_uuid = _parse_landing_uuid(d.pop("landing_uuid", UNSET))

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        workflow_invocation_collection_view = cls(
            create_time=create_time,
            history_id=history_id,
            id=id,
            model_class=model_class,
            state=state,
            update_time=update_time,
            workflow_id=workflow_id,
            landing_uuid=landing_uuid,
            uuid=uuid,
        )

        workflow_invocation_collection_view.additional_properties = d
        return workflow_invocation_collection_view

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
