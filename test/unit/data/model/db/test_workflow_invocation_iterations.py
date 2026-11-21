"""Several association rows per (invocation, subworkflow step), one per loop iteration.

Runs on SQLite by default and on PostgreSQL when GALAXY_TEST_DBURI is set. PostgreSQL
matters here: a scalar subquery that returns more than one row is an error there,
while SQLite silently returns the first row.
"""

from decimal import Decimal
from typing import NamedTuple

import pytest
from sqlalchemy import (
    create_engine,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from galaxy import model as m
from galaxy.managers.jobs import (
    get_job_metrics_for_invocation,
    invocation_job_source_iter,
)
from galaxy.model.database_utils import DbUrl
from galaxy.model.unittest_utils.model_testing_utils import (  # noqa: F401  (url is a fixture we have to import explicitly)
    create_and_drop_database,
    url,
)
from galaxy.schema.states import InvocationState


class LoopTree(NamedTuple):
    invocation: m.WorkflowInvocation
    loop_step: m.WorkflowStep
    children: list[m.WorkflowInvocation]
    tool_job: m.Job
    child_jobs: list[m.Job]


@pytest.fixture(scope="module")
def db_url(url):  # noqa: F811
    with create_and_drop_database(DbUrl(url)):
        yield url


@pytest.fixture(scope="module")
def engine(db_url):
    engine = create_engine(db_url)
    yield engine
    engine.dispose()


def _job(session: Session, state: str, metric_value: int) -> m.Job:
    job = m.Job()
    job.tool_id = "cat1"
    job.state = state
    job.numeric_metrics.append(
        m.JobMetricNumeric(plugin="core", metric_name="runtime_seconds", metric_value=Decimal(metric_value))
    )
    session.add(job)
    return job


def _child_invocation(
    session: Session, history: m.History, workflow: m.Workflow, state: str, job: m.Job
) -> m.WorkflowInvocation:
    tool_step = workflow.steps[0]
    invocation = m.WorkflowInvocation()
    invocation.workflow = workflow
    invocation.history = history
    invocation.state = state
    invocation_step = m.WorkflowInvocationStep()
    invocation_step.workflow_step = tool_step
    invocation_step.job = job
    invocation.steps.append(invocation_step)
    session.add(invocation)
    return invocation


def _make_tree(session: Session, iterations: list[int | None], child_states: list[str] | None = None) -> LoopTree:
    child_states = child_states or [InvocationState.COMPLETED.value] * len(iterations)
    user = m.User(email="loop@example.org", password="password")
    history = m.History(user=user)

    workflow = m.Workflow()
    tool_step = m.WorkflowStep()
    tool_step.order_index = 0
    tool_step.type = "tool"
    loop_step = m.WorkflowStep()
    loop_step.order_index = 1
    loop_step.type = "subworkflow"
    loop_step.subworkflow = m.Workflow()
    body_step = m.WorkflowStep()
    body_step.order_index = 0
    body_step.type = "tool"
    loop_step.subworkflow.steps.append(body_step)
    workflow.steps.extend([tool_step, loop_step])

    invocation = m.WorkflowInvocation()
    invocation.workflow = workflow
    invocation.history = history
    invocation.state = InvocationState.SCHEDULED.value

    tool_job = _job(session, "ok", 1)
    tool_invocation_step = m.WorkflowInvocationStep()
    tool_invocation_step.workflow_step = tool_step
    tool_invocation_step.job = tool_job
    loop_invocation_step = m.WorkflowInvocationStep()
    loop_invocation_step.workflow_step = loop_step
    invocation.steps.extend([tool_invocation_step, loop_invocation_step])

    children = []
    child_jobs = []
    for index, (iteration, child_state) in enumerate(zip(iterations, child_states)):
        child_job = _job(session, "ok" if child_state == InvocationState.COMPLETED.value else "running", 10 + index)
        child = _child_invocation(session, history, loop_step.subworkflow, child_state, child_job)
        association = invocation.attach_subworkflow_invocation_for_step(loop_step, child)
        association.iteration = iteration
        children.append(child)
        child_jobs.append(child_job)

    session.add(invocation)
    session.commit()
    return LoopTree(invocation, loop_step, children, tool_job, child_jobs)


def _loaded_loop_invocation_step(session: Session, tree: LoopTree) -> m.WorkflowInvocationStep:
    session.expire_all()
    stmt = select(m.WorkflowInvocationStep).where(
        m.WorkflowInvocationStep.workflow_invocation_id == tree.invocation.id,
        m.WorkflowInvocationStep.workflow_step_id == tree.loop_step.id,
    )
    return session.scalars(stmt).one()


def test_subworkflow_invocation_id_is_latest_iteration(session):
    tree = _make_tree(session, [0, 1, 2])
    assert _loaded_loop_invocation_step(session, tree).subworkflow_invocation_id == tree.children[2].id


def test_subworkflow_invocation_id_single_child(session):
    tree = _make_tree(session, [None])
    assert _loaded_loop_invocation_step(session, tree).subworkflow_invocation_id == tree.children[0].id


def test_null_iterations_are_not_unique(session):
    tree = _make_tree(session, [None, None])
    session.expire_all()
    associations = session.get(m.WorkflowInvocation, tree.invocation.id).subworkflow_invocations
    assert [assoc.iteration for assoc in associations] == [None, None]


def test_duplicate_iteration_is_rejected(session):
    with pytest.raises(IntegrityError) as error:
        _make_tree(session, [0, 0])
    assert "unique" in str(error.value.orig).lower()
    session.rollback()


def test_iteration_associations(session):
    tree = _make_tree(session, [2, 0, 1])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    loop_step = session.get(m.WorkflowStep, tree.loop_step.id)
    associations = invocation.iteration_associations(loop_step)
    assert [assoc.iteration for assoc in associations] == [0, 1, 2]
    assert [assoc.subworkflow_invocation_id for assoc in associations] == [
        tree.children[1].id,
        tree.children[2].id,
        tree.children[0].id,
    ]


def test_get_subworkflow_invocation_for_step_is_latest_iteration(session):
    tree = _make_tree(session, [2, 0, 1])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    loop_step = session.get(m.WorkflowStep, tree.loop_step.id)
    assert invocation.get_subworkflow_invocation_for_step(loop_step).id == tree.children[0].id


def test_get_subworkflow_invocation_for_step_single_child(session):
    tree = _make_tree(session, [None])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    loop_step = session.get(m.WorkflowStep, tree.loop_step.id)
    assert invocation.get_subworkflow_invocation_for_step(loop_step).id == tree.children[0].id
    assert [assoc.iteration for assoc in invocation.iteration_associations(loop_step)] == [None]


def test_invocation_job_source_iter_visits_every_iteration(session):
    tree = _make_tree(session, [0, 1, 2])
    sources = list(invocation_job_source_iter(session, tree.invocation.id))
    assert sources == [("Job", job.id, None) for job in [tree.tool_job, *tree.child_jobs]]


def test_invocation_job_source_iter_single_child(session):
    tree = _make_tree(session, [None])
    sources = list(invocation_job_source_iter(session, tree.invocation.id))
    assert sources == [("Job", tree.tool_job.id, None), ("Job", tree.child_jobs[0].id, None)]


def test_job_metrics_label_iterations(session):
    tree = _make_tree(session, [0, 1, 2])
    metrics = get_job_metrics_for_invocation(session, tree.invocation.id)
    assert [(row[0], row[1]) for row in metrics] == [
        (0, tree.tool_job.id),
        ("1[0].0", tree.child_jobs[0].id),
        ("1[1].0", tree.child_jobs[1].id),
        ("1[2].0", tree.child_jobs[2].id),
    ]


def test_job_metrics_label_single_child(session):
    tree = _make_tree(session, [None])
    metrics = get_job_metrics_for_invocation(session, tree.invocation.id)
    assert [(row[0], row[1]) for row in metrics] == [(0, tree.tool_job.id), ("1.0", tree.child_jobs[0].id)]


def test_recursive_job_state_summary_sums_iterations(session):
    running = InvocationState.SCHEDULED.value
    tree = _make_tree(session, [0, 1, 2], [InvocationState.COMPLETED.value, running, InvocationState.COMPLETED.value])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    assert invocation.compute_recursive_job_state_summary() == {"ok": 3, "running": 1}


def test_recursive_job_state_summary_single_child(session):
    tree = _make_tree(session, [None])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    assert invocation.compute_recursive_job_state_summary() == {"ok": 2}


@pytest.mark.parametrize(
    "child_states, complete",
    [
        ([InvocationState.COMPLETED.value] * 3, True),
        ([InvocationState.COMPLETED.value, InvocationState.SCHEDULED.value, InvocationState.COMPLETED.value], False),
        ([InvocationState.COMPLETED.value, InvocationState.COMPLETED.value, InvocationState.SCHEDULED.value], False),
    ],
)
def test_loop_step_complete_only_when_every_iteration_completes(session, child_states, complete):
    tree = _make_tree(session, [0, 1, 2], child_states)
    assert _loaded_loop_invocation_step(session, tree).is_complete is complete


@pytest.mark.parametrize("child_state, complete", [("completed", True), ("scheduled", False)])
def test_subworkflow_step_complete_single_child(session, child_state, complete):
    tree = _make_tree(session, [None], [child_state])
    assert _loaded_loop_invocation_step(session, tree).is_complete is complete
