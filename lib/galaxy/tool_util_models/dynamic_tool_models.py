import logging
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

from pydantic import BaseModel
from typing_extensions import Literal

from galaxy.tool_util_models import (
    DynamicToolSources,
    lift_user_tool_source,
    UserToolSource,
)

log = logging.getLogger(__name__)


class BaseDynamicToolCreatePayload(BaseModel):
    active: Optional[bool] = None
    hidden: Optional[bool] = None


class DynamicToolCreatePayload(BaseDynamicToolCreatePayload):
    src: Literal["representation"] = "representation"
    representation: DynamicToolSources
    active: Optional[bool] = True
    hidden: Optional[bool] = False


class DynamicUnprivilegedToolCreatePayload(DynamicToolCreatePayload):
    representation: UserToolSource

    @classmethod
    def from_existing_representation(cls, representation: Dict[str, Any]) -> "DynamicUnprivilegedToolCreatePayload":
        """Payload copying a tool Galaxy already stores or received in a workflow, read like a stored tool."""
        status, lifted, changed = lift_user_tool_source(representation)
        if changed:
            log.info("Copying user-defined tool %s with changes: %s", representation.get("id"), ", ".join(changed))
        return cls(representation=representation if status == "invalid" else lifted)


class PathBasedDynamicToolCreatePayload(BaseDynamicToolCreatePayload):
    src: Literal["from_path"]
    path: str
    tool_directory: Optional[str] = None


DynamicToolPayload = Union[DynamicToolCreatePayload, PathBasedDynamicToolCreatePayload]
