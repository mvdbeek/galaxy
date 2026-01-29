from dataclasses import dataclass

__all__ = ["JobIdResponse"]


@dataclass
class JobIdResponse:
    """
    Contains the ID of the job associated with a particular request.

    Args:
        job_id (str)             :
    """

    job_id: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "job_id": "job_id",
        }
        key_transform_with_dump = {
            "job_id": "job_id",
        }
