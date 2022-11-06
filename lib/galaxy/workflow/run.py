import logging
import os
import uuid
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    TYPE_CHECKING,
    Union,
)

from typing_extensions import Protocol

from galaxy import model
from galaxy.model import (
    WorkflowInvocation,
    WorkflowInvocationStep,
)
from galaxy.tool_util.cwl.util import abs_path
from galaxy.util import ExecutionTimer
from galaxy.workflow import modules
from galaxy.workflow.run_request import (
    workflow_request_to_run_config,
    workflow_run_config_to_request,
    WorkflowRunConfig,
)

if TYPE_CHECKING:
    from galaxy.model import (
        Workflow,
        WorkflowOutput,
        WorkflowStep,
        WorkflowStepConnection,
    )
    from galaxy.webapps.base.webapp import GalaxyWebTransaction
    from galaxy.work.context import WorkRequestContext

log = logging.getLogger(__name__)

WorkflowOutputsType = Dict[int, Any]


# Entry point for core workflow scheduler.
def schedule(
    trans: "WorkRequestContext",
    workflow: "Workflow",
    workflow_run_config: WorkflowRunConfig,
    workflow_invocation: WorkflowInvocation,
) -> Tuple[WorkflowOutputsType, WorkflowInvocation]:
    return __invoke(trans, workflow, workflow_run_config, workflow_invocation)


def __invoke(
    trans: "WorkRequestContext",
    workflow: "Workflow",
    workflow_run_config: WorkflowRunConfig,
    workflow_invocation: Optional[WorkflowInvocation] = None,
    populate_state: bool = False,
) -> Tuple[WorkflowOutputsType, WorkflowInvocation]:
    """Run the supplied workflow in the supplied target_history."""
    if populate_state:
        modules.populate_module_and_state(
            trans,
            workflow,
            workflow_run_config.param_map,
            allow_tool_state_corrections=workflow_run_config.allow_tool_state_corrections,
        )

    invoker = WorkflowInvoker(
        trans,
        workflow,
        workflow_run_config,
        workflow_invocation=workflow_invocation,
    )
    workflow_invocation = invoker.workflow_invocation
    try:
        outputs = invoker.invoke()
    except modules.CancelWorkflowEvaluation:
        if workflow_invocation.cancel():
            trans.sa_session.add(workflow_invocation)
        outputs = {}
    except Exception:
        log.exception("Failed to execute scheduled workflow.")
        # Running workflow invocation in background, just mark
        # persistent workflow invocation as failed.
        workflow_invocation.fail()
        trans.sa_session.add(workflow_invocation)
        outputs = {}

    # Be sure to update state of workflow_invocation.
    trans.sa_session.flush()

    return outputs, workflow_invocation


def queue_invoke(
    trans: "GalaxyWebTransaction",
    workflow: "Workflow",
    workflow_run_config: WorkflowRunConfig,
    request_params: Optional[Dict[str, Any]] = None,
    populate_state: bool = True,
    flush: bool = True,
) -> WorkflowInvocation:
    request_params = request_params or {}
    if populate_state:
        modules.populate_module_and_state(
            trans,
            workflow,
            workflow_run_config.param_map,
            allow_tool_state_corrections=workflow_run_config.allow_tool_state_corrections,
        )
    workflow_invocation = workflow_run_config_to_request(trans, workflow_run_config, workflow)
    workflow_invocation.workflow = workflow
    return trans.app.workflow_scheduling_manager.queue(workflow_invocation, request_params, flush=flush)


