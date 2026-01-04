from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HDCJobStateSummary")


@_attrs_define
class HDCJobStateSummary:
    """Overview of the job states working inside a dataset collection.

    Attributes:
        all_jobs (int | Unset): Total number of jobs associated with a dataset collection. Default: 0.
        deleted (int | Unset): Number of jobs in the `deleted` state. Default: 0.
        deleted_new (int | Unset): Number of jobs in the `deleted_new` state. Default: 0.
        error (int | Unset): Number of jobs in the `error` state. Default: 0.
        failed (int | Unset): Number of jobs in the `failed` state. Default: 0.
        new (int | Unset): Number of jobs in the `new` state. Default: 0.
        ok (int | Unset): Number of jobs in the `ok` state. Default: 0.
        paused (int | Unset): Number of jobs in the `paused` state. Default: 0.
        queued (int | Unset): Number of jobs in the `queued` state. Default: 0.
        resubmitted (int | Unset): Number of jobs in the `resubmitted` state. Default: 0.
        running (int | Unset): Number of jobs in the `running` state. Default: 0.
        skipped (int | Unset): Number of jobs that were skipped due to conditional workflow step execution. Default: 0.
        upload (int | Unset): Number of jobs in the `upload` state. Default: 0.
        waiting (int | Unset): Number of jobs in the `waiting` state. Default: 0.
    """

    all_jobs: int | Unset = 0
    deleted: int | Unset = 0
    deleted_new: int | Unset = 0
    error: int | Unset = 0
    failed: int | Unset = 0
    new: int | Unset = 0
    ok: int | Unset = 0
    paused: int | Unset = 0
    queued: int | Unset = 0
    resubmitted: int | Unset = 0
    running: int | Unset = 0
    skipped: int | Unset = 0
    upload: int | Unset = 0
    waiting: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_jobs = self.all_jobs

        deleted = self.deleted

        deleted_new = self.deleted_new

        error = self.error

        failed = self.failed

        new = self.new

        ok = self.ok

        paused = self.paused

        queued = self.queued

        resubmitted = self.resubmitted

        running = self.running

        skipped = self.skipped

        upload = self.upload

        waiting = self.waiting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_jobs is not UNSET:
            field_dict["all_jobs"] = all_jobs
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if deleted_new is not UNSET:
            field_dict["deleted_new"] = deleted_new
        if error is not UNSET:
            field_dict["error"] = error
        if failed is not UNSET:
            field_dict["failed"] = failed
        if new is not UNSET:
            field_dict["new"] = new
        if ok is not UNSET:
            field_dict["ok"] = ok
        if paused is not UNSET:
            field_dict["paused"] = paused
        if queued is not UNSET:
            field_dict["queued"] = queued
        if resubmitted is not UNSET:
            field_dict["resubmitted"] = resubmitted
        if running is not UNSET:
            field_dict["running"] = running
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if upload is not UNSET:
            field_dict["upload"] = upload
        if waiting is not UNSET:
            field_dict["waiting"] = waiting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_jobs = d.pop("all_jobs", UNSET)

        deleted = d.pop("deleted", UNSET)

        deleted_new = d.pop("deleted_new", UNSET)

        error = d.pop("error", UNSET)

        failed = d.pop("failed", UNSET)

        new = d.pop("new", UNSET)

        ok = d.pop("ok", UNSET)

        paused = d.pop("paused", UNSET)

        queued = d.pop("queued", UNSET)

        resubmitted = d.pop("resubmitted", UNSET)

        running = d.pop("running", UNSET)

        skipped = d.pop("skipped", UNSET)

        upload = d.pop("upload", UNSET)

        waiting = d.pop("waiting", UNSET)

        hdc_job_state_summary = cls(
            all_jobs=all_jobs,
            deleted=deleted,
            deleted_new=deleted_new,
            error=error,
            failed=failed,
            new=new,
            ok=ok,
            paused=paused,
            queued=queued,
            resubmitted=resubmitted,
            running=running,
            skipped=skipped,
            upload=upload,
            waiting=waiting,
        )

        hdc_job_state_summary.additional_properties = d
        return hdc_job_state_summary

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
