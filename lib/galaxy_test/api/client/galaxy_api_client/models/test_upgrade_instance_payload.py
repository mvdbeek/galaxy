from dataclasses import dataclass

from .test_upgrade_instance_payload_secrets import TestUpgradeInstancePayloadSecrets
from .test_upgrade_instance_payload_variables import TestUpgradeInstancePayloadVariables

__all__ = ["TestUpgradeInstancePayload"]


@dataclass
class TestUpgradeInstancePayload:
    """
    TestUpgradeInstancePayload dataclass

    Args:
        secrets (TestUpgradeInstancePayloadSecrets)
                                 :
        template_version (int)   :
        variables (TestUpgradeInstancePayloadVariables)
                                 :
    """

    secrets: TestUpgradeInstancePayloadSecrets
    template_version: int
    variables: TestUpgradeInstancePayloadVariables

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
