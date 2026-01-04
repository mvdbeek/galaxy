from dataclasses import dataclass

from .inputs import Inputs
from .parameters import Parameters
from .preferred_intermediate_object_store_id import PreferredIntermediateObjectStoreId
from .preferred_object_store_id import PreferredObjectStoreId
from .preferred_outputs_object_store_id import PreferredOutputsObjectStoreId
from .replacement_params import ReplacementParams
from .resource_params import ResourceParams

__all__ = ["WorkflowInvocationRequestModel"]


@dataclass
class WorkflowInvocationRequestModel:
    """
    Model a workflow invocation request (InvokeWorkflowPayload) for an existing invocation.

    Args:
        history_id (str)         : The encoded history id the workflow was run in.
        inputs (Inputs)          : Values for inputs
        inputs_by (str)          : How the 'inputs' field maps its inputs
                                   (datasets/collections/step parameters) to workflows
                                   steps.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        instance (Optional[bool]): This API yields a particular workflow instance, newer
                                   workflows belonging to the same storedworkflow may have
                                   different state.
        parameters (Optional[Parameters])
                                 : Parameters specified per-step for the workflow
                                   invocation, this is legacy and you should generally use
                                   inputs and only specify the formal parameters of a
                                   workflow instead. If these are set, the workflow was not
                                   executed in a best-practice fashion and we the resulting
                                   invocation request may not fully reflect the executed
                                   workflow state.
        parameters_normalized (Optional[bool])
                                 : Indicates if legacy parameters are already normalized to
                                   be indexed by the order_index and are specified as a
                                   dictionary per step. Legacy-style parameters could
                                   previously be specified as one parameter per step or by
                                   tool ID.
        preferred_intermediate_object_store_id (Optional[PreferredIntermediateObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   the intermediate datasets of this workflow -  - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        preferred_outputs_object_store_id (Optional[PreferredOutputsObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   the marked output datasets of this workflow - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences.
        replacement_params (Optional[ReplacementParams])
                                 : Class of parameters mostly used for string replacement in
                                   PJAs. In best practice workflows, these should be
                                   replaced with input parameters
        resource_params (Optional[ResourceParams])
                                 : If a workflow_resource_params_file file is defined and
                                   the target workflow is configured to consumer resource
                                   parameters, they can be specified with this parameter.
                                   See https://github.com/galaxyproject/galaxy/pull/4830 for
                                   more information.
        use_cached_job (Optional[bool])
                                 : Indicated whether to use a cached job for workflow
                                   invocation.
    """

    history_id: str  # The encoded history id the workflow was run in.
    inputs: Inputs  # Values for inputs
    inputs_by: str  # How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    instance: bool | None = (
        True  # This API yields a particular workflow instance, newer workflows belonging to the same storedworkflow may have different state.
    )
    parameters: Parameters | None = (
        None  # Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead. If these are set, the workflow was not executed in a best-practice fashion and we the resulting invocation request may not fully reflect the executed workflow state.
    )
    parameters_normalized: bool | None = (
        True  # Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.
    )
    preferred_intermediate_object_store_id: PreferredIntermediateObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the intermediate datasets of this workflow -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_outputs_object_store_id: PreferredOutputsObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences.
    )
    replacement_params: ReplacementParams | None = (
        None  # Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters
    )
    resource_params: ResourceParams | None = (
        None  # If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.
    )
    use_cached_job: bool | None = False  # Indicated whether to use a cached job for workflow invocation.
