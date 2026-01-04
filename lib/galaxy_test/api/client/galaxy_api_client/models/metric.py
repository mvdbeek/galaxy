from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Metric")


@_attrs_define
class Metric:
    """
    Attributes:
        args (str): A JSON string containing an array of extra data.
        level (int): An integer representing the metric's log level.
        namespace (str): Label indicating the source of the metric.
        time (str): The timestamp in ISO format.
    """

    args: str
    level: int
    namespace: str
    time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        args = self.args

        level = self.level

        namespace = self.namespace

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
                "level": level,
                "namespace": namespace,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        args = d.pop("args")

        level = d.pop("level")

        namespace = d.pop("namespace")

        time = d.pop("time")

        metric = cls(
            args=args,
            level=level,
            namespace=namespace,
            time=time,
        )

        metric.additional_properties = d
        return metric

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
