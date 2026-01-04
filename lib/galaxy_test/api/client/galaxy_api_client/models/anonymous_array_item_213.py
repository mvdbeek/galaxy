from typing import TypeAlias

from .job_output_association import JobOutputAssociation
from .job_output_collection_association import JobOutputCollectionAssociation

__all__ = ["AnonymousArrayItem213"]

AnonymousArrayItem213: TypeAlias = JobOutputAssociation | JobOutputCollectionAssociation
