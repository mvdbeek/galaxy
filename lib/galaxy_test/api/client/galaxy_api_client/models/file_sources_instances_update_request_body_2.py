from typing import TypeAlias

from .update_instance_payload import UpdateInstancePayload
from .update_instance_secret_payload import UpdateInstanceSecretPayload
from .upgrade_instance_payload import UpgradeInstancePayload

__all__ = ["FileSourcesInstancesUpdateRequestBody2"]

FileSourcesInstancesUpdateRequestBody2: TypeAlias = (
    UpdateInstancePayload | UpdateInstanceSecretPayload | UpgradeInstancePayload
)
