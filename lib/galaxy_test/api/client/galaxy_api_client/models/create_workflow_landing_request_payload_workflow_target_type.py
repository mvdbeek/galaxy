from enum import Enum


class CreateWorkflowLandingRequestPayloadWorkflowTargetType(str, Enum):
    STORED_WORKFLOW = "stored_workflow"
    TRS_URL = "trs_url"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
