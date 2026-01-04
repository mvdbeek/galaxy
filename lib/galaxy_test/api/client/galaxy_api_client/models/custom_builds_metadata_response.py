from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.label_value_pair import LabelValuePair


T = TypeVar("T", bound="CustomBuildsMetadataResponse")


@_attrs_define
class CustomBuildsMetadataResponse:
    """
    Attributes:
        fasta_hdas (list[LabelValuePair]): A list of label/value pairs with all the datasets of type `FASTA` contained
            in the History.
             - `label` is item position followed by the name of the dataset.
             - `value` is the encoded database ID of the dataset.
        installed_builds (list[LabelValuePair]): TODO
    """

    fasta_hdas: list[LabelValuePair]
    installed_builds: list[LabelValuePair]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fasta_hdas = []
        for fasta_hdas_item_data in self.fasta_hdas:
            fasta_hdas_item = fasta_hdas_item_data.to_dict()
            fasta_hdas.append(fasta_hdas_item)

        installed_builds = []
        for installed_builds_item_data in self.installed_builds:
            installed_builds_item = installed_builds_item_data.to_dict()
            installed_builds.append(installed_builds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fasta_hdas": fasta_hdas,
                "installed_builds": installed_builds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_value_pair import LabelValuePair

        d = dict(src_dict)
        fasta_hdas = []
        _fasta_hdas = d.pop("fasta_hdas")
        for fasta_hdas_item_data in _fasta_hdas:
            fasta_hdas_item = LabelValuePair.from_dict(fasta_hdas_item_data)

            fasta_hdas.append(fasta_hdas_item)

        installed_builds = []
        _installed_builds = d.pop("installed_builds")
        for installed_builds_item_data in _installed_builds:
            installed_builds_item = LabelValuePair.from_dict(installed_builds_item_data)

            installed_builds.append(installed_builds_item)

        custom_builds_metadata_response = cls(
            fasta_hdas=fasta_hdas,
            installed_builds=installed_builds,
        )

        custom_builds_metadata_response.additional_properties = d
        return custom_builds_metadata_response

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
