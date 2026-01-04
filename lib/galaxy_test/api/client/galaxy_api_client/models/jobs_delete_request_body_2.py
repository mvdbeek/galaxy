from typing import TypeAlias

from .delete_job_payload import DeleteJobPayload

__all__ = ["JobsDeleteRequestBody2"]

JobsDeleteRequestBody2: TypeAlias = DeleteJobPayload | None
"""Alias for The values to delete/cancel a job"""
