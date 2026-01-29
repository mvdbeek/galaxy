from dataclasses import dataclass

from .invoke_workflow_payload_allow_tool_state_corrections import InvokeWorkflowPayloadAllowToolStateCorrections
from .invoke_workflow_payload_batch import InvokeWorkflowPayloadBatch
from .invoke_workflow_payload_ds_map import InvokeWorkflowPayloadDsMap
from .invoke_workflow_payload_effective_outputs import InvokeWorkflowPayloadEffectiveOutputs
from .invoke_workflow_payload_history import InvokeWorkflowPayloadHistory
from .invoke_workflow_payload_history_id import InvokeWorkflowPayloadHistoryId
from .invoke_workflow_payload_inputs import InvokeWorkflowPayloadInputs
from .invoke_workflow_payload_inputs_by import InvokeWorkflowPayloadInputsBy
from .invoke_workflow_payload_instance import InvokeWorkflowPayloadInstance
from .invoke_workflow_payload_landing_uuid import InvokeWorkflowPayloadLandingUuid
from .invoke_workflow_payload_legacy import InvokeWorkflowPayloadLegacy
from .invoke_workflow_payload_new_history_name import InvokeWorkflowPayloadNewHistoryName
from .invoke_workflow_payload_no_add_to_history import InvokeWorkflowPayloadNoAddToHistory
from .invoke_workflow_payload_parameters import InvokeWorkflowPayloadParameters
from .invoke_workflow_payload_parameters_normalized import InvokeWorkflowPayloadParametersNormalized
from .invoke_workflow_payload_preferred_intermediate_object_store_id import (
    InvokeWorkflowPayloadPreferredIntermediateObjectStoreId,
)
from .invoke_workflow_payload_preferred_object_store_id import InvokeWorkflowPayloadPreferredObjectStoreId
from .invoke_workflow_payload_preferred_outputs_object_store_id import (
    InvokeWorkflowPayloadPreferredOutputsObjectStoreId,
)
from .invoke_workflow_payload_replacement_params import InvokeWorkflowPayloadReplacementParams
from .invoke_workflow_payload_require_exact_tool_versions import InvokeWorkflowPayloadRequireExactToolVersions
from .invoke_workflow_payload_resource_params import InvokeWorkflowPayloadResourceParams
from .invoke_workflow_payload_scheduler import InvokeWorkflowPayloadScheduler
from .invoke_workflow_payload_use_cached_job import InvokeWorkflowPayloadUseCachedJob
from .invoke_workflow_payload_version import InvokeWorkflowPayloadVersion

__all__ = ["InvokeWorkflowPayload"]


