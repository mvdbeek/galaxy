from typing import TypeAlias

from .delete_job_payload import DeleteJobPayload

__all__ = ["JobsDeleteRequestBody"]

JobsDeleteRequestBody: TypeAlias = DeleteJobPayload | None
"""Alias for The values to delete/cancel a job"""
