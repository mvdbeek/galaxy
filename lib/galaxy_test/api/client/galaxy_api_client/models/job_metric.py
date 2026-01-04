from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobMetric")


@_attrs_define
class JobMetric:
    """
    Example:
        {'name': 'start_epoch', 'plugin': 'core', 'raw_value': '1614261340.0000000', 'title': 'Job Start Time', 'value':
            '2021-02-25 14:55:40'}

    Attributes:
        name (str): The name of the metric variable.
        plugin (str): The instrumenter plugin that generated this metric.
        raw_value (str): The raw value of the metric as a string.
        title (str): A descriptive title for this metric.
        value (str): The textual representation of the metric value.
    """

    name: str
    plugin: str
    raw_value: str
    title: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        plugin = self.plugin

        raw_value = self.raw_value

        title = self.title

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "plugin": plugin,
                "raw_value": raw_value,
                "title": title,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        plugin = d.pop("plugin")

        raw_value = d.pop("raw_value")

        title = d.pop("title")

        value = d.pop("value")

        job_metric = cls(
            name=name,
            plugin=plugin,
            raw_value=raw_value,
            title=title,
            value=value,
        )

        job_metric.additional_properties = d
        return job_metric

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
