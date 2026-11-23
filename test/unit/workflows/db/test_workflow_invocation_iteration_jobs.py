"""Job sources and metrics of an invocation whose loop step has several iterations.

Runs on SQLite by default and on PostgreSQL when GALAXY_TEST_DBURI is set.
"""

import pytest
from sqlalchemy import create_engine

from galaxy.managers.jobs import (
    get_job_metrics_for_invocation,
    invocation_job_source_iter,
)
from galaxy.model.database_utils import DbUrl
from galaxy.model.unittest_utils.model_testing_utils import (  # noqa: F401  (url is a fixture we have to import explicitly)
    create_and_drop_database,
    url,
)
from ...data.model.db.workflow_loop_trees import make_tree


@pytest.fixture(scope="module")
def db_url(url):  # noqa: F811
    with create_and_drop_database(DbUrl(url)):
        yield url


@pytest.fixture(scope="module")
def engine(db_url):
    engine = create_engine(db_url)
    yield engine
    engine.dispose()


def test_invocation_job_source_iter_visits_every_iteration(session):
    tree = make_tree(session, [0, 1, 2])
    sources = list(invocation_job_source_iter(session, tree.invocation.id))
    assert sources == [("Job", job.id, None) for job in [tree.tool_job, *tree.child_jobs]]


def test_invocation_job_source_iter_single_child(session):
    tree = make_tree(session, [None])
    sources = list(invocation_job_source_iter(session, tree.invocation.id))
    assert sources == [("Job", tree.tool_job.id, None), ("Job", tree.child_jobs[0].id, None)]


def test_job_metrics_label_iterations(session):
    tree = make_tree(session, [0, 1, 2])
    metrics = get_job_metrics_for_invocation(session, tree.invocation.id)
    assert [(row[0], row[1]) for row in metrics] == [
        (0, tree.tool_job.id),
        ("1[0].0", tree.child_jobs[0].id),
        ("1[1].0", tree.child_jobs[1].id),
        ("1[2].0", tree.child_jobs[2].id),
    ]


def test_job_metrics_label_single_child(session):
    tree = make_tree(session, [None])
    metrics = get_job_metrics_for_invocation(session, tree.invocation.id)
    assert [(row[0], row[1]) for row in metrics] == [(0, tree.tool_job.id), ("1.0", tree.child_jobs[0].id)]
