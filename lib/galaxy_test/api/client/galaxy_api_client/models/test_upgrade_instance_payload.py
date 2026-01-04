from dataclasses import dataclass

from .secrets import Secrets
from .variables import Variables

__all__ = ["TestUpgradeInstancePayload"]


@dataclass
class TestUpgradeInstancePayload:
    """
    TestUpgradeInstancePayload dataclass.

    Args:
        secrets (Secrets)        :
        template_version (int)   :
        variables (Variables)    :
    """

    secrets: Secrets
    template_version: int
    variables: Variables
