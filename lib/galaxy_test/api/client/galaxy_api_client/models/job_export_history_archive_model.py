from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobExportHistoryArchiveModel")


@_attrs_define
class JobExportHistoryArchiveModel:
    """
    Attributes:
        download_url (str): Relative API URL to download the exported history archive.
        external_download_latest_url (str): Fully qualified URL to download the latests version of the exported history
            archive.
        external_download_permanent_url (str): Fully qualified URL to download this particular version of the exported
            history archive.
        id (str): The encoded database ID of the export request. Example: 0123456789ABCDEF.
        job_id (str): The encoded database ID of the job that generated this history export archive. Example:
            0123456789ABCDEF.
        preparing (bool): Whether the archive is currently being built or in preparation.
        ready (bool): Whether the export has completed successfully and the archive is ready
        up_to_date (bool): False, if a new export archive should be generated.
    """

    download_url: str
    external_download_latest_url: str
    external_download_permanent_url: str
    id: str
    job_id: str
    preparing: bool
    ready: bool
    up_to_date: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        external_download_latest_url = self.external_download_latest_url

        external_download_permanent_url = self.external_download_permanent_url

        id = self.id

        job_id = self.job_id

        preparing = self.preparing

        ready = self.ready

        up_to_date = self.up_to_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "download_url": download_url,
                "external_download_latest_url": external_download_latest_url,
                "external_download_permanent_url": external_download_permanent_url,
                "id": id,
                "job_id": job_id,
                "preparing": preparing,
                "ready": ready,
                "up_to_date": up_to_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_url = d.pop("download_url")

        external_download_latest_url = d.pop("external_download_latest_url")

        external_download_permanent_url = d.pop("external_download_permanent_url")

        id = d.pop("id")

        job_id = d.pop("job_id")

        preparing = d.pop("preparing")

        ready = d.pop("ready")

        up_to_date = d.pop("up_to_date")

        job_export_history_archive_model = cls(
            download_url=download_url,
            external_download_latest_url=external_download_latest_url,
            external_download_permanent_url=external_download_permanent_url,
            id=id,
            job_id=job_id,
            preparing=preparing,
            ready=ready,
            up_to_date=up_to_date,
        )

        job_export_history_archive_model.additional_properties = d
        return job_export_history_archive_model

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
