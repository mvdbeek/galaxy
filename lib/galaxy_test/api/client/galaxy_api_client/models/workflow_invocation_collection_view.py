from dataclasses import dataclass
from datetime import datetime

from .invocation_state import InvocationState
from .landing_uuid import LandingUuid
from .uuid_ import Uuid_

__all__ = ["WorkflowInvocationCollectionView"]


@dataclass
class WorkflowInvocationCollectionView:
    """
    WorkflowInvocationCollectionView dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        history_id (str)         : The encoded ID of the history associated with the
                                   invocation.
        id_ (str)                : The encoded ID of the workflow invocation.
        model_class (str)        : The name of the database model class.
        state (InvocationState)  :
        update_time (datetime)   : The last time and date this item was updated.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        landing_uuid (Optional[LandingUuid])
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    create_time: datetime  # The time and date this item was created.
    history_id: str  # The encoded ID of the history associated with the invocation.
    id_: str  # The encoded ID of the workflow invocation.
    model_class: str  # The name of the database model class.
    state: InvocationState
    update_time: datetime  # The last time and date this item was updated.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    landing_uuid: LandingUuid | None = None  # The UUID of the workflow landing request associated with this invocation.
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
