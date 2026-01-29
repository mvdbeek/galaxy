from enum import Enum, unique

__all__ = ["CreateWorkflowLandingRequestPayloadWorkflowTargetType"]


@unique
class CreateWorkflowLandingRequestPayloadWorkflowTargetType(str, Enum):
    """
    CreateWorkflowLandingRequestPayloadWorkflowTargetType Enum

    Args:
        stored_workflow (str)    : Value for STORED_WORKFLOW
        workflow (str)           : Value for WORKFLOW
        trs_url (str)            : Value for TRS_URL
    """

    STORED_WORKFLOW = "stored_workflow"
    WORKFLOW = "workflow"
    TRS_URL = "trs_url"
