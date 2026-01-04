from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="YamlTemplateConfigFile")


@_attrs_define
class YamlTemplateConfigFile:
    """
    Attributes:
        content (str):
        eval_engine (Literal['ecmascript'] | Unset):  Default: 'ecmascript'.
        filename (None | str | Unset):
        name (None | str | Unset):
    """

    content: str
    eval_engine: Literal["ecmascript"] | Unset = "ecmascript"
    filename: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        eval_engine = self.eval_engine

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if eval_engine is not UNSET:
            field_dict["eval_engine"] = eval_engine
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        eval_engine = cast(Literal["ecmascript"] | Unset, d.pop("eval_engine", UNSET))
        if eval_engine != "ecmascript" and not isinstance(eval_engine, Unset):
            raise ValueError(f"eval_engine must match const 'ecmascript', got '{eval_engine}'")

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        yaml_template_config_file = cls(
            content=content,
            eval_engine=eval_engine,
            filename=filename,
            name=name,
        )

        yaml_template_config_file.additional_properties = d
        return yaml_template_config_file

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
