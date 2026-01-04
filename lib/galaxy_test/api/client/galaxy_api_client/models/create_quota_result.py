from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateQuotaResult")


@_attrs_define
class CreateQuotaResult:
    """
    Attributes:
        id (str): The `encoded identifier` of the quota. Example: 0123456789ABCDEF.
        message (str): Text message describing the result of the operation.
        model_class (Literal['Quota']): The name of the database model class.
        name (str): The name of the quota. This must be unique within a Galaxy instance.
        url (str): The relative URL to get this particular Quota details from the rest API.
        quota_source_label (None | str | Unset): Quota source label
    """

    id: str
    message: str
    model_class: Literal["Quota"]
    name: str
    url: str
    quota_source_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message = self.message

        model_class = self.model_class

        name = self.name

        url = self.url

        quota_source_label: None | str | Unset
        if isinstance(self.quota_source_label, Unset):
            quota_source_label = UNSET
        else:
            quota_source_label = self.quota_source_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "message": message,
                "model_class": model_class,
                "name": name,
                "url": url,
            }
        )
        if quota_source_label is not UNSET:
            field_dict["quota_source_label"] = quota_source_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        message = d.pop("message")

        model_class = cast(Literal["Quota"], d.pop("model_class"))
        if model_class != "Quota":
            raise ValueError(f"model_class must match const 'Quota', got '{model_class}'")

        name = d.pop("name")

        url = d.pop("url")

        def _parse_quota_source_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota_source_label = _parse_quota_source_label(d.pop("quota_source_label", UNSET))

        create_quota_result = cls(
            id=id,
            message=message,
            model_class=model_class,
            name=name,
            url=url,
            quota_source_label=quota_source_label,
        )

        create_quota_result.additional_properties = d
        return create_quota_result

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
