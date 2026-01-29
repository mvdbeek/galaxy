from dataclasses import dataclass

from .description import Description
from .secrets import Secrets
from .uuid_ import Uuid_
from .variables import Variables

__all__ = ["CreateInstancePayload"]


@dataclass
class CreateInstancePayload:
    """
    CreateInstancePayload dataclass.

    Args:
        name (str)               :
        secrets (Secrets)        :
        template_id (str)        :
        template_version (int)   :
        variables (Variables)    :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    name: str
    secrets: Secrets
    template_id: str
    template_version: int
    variables: Variables
    description: Description | None = ""  # Detailed text description for this Quota.
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
