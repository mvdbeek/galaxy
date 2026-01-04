from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_object_metadata import ExportObjectMetadata


T = TypeVar("T", bound="ObjectExportTaskResponse")


@_attrs_define
class ObjectExportTaskResponse:
    """
    Attributes:
        create_time (datetime.datetime): The time and date this item was created.
        id (str): The encoded database ID of the export request. Example: 0123456789ABCDEF.
        preparing (bool): Whether the archive is currently being built or in preparation.
        ready (bool): Whether the export has completed successfully and the archive is ready
        task_uuid (str): The identifier of the task processing the export.
        up_to_date (bool): False, if a new export archive should be generated.
        export_metadata (ExportObjectMetadata | None | Unset):
    """

    create_time: datetime.datetime
    id: str
    preparing: bool
    ready: bool
    task_uuid: str
    up_to_date: bool
    export_metadata: ExportObjectMetadata | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_object_metadata import ExportObjectMetadata

        create_time = self.create_time.isoformat()

        id = self.id

        preparing = self.preparing

        ready = self.ready

        task_uuid = self.task_uuid

        up_to_date = self.up_to_date

        export_metadata: dict[str, Any] | None | Unset
        if isinstance(self.export_metadata, Unset):
            export_metadata = UNSET
        elif isinstance(self.export_metadata, ExportObjectMetadata):
            export_metadata = self.export_metadata.to_dict()
        else:
            export_metadata = self.export_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_time": create_time,
                "id": id,
                "preparing": preparing,
                "ready": ready,
                "task_uuid": task_uuid,
                "up_to_date": up_to_date,
            }
        )
        if export_metadata is not UNSET:
            field_dict["export_metadata"] = export_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_object_metadata import ExportObjectMetadata

        d = dict(src_dict)
        create_time = isoparse(d.pop("create_time"))

        id = d.pop("id")

        preparing = d.pop("preparing")

        ready = d.pop("ready")

        task_uuid = d.pop("task_uuid")

        up_to_date = d.pop("up_to_date")

        def _parse_export_metadata(data: object) -> ExportObjectMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                export_metadata_type_0 = ExportObjectMetadata.from_dict(data)

                return export_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportObjectMetadata | None | Unset, data)

        export_metadata = _parse_export_metadata(d.pop("export_metadata", UNSET))

        object_export_task_response = cls(
            create_time=create_time,
            id=id,
            preparing=preparing,
            ready=ready,
            task_uuid=task_uuid,
            up_to_date=up_to_date,
            export_metadata=export_metadata,
        )

        object_export_task_response.additional_properties = d
        return object_export_task_response

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
