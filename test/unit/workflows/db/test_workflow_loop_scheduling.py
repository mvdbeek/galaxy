"""Database parts of the workflow loop scheduler.

Runs on SQLite by default and on PostgreSQL when GALAXY_TEST_DBURI is set.
"""

from typing import (
    Any,
    cast,
)
from uuid import uuid4

import pytest
from sqlalchemy import (
    create_engine,
    event,
)
from sqlalchemy.orm import Session

from galaxy import model as m
from galaxy.model.database_utils import DbUrl
from galaxy.model.unittest_utils.model_testing_utils import (  # noqa: F401  (url is a fixture we have to import explicitly)
    create_and_drop_database,
    url,
)
from galaxy.schema.invocation import FailureReason
from galaxy.schema.states import InvocationState
from galaxy.tools.parameters.workflow_utils import NO_REPLACEMENT
from galaxy.util.bunch import Bunch
from galaxy.workflow import modules
from galaxy.workflow.loop import (
    all_iterations_outputs,
    iteration_job_states,
    parse_loop,
    record_loop_inputs,
    recorded_loop_inputs,
)
from galaxy.workflow.run import (
    ModuleInjector,
    WorkflowProgress,
)


@pytest.fixture(scope="module")
def db_url(url):  # noqa: F811
    with create_and_drop_database(DbUrl(url)):
        yield url


@pytest.fixture(scope="module")
def engine(db_url):
    engine = create_engine(db_url)
    yield engine
    engine.dispose()


def _loop_invocation(session: Session) -> tuple[m.WorkflowInvocation, m.WorkflowStep]:
    history = m.History(user=m.User(email="loop-scheduling@example.org", password="password"))
    workflow = m.Workflow()
    loop_step = m.WorkflowStep()
    loop_step.order_index = 0
    loop_step.type = "subworkflow"
    loop_step.subworkflow = m.Workflow()
    workflow.steps.append(loop_step)
    invocation = m.WorkflowInvocation()
    invocation.workflow = workflow
    invocation.history = history
    invocation.state = InvocationState.READY.value
    for iteration in (0, 1):
        child = m.WorkflowInvocation()
        child.state = InvocationState.NEW.value
        invocation.attach_subworkflow_invocation_for_step(loop_step, child).iteration = iteration
    session.add(invocation)
    session.commit()
    return invocation, loop_step


def test_allocating_an_existing_iteration_delays(session):
    invocation, loop_step = _loop_invocation(session)
    progress = WorkflowProgress(invocation, {}, cast(ModuleInjector, None), {})
    first_iteration = invocation.iteration_associations(loop_step)[0]
    with pytest.raises(modules.DelayedWorkflowEvaluation):
        progress._allocate_loop_iteration(
            cast(Any, Bunch(sa_session=session)),
            loop_step,
            first_iteration,
            1,
            parse_loop({"inputs": {"i1": {"output_source": "o1"}}}),
            {},
        )
    # The session stays usable and still holds the two iterations.
    session.refresh(invocation)
    assert [assoc.iteration for assoc in invocation.iteration_associations(loop_step)] == [0, 1]


def _iteration_tree(session: Session, mapped_jobs: int, inner_iterations: int) -> tuple[m.WorkflowInvocation, m.Job]:
    """An iteration with a direct job, a mapped step and an inner loop whose iterations each run one job."""
    history = m.History(user=m.User(email=f"loop-tree-{mapped_jobs}@example.org", password="password"))
    workflow = m.Workflow()
    tool_step = m.WorkflowStep()
    tool_step.order_index = 0
    tool_step.type = "tool"
    inner_loop_step = m.WorkflowStep()
    inner_loop_step.order_index = 1
    inner_loop_step.type = "subworkflow"
    inner_loop_step.subworkflow = m.Workflow()
    workflow.steps.extend([tool_step, inner_loop_step])

    def invocation_with_job(state: str) -> tuple[m.WorkflowInvocation, m.Job]:
        invocation = m.WorkflowInvocation()
        invocation.workflow = workflow
        invocation.history = history
        invocation.state = InvocationState.SCHEDULED.value
        job = m.Job()
        job.state = state
        invocation_step = m.WorkflowInvocationStep()
        invocation_step.workflow_step = tool_step
        invocation_step.job = job
        invocation.steps.append(invocation_step)
        return invocation, job

    iteration, running_job = invocation_with_job(m.Job.states.RUNNING)
    implicit_collection_jobs = m.ImplicitCollectionJobs()
    for index in range(mapped_jobs):
        job = m.Job()
        job.state = m.Job.states.OK
        implicit_collection_jobs.jobs.append(m.ImplicitCollectionJobsJobAssociation(job=job, order_index=index))
    mapped_step = m.WorkflowInvocationStep()
    mapped_step.workflow_step = tool_step
    mapped_step.implicit_collection_jobs = implicit_collection_jobs
    iteration.steps.append(mapped_step)
    for inner_iteration in range(inner_iterations):
        child, _ = invocation_with_job(m.Job.states.SKIPPED if inner_iteration else m.Job.states.ERROR)
        iteration.attach_subworkflow_invocation_for_step(inner_loop_step, child).iteration = inner_iteration
    session.add(iteration)
    session.commit()
    return iteration, running_job