class WorkflowInvoker:
    def __init__(
        self,
        trans: "WorkRequestContext",
        workflow: "Workflow",
        workflow_run_config: WorkflowRunConfig,
        workflow_invocation: Optional[WorkflowInvocation] = None,
        progress: Optional["WorkflowProgress"] = None,
    ) -> None:
        self.trans = trans
        self.workflow = workflow
        self.workflow_invocation: WorkflowInvocation
        if progress is not None:
            assert workflow_invocation is None
            workflow_invocation = progress.workflow_invocation

        if workflow_invocation is None:
            invocation_uuid = uuid.uuid1()

            workflow_invocation = WorkflowInvocation()
            workflow_invocation.workflow = self.workflow

            # In one way or another, following attributes will become persistent
            # so they are available during delayed/revisited workflow scheduling.
            workflow_invocation.uuid = invocation_uuid
            workflow_invocation.history = workflow_run_config.target_history

        self.workflow_invocation = workflow_invocation

        module_injector = modules.WorkflowModuleInjector(trans)
        if progress is None:
            progress = WorkflowProgress(
                self.workflow_invocation,
                workflow_run_config.inputs,
                module_injector,
                param_map=workflow_run_config.param_map,
                jobs_per_scheduling_iteration=getattr(
                    trans.app.config, "maximum_workflow_jobs_per_scheduling_iteration", -1
                ),
                copy_inputs_to_history=workflow_run_config.copy_inputs_to_history,
                use_cached_job=workflow_run_config.use_cached_job,
                replacement_dict=workflow_run_config.replacement_dict,
            )
        self.progress = progress

    def invoke(self) -> Dict[int, Any]:
        workflow_invocation = self.workflow_invocation
        config = self.trans.app.config
        maximum_duration = getattr(config, "maximum_workflow_invocation_duration", -1)
        if maximum_duration > 0 and workflow_invocation.seconds_since_created > maximum_duration:
            log.debug(
                f"Workflow invocation [{workflow_invocation.id}] exceeded maximum number of seconds allowed for scheduling [{maximum_duration}], failing."
            )
            workflow_invocation.state = model.WorkflowInvocation.states.FAILED
            # All jobs ran successfully, so we can save now
            self.trans.sa_session.add(workflow_invocation)

            # Not flushing in here, because web controller may create multiple
            # invocations.
            return self.progress.outputs

        if workflow_invocation.history.deleted:
            log.info("Cancelled workflow evaluation due to deleted history")
            raise modules.CancelWorkflowEvaluation()

        remaining_steps = self.progress.remaining_steps()
        delayed_steps = False
        max_jobs_per_iteration_reached = False
        for (step, workflow_invocation_step) in remaining_steps:
            max_jobs_to_schedule = self.progress.maximum_jobs_to_schedule_or_none
            if max_jobs_to_schedule is not None and max_jobs_to_schedule <= 0:
                max_jobs_per_iteration_reached = True
                break
            step_delayed = False
            step_timer = ExecutionTimer()
            try:
                self.__check_implicitly_dependent_steps(step)

                if not workflow_invocation_step:
                    workflow_invocation_step = WorkflowInvocationStep()
                    assert workflow_invocation_step
                    workflow_invocation_step.workflow_invocation = workflow_invocation
                    workflow_invocation_step.workflow_step = step
                    workflow_invocation_step.state = "new"

                    workflow_invocation.steps.append(workflow_invocation_step)

                assert workflow_invocation_step
                incomplete_or_none = self._invoke_step(workflow_invocation_step)
                if incomplete_or_none is False:
                    step_delayed = delayed_steps = True
                    workflow_invocation_step.state = "ready"
                    self.progress.mark_step_outputs_delayed(step, why="Not all jobs scheduled for state.")
                else:
                    workflow_invocation_step.state = "scheduled"
            except modules.DelayedWorkflowEvaluation as de:
                step_delayed = delayed_steps = True
                self.progress.mark_step_outputs_delayed(step, why=de.why)
            except Exception:
                log.exception(
                    "Failed to schedule %s, problem occurred on %s.",
                    self.workflow_invocation.workflow.log_str(),
                    step.log_str(),
                )
                raise

            if not step_delayed:
                log.debug(f"Workflow step {step.id} of invocation {workflow_invocation.id} invoked {step_timer}")

        if delayed_steps or max_jobs_per_iteration_reached:
            state = model.WorkflowInvocation.states.READY
        else:
            state = model.WorkflowInvocation.states.SCHEDULED
        workflow_invocation.state = state

        # All jobs ran successfully, so we can save now
        self.trans.sa_session.add(workflow_invocation)

        # Not flushing in here, because web controller may create multiple
        # invocations.
        return self.progress.outputs

    def __check_implicitly_dependent_steps(self, step):
        """Method will delay the workflow evaluation if implicitly dependent
        steps (steps dependent but not through an input->output way) are not
        yet complete.
        """
        for input_connection in step.input_connections:
            if input_connection.non_data_connection:
                output_id = input_connection.output_step.id
                self.__check_implicitly_dependent_step(output_id)

    def __check_implicitly_dependent_step(self, output_id):
        step_invocation = self.workflow_invocation.step_invocation_for_step_id(output_id)

        # No steps created yet - have to delay evaluation.
        if not step_invocation:
            delayed_why = f"depends on step [{output_id}] but that step has not been invoked yet"
            raise modules.DelayedWorkflowEvaluation(why=delayed_why)

        if step_invocation.state != "scheduled":
            delayed_why = f"depends on step [{output_id}] job has not finished scheduling yet"
            raise modules.DelayedWorkflowEvaluation(delayed_why)

        # TODO: Handle implicit dependency on stuff like pause steps.
        for job in step_invocation.jobs:
            # At least one job in incomplete.
            if not job.finished:
                delayed_why = (
                    f"depends on step [{output_id}] but one or more jobs created from that step have not finished yet"
                )
                raise modules.DelayedWorkflowEvaluation(why=delayed_why)

            if job.state != job.states.OK:
                raise modules.CancelWorkflowEvaluation()

    def _invoke_step(self, invocation_step: WorkflowInvocationStep) -> Optional[bool]:
        incomplete_or_none = invocation_step.workflow_step.module.execute(
            self.trans, self.progress, invocation_step, use_cached_job=self.progress.use_cached_job
        )
        return incomplete_or_none


