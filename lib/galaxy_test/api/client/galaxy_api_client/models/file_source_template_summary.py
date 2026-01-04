from dataclasses import dataclass

from .description import Description
from .name import Name
from .secrets import Secrets
from .type_ import Type_
from .variables import Variables

__all__ = ["FileSourceTemplateSummary"]


@dataclass
class FileSourceTemplateSummary:
    """
    FileSourceTemplateSummary dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        id_ (str)                :
        name (Optional[Name])    : The name of the creator.
        type_ (Type_)            : The type of content to be created in the history.
        hidden (Optional[bool])  :
        secrets (Optional[Secrets])
                                 :
        variables (Optional[Variables])
                                 :
        version (Optional[int])  :
    """

    description: Description | None  # Detailed text description for this Quota.
    id_: str
    name: Name | None  # The name of the creator.
    type_: Type_  # The type of content to be created in the history.
    hidden: bool | None = False
    secrets: Secrets | None = None
    variables: Variables | None = None
    version: int | None = 0
