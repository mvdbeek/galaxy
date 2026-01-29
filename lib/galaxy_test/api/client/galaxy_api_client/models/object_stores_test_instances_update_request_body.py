from typing import TypeAlias

from .test_update_instance_payload import TestUpdateInstancePayload
from .test_upgrade_instance_payload import TestUpgradeInstancePayload

__all__ = ["ObjectStoresTestInstancesUpdateRequestBody"]

ObjectStoresTestInstancesUpdateRequestBody: TypeAlias = TestUpgradeInstancePayload | TestUpdateInstancePayload
