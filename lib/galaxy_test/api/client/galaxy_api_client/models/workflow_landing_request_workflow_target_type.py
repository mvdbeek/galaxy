from enum import Enum


class WorkflowLandingRequestWorkflowTargetType(str, Enum):
    STORED_WORKFLOW = "stored_workflow"
    TRS_URL = "trs_url"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
