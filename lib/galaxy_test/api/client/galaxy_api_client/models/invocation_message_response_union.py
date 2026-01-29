from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .invocation_cancellation_history_deleted_response import InvocationCancellationHistoryDeletedResponse
from .invocation_cancellation_review_failed_response import InvocationCancellationReviewFailedResponse
from .invocation_cancellation_user_request_response import InvocationCancellationUserRequestResponse
from .invocation_evaluation_warning_workflow_output_not_found_response import (
    InvocationEvaluationWarningWorkflowOutputNotFoundResponse,
)
from .invocation_failure_collection_failed_response import InvocationFailureCollectionFailedResponse
from .invocation_failure_dataset_failed_response import InvocationFailureDatasetFailedResponse
from .invocation_failure_expression_evaluation_failed_response import (
    InvocationFailureExpressionEvaluationFailedResponse,
)
from .invocation_failure_job_failed_response import InvocationFailureJobFailedResponse
from .invocation_failure_output_not_found_response import InvocationFailureOutputNotFoundResponse
from .invocation_failure_when_not_boolean_response import InvocationFailureWhenNotBooleanResponse
from .invocation_failure_workflow_parameter_invalid_response import InvocationFailureWorkflowParameterInvalidResponse
from .invocation_unexpected_failure_response import InvocationUnexpectedFailureResponse

__all__ = ["InvocationMessageResponseUnion", "InvocationMessageResponseUnionDiscriminator"]


@dataclass(frozen=True)
class InvocationMessageResponseUnionDiscriminator:
    """Discriminator metadata for InvocationMessageResponseUnion union."""

    property_name: str = "reason"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("cancelled_on_review", "InvocationCancellationReviewFailedResponse"),
        ("collection_failed", "InvocationFailureCollectionFailedResponse"),
        ("dataset_failed", "InvocationFailureDatasetFailedResponse"),
        ("expression_evaluation_failed", "InvocationFailureExpressionEvaluationFailedResponse"),
        ("history_deleted", "InvocationCancellationHistoryDeletedResponse"),
        ("job_failed", "InvocationFailureJobFailedResponse"),
        ("output_not_found", "InvocationFailureOutputNotFoundResponse"),
        ("unexpected_failure", "InvocationUnexpectedFailureResponse"),
        ("user_request", "InvocationCancellationUserRequestResponse"),
        ("when_not_boolean", "InvocationFailureWhenNotBooleanResponse"),
        ("workflow_output_not_found", "InvocationEvaluationWarningWorkflowOutputNotFoundResponse"),
        ("workflow_parameter_invalid", "InvocationFailureWorkflowParameterInvalidResponse"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .invocation_cancellation_history_deleted_response import InvocationCancellationHistoryDeletedResponse
        from .invocation_cancellation_review_failed_response import InvocationCancellationReviewFailedResponse
        from .invocation_cancellation_user_request_response import InvocationCancellationUserRequestResponse
        from .invocation_evaluation_warning_workflow_output_not_found_response import (
            InvocationEvaluationWarningWorkflowOutputNotFoundResponse,
        )
        from .invocation_failure_collection_failed_response import InvocationFailureCollectionFailedResponse
        from .invocation_failure_dataset_failed_response import InvocationFailureDatasetFailedResponse
        from .invocation_failure_expression_evaluation_failed_response import (
            InvocationFailureExpressionEvaluationFailedResponse,
        )
        from .invocation_failure_job_failed_response import InvocationFailureJobFailedResponse
        from .invocation_failure_output_not_found_response import InvocationFailureOutputNotFoundResponse
        from .invocation_failure_when_not_boolean_response import InvocationFailureWhenNotBooleanResponse
        from .invocation_failure_workflow_parameter_invalid_response import (
            InvocationFailureWorkflowParameterInvalidResponse,
        )
        from .invocation_unexpected_failure_response import InvocationUnexpectedFailureResponse

        return {
            "cancelled_on_review": InvocationCancellationReviewFailedResponse,
            "collection_failed": InvocationFailureCollectionFailedResponse,
            "dataset_failed": InvocationFailureDatasetFailedResponse,
            "expression_evaluation_failed": InvocationFailureExpressionEvaluationFailedResponse,
            "history_deleted": InvocationCancellationHistoryDeletedResponse,
            "job_failed": InvocationFailureJobFailedResponse,
            "output_not_found": InvocationFailureOutputNotFoundResponse,
            "unexpected_failure": InvocationUnexpectedFailureResponse,
            "user_request": InvocationCancellationUserRequestResponse,
            "when_not_boolean": InvocationFailureWhenNotBooleanResponse,
            "workflow_output_not_found": InvocationEvaluationWarningWorkflowOutputNotFoundResponse,
            "workflow_parameter_invalid": InvocationFailureWorkflowParameterInvalidResponse,
        }


InvocationMessageResponseUnion: TypeAlias = Annotated[
    InvocationCancellationReviewFailedResponse
    | InvocationCancellationHistoryDeletedResponse
    | InvocationCancellationUserRequestResponse
    | InvocationFailureDatasetFailedResponse
    | InvocationFailureCollectionFailedResponse
    | InvocationFailureJobFailedResponse
    | InvocationFailureOutputNotFoundResponse
    | InvocationFailureExpressionEvaluationFailedResponse
    | InvocationFailureWhenNotBooleanResponse
    | InvocationUnexpectedFailureResponse
    | InvocationEvaluationWarningWorkflowOutputNotFoundResponse
    | InvocationFailureWorkflowParameterInvalidResponse,
    InvocationMessageResponseUnionDiscriminator(),
]
