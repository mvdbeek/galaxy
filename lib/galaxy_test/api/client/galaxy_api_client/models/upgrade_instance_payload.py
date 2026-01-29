from dataclasses import dataclass

from .upgrade_instance_payload_secrets import UpgradeInstancePayloadSecrets
from .upgrade_instance_payload_variables import UpgradeInstancePayloadVariables

__all__ = ["UpgradeInstancePayload"]


@dataclass
class UpgradeInstancePayload:
    """
    UpgradeInstancePayload dataclass

    Args:
        secrets (UpgradeInstancePayloadSecrets)
                                 :
        template_version (int)   :
        variables (UpgradeInstancePayloadVariables)
                                 :
    """

    secrets: UpgradeInstancePayloadSecrets
    template_version: int
    variables: UpgradeInstancePayloadVariables

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "secrets": "secrets",
            "template_version": "template_version",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "secrets": "secrets",
            "template_version": "template_version",
            "variables": "variables",
        }
