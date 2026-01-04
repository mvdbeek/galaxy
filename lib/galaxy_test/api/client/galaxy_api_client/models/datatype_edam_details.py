from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatatypeEDAMDetails")


@_attrs_define
class DatatypeEDAMDetails:
    """
    Attributes:
        definition (None | str): The EDAM definition
        label (None | str): The EDAM label
        prefix_iri (str): The EDAM prefixed Resource Identifier
    """

    definition: None | str
    label: None | str
    prefix_iri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        definition: None | str
        definition = self.definition

        label: None | str
        label = self.label

        prefix_iri = self.prefix_iri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "definition": definition,
                "label": label,
                "prefix_IRI": prefix_iri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_definition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        definition = _parse_definition(d.pop("definition"))

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        prefix_iri = d.pop("prefix_IRI")

        datatype_edam_details = cls(
            definition=definition,
            label=label,
            prefix_iri=prefix_iri,
        )

        datatype_edam_details.additional_properties = d
        return datatype_edam_details

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
