from typing import TypeAlias

from .job_output_association import JobOutputAssociation
from .job_output_collection_association import JobOutputCollectionAssociation

__all__ = ["AnonymousArrayItem118"]

AnonymousArrayItem118: TypeAlias = JobOutputAssociation | JobOutputCollectionAssociation
