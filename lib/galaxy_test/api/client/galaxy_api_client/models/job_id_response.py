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