@pytest.mark.parametrize("mapped_jobs,inner_iterations", [(2, 2), (40, 12)])
def test_iteration_job_states_in_one_query(session, engine, mapped_jobs, inner_iterations):
    iteration, running_job = _iteration_tree(session, mapped_jobs, inner_iterations)
    error_job_id = iteration.subworkflow_invocations[0].subworkflow_invocation.steps[0].job.id
    statements = []

    def count(*args):
        statements.append(args)

    event.listen(engine, "before_cursor_execute", count)
    try:
        job_states = iteration_job_states(session, iteration.id)
    finally:
        event.remove(engine, "before_cursor_execute", count)
    assert len(statements) == 1
    assert job_states[m.Job.states.RUNNING] == running_job.id
    assert job_states[m.Job.states.ERROR] == error_job_id
    assert set(job_states) == {m.Job.states.RUNNING, m.Job.states.ERROR, m.Job.states.OK, m.Job.states.SKIPPED}


def test_cancelled_iteration_cancels_the_loop_whatever_its_jobs(session):
    # Cancelling an iteration deletes its jobs; that must read as a cancellation, not a failed job.
    invocation, loop_step = _loop_invocation(session)
    association = invocation.iteration_associations(loop_step)[-1]
    iteration = association.subworkflow_invocation
    iteration.state = InvocationState.CANCELLED.value
    job = m.Job()
    job.state = m.Job.states.DELETED
    invocation_step = m.WorkflowInvocationStep()
    invocation_step.workflow_step = loop_step
    invocation_step.job = job
    iteration.steps.append(invocation_step)
    session.commit()
    progress = WorkflowProgress(invocation, {}, cast(ModuleInjector, None), {})
    with pytest.raises(modules.CancelWorkflowEvaluation):
        progress._check_loop_iteration_settled(cast(Any, Bunch(sa_session=session)), loop_step, association)


def _list(identifiers: list[str]) -> m.HistoryDatasetCollectionAssociation:
    collection = m.DatasetCollection(collection_type="list")
    for identifier in identifiers:
        m.DatasetCollectionElement(collection=collection, element=_dataset(), element_identifier=identifier)
    return m.HistoryDatasetCollectionAssociation(collection=collection)


def _dataset() -> m.HistoryDatasetAssociation:
    return m.HistoryDatasetAssociation(create_dataset=True, flush=False)


def _loop_step_with_outputs(session: Session, labels: list[str]) -> tuple[m.WorkflowStep, m.History]:
    history = m.History(user=m.User(email=f"{uuid4()}@example.org", password="password"))
    workflow = m.Workflow()
    loop_step = m.WorkflowStep()
    loop_step.order_index = 0
    loop_step.type = "subworkflow"
    loop_step.subworkflow = m.Workflow()
    workflow.steps.append(loop_step)
    for order_index, label in enumerate(labels):
        body_step = m.WorkflowStep()
        body_step.order_index = order_index
        body_step.type = "tool"
        m.WorkflowOutput(body_step, output_name="sum", label=label)
        loop_step.subworkflow.steps.append(body_step)
    session.add_all([history, workflow])
    # PostgreSQL takes new hids on a separate connection, which only sees committed rows.
    session.commit()
    return loop_step, history


def _all_iterations(
    session: Session, outputs_per_iteration: list[dict[str, Any]], skipped: dict[str, Any] | None = None
) -> m.HistoryDatasetCollectionAssociation:
    loop_step, history = _loop_step_with_outputs(session, ["o1"])
    return all_iterations_outputs(loop_step, history, outputs_per_iteration, skipped or {})["o1"]


def test_all_iterations_builds_nothing_when_an_output_fails(session):
    loop_step, history = _loop_step_with_outputs(session, ["o1", "o2"])
    outputs_per_iteration: list[dict[str, Any]] = [
        {"o1": _dataset(), "o2": _dataset()},
        {"o1": _dataset(), "o2": NO_REPLACEMENT},
    ]
    with pytest.raises(modules.FailWorkflowEvaluation):
        all_iterations_outputs(loop_step, history, outputs_per_iteration, {})
    assert list(history.dataset_collections) == []