STEP_OUTPUT_DELAYED = object()


class ModuleInjector(Protocol):
    trans: "WorkRequestContext"

    def inject(self, step, step_args=None, steps=None, **kwargs):
        pass


class WorkflowProgress:
    def __init__(
        self,
        workflow_invocation: WorkflowInvocation,
        inputs_by_step_id: Any,
        module_injector: ModuleInjector,
        param_map: Dict[int, Dict[str, Any]],
        jobs_per_scheduling_iteration: int = -1,
        copy_inputs_to_history: bool = False,
        use_cached_job: bool = False,
        replacement_dict: Optional[Dict[str, str]] = None,
        workflow_mapping_structure=None,
    ) -> None:
        self.outputs: Dict[int, Any] = {}
        self.module_injector = module_injector
        self.workflow_invocation = workflow_invocation
        self.inputs_by_step_id = inputs_by_step_id
        self.param_map = param_map
        self.jobs_per_scheduling_iteration = jobs_per_scheduling_iteration
        self.jobs_scheduled_this_iteration = 0
        self.copy_inputs_to_history = copy_inputs_to_history
        self.use_cached_job = use_cached_job
        self.replacement_dict = replacement_dict or {}
        self.workflow_mapping_structure = workflow_mapping_structure

    @property
    def maximum_jobs_to_schedule_or_none(self) -> Optional[int]:
        if self.jobs_per_scheduling_iteration > 0:
            return self.jobs_per_scheduling_iteration - self.jobs_scheduled_this_iteration
        else:
            return None

    @property
    def trans(self):
        return self.module_injector.trans

    def record_executed_job_count(self, job_count: int) -> None:
        self.jobs_scheduled_this_iteration += job_count

    def remaining_steps(
        self,
    ) -> List[Tuple["WorkflowStep", Optional[WorkflowInvocationStep]]]:
        # Previously computed and persisted step states.
        step_states = self.workflow_invocation.step_states_by_step_id()
        steps = self.workflow_invocation.workflow.steps

        # TODO: Wouldn't a generator be much better here so we don't have to reason about
        # steps we are no where near ready to schedule?
        remaining_steps = []
        step_invocations_by_id = self.workflow_invocation.step_invocations_by_step_id()
        for step in steps:
            step_id = step.id
            if not hasattr(step, "module"):
                self.module_injector.inject(step, step_args=self.param_map.get(step.id, {}))
                if step_id not in step_states:
                    raise Exception(
                        f"Workflow invocation [{self.workflow_invocation.id}] has no step state for step {step.log_str()}. States ids are {list(step_states.keys())}."
                    )
                runtime_state = step_states[step_id].value
                assert step.module
                step.state = step.module.decode_runtime_state(runtime_state)

            invocation_step = step_invocations_by_id.get(step_id, None)
            if invocation_step and invocation_step.state == "scheduled":
                self._recover_mapping(invocation_step)
            else:
                remaining_steps.append((step, invocation_step))
        return remaining_steps

    def replacement_for_input_connections(self, step: "WorkflowStep", input_dict, connections):
        replacement = modules.NO_REPLACEMENT

        prefixed_name = input_dict["name"]
        step_input = step.inputs_by_name.get(prefixed_name, None)

        merge_type = model.WorkflowStepInput.default_merge_type
        if step_input:
            merge_type = step_input.merge_type

        is_data = input_dict["input_type"] in ["dataset", "dataset_collection"]
        if len(connections) == 1:
            replacement = self.replacement_for_connection(connections[0], is_data=is_data)
        else:
            # We've mapped multiple individual inputs to a single parameter,
            # promote output to a collection.
            inputs = []
            input_history_content_type = None
            input_collection_type = None
            for i, c in enumerate(connections):
                input_from_connection = self.replacement_for_connection(c, is_data=is_data)
                is_data = hasattr(input_from_connection, "history_content_type")
                if is_data:
                    input_history_content_type = input_from_connection.history_content_type
                    if i == 0:
                        if input_history_content_type == "dataset_collection":
                            input_collection_type = input_from_connection.collection.collection_type
                        else:
                            input_collection_type = None
                    else:
                        if input_collection_type is None:
                            if input_history_content_type != "dataset":
                                raise Exception("Cannot map over a combination of datasets and collections.")
                        else:
                            if input_history_content_type != "dataset_collection":
                                raise Exception("Cannot merge over combinations of datasets and collections.")
                            elif input_from_connection.collection.collection_type != input_collection_type:
                                raise Exception("Cannot merge collections of different collection types.")

                inputs.append(input_from_connection)

            if input_dict["input_type"] == "dataset_collection":
                # TODO: Implement more nested types here...
                if input_dict.get("collection_types") != ["list"]:
                    return self.replacement_for_connection(connections[0], is_data=is_data)

            collection = model.DatasetCollection()
            # If individual datasets provided (type is None) - premote to a list.
            collection.collection_type = input_collection_type or "list"

            next_index = 0
            if input_collection_type is None:

                if merge_type == "merge_nested":
                    raise NotImplementedError()

                for input in inputs:
                    model.DatasetCollectionElement(
                        collection=collection,
                        element=input,
                        element_index=next_index,
                        element_identifier=str(next_index),
                    )
                    next_index += 1

            elif input_collection_type == "list":
                if merge_type == "merge_flattened":
                    for input in inputs:
                        for dataset_instance in input.dataset_instances:
                            model.DatasetCollectionElement(
                                collection=collection,
                                element=dataset_instance,
                                element_index=next_index,
                                element_identifier=str(next_index),
                            )
                            next_index += 1
                elif merge_type == "merge_nested":
                    # Increase nested level of collection
                    collection.collection_type = f"list:{input_collection_type}"
                    for input in inputs:
                        model.DatasetCollectionElement(
                            collection=collection,
                            element=input.collection,
                            element_index=next_index,
                            element_identifier=str(next_index),
                        )
                        next_index += 1
            else:
                raise NotImplementedError()

            return modules.EphemeralCollection(
                collection=collection,
                history=self.workflow_invocation.history,
            )

        return replacement

    def replacement_for_input(self, step: "WorkflowStep", input_dict: Dict[str, Any]) -> Any:
        replacement: Union[
            modules.NoReplacement,
            model.DatasetCollectionInstance,
            List[model.DatasetCollectionInstance],
        ] = modules.NO_REPLACEMENT
        prefixed_name = input_dict["name"]
        multiple = input_dict["multiple"]
        if prefixed_name in step.input_connections_by_name:
            connection = step.input_connections_by_name[prefixed_name]
            if input_dict["input_type"] == "dataset" and multiple:
                temp = [self.replacement_for_connection(c) for c in connection]
                # If replacement is just one dataset collection, replace tool
                # input_dict with dataset collection - tool framework will extract
                # datasets properly.
                if len(temp) == 1:
                    if isinstance(temp[0], model.HistoryDatasetCollectionAssociation):
                        replacement = temp[0]
                    else:
                        replacement = temp
                else:
                    replacement = temp
            else:
                replacement = self.replacement_for_input_connections(
                    step,
                    input_dict,
                    connection,
                )

        return replacement

    def replacement_for_connection(self, connection: "WorkflowStepConnection", is_data: bool = True) -> Any:
        output_step_id = connection.output_step.id
        if output_step_id not in self.outputs:
            message = f"No outputs found for step id {output_step_id}, outputs are {self.outputs}"
            raise Exception(message)
        step_outputs = self.outputs[output_step_id]
        if step_outputs is STEP_OUTPUT_DELAYED:
            delayed_why = f"dependent step [{output_step_id}] delayed, so this step must be delayed"
            raise modules.DelayedWorkflowEvaluation(why=delayed_why)
        output_name = connection.output_name
        try:
            replacement = step_outputs[output_name]
        except KeyError:
            if connection.non_data_connection:
                replacement = modules.NO_REPLACEMENT
            else:
                # If this not a implicit connection (the state of which is checked before in `check_implicitly_dependent_steps`)
                # we must resolve this.
                message = f"Workflow evaluation problem - failed to find output_name '{output_name}' in step_outputs {step_outputs}"
                raise Exception(message)
        if isinstance(replacement, model.HistoryDatasetCollectionAssociation):
            if not replacement.collection.populated:
                if not replacement.waiting_for_elements:
                    # If we are not waiting for elements, there was some
                    # problem creating the collection. Collection will never
                    # be populated.
                    # TODO: consider distinguish between cancelled and failed?
                    raise modules.CancelWorkflowEvaluation()

                delayed_why = f"dependent collection [{replacement.id}] not yet populated with datasets"
                raise modules.DelayedWorkflowEvaluation(why=delayed_why)

        if isinstance(replacement, model.DatasetCollection):
            raise NotImplementedError
        if not is_data and isinstance(
            replacement, (model.HistoryDatasetAssociation, model.HistoryDatasetCollectionAssociation)
        ):
            dataset_instances = []
            if isinstance(replacement, model.HistoryDatasetAssociation):
                dataset_instances = [replacement]
            else:
                dataset_instances = replacement.dataset_instances

            pending = False
            for dataset_instance in dataset_instances:
                if dataset_instance.is_pending:
                    pending = True
                elif not dataset_instance.is_ok:
                    raise modules.CancelWorkflowEvaluation()

            if pending:
                raise modules.DelayedWorkflowEvaluation()

        return replacement

    def get_replacement_workflow_output(self, workflow_output: "WorkflowOutput") -> Any:
        step = workflow_output.workflow_step
        output_name = workflow_output.output_name
        step_outputs = self.outputs[step.id]
        if step_outputs is STEP_OUTPUT_DELAYED:
            delayed_why = f"depends on workflow output [{output_name}] but that output has not been created yet"
            raise modules.DelayedWorkflowEvaluation(why=delayed_why)
        else:
            return step_outputs[output_name]

    def raw_to_galaxy(self, as_dict_value):
        trans = self.trans
        app = trans.app
        history = self.workflow_invocation.history

        relative_to = "/"  # TODO
        path = abs_path(as_dict_value.get("location"), relative_to)

        name = os.path.basename(path)
        primary_data = model.HistoryDatasetAssociation(
            name=name,
            extension="data",  # TODO: cwl default...
            designation=None,
            visible=True,
            dbkey="?",
            create_dataset=True,
            flush=False,
            sa_session=trans.sa_session,
        )
        primary_data.link_to(path)
        permissions = app.security_agent.history_get_default_permissions(history)
        app.security_agent.set_all_dataset_permissions(primary_data.dataset, permissions, new=True, flush=False)
        trans.sa_session.add(primary_data)
        history.stage_addition(primary_data)
        history.add_pending_items()
        primary_data.init_meta()
        primary_data.set_meta()
        primary_data.set_peek()
        primary_data.raw_set_dataset_state("ok")
        trans.sa_session.flush()
        return primary_data

    def set_outputs_for_input(
        self, invocation_step: WorkflowInvocationStep, outputs: Any = None, already_persisted: bool = False
    ) -> None:
        step = invocation_step.workflow_step

        if outputs is None:
            outputs = {}

        if self.inputs_by_step_id:
            step_id = step.id
            if step_id not in self.inputs_by_step_id and "output" not in outputs:
                default_value = step.input_default_value
                if default_value or step.input_optional:
                    outputs["output"] = default_value
                else:
                    raise ValueError(f"{step.log_str()} not found in inputs_step_id {self.inputs_by_step_id}")
            elif step_id in self.inputs_by_step_id:
                outputs["output"] = self.inputs_by_step_id[step_id]

        output = outputs.get("output")
        # TODO: handle extra files and directory types and collections and all the stuff...
        if output and isinstance(output, dict) and output.get("class") == "File":
            primary_data = self.raw_to_galaxy(output)
            outputs["output"] = primary_data

        log.debug("outputs are %s", outputs)
        self.set_step_outputs(invocation_step, outputs, already_persisted=already_persisted)

    def set_step_outputs(
        self, invocation_step: WorkflowInvocationStep, outputs: Dict[str, Any], already_persisted: bool = False
    ) -> None:
        step = invocation_step.workflow_step
        if invocation_step.output_value:
            outputs[invocation_step.output_value.workflow_output.output_name] = invocation_step.output_value.value
        self.outputs[step.id] = outputs
        if not already_persisted:
            workflow_outputs_by_name = {wo.output_name: wo for wo in step.workflow_outputs}
            for output_name, output_object in outputs.items():
                if hasattr(output_object, "history_content_type"):
                    invocation_step.add_output(output_name, output_object)
                else:
                    # Add this non-data, non workflow-output output to the workflow outputs.
                    # This is required for recovering the output in the next scheduling iteration,
                    # and should be replaced with a WorkflowInvocationStepOutputValue ASAP.
                    if not workflow_outputs_by_name.get(output_name) and not output_object == modules.NO_REPLACEMENT:
                        workflow_output = model.WorkflowOutput(step, output_name=output_name)
                        step.workflow_outputs.append(workflow_output)
            for workflow_output in step.workflow_outputs:
                output_name = workflow_output.output_name
                if output_name not in outputs:
                    message = f"Failed to find expected workflow output [{output_name}] in step outputs [{outputs}]"
                    # raise KeyError(message)
                    # Pre-18.01 we would have never even detected this output wasn't configured
                    # and even in 18.01 we don't have a way to tell the user something bad is
                    # happening so I guess we just log a debug message and continue sadly for now.
                    # Once https://github.com/galaxyproject/galaxy/issues/5142 is complete we could
                    # at least tell the user what happened, give them a warning.
                    log.debug(message)
                    continue
                output = outputs[output_name]
                self._record_workflow_output(
                    step,
                    workflow_output,
                    output=output,
                )

    def _record_workflow_output(self, step: "WorkflowStep", workflow_output: "WorkflowOutput", output: Any) -> None:
        self.workflow_invocation.add_output(workflow_output, step, output)

    def mark_step_outputs_delayed(self, step: "WorkflowStep", why: Optional[str] = None) -> None:
        if why:
            message = f"Marking step {step.id} outputs of invocation {self.workflow_invocation.id} delayed ({why})"
            log.debug(message)
        self.outputs[step.id] = STEP_OUTPUT_DELAYED

    def _subworkflow_invocation(self, step: "WorkflowStep") -> WorkflowInvocation:
        workflow_invocation = self.workflow_invocation
        subworkflow_invocation = workflow_invocation.get_subworkflow_invocation_for_step(step)
        if subworkflow_invocation is None:
            raise Exception(f"Failed to find persisted workflow invocation for step [{step.id}]")
        return subworkflow_invocation

    def subworkflow_invoker(
        self, trans: "WorkRequestContext", step: "WorkflowStep", structure, use_cached_job: bool = False
    ) -> WorkflowInvoker:
        subworkflow_invocation = self._subworkflow_invocation(step)
        workflow_run_config = workflow_request_to_run_config(subworkflow_invocation, use_cached_job)
        subworkflow_progress = self.subworkflow_progress(
            subworkflow_invocation, step, workflow_run_config.param_map, structure
        )
        subworkflow_invocation = subworkflow_progress.workflow_invocation
        return WorkflowInvoker(
            trans,
            workflow=subworkflow_invocation.workflow,
            workflow_run_config=workflow_run_config,
            progress=subworkflow_progress,
        )

    def subworkflow_progress(
        self, subworkflow_invocation: WorkflowInvocation, step: "WorkflowStep", param_map: Dict, structure=None
    ) -> "WorkflowProgress":
        subworkflow = subworkflow_invocation.workflow
        subworkflow_inputs = {}
        for input_subworkflow_step in subworkflow.input_steps:
            subworkflow_step_id = input_subworkflow_step.id
            connections = []
            for input_connection in step.input_connections:
                if input_connection.input_subworkflow_step_id == subworkflow_step_id:
                    connections.append(input_connection)

            if not connections and not input_subworkflow_step.input_optional:
                raise Exception("Could not find connections for all subworkflow inputs.")

            if connections:
                replacement = self.replacement_for_input_connections(
                    step,
                    dict(
                        name=input_subworkflow_step.label,  # TODO: only module knows this unfortunately
                        input_type=input_subworkflow_step.input_type,
                    ),
                    connections,
                )
            subworkflow_inputs[subworkflow_step_id] = replacement

        return WorkflowProgress(
            subworkflow_invocation,
            subworkflow_inputs,
            self.module_injector,
            param_map=param_map,
            use_cached_job=self.use_cached_job,
            replacement_dict=self.replacement_dict,
            workflow_mapping_structure=structure,
        )

    def _recover_mapping(self, step_invocation: WorkflowInvocationStep) -> None:
        try:
            step_invocation.workflow_step.module.recover_mapping(step_invocation, self)
        except modules.DelayedWorkflowEvaluation as de:
            self.mark_step_outputs_delayed(step_invocation.workflow_step, de.why)


__all__ = ("queue_invoke", "WorkflowRunConfig")
