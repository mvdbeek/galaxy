from enum import Enum, unique

__all__ = ["InvocationMessageResponseUnionReasonEnum"]


@unique
class InvocationMessageResponseUnionReasonEnum(str, Enum):
    """
    Discriminator enum for InvocationMessageResponseUnion union types.

    Args:
        cancelled_on_review (str): Value for CANCELLED_ON_REVIEW
        history_deleted (str)    : Value for HISTORY_DELETED
        user_request (str)       : Value for USER_REQUEST
        dataset_failed (str)     : Value for DATASET_FAILED
        collection_failed (str)  : Value for COLLECTION_FAILED
        job_failed (str)         : Value for JOB_FAILED
        output_not_found (str)   : Value for OUTPUT_NOT_FOUND
        expression_evaluation_failed (str)
                                 : Value for EXPRESSION_EVALUATION_FAILED
        when_not_boolean (str)   : Value for WHEN_NOT_BOOLEAN
        unexpected_failure (str) : Value for UNEXPECTED_FAILURE
        workflow_output_not_found (str)
                                 : Value for WORKFLOW_OUTPUT_NOT_FOUND
        workflow_parameter_invalid (str)
                                 : Value for WORKFLOW_PARAMETER_INVALID
    """

    CANCELLED_ON_REVIEW = "cancelled_on_review"
    HISTORY_DELETED = "history_deleted"
    USER_REQUEST = "user_request"
    DATASET_FAILED = "dataset_failed"
    COLLECTION_FAILED = "collection_failed"
    JOB_FAILED = "job_failed"
    OUTPUT_NOT_FOUND = "output_not_found"
    EXPRESSION_EVALUATION_FAILED = "expression_evaluation_failed"
    WHEN_NOT_BOOLEAN = "when_not_boolean"
    UNEXPECTED_FAILURE = "unexpected_failure"
    WORKFLOW_OUTPUT_NOT_FOUND = "workflow_output_not_found"
    WORKFLOW_PARAMETER_INVALID = "workflow_parameter_invalid"
