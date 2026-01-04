from typing import TypeAlias

from .job_output_association import JobOutputAssociation
from .job_output_collection_association import JobOutputCollectionAssociation

__all__ = ["AnonymousArrayItem214"]

AnonymousArrayItem214: TypeAlias = JobOutputAssociation | JobOutputCollectionAssociation
