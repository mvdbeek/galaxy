from dataclasses import dataclass

from .test_update_instance_payload_variables import TestUpdateInstancePayloadVariables

__all__ = ["TestUpdateInstancePayload"]


@dataclass
class TestUpdateInstancePayload:
    """
    TestUpdateInstancePayload dataclass

    Args:
        variables (TestUpdateInstancePayloadVariables | None)
                                 :
    """

    variables: TestUpdateInstancePayloadVariables | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "variables": "variables",
        }
        key_transform_with_dump = {
            "variables": "variables",
        }
