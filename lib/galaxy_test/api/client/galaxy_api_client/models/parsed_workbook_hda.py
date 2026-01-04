from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParsedWorkbookHda")


@_attrs_define
class ParsedWorkbookHda:
    """
    Attributes:
        id (str):
        model_class (Literal['HistoryDatasetAssociation'] | Unset):  Default: 'HistoryDatasetAssociation'.
    """

    id: str
    model_class: Literal["HistoryDatasetAssociation"] | Unset = "HistoryDatasetAssociation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_class = self.model_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if model_class is not UNSET:
            field_dict["model_class"] = model_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        model_class = cast(Literal["HistoryDatasetAssociation"] | Unset, d.pop("model_class", UNSET))
        if model_class != "HistoryDatasetAssociation" and not isinstance(model_class, Unset):
            raise ValueError(f"model_class must match const 'HistoryDatasetAssociation', got '{model_class}'")

        parsed_workbook_hda = cls(
            id=id,
            model_class=model_class,
        )

        parsed_workbook_hda.additional_properties = d
        return parsed_workbook_hda

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
