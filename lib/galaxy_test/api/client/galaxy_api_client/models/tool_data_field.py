from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fields import Fields
    from ..models.files import Files


T = TypeVar("T", bound="ToolDataField")


@_attrs_define
class ToolDataField:
    """
    Attributes:
        base_dir (list[str]): A list of directories where the data files are stored
        fields (Fields):
        files (Files): A dictionary of file names and their size in bytes
        fingerprint (str): SHA1 Hash
        model_class (str): The name of class modelling this tool data field
        name (str): The name of the field
    """

    base_dir: list[str]
    fields: Fields
    files: Files
    fingerprint: str
    model_class: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_dir = self.base_dir

        fields = self.fields.to_dict()

        files = self.files.to_dict()

        fingerprint = self.fingerprint

        model_class = self.model_class

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_dir": base_dir,
                "fields": fields,
                "files": files,
                "fingerprint": fingerprint,
                "model_class": model_class,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields import Fields
        from ..models.files import Files

        d = dict(src_dict)
        base_dir = cast(list[str], d.pop("base_dir"))

        fields = Fields.from_dict(d.pop("fields"))

        files = Files.from_dict(d.pop("files"))

        fingerprint = d.pop("fingerprint")

        model_class = d.pop("model_class")

        name = d.pop("name")

        tool_data_field = cls(
            base_dir=base_dir,
            fields=fields,
            files=files,
            fingerprint=fingerprint,
            model_class=model_class,
            name=name,
        )

        tool_data_field.additional_properties = d
        return tool_data_field

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
