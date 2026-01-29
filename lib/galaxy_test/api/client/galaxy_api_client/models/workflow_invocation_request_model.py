from dataclasses import dataclass

from .workflow_invocation_request_model_inputs import WorkflowInvocationRequestModelInputs
from .workflow_invocation_request_model_parameters import WorkflowInvocationRequestModelParameters
from .workflow_invocation_request_model_preferred_intermediate_object_store_id import (
    WorkflowInvocationRequestModelPreferredIntermediateObjectStoreId,
)
from .workflow_invocation_request_model_preferred_object_store_id import (
    WorkflowInvocationRequestModelPreferredObjectStoreId,
)
from .workflow_invocation_request_model_preferred_outputs_object_store_id import (
    WorkflowInvocationRequestModelPreferredOutputsObjectStoreId,
)
from .workflow_invocation_request_model_replacement_params import WorkflowInvocationRequestModelReplacementParams
from .workflow_invocation_request_model_resource_params import WorkflowInvocationRequestModelResourceParams

__all__ = ["WorkflowInvocationRequestModel"]


@dataclass
class WorkflowInvocationRequestModel:
    """
    Model a workflow invocation request (InvokeWorkflowPayload) for an existing invocation.

    Args:
        history_id (str)         : The encoded history id the workflow was run in.
        inputs (WorkflowInvocationRequestModelInputs)
                                 : Values for inputs
        inputs_by (str)          : How the 'inputs' field maps its inputs
                                   (datasets/collections/step parameters) to workflows
                                   steps.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        instance (bool | None)   : This API yields a particular workflow instance, newer
                                   workflows belonging to the same storedworkflow may have
                                   different state.
        parameters (WorkflowInvocationRequestModelParameters | None)
                                 : Parameters specified per-step for the workflow
                                   invocation, this is legacy and you should generally use
                                   inputs and only specify the formal parameters of a
                                   workflow instead. If these are set, the workflow was not
                                   executed in a best-practice fashion and we the resulting
                                   invocation request may not fully reflect the executed
                                   workflow state.
        parameters_normalized (bool | None)
                                 : Indicates if legacy parameters are already normalized to
                                   be indexed by the order_index and are specified as a
                                   dictionary per step. Legacy-style parameters could
                                   previously be specified as one parameter per step or by
                                   tool ID.
        preferred_intermediate_object_store_id (WorkflowInvocationRequestModelPreferredIntermediateObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   the intermediate datasets of this workflow -  - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences
        preferred_object_store_id (WorkflowInvocationRequestModelPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        preferred_outputs_object_store_id (WorkflowInvocationRequestModelPreferredOutputsObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   the marked output datasets of this workflow - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences.
        replacement_params (WorkflowInvocationRequestModelReplacementParams | None)
                                 : Class of parameters mostly used for string replacement in
                                   PJAs. In best practice workflows, these should be
                                   replaced with input parameters
        resource_params (WorkflowInvocationRequestModelResourceParams | None)
                                 : If a workflow_resource_params_file file is defined and
                                   the target workflow is configured to consumer resource
                                   parameters, they can be specified with this parameter.
                                   See https://github.com/galaxyproject/galaxy/pull/4830 for
                                   more information.
        use_cached_job (bool | None)
                                 : Indicated whether to use a cached job for workflow
                                   invocation.
    """

    history_id: str  # The encoded history id the workflow was run in.
    inputs: WorkflowInvocationRequestModelInputs  # Values for inputs
    inputs_by: str  # How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    instance: bool | None = (
        True  # This API yields a particular workflow instance, newer workflows belonging to the same storedworkflow may have different state.
    )
    parameters: WorkflowInvocationRequestModelParameters | None = (
        None  # Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead. If these are set, the workflow was not executed in a best-practice fashion and we the resulting invocation request may not fully reflect the executed workflow state.
    )
    parameters_normalized: bool | None = (
        True  # Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.
    )
    preferred_intermediate_object_store_id: WorkflowInvocationRequestModelPreferredIntermediateObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the intermediate datasets of this workflow -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_object_store_id: WorkflowInvocationRequestModelPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_outputs_object_store_id: WorkflowInvocationRequestModelPreferredOutputsObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences.
    )
    replacement_params: WorkflowInvocationRequestModelReplacementParams | None = (
        None  # Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters
    )
    resource_params: WorkflowInvocationRequestModelResourceParams | None = (
        None  # If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.
    )
    use_cached_job: bool | None = False  # Indicated whether to use a cached job for workflow invocation.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "inputs": "inputs",
            "inputs_by": "inputs_by",
            "instance": "instance",
            "parameters": "parameters",
            "parameters_normalized": "parameters_normalized",
            "preferred_intermediate_object_store_id": "preferred_intermediate_object_store_id",
            "preferred_object_store_id": "preferred_object_store_id",
            "preferred_outputs_object_store_id": "preferred_outputs_object_store_id",
            "replacement_params": "replacement_params",
            "resource_params": "resource_params",
            "use_cached_job": "use_cached_job",
            "workflow_id": "workflow_id",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "inputs": "inputs",
            "inputs_by": "inputs_by",
            "instance": "instance",
            "parameters": "parameters",
            "parameters_normalized": "parameters_normalized",
            "preferred_intermediate_object_store_id": "preferred_intermediate_object_store_id",
            "preferred_object_store_id": "preferred_object_store_id",
            "preferred_outputs_object_store_id": "preferred_outputs_object_store_id",
            "replacement_params": "replacement_params",
            "resource_params": "resource_params",
            "use_cached_job": "use_cached_job",
            "workflow_id": "workflow_id",
        }