def test_all_iterations_of_datasets_is_a_list_by_iteration(session):
    datasets = [_dataset(), _dataset(), _dataset()]
    hdca = _all_iterations(session, [{"o1": dataset} for dataset in datasets])
    session.flush()
    assert hdca.collection.collection_type == "list"
    assert [(element.element_identifier, element.hda) for element in hdca.collection.elements] == [
        ("0", datasets[0]),
        ("1", datasets[1]),
        ("2", datasets[2]),
    ]


def test_all_iterations_of_collections_nests_them(session):
    collections = [_list(["a"]), _list(["a", "b"])]
    hdca = _all_iterations(session, [{"o1": collection} for collection in collections])
    session.flush()
    assert hdca.collection.collection_type == "list:list"
    assert [element.child_collection for element in hdca.collection.elements] == [
        collection.collection for collection in collections
    ]


def test_all_iterations_without_iterations_is_empty(session):
    assert _all_iterations(session, [], {"o1": _dataset()}).collection.collection_type == "list"
    empty = _all_iterations(session, [], {"o1": _list(["a"])})
    session.flush()
    assert empty.collection.collection_type == "list:list"
    assert empty.collection.elements == []


def test_all_iterations_needs_datasets_or_collections_of_one_kind(session):
    mixed: list[list[dict[str, Any]]] = [
        [{"o1": _dataset()}, {"o1": _list(["a"])}],
        [{"o1": _dataset()}, {"o1": NO_REPLACEMENT}],
    ]
    for outputs_per_iteration in mixed:
        with pytest.raises(modules.FailWorkflowEvaluation) as exc_info:
            _all_iterations(session, outputs_per_iteration)
        assert exc_info.value.why.reason == FailureReason.loop_failed
    session.rollback()


def test_recorded_loop_inputs_read_back(session):
    history = m.History(user=m.User(email=f"{uuid4()}@example.org", password="password"))
    workflow = m.Workflow()
    loop_step = m.WorkflowStep()
    loop_step.order_index = 0
    loop_step.type = "subworkflow"
    loop_step.subworkflow = m.Workflow()
    workflow.steps.append(loop_step)
    labels = {
        "nothing": "parameter_input",
        "number": "parameter_input",
        "data": "data_input",
        "list": "data_collection_input",
    }
    for order_index, (label, step_type) in enumerate(labels.items()):
        input_step = m.WorkflowStep()
        input_step.order_index = order_index
        input_step.type = step_type
        input_step.label = label
        loop_step.subworkflow.steps.append(input_step)
    dataset = m.HistoryDatasetAssociation(create_dataset=True, flush=False, history=history)
    collection = m.HistoryDatasetCollectionAssociation(collection=m.DatasetCollection(collection_type="list"))
    history.add_dataset_collection(collection, set_hid=False)
    iteration = m.WorkflowInvocation()
    iteration.workflow = loop_step.subworkflow
    iteration.history = history
    iteration.state = InvocationState.NEW.value
    session.add_all([workflow, iteration])
    loop = parse_loop({"inputs": {label: {"output_source": "o"} for label in labels}})
    record_loop_inputs(loop_step, loop, iteration, {"nothing": None, "number": 7, "data": dataset, "list": collection})
    session.commit()
    session.expire_all()
    assert recorded_loop_inputs(loop_step, loop, iteration) == {
        "nothing": None,
        "number": 7,
        "data": dataset,
        "list": collection,
    }


class _ProgressWithoutOutputs:
    def get_replacement_workflow_output(self, workflow_output):
        raise KeyError(workflow_output.output_name)


def test_last_iteration_without_its_output_records_failed(session):
    loop_step, history = _loop_step_with_outputs(session, ["o1"])
    with session.no_autoflush:
        invocation = m.WorkflowInvocation()
        invocation.state = InvocationState.READY.value
        session.add(invocation)
        invocation.workflow = loop_step.workflow
        invocation.history = history
        iteration = m.WorkflowInvocation()
        iteration.state = InvocationState.SCHEDULED.value
        association = invocation.attach_subworkflow_invocation_for_step(loop_step, iteration)
        association.iteration = 0
        invocation_step = m.WorkflowInvocationStep()
        invocation_step.workflow_step = loop_step
        invocation.steps.append(invocation_step)
    session.commit()
    progress = WorkflowProgress(invocation, {}, cast(ModuleInjector, None), {})
    loop = parse_loop({"inputs": {"o1": {"output_source": "o1"}}})
    with pytest.raises(modules.FailWorkflowEvaluation) as exc_info:
        progress._finish_loop(
            cast(Any, Bunch(sa_session=session)),
            invocation_step,
            association,
            loop,
            cast(Any, _ProgressWithoutOutputs()),
        )
    assert exc_info.value.why.reason == FailureReason.output_not_found
    assert association.loop_outcome == "failed"
