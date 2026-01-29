from dataclasses import dataclass

from .secrets import Secrets
from .variables import Variables

__all__ = ["UpgradeInstancePayload"]


@dataclass
class UpgradeInstancePayload:
    """
    UpgradeInstancePayload dataclass.

    Args:
        secrets (Secrets)        :
        template_version (int)   :
        variables (Variables)    :
    """

    secrets: Secrets
    template_version: int
    variables: Variables
