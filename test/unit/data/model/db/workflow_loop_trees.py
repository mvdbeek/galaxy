"""A workflow invocation whose subworkflow step has several child invocations, one per loop iteration."""

from decimal import Decimal
from typing import NamedTuple

from sqlalchemy.orm import Session

from galaxy import model as m
from galaxy.schema.states import InvocationState


class LoopTree(NamedTuple):
    invocation: m.WorkflowInvocation
    loop_step: m.WorkflowStep
    children: list[m.WorkflowInvocation]
    tool_job: m.Job
    child_jobs: list[m.Job]


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


def make_tree(session: Session, iterations: list[int | None], child_states: list[str] | None = None) -> LoopTree:
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
