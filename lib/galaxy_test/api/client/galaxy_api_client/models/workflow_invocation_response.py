from typing import TypeAlias

from .workflow_invocation_collection_view import WorkflowInvocationCollectionView
from .workflow_invocation_element_view import WorkflowInvocationElementView

__all__ = ["WorkflowInvocationResponse"]

WorkflowInvocationResponse: TypeAlias = WorkflowInvocationElementView | WorkflowInvocationCollectionView
