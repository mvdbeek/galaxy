from dataclasses import dataclass

from .allow_tool_state_corrections import AllowToolStateCorrections
from .batch import Batch
from .ds_map import DsMap
from .effective_outputs import EffectiveOutputs
from .history import History
from .history_id import HistoryId
from .inputs import Inputs
from .inputs_by import InputsBy
from .instance import Instance
from .landing_uuid import LandingUuid
from .legacy import Legacy
from .new_history_name import NewHistoryName
from .no_add_to_history import NoAddToHistory
from .parameters import Parameters
from .parameters_normalized import ParametersNormalized
from .preferred_intermediate_object_store_id import PreferredIntermediateObjectStoreId
from .preferred_object_store_id import PreferredObjectStoreId
from .preferred_outputs_object_store_id import PreferredOutputsObjectStoreId
from .replacement_params import ReplacementParams
from .require_exact_tool_versions import RequireExactToolVersions
from .resource_params import ResourceParams
from .scheduler import Scheduler
from .use_cached_job import UseCachedJob
from .version import Version

__all__ = ["InvokeWorkflowPayload"]


@dataclass
class InvokeWorkflowPayload:
    """
    InvokeWorkflowPayload dataclass.

    Args:
        allow_tool_state_corrections (Optional[AllowToolStateCorrections])
                                 : Indicates if tool state corrections are allowed for
                                   workflow invocation.
        batch (Optional[Batch])  : Indicates if the workflow is invoked as a batch.
        ds_map (Optional[DsMap]) : An older alternative to specifying inputs using database
                                   IDs, do not use this and use inputs instead
        effective_outputs (Optional[EffectiveOutputs])
                                 : TODO
        history (Optional[History])
                                 : The encoded history id - passed exactly like this
                                   'hist_id=...' -  into which to import. Or the name of the
                                   new history into which to import.
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        inputs (Optional[Inputs]): TODO
        inputs_by (Optional[InputsBy])
                                 : How the 'inputs' field maps its inputs
                                   (datasets/collections/step parameters) to workflows
                                   steps.
        instance (Optional[Instance])
                                 : True when fetching by Workflow ID, False when fetching by
                                   StoredWorkflow ID
        landing_uuid (Optional[LandingUuid])
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        legacy (Optional[Legacy]): Indicating if to use legacy workflow invocation.
        new_history_name (Optional[NewHistoryName])
                                 : The name of the new history into which to import.
        no_add_to_history (Optional[NoAddToHistory])
                                 : Indicates if the workflow invocation should not be added
                                   to the history.
        parameters (Optional[Parameters])
                                 : Parameters specified per-step for the workflow
                                   invocation, this is legacy and you should generally use
                                   inputs and only specify the formal parameters of a
                                   workflow instead.
        parameters_normalized (Optional[ParametersNormalized])
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
        require_exact_tool_versions (Optional[RequireExactToolVersions])
                                 : If true, exact tool versions are required for workflow
                                   invocation.
        resource_params (Optional[ResourceParams])
                                 : If a workflow_resource_params_file file is defined and
                                   the target workflow is configured to consumer resource
                                   parameters, they can be specified with this parameter.
                                   See https://github.com/galaxyproject/galaxy/pull/4830 for
                                   more information.
        scheduler (Optional[Scheduler])
                                 : Scheduler to use for workflow invocation.
        use_cached_job (Optional[UseCachedJob])
                                 : Indicated whether to use a cached job for workflow
                                   invocation.
        version (Optional[Version])
                                 : The version of the workflow to invoke.
    """

    allow_tool_state_corrections: AllowToolStateCorrections | None = (
        False  # Indicates if tool state corrections are allowed for workflow invocation.
    )
    batch: Batch | None = False  # Indicates if the workflow is invoked as a batch.
    ds_map: DsMap | None = (
        None  # An older alternative to specifying inputs using database IDs, do not use this and use inputs instead
    )
    effective_outputs: EffectiveOutputs | None = None  # TODO
    history: History | None = (
        None  # The encoded history id - passed exactly like this 'hist_id=...' -  into which to import. Or the name of the new history into which to import.
    )
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    inputs: Inputs | None = None  # TODO
    inputs_by: InputsBy | None = (
        None  # How the 'inputs' field maps its inputs (datasets/collections/step parameters) to workflows steps.
    )
    instance: Instance | None = False  # True when fetching by Workflow ID, False when fetching by StoredWorkflow ID
    landing_uuid: LandingUuid | None = None  # The UUID of the workflow landing request associated with this invocation.
    legacy: Legacy | None = False  # Indicating if to use legacy workflow invocation.
    new_history_name: NewHistoryName | None = None  # The name of the new history into which to import.
    no_add_to_history: NoAddToHistory | None = (
        False  # Indicates if the workflow invocation should not be added to the history.
    )
    parameters: Parameters | None = (
        None  # Parameters specified per-step for the workflow invocation, this is legacy and you should generally use inputs and only specify the formal parameters of a workflow instead.
    )
    parameters_normalized: ParametersNormalized | None = (
        False  # Indicates if legacy parameters are already normalized to be indexed by the order_index and are specified as a dictionary per step. Legacy-style parameters could previously be specified as one parameter per step or by tool ID.
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
    require_exact_tool_versions: RequireExactToolVersions | None = (
        True  # If true, exact tool versions are required for workflow invocation.
    )
    resource_params: ResourceParams | None = (
        None  # If a workflow_resource_params_file file is defined and the target workflow is configured to consumer resource parameters, they can be specified with this parameter. See https://github.com/galaxyproject/galaxy/pull/4830 for more information.
    )
    scheduler: Scheduler | None = None  # Scheduler to use for workflow invocation.
    use_cached_job: UseCachedJob | None = False  # Indicated whether to use a cached job for workflow invocation.
    version: Version | None = "1.0"  # The version of the workflow to invoke.
