from typing import TypeAlias

from .update_instance_payload import UpdateInstancePayload
from .update_instance_secret_payload import UpdateInstanceSecretPayload
from .upgrade_instance_payload import UpgradeInstancePayload

__all__ = ["ObjectStoresInstancesUpdateRequestBody"]

ObjectStoresInstancesUpdateRequestBody: TypeAlias = (
    UpdateInstanceSecretPayload | UpgradeInstancePayload | UpdateInstancePayload
)
