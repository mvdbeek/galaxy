from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invocation_serialization_view import InvocationSerializationView
from ..models.model_store_format import ModelStoreFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_invocations_from_store_payload_store_dict_type_0 import (
        CreateInvocationsFromStorePayloadStoreDictType0,
    )


T = TypeVar("T", bound="CreateInvocationsFromStorePayload")


@_attrs_define
class CreateInvocationsFromStorePayload:
    """
    Attributes:
        history_id (str): The ID of the history associated with the invocations. Example: 0123456789ABCDEF.
        legacy_job_state (bool | Unset): Populate the invocation step state with the job state instead of the invocation
            step state.
                    This will also produce one step per job in mapping jobs to mimic the older behavior with respect to
            collections.
                    Partially scheduled steps may provide incomplete information and the listed steps outputs
                    are not the mapped over step outputs but the individual job outputs. Default: False.
        model_store_format (ModelStoreFormat | None | Unset):
        step_details (bool | Unset): Include details for individual invocation steps and populate a steps attribute in
            the resulting dictionary Default: False.
        store_content_uri (None | str | Unset):
        store_dict (CreateInvocationsFromStorePayloadStoreDictType0 | None | Unset):
        view (InvocationSerializationView | None | Unset): The name of the view used to serialize this item. This will
            return a predefined set of attributes of the item.
    """

    history_id: str
    legacy_job_state: bool | Unset = False
    model_store_format: ModelStoreFormat | None | Unset = UNSET
    step_details: bool | Unset = False
    store_content_uri: None | str | Unset = UNSET
    store_dict: CreateInvocationsFromStorePayloadStoreDictType0 | None | Unset = UNSET
    view: InvocationSerializationView | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_invocations_from_store_payload_store_dict_type_0 import (
            CreateInvocationsFromStorePayloadStoreDictType0,
        )

        history_id = self.history_id

        legacy_job_state = self.legacy_job_state

        model_store_format: None | str | Unset
        if isinstance(self.model_store_format, Unset):
            model_store_format = UNSET
        elif isinstance(self.model_store_format, ModelStoreFormat):
            model_store_format = self.model_store_format.value
        else:
            model_store_format = self.model_store_format

        step_details = self.step_details

        store_content_uri: None | str | Unset
        if isinstance(self.store_content_uri, Unset):
            store_content_uri = UNSET
        else:
            store_content_uri = self.store_content_uri

        store_dict: dict[str, Any] | None | Unset
        if isinstance(self.store_dict, Unset):
            store_dict = UNSET
        elif isinstance(self.store_dict, CreateInvocationsFromStorePayloadStoreDictType0):
            store_dict = self.store_dict.to_dict()
        else:
            store_dict = self.store_dict

        view: None | str | Unset
        if isinstance(self.view, Unset):
            view = UNSET
        elif isinstance(self.view, InvocationSerializationView):
            view = self.view.value
        else:
            view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_id": history_id,
            }
        )
        if legacy_job_state is not UNSET:
            field_dict["legacy_job_state"] = legacy_job_state
        if model_store_format is not UNSET:
            field_dict["model_store_format"] = model_store_format
        if step_details is not UNSET:
            field_dict["step_details"] = step_details
        if store_content_uri is not UNSET:
            field_dict["store_content_uri"] = store_content_uri
        if store_dict is not UNSET:
            field_dict["store_dict"] = store_dict
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_invocations_from_store_payload_store_dict_type_0 import (
            CreateInvocationsFromStorePayloadStoreDictType0,
        )

        d = dict(src_dict)
        history_id = d.pop("history_id")

        legacy_job_state = d.pop("legacy_job_state", UNSET)

        def _parse_model_store_format(data: object) -> ModelStoreFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_store_format_type_0 = ModelStoreFormat(data)

                return model_store_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelStoreFormat | None | Unset, data)

        model_store_format = _parse_model_store_format(d.pop("model_store_format", UNSET))

        step_details = d.pop("step_details", UNSET)

        def _parse_store_content_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        store_content_uri = _parse_store_content_uri(d.pop("store_content_uri", UNSET))

        def _parse_store_dict(data: object) -> CreateInvocationsFromStorePayloadStoreDictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                store_dict_type_0 = CreateInvocationsFromStorePayloadStoreDictType0.from_dict(data)

                return store_dict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateInvocationsFromStorePayloadStoreDictType0 | None | Unset, data)

        store_dict = _parse_store_dict(d.pop("store_dict", UNSET))

        def _parse_view(data: object) -> InvocationSerializationView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                view_type_0 = InvocationSerializationView(data)

                return view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvocationSerializationView | None | Unset, data)

        view = _parse_view(d.pop("view", UNSET))

        create_invocations_from_store_payload = cls(
            history_id=history_id,
            legacy_job_state=legacy_job_state,
            model_store_format=model_store_format,
            step_details=step_details,
            store_content_uri=store_content_uri,
            store_dict=store_dict,
            view=view,
        )

        create_invocations_from_store_payload.additional_properties = d
        return create_invocations_from_store_payload

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
