"""Several association rows per (invocation, subworkflow step), one per loop iteration.

Runs on SQLite by default and on PostgreSQL when GALAXY_TEST_DBURI is set. PostgreSQL
matters here: a scalar subquery that returns more than one row is an error there,
while SQLite silently returns the first row.
"""

import pytest
from sqlalchemy import (
    create_engine,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from galaxy import model as m
from galaxy.model.database_utils import DbUrl
from galaxy.model.unittest_utils.model_testing_utils import (  # noqa: F401  (url is a fixture we have to import explicitly)
    create_and_drop_database,
    url,
)
from galaxy.schema.states import InvocationState
from .workflow_loop_trees import (
    LoopTree,
    make_tree,
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


def _loaded_loop_invocation_step(session: Session, tree: LoopTree) -> m.WorkflowInvocationStep:
    session.expire_all()
    stmt = select(m.WorkflowInvocationStep).where(
        m.WorkflowInvocationStep.workflow_invocation_id == tree.invocation.id,
        m.WorkflowInvocationStep.workflow_step_id == tree.loop_step.id,
    )
    return session.scalars(stmt).one()


def test_subworkflow_invocation_id_is_latest_iteration(session):
    tree = make_tree(session, [0, 1, 2])
    assert _loaded_loop_invocation_step(session, tree).subworkflow_invocation_id == tree.children[2].id


def test_subworkflow_invocation_id_single_child(session):
    tree = make_tree(session, [None])
    assert _loaded_loop_invocation_step(session, tree).subworkflow_invocation_id == tree.children[0].id


def test_null_iterations_are_not_unique(session):
    tree = make_tree(session, [None, None])
    session.expire_all()
    associations = session.get(m.WorkflowInvocation, tree.invocation.id).subworkflow_invocations
    assert [assoc.iteration for assoc in associations] == [None, None]


def test_duplicate_iteration_is_rejected(session):
    with pytest.raises(IntegrityError) as error:
        make_tree(session, [0, 0])
    assert "unique" in str(error.value.orig).lower()
    session.rollback()


def test_iteration_associations(session):
    tree = make_tree(session, [2, 0, 1])
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
    tree = make_tree(session, [2, 0, 1])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    loop_step = session.get(m.WorkflowStep, tree.loop_step.id)
    assert invocation.get_subworkflow_invocation_for_step(loop_step).id == tree.children[0].id


def test_get_subworkflow_invocation_for_step_single_child(session):
    tree = make_tree(session, [None])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    loop_step = session.get(m.WorkflowStep, tree.loop_step.id)
    assert invocation.get_subworkflow_invocation_for_step(loop_step).id == tree.children[0].id
    assert [assoc.iteration for assoc in invocation.iteration_associations(loop_step)] == [None]


def test_recursive_job_state_summary_sums_iterations(session):
    running = InvocationState.SCHEDULED.value
    tree = make_tree(session, [0, 1, 2], [InvocationState.COMPLETED.value, running, InvocationState.COMPLETED.value])
    session.expire_all()
    invocation = session.get(m.WorkflowInvocation, tree.invocation.id)
    assert invocation.compute_recursive_job_state_summary() == {"ok": 3, "running": 1}


def test_recursive_job_state_summary_single_child(session):
    tree = make_tree(session, [None])
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
    tree = make_tree(session, [0, 1, 2], child_states)
    assert _loaded_loop_invocation_step(session, tree).is_complete is complete


@pytest.mark.parametrize("child_state, complete", [("completed", True), ("scheduled", False)])
def test_subworkflow_step_complete_single_child(session, child_state, complete):
    tree = make_tree(session, [None], [child_state])
    assert _loaded_loop_invocation_step(session, tree).is_complete is complete
