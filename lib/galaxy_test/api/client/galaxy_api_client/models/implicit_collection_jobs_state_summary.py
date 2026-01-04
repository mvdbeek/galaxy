from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_collection_populated_state import DatasetCollectionPopulatedState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.states import States


T = TypeVar("T", bound="ImplicitCollectionJobsStateSummary")


@_attrs_define
class ImplicitCollectionJobsStateSummary:
    """
    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        model (Literal['ImplicitCollectionJobs']): The name of the database model class.
        populated_state (DatasetCollectionPopulatedState):
        states (States | Unset): A dictionary of job states and the number of jobs in that state.
    """

    id: str
    model: Literal["ImplicitCollectionJobs"]
    populated_state: DatasetCollectionPopulatedState
    states: States | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model = self.model

        populated_state = self.populated_state.value

        states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model": model,
                "populated_state": populated_state,
            }
        )
        if states is not UNSET:
            field_dict["states"] = states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.states import States

        d = dict(src_dict)
        id = d.pop("id")

        model = cast(Literal["ImplicitCollectionJobs"], d.pop("model"))
        if model != "ImplicitCollectionJobs":
            raise ValueError(f"model must match const 'ImplicitCollectionJobs', got '{model}'")

        populated_state = DatasetCollectionPopulatedState(d.pop("populated_state"))

        _states = d.pop("states", UNSET)
        states: States | Unset
        if isinstance(_states, Unset):
            states = UNSET
        else:
            states = States.from_dict(_states)

        implicit_collection_jobs_state_summary = cls(
            id=id,
            model=model,
            populated_state=populated_state,
            states=states,
        )

        implicit_collection_jobs_state_summary.additional_properties = d
        return implicit_collection_jobs_state_summary

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
