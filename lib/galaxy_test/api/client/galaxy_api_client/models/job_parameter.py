from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encoded_job_parameter_history_item import EncodedJobParameterHistoryItem


T = TypeVar("T", bound="JobParameter")


@_attrs_define
class JobParameter:
    """
    Attributes:
        depth (int): The depth of the job parameter.
        text (str): Text associated with the job parameter.
        notes (None | str | Unset): Notes associated with the job parameter.
        value (bool | float | int | list[EncodedJobParameterHistoryItem | None] | None | str | Unset): The values of the
            job parameter
    """

    depth: int
    text: str
    notes: None | str | Unset = UNSET
    value: bool | float | int | list[EncodedJobParameterHistoryItem | None] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.encoded_job_parameter_history_item import EncodedJobParameterHistoryItem

        depth = self.depth

        text = self.text

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        value: bool | float | int | list[dict[str, Any] | None] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item: dict[str, Any] | None
                if isinstance(value_type_0_item_data, EncodedJobParameterHistoryItem):
                    value_type_0_item = value_type_0_item_data.to_dict()
                else:
                    value_type_0_item = value_type_0_item_data
                value.append(value_type_0_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "depth": depth,
                "text": text,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoded_job_parameter_history_item import EncodedJobParameterHistoryItem

        d = dict(src_dict)
        depth = d.pop("depth")

        text = d.pop("text")

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_value(
            data: object,
        ) -> bool | float | int | list[EncodedJobParameterHistoryItem | None] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:

                    def _parse_value_type_0_item(data: object) -> EncodedJobParameterHistoryItem | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_0_item_type_0 = EncodedJobParameterHistoryItem.from_dict(data)

                            return value_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(EncodedJobParameterHistoryItem | None, data)

                    value_type_0_item = _parse_value_type_0_item(value_type_0_item_data)

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | int | list[EncodedJobParameterHistoryItem | None] | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        job_parameter = cls(
            depth=depth,
            text=text,
            notes=notes,
            value=value,
        )

        job_parameter.additional_properties = d
        return job_parameter

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
