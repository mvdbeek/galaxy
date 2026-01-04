from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkflowJobMetric")


@_attrs_define
class WorkflowJobMetric:
    """
    Example:
        {'name': 'start_epoch', 'plugin': 'core', 'raw_value': '1614261340.0000000', 'title': 'Job Start Time', 'value':
            '2021-02-25 14:55:40'}

    Attributes:
        job_id (str):
        name (str): The name of the metric variable.
        plugin (str): The instrumenter plugin that generated this metric.
        raw_value (str): The raw value of the metric as a string.
        step_index (int):
        step_label (None | str):
        title (str): A descriptive title for this metric.
        tool_id (str):
        value (str): The textual representation of the metric value.
    """

    job_id: str
    name: str
    plugin: str
    raw_value: str
    step_index: int
    step_label: None | str
    title: str
    tool_id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        name = self.name

        plugin = self.plugin

        raw_value = self.raw_value

        step_index = self.step_index

        step_label: None | str
        step_label = self.step_label

        title = self.title

        tool_id = self.tool_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "name": name,
                "plugin": plugin,
                "raw_value": raw_value,
                "step_index": step_index,
                "step_label": step_label,
                "title": title,
                "tool_id": tool_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        name = d.pop("name")

        plugin = d.pop("plugin")

        raw_value = d.pop("raw_value")

        step_index = d.pop("step_index")

        def _parse_step_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_label = _parse_step_label(d.pop("step_label"))

        title = d.pop("title")

        tool_id = d.pop("tool_id")

        value = d.pop("value")

        workflow_job_metric = cls(
            job_id=job_id,
            name=name,
            plugin=plugin,
            raw_value=raw_value,
            step_index=step_index,
            step_label=step_label,
            title=title,
            tool_id=tool_id,
            value=value,
        )

        workflow_job_metric.additional_properties = d
        return workflow_job_metric

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
