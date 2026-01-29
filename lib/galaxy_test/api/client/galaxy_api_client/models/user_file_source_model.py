from dataclasses import dataclass

from .description import Description
from .secrets import Secrets
from .type_ import Type_
from .variables import Variables

__all__ = ["UserFileSourceModel"]


@dataclass
class UserFileSourceModel:
    """
    UserFileSourceModel dataclass.

    Args:
        active (bool)            :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        hidden (bool)            :
        name (str)               :
        purged (bool)            :
        secrets (Secrets)        :
        template_id (str)        :
        template_version (int)   :
        type_ (Type_)            : The type of content to be created in the history.
        uri_root (str)           :
        uuid_ (str)              :
        variables (Variables)    :
    """

    active: bool
    description: Description | None  # Detailed text description for this Quota.
    hidden: bool
    name: str
    purged: bool
    secrets: Secrets
    template_id: str
    template_version: int
    type_: Type_  # The type of content to be created in the history.
    uri_root: str
    uuid_: str
    variables: Variables
