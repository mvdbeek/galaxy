from dataclasses import dataclass
from datetime import datetime

from .invocation_state import InvocationState
from .uuid__9 import Uuid9
from .workflow_invocation_collection_view_landing_uuid import WorkflowInvocationCollectionViewLandingUuid

__all__ = ["WorkflowInvocationCollectionView"]


@dataclass
class WorkflowInvocationCollectionView:
    """
    WorkflowInvocationCollectionView dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        history_id (str)         : The encoded ID of the history associated with the
                                   invocation.
        id_ (str)                : The encoded ID of the workflow invocation. (maps from
                                   'id')
        model_class (str)        : The name of the database model class.
        state (InvocationState)  :
        update_time (datetime)   : The last time and date this item was updated.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        landing_uuid (WorkflowInvocationCollectionViewLandingUuid | None)
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        uuid_ (Uuid9 | None)     : Universal unique identifier of the workflow invocation.
                                   (maps from 'uuid')
    """

    create_time: datetime  # The time and date this item was created.
    history_id: str  # The encoded ID of the history associated with the invocation.
    id_: str  # The encoded ID of the workflow invocation. (maps from 'id')
    model_class: str  # The name of the database model class.
    state: InvocationState
    update_time: datetime  # The last time and date this item was updated.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    landing_uuid: WorkflowInvocationCollectionViewLandingUuid | None = (
        None  # The UUID of the workflow landing request associated with this invocation.
    )
    uuid_: Uuid9 | None = None  # Universal unique identifier of the workflow invocation. (maps from 'uuid')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "history_id": "history_id",
            "id": "id_",
            "landing_uuid": "landing_uuid",
            "model_class": "model_class",
            "state": "state",
            "update_time": "update_time",
            "uuid": "uuid_",
            "workflow_id": "workflow_id",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "history_id": "history_id",
            "id_": "id",
            "landing_uuid": "landing_uuid",
            "model_class": "model_class",
            "state": "state",
            "update_time": "update_time",
            "uuid_": "uuid",
            "workflow_id": "workflow_id",
        }