@dataclass
class InvokeWorkflowPayload:
    """
    InvokeWorkflowPayload dataclass

    Args:
        allow_tool_state_corrections (InvokeWorkflowPayloadAllowToolStateCorrections | None)
                                 : Indicates if tool state corrections are allowed for
                                   workflow invocation.
        batch (InvokeWorkflowPayloadBatch | None)
                                 : Indicates if the workflow is invoked as a batch.
        ds_map (InvokeWorkflowPayloadDsMap | None)
                                 : An older alternative to specifying inputs using database
                                   IDs, do not use this and use inputs instead
        effective_outputs (InvokeWorkflowPayloadEffectiveOutputs | None)
                                 : TODO
        history (InvokeWorkflowPayloadHistory | None)
                                 : The encoded history id - passed exactly like this
                                   'hist_id=...' -  into which to import. Or the name of the
                                   new history into which to import.
        history_id (InvokeWorkflowPayloadHistoryId | None)
                                 : The encoded history id into which to import.
        inputs (InvokeWorkflowPayloadInputs | None)
                                 : Specify values for formal inputs to the workflow
        inputs_by (InvokeWorkflowPayloadInputsBy | None)
                                 : How the 'inputs' field maps its inputs
                                   (datasets/collections/step parameters) to workflows
                                   steps.
        instance (InvokeWorkflowPayloadInstance | None)
                                 : True when fetching by Workflow ID, False when fetching by
                                   StoredWorkflow ID
        landing_uuid (InvokeWorkflowPayloadLandingUuid | None)
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        legacy (InvokeWorkflowPayloadLegacy | None)
                                 : Indicating if to use legacy workflow invocation.
        new_history_name (InvokeWorkflowPayloadNewHistoryName | None)
                                 : The name of the new history into which to import.
        no_add_to_history (InvokeWorkflowPayloadNoAddToHistory | None)
                                 : Indicates if the workflow invocation should not be added
                                   to the history.
        parameters (InvokeWorkflowPayloadParameters | None)
                                 : Parameters specified per-step for the workflow
                                   invocation, this is legacy and you should generally use
                                   inputs and only specify the formal parameters of a
                                   workflow instead.
        parameters_normalized (InvokeWorkflowPayloadParametersNormalized | None)
                                 : Indicates if legacy parameters are already normalized to
                                   be indexed by the order_index and are specified as a
                                   dictionary per step. Legacy-style parameters could
                                   previously be specified as one parameter per step or by
                                   tool ID.
        preferred_intermediate_object_store_id (InvokeWorkflowPayloadPreferredIntermediateObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   the intermediate datasets of this workflow -  - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences
        preferred_object_store_id (InvokeWorkflowPayloadPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        preferred_outputs_object_store_id (InvokeWorkflowPayloadPreferredOutputsObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   the marked output datasets of this workflow - Galaxy's
                                   job configuration may override this in some cases but
                                   this workflow preference will override tool and user
                                   preferences.
        replacement_params (InvokeWorkflowPayloadReplacementParams | None)
                                 : Class of parameters mostly used for string replacement in
                                   PJAs. In best practice workflows, these should be
                                   replaced with input parameters
        require_exact_tool_versions (InvokeWorkflowPayloadRequireExactToolVersions | None)
                                 : If true, exact tool versions are required for workflow
                                   invocation.
        resource_params (InvokeWorkflowPayloadResourceParams | None)
                                 : If a workflow_resource_params_file file is defined and
                                   the target workflow is configured to consumer resource
                                   parameters, they can be specified with this parameter.
                                   See https://github.com/galaxyproject/galaxy/pull/4830 for
                                   more information.
        scheduler (InvokeWorkflowPayloadScheduler | None)
                                 : Scheduler to use for workflow invocation.
        use_cached_job (InvokeWorkflowPayloadUseCachedJob | None)
                                 : Indicated whether to use a cached job for workflow
                                   invocation.
        version (InvokeWorkflowPayloadVersion | None)
                                 : The version of the workflow to invoke.
    """

    allow_tool_state_corrections: InvokeWorkflowPayloadAllowToolStateCorrections | None = (
        False  # Indicates if tool state corrections are allowed for workflow invocation.
    )
    batch: InvokeWorkflowPayloadBatch | None = False  # Indicates if the workflow is invoked as a batch.
    ds_map: InvokeWorkflowPayloadDsMap | None = (
        None  # An older alternative to specifying inputs using database IDs, do not use this and use inputs instead
    )
    effective_outputs: InvokeWorkflowPayloadEffectiveOutputs | None = None  # TODO
    history: InvokeWorkflowPayloadHistory | None = (
        None  # The encoded history id - passed exactly like this 'hist_id=...' -  into which to import. Or the name of the new history into which to import.
    )
    history_id: InvokeWorkflowPayloadHistoryId | None = None  # The encoded history id into which to import.
    inputs: InvokeWorkflowPayloadInputs | None = None  # Specify values for formal inputs to the workflow
    inputs_by: InvokeWorkflowPayloadInputsBy | None = (
        None  # How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps.
    )
    instance: InvokeWorkflowPayloadInstance | None = (
        False  # True when fetching by Workflow ID, False when fetching by StoredWorkflow ID
    )
    landing_uuid: InvokeWorkflowPayloadLandingUuid | None = (
        None  # The UUID of the workflow landing request associated with this invocation.
    )
    legacy: InvokeWorkflowPayloadLegacy | None = False  # Indicating if to use legacy workflow invocation.
    new_history_name: InvokeWorkflowPayloadNewHistoryName | None = (
        None  # The name of the new history into which to import.
    )
    no_add_to_history: InvokeWorkflowPayloadNoAddToHistory | None = (
        False  # Indicates if the workflow invocation should not be added to the history.
    )
    parameters: InvokeWorkflowPayloadParameters | None = (
        None  # Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead.
    )
    parameters_normalized: InvokeWorkflowPayloadParametersNormalized | None = (
        False  # Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.
    )
    preferred_intermediate_object_store_id: InvokeWorkflowPayloadPreferredIntermediateObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the intermediate datasets of this workflow -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_object_store_id: InvokeWorkflowPayloadPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    preferred_outputs_object_store_id: InvokeWorkflowPayloadPreferredOutputsObjectStoreId | None = (
        None  # The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences.
    )
    replacement_params: InvokeWorkflowPayloadReplacementParams | None = (
        None  # Class of parameters mostly used for string replacement in PJAs. In best practice workflows, these should be replaced with input parameters
    )
    require_exact_tool_versions: InvokeWorkflowPayloadRequireExactToolVersions | None = (
        True  # If true, exact tool versions are required for workflow invocation.
    )
    resource_params: InvokeWorkflowPayloadResourceParams | None = (
        None  # If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.
    )
    scheduler: InvokeWorkflowPayloadScheduler | None = None  # Scheduler to use for workflow invocation.
    use_cached_job: InvokeWorkflowPayloadUseCachedJob | None = (
        False  # Indicated whether to use a cached job for workflow invocation.
    )
    version: InvokeWorkflowPayloadVersion | None = None  # The version of the workflow to invoke.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "allow_tool_state_corrections": "allow_tool_state_corrections",
            "batch": "batch",
            "ds_map": "ds_map",
            "effective_outputs": "effective_outputs",
            "history": "history",
            "history_id": "history_id",
            "inputs": "inputs",
            "inputs_by": "inputs_by",
            "instance": "instance",
            "landing_uuid": "landing_uuid",
            "legacy": "legacy",
            "new_history_name": "new_history_name",
            "no_add_to_history": "no_add_to_history",
            "parameters": "parameters",
            "parameters_normalized": "parameters_normalized",
            "preferred_intermediate_object_store_id": "preferred_intermediate_object_store_id",
            "preferred_object_store_id": "preferred_object_store_id",
            "preferred_outputs_object_store_id": "preferred_outputs_object_store_id",
            "replacement_params": "replacement_params",
            "require_exact_tool_versions": "require_exact_tool_versions",
            "resource_params": "resource_params",
            "scheduler": "scheduler",
            "use_cached_job": "use_cached_job",
            "version": "version",
        }
        key_transform_with_dump = {
            "allow_tool_state_corrections": "allow_tool_state_corrections",
            "batch": "batch",
            "ds_map": "ds_map",
            "effective_outputs": "effective_outputs",
            "history": "history",
            "history_id": "history_id",
            "inputs": "inputs",
            "inputs_by": "inputs_by",
            "instance": "instance",
            "landing_uuid": "landing_uuid",
            "legacy": "legacy",
            "new_history_name": "new_history_name",
            "no_add_to_history": "no_add_to_history",
            "parameters": "parameters",
            "parameters_normalized": "parameters_normalized",
            "preferred_intermediate_object_store_id": "preferred_intermediate_object_store_id",
            "preferred_object_store_id": "preferred_object_store_id",
            "preferred_outputs_object_store_id": "preferred_outputs_object_store_id",
            "replacement_params": "replacement_params",
            "require_exact_tool_versions": "require_exact_tool_versions",
            "resource_params": "resource_params",
            "scheduler": "scheduler",
            "use_cached_job": "use_cached_job",
            "version": "version",
        }
