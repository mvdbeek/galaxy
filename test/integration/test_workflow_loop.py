"""Integration tests for workflow loops.

Tests named after a CWL v1.3 loop test id translate that test, with the CWL inputs and expected
values. The others test rules that only Galaxy has: the iteration limit, cancellation, failed
body jobs, the nesting depth, collection feedback, export and import, and other job runners.
"""

import os
from copy import deepcopy
from textwrap import indent
from typing import Any
from unittest.mock import patch

import yaml
from gxformat2 import python_to_workflow
from sqlalchemy import select

from galaxy.model import Job
from galaxy_test.base.api import UsesCeleryTasks
from galaxy_test.base.populators import (
    DatasetCollectionPopulator,
    DatasetPopulator,
    RunJobsSummary,
    wait_on,
    WorkflowPopulator,
)
from galaxy_test.driver import integration_util

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
EMBEDDED_PULSAR_JOB_CONFIG_FILE = os.path.join(SCRIPT_DIRECTORY, "embedded_pulsar_job_conf.yml")

# Body of most loops: adds 1 to the integer i1.
ADD_ONE_BODY = """
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: add/sum
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
"""

# Body that adds i2 to i1 and passes i2 on.
ADD_TWO_BODY = """
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: add/sum
  o2:
    outputSource: i2
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
      b: i2
"""

SINGLE_VARIABLE_LOOP = {"loop": {"inputs": {"i1": {"output_source": "o1"}}}}


def loop_workflow(format2: str, loops: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Convert a format2 workflow to .ga and add the loop of each step named by its label path.

    gxformat2 has no loop yet, so the loops are added to the converted workflow.
    """
    workflow = python_to_workflow(yaml.safe_load(format2), galaxy_interface=None, workflow_directory=None)
    for label_path, loop in loops.items():
        steps = workflow["steps"]
        *parent_labels, label = label_path.split("/")
        for parent_label in parent_labels:
            steps = _step_by_label(steps, parent_label)["subworkflow"]["steps"]
        _step_by_label(steps, label)["loop"] = deepcopy(loop)
    return workflow


def single_loop_workflow(when: str, body: str = ADD_ONE_BODY, extra_inputs: str = "") -> dict[str, Any]:
    """A workflow with one loop step over ``body`` that feeds o1 back into i1."""
    return loop_workflow(
        f"""
class: GalaxyWorkflow
inputs:
  i1: int
{extra_inputs}
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
    when: {when!r}
    run:
{indent(body, " " * 6)}
""",
        SINGLE_VARIABLE_LOOP,
    )


def nested_loops_workflow(depth: int) -> dict[str, Any]:
    body = ADD_ONE_BODY
    label_path: list[str] = []
    for level in range(depth):
        label_path.insert(0, f"loop{level}")
        body = f"""
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: loop{level}/o1
steps:
  loop{level}:
    in:
      i1: i1
    when: $(inputs.i1 < 3)
    run:
{indent(body, " " * 6)}
"""
    loops: dict[str, dict[str, Any]] = {}
    for end in range(1, depth + 1):
        loops["/".join(label_path[:end])] = SINGLE_VARIABLE_LOOP["loop"]
    return loop_workflow(body, loops)


def _step_by_label(steps: dict[str, Any], label: str) -> dict[str, Any]:
    return next(step for step in steps.values() if step.get("label") == label)


class BaseWorkflowLoopIntegrationTestCase(integration_util.IntegrationTestCase):
    framework_tool_and_types = True
    dataset_populator: DatasetPopulator
    dataset_collection_populator: DatasetCollectionPopulator
    workflow_populator: WorkflowPopulator

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["enable_beta_workflow_loop"] = True

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.dataset_collection_populator = DatasetCollectionPopulator(self.galaxy_interactor)
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    def _run(
        self, workflow: dict[str, Any], test_data: dict[str, Any] | str, assert_ok: bool = True, wait: bool = True
    ) -> RunJobsSummary:
        history_id = self.dataset_populator.new_history()
        return self.workflow_populator.run_workflow(
            workflow, test_data=test_data, history_id=history_id, client_convert=False, assert_ok=assert_ok, wait=wait
        )

    def _run_failing(self, workflow: dict[str, Any], test_data: dict[str, Any]) -> dict[str, Any]:
        summary = self._run(workflow, test_data, assert_ok=False, wait=False)
        self.workflow_populator.wait_for_invocation(None, summary.invocation_id, assert_ok=False)
        invocation = self.workflow_populator.get_invocation(summary.invocation_id, step_details=True)
        assert invocation["state"] == "failed", invocation
        return invocation

    def _output_value(self, summary: RunJobsSummary, label: str) -> Any:
        invocation = self.workflow_populator.get_invocation(summary.invocation_id)
        output = invocation["outputs"][label]
        content = self.dataset_populator.get_history_dataset_content(summary.history_id, dataset_id=output["id"])
        return yaml.safe_load(content)

    def _output_collection_values(self, summary: RunJobsSummary, label: str) -> dict[str, Any]:
        invocation = self.workflow_populator.get_invocation(summary.invocation_id)
        hdca = self.dataset_populator.get_history_collection_details(
            summary.history_id, content_id=invocation["output_collections"][label]["id"]
        )
        return {
            element["element_identifier"]: yaml.safe_load(
                self.dataset_populator.get_history_dataset_content(
                    summary.history_id, dataset_id=element["object"]["id"]
                )
            )
            for element in hdca["elements"]
        }

    def _output_list(self, summary: RunJobsSummary, label: str) -> tuple[str, list[Any]]:
        """The collection type of a collection output and its values, nested lists for nested collections."""
        invocation = self.workflow_populator.get_invocation(summary.invocation_id)
        hdca = self.dataset_populator.get_history_collection_details(
            summary.history_id, content_id=invocation["output_collections"][label]["id"]
        )

        def values(elements: list[dict[str, Any]]) -> list[Any]:
            return [
                (
                    values(element["object"]["elements"])
                    if element["element_type"] == "dataset_collection"
                    else yaml.safe_load(
                        self.dataset_populator.get_history_dataset_content(
                            summary.history_id, dataset_id=element["object"]["id"]
                        )
                    )
                )
                for element in elements
            ]

        # The iterations are the elements, identified by their number.
        identifiers = [element["element_identifier"] for element in hdca["elements"]]
        assert identifiers == [str(iteration) for iteration in range(len(identifiers))]
        return hdca["collection_type"], values(hdca["elements"])

    def _all_iterations_collections(self, history_id: str) -> list[tuple[str, bool]]:
        contents = self._get(f"histories/{history_id}/contents").json()
        return [
            (item["name"], item["visible"])
            for item in contents
            if item["history_content_type"] == "dataset_collection" and item["name"].endswith("(all iterations)")
        ]

    def _iterations(self, invocation_id: str, label: str = "loop") -> list[dict[str, Any]]:
        invocation = self.workflow_populator.get_invocation(invocation_id, step_details=True)
        step = next(step for step in invocation["steps"] if step["workflow_step_label"] == label)
        return step["iterations"]

    def _outcomes(self, invocation_id: str, label: str = "loop") -> list[str | None]:
        return [iteration["loop_outcome"] for iteration in self._iterations(invocation_id, label)]

    def _iteration_states(self, invocation_id: str, label: str = "loop") -> list[str]:
        return [
            self.workflow_populator.get_invocation(iteration["subworkflow_invocation_id"])["state"]
            for iteration in self._iterations(invocation_id, label)
        ]


class TestWorkflowLoop(BaseWorkflowLoopIntegrationTestCase):
    def test_configuration_tells_the_editor_loops_are_enabled(self):
        response = self._get("configuration")
        self._assert_status_code_is(response, 200)
        assert response.json()["enable_beta_workflow_loop"] is True

    def test_loop_condition_compares_with_a_connected_input_the_body_does_not_take(self):
        # `limit` is connected to the loop step but is no input of the subworkflow, as the editor's condition port.
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  limit: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      limit: limit
    when: $(inputs.i1 < inputs.limit)
    run:
{indent(ADD_ONE_BODY, " " * 6)}
""",
            SINGLE_VARIABLE_LOOP,
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "limit": {"value": 5, "type": "raw"}})
        assert self._output_value(summary, "o1") == 5
        assert self._outcomes(summary.invocation_id) == ["continue"] * 3 + ["stop"]

    def test_loop_single_variable(self):
        summary = self._run(single_loop_workflow("$(inputs.i1 < 10)"), {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10
        iterations = self._iterations(summary.invocation_id)
        assert [iteration["iteration"] for iteration in iterations] == list(range(9))
        assert self._outcomes(summary.invocation_id) == ["continue"] * 8 + ["stop"]
        # Every iteration is its own subworkflow invocation, the step points at the last one.
        assert len({iteration["subworkflow_invocation_id"] for iteration in iterations}) == 9
        step_jobs = self.dataset_populator.history_jobs_for_tool(summary.history_id, "expression_add_int")
        assert len(step_jobs) == 9

    def test_loop_single_variable_boolean_feedback(self):
        # The `when` of this loop is a plain reference to a boolean the body computes, no JavaScript.
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1: int
  go_on: boolean
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      go_on: go_on
    when: $(inputs.go_on)
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
        go_on: boolean
      outputs:
        o1:
          outputSource: add/sum
        go_on:
          outputSource: add/below_limit
      steps:
        add:
          tool_id: expression_add_int
          in:
            a: i1
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1"}, "go_on": {"output_source": "go_on"}}}},
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "go_on": {"value": True, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10
        assert self._outcomes(summary.invocation_id) == ["continue"] * 8 + ["stop"]

    def test_loop_single_variable_no_iteration(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  picked:
    outputSource: pick/integer_param
steps:
  loop:
    in:
      i1: i1
    when: $(inputs.i1 < 1)
    run:
{indent(ADD_ONE_BODY, " " * 6)}
  pick:
    tool_id: pick_value
    state:
      style_cond:
        pick_style: first_or_default
        type_cond:
          param_type: integer
          default_value: 42
    in:
      style_cond|type_cond|pick_from_0|value: loop/o1
""",
            SINGLE_VARIABLE_LOOP,
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        # pick_value saw the loop's skipped output.
        assert self._output_value(summary, "picked") == 42
        assert self._outcomes(summary.invocation_id) == ["skipped"]
        body_jobs = self.dataset_populator.history_jobs_for_tool(summary.history_id, "expression_add_int")
        assert [job["state"] for job in body_jobs] == ["skipped"]

    def test_loop_two_variables(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_TWO_BODY, " " * 6)}
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1"}, "i2": {"output_source": "o2"}}}},
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10

    def test_loop_two_variables_single_backpropagation(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_TWO_BODY, " " * 6)}
""",
            SINGLE_VARIABLE_LOOP,
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10

    def test_loop_value_from(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_TWO_BODY, " " * 6)}
""",
            {"loop": {"inputs": {"i1": {"value_from": "$(inputs.i1 + 1)"}}}},
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10
        assert len(self._iterations(summary.invocation_id)) == 9
        downloaded = self.workflow_populator.download_workflow(summary.workflow_id, style="ga")
        assert _step_by_label(downloaded["steps"], "loop")["loop"]["inputs"] == {
            "i1": {"value_from": "$(inputs.i1 + 1)"}
        }

    def test_loop_defaultvalue(self):
        # The feedback part of loop_defaultvalue, with the last iteration's output: the first
        # iteration's body step is skipped, its null output is fed back as the rule's default 5.
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: big_values/sum
steps:
  big_values:
    tool_id: expression_add_int
    when: $(inputs.a >= 5)
    state:
      b: 3
    in:
      a: i1
"""
        workflow = single_loop_workflow("$(inputs.i1 < 20)", body=body)
        _step_by_label(workflow["steps"], "loop")["loop"] = {"inputs": {"i1": {"output_source": "o1", "default": 5}}}
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        # 1 (skipped, default 5), 5 -> 8, 8 -> 11, 11 -> 14, 14 -> 17, 17 -> 20.
        assert self._output_value(summary, "o1") == 20
        assert len(self._iterations(summary.invocation_id)) == 6

    def test_loop_value_from_with_output_source(self):
        # self is the body output: o1 = i1 + 1, next i1 = 2 * o1; 1 -> 4 -> 10 stops with o1 = 5.
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        _step_by_label(workflow["steps"], "loop")["loop"] = {
            "inputs": {"i1": {"output_source": "o1", "value_from": "$(self * 2)"}}
        }
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 5
        assert len(self._iterations(summary.invocation_id)) == 2

    def test_loop_default_and_value_from(self):
        # The skipped first output becomes the default 5 before value_from adds 1:
        # i1 = 1, 6, 10, 14, 18; the last iteration's output is 18 + 3.
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: big_values/sum
steps:
  big_values:
    tool_id: expression_add_int
    when: $(inputs.a >= 5)
    state:
      b: 3
    in:
      a: i1
"""
        workflow = single_loop_workflow("$(inputs.i1 < 20)", body=body)
        _step_by_label(workflow["steps"], "loop")["loop"] = {
            "inputs": {"i1": {"output_source": "o1", "default": 5, "value_from": "$(self + 1)"}}
        }
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 21
        assert len(self._iterations(summary.invocation_id)) == 5

    def test_loop_value_from_reads_other_input(self):
        # i2 has no rule and keeps its value: i1 = 1, 3, 5, 7, 9; the last output is 9 + 2.
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_TWO_BODY, " " * 6)}
""",
            {"loop": {"inputs": {"i1": {"value_from": "$(inputs.i1 + inputs.i2)"}}}},
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 2, "type": "raw"}})
        assert self._output_value(summary, "o1") == 11
        assert len(self._iterations(summary.invocation_id)) == 5

    def test_loop_fail_value_from_exception_second_iteration(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        value_from = '${ if (inputs.i1 >= 2) { throw new Error("failed"); } return inputs.i1 + 1; }'
        _step_by_label(workflow["steps"], "loop")["loop"] = {"inputs": {"i1": {"value_from": value_from}}}
        invocation = self._run_failing(workflow, {"i1": {"value": 1, "type": "raw"}})
        # The same failure reason as an expression in ``when`` that throws.
        assert invocation["messages"][0]["reason"] == "expression_evaluation_failed"
        assert self._outcomes(invocation["id"]) == ["continue", "failed"]

    def test_validate_loop_fail_default_for_dataset_input(self):
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
steps:
  loop:
    in:
      i1: i1
    when: $(true)
    run:
      class: GalaxyWorkflow
      inputs:
        i1:
          type: collection
          collection_type: list
      outputs:
        o1:
          outputSource: sort/output
      steps:
        sort:
          tool_id: __SORTLIST__
          in:
            input: i1
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1", "default": 5}}}},
        )
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "a dataset or collection input, is not supported" in response.json()["err_msg"]

    def test_loop_opt_var(self):
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
  i2:
    type: int
    optional: true
    default: 3
outputs:
  o1:
    outputSource: add/sum
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
      b: i2
"""
        # i2 is never connected; its default reaches every iteration: 1, 4, 7, 10.
        summary = self._run(single_loop_workflow("$(inputs.i1 < 10)", body=body), {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 10
        assert len(self._iterations(summary.invocation_id)) == 3

    def test_loop_output_read_by_next_step(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: next/sum
steps:
  loop:
    in:
      i1: i1
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_ONE_BODY, " " * 6)}
  next:
    tool_id: expression_add_int
    state:
      b: 90
    in:
      a: loop/o1
""",
            SINGLE_VARIABLE_LOOP,
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 100
        jobs = self.dataset_populator.history_jobs_for_tool(summary.history_id, "expression_add_int")
        # Nine iterations and a single run of the next step.
        assert len(jobs) == 10

    def test_scatter_inside_loop(self):
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1[0] < 10)
    run:
      class: GalaxyWorkflow
      inputs:
        i1:
          type: collection
          collection_type: list
        i2: int
      outputs:
        o1:
          outputSource: add/sum
      steps:
        add:
          tool_id: expression_add_int
          in:
            a: i1
            b: i2
""",
            SINGLE_VARIABLE_LOOP,
        )
        elements = [
            {"identifier": f"e{value}", "content": str(value), "ext": "expression.json"} for value in range(1, 6)
        ]
        summary = self._run(
            workflow, {"i1": {"collection_type": "list", "elements": elements}, "i2": {"value": 1, "type": "raw"}}
        )
        assert self._output_collection_values(summary, "o1") == {f"e{value}": value + 9 for value in range(1, 6)}
        assert len(self._iterations(summary.invocation_id)) == 9

    def test_loop_nested_last_iteration(self):
        # The last-iteration variant of loop_nested: the outer loop feeds back a counter from a body
        # step, as Galaxy has no feedback valueFrom yet. The inner loop starts again at i1 in every
        # outer iteration.
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop1/o1
steps:
  loop1:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i2 < 4)
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
        i2: int
      outputs:
        o1:
          outputSource: loop2/o1
        o2:
          outputSource: next_i2/sum
      steps:
        next_i2:
          tool_id: expression_add_int
          in:
            a: i2
        loop2:
          in:
            i1: i1
            i2: i2
          when: $(inputs.i1 <= inputs.i2)
          run:
            class: GalaxyWorkflow
            inputs:
              i1: int
              i2: int
            outputs:
              o1:
                outputSource: add/sum
            steps:
              add:
                tool_id: expression_add_int
                in:
                  a: i1
""",
            {
                "loop1": {"inputs": {"i2": {"output_source": "o2"}}},
                "loop1/loop2": {"inputs": {"i1": {"output_source": "o1"}}},
            },
        )
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "o1") == 4
        outer_iterations = self._iterations(summary.invocation_id, "loop1")
        assert [iteration["loop_outcome"] for iteration in outer_iterations] == ["continue", "continue", "stop"]
        inner_iteration_counts = [
            len(self._iterations(iteration["subworkflow_invocation_id"], "loop2")) for iteration in outer_iterations
        ]
        assert inner_iteration_counts == [1, 2, 3]

    def test_loop_with_all_output_method(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        _step_by_label(workflow["steps"], "loop")["loop"]["output_method"] = "all_iterations"
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_list(summary, "o1") == ("list", list(range(2, 11)))
        downloaded = self.workflow_populator.download_workflow(summary.workflow_id, style="ga")
        assert _step_by_label(downloaded["steps"], "loop")["loop"]["output_method"] == "all_iterations"

    def test_loop_with_all_output_method_no_iteration(self):
        workflow = single_loop_workflow("$(inputs.i1 < 1)")
        _step_by_label(workflow["steps"], "loop")["loop"]["output_method"] = "all_iterations"
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_list(summary, "o1") == ("list", [])
        assert self._outcomes(summary.invocation_id) == ["skipped"]

    def test_loop_defaultvalue_all_iterations(self):
        # loop_defaultvalue: the skipped first iteration contributes a null, as in CWL before pickValue.
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: big_values/sum
steps:
  big_values:
    tool_id: expression_add_int
    when: $(inputs.a >= 5)
    state:
      b: 3
    in:
      a: i1
"""
        workflow = single_loop_workflow("$(inputs.i1 < 20)", body=body)
        _step_by_label(workflow["steps"], "loop")["loop"] = {
            "inputs": {"i1": {"output_source": "o1", "default": 5}},
            "output_method": "all_iterations",
        }
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        collection_type, values = self._output_list(summary, "o1")
        assert collection_type == "list"
        assert values == [None, 8, 11, 14, 17, 20]
        assert [value for value in values if value is not None] == [8, 11, 14, 17, 20]

    def _nested_loops(self, outer_method: str, inner_method: str) -> RunJobsSummary:
        # loop_nested: the outer loop counts i2 up with value_from, the inner loop starts again
        # from i1 in every outer iteration and counts i1 up to i2.
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
outputs:
  o1:
    outputSource: loop1/o1
steps:
  loop1:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i2 < 4)
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
        i2: int
      outputs:
        o1:
          outputSource: loop2/o1
      steps:
        loop2:
          in:
            i1: i1
            i2: i2
          when: $(inputs.i1 <= inputs.i2)
          run:
            class: GalaxyWorkflow
            inputs:
              i1: int
              i2: int
            outputs:
              o1:
                outputSource: add/sum
            steps:
              add:
                tool_id: expression_add_int
                in:
                  a: i1
""",
            {
                "loop1": {"inputs": {"i2": {"value_from": "$(inputs.i2 + 1)"}}, "output_method": outer_method},
                "loop1/loop2": {"inputs": {"i1": {"output_source": "o1"}}, "output_method": inner_method},
            },
        )
        return self._run(workflow, {"i1": {"value": 1, "type": "raw"}, "i2": {"value": 1, "type": "raw"}})

    def test_loop_nested(self):
        summary = self._nested_loops("all_iterations", "last_iteration")
        assert self._output_list(summary, "o1") == ("list", [2, 3, 4])

    def test_loop_nested_all(self):
        summary = self._nested_loops("all_iterations", "all_iterations")
        assert self._output_list(summary, "o1") == ("list:list", [[2], [2, 3], [2, 3, 4]])

    def test_loop_nested_all_inside_last_iteration(self):
        # The outer loop publishes the list the inner loop collected in its last iteration.
        summary = self._nested_loops("last_iteration", "all_iterations")
        assert self._output_list(summary, "o1") == ("list", [2, 3, 4])

    def test_scatter_inside_loop_all_iterations(self):
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
  i2: int
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1[0] < 4)
    run:
      class: GalaxyWorkflow
      inputs:
        i1:
          type: collection
          collection_type: list
        i2: int
      outputs:
        o1:
          outputSource: add/sum
      steps:
        add:
          tool_id: expression_add_int
          in:
            a: i1
            b: i2
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1"}}, "output_method": "all_iterations"}},
        )
        elements = [{"identifier": f"e{value}", "content": str(value), "ext": "expression.json"} for value in (1, 5)]
        summary = self._run(
            workflow, {"i1": {"collection_type": "list", "elements": elements}, "i2": {"value": 1, "type": "raw"}}
        )
        # Each iteration's list becomes one element of a list:list.
        assert self._output_list(summary, "o1") == ("list:list", [[2, 6], [3, 7], [4, 8]])

    def _all_iterations_then(self, when: str, next_step: str = "", outputs: str = "") -> dict[str, Any]:
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
{outputs or "  {}"}
steps:
  loop:
    in:
      i1: i1
    when: {when!r}
    run:
{indent(ADD_ONE_BODY, " " * 6)}
{next_step}
""",
            {"loop": {**SINGLE_VARIABLE_LOOP["loop"], "output_method": "all_iterations"}},
        )
        return workflow

    def test_loop_all_iterations_mapped_over_downstream(self):
        next_step = """  next:
    tool_id: expression_add_int
    state:
      b: 90
    in:
      a: loop/o1
"""
        outputs = "  next:\n    outputSource: next/sum"
        workflow = self._all_iterations_then("$(inputs.i1 < 10)", next_step, outputs)
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_list(summary, "next") == ("list", list(range(92, 101)))

    def test_loop_all_iterations_no_iteration_mapped_over_downstream(self):
        next_step = """  next:
    tool_id: expression_add_int
    in:
      a: loop/o1
"""
        outputs = "  next:\n    outputSource: next/sum"
        workflow = self._all_iterations_then("$(inputs.i1 < 1)", next_step, outputs)
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_list(summary, "next") == ("list", [])
        assert self.workflow_populator.get_invocation(summary.invocation_id)["state"] in ("scheduled", "completed")

    def test_loop_all_iterations_visibility(self):
        # Shown unless the workflow marks outputs and not this one, as the editor hides step outputs.
        cases = [
            ("", True),
            ("  o1:\n    outputSource: loop/o1", True),
            ("  i1_again:\n    outputSource: i1", False),
        ]
        for outputs, visible in cases:
            summary = self._run(
                self._all_iterations_then("$(inputs.i1 < 3)", outputs=outputs), {"i1": {"value": 1, "type": "raw"}}
            )
            assert self._all_iterations_collections(summary.history_id) == [("o1 (all iterations)", visible)], outputs

    def test_loop_all_iterations_failure_in_third_iteration_builds_nothing(self):
        when = '${ if (inputs.i1 >= 3) { throw new Error("failed"); } return true; }'
        invocation = self._run_failing(self._all_iterations_then(when), {"i1": {"value": 1, "type": "raw"}})
        assert self._outcomes(invocation["id"]) == ["continue", "failed"]
        assert self._all_iterations_collections(invocation["history_id"]) == []

    def test_loop_last_iteration_feeding_back_all_iterations_list(self):
        # The inner list is identified 0, 1, 2; the outer loop's first collection a, b: rule 15 refuses it.
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  c:
    type: collection
    collection_type: list
  i1: int
steps:
  outer:
    in:
      c: c
      i1: i1
    when: $(true)
    run:
      class: GalaxyWorkflow
      inputs:
        c:
          type: collection
          collection_type: list
        i1: int
      outputs:
        numbers:
          outputSource: inner/o1
      steps:
        inner:
          in:
            i1: i1
          when: $(inputs.i1 < 4)
          run:
            class: GalaxyWorkflow
            inputs:
              i1: int
            outputs:
              o1:
                outputSource: add/sum
            steps:
              add:
                tool_id: expression_add_int
                in:
                  a: i1
""",
            {
                "outer": {"inputs": {"c": {"output_source": "numbers"}}},
                "outer/inner": {"inputs": {"i1": {"output_source": "o1"}}, "output_method": "all_iterations"},
            },
        )
        elements = [{"identifier": identifier, "content": "1", "ext": "expression.json"} for identifier in ("a", "b")]
        invocation = self._run_failing(
            workflow, {"c": {"collection_type": "list", "elements": elements}, "i1": {"value": 1, "type": "raw"}}
        )
        assert invocation["messages"][0]["details"] == (
            "Loop input 'c' must keep its collection type, element identifiers and their order."
        )
        assert self._outcomes(invocation["id"], "outer") == ["failed"]

    def _two_branch_loop(self, rule: dict[str, Any], small_when: str, big_when: str, method: str) -> dict[str, Any]:
        # Of the two body steps, small adds 1 and big adds 3; each runs only when its test is true.
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  osmall:
    outputSource: loop/osmall
  obig:
    outputSource: loop/obig
steps:
  loop:
    in:
      i1: i1
    when: $(inputs.i1 < 20)
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
      outputs:
        osmall:
          outputSource: small_values/sum
        obig:
          outputSource: big_values/sum
      steps:
        small_values:
          tool_id: expression_add_int
          when: {small_when!r}
          in:
            a: i1
        big_values:
          tool_id: expression_add_int
          when: {big_when!r}
          state:
            b: 3
          in:
            a: i1
""",
            {"loop": {"inputs": {"i1": rule}, "output_method": method}},
        )
        return workflow

    def test_loop_multi_source_input(self):
        rule = {"output_source": ["osmall", "obig"], "pick_value": "the_only_non_null"}
        workflow = self._two_branch_loop(rule, "$(inputs.a < 5)", "$(inputs.a >= 5)", "all_iterations")
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        _, small = self._output_list(summary, "osmall")
        _, big = self._output_list(summary, "obig")
        # CWL merges the two lists with merge_flattened and all_non_null; one is null in each iteration.
        assert [s if s is not None else b for s, b in zip(small, big)] == [2, 3, 4, 5, 8, 11, 14, 17, 20]
        assert all((s is None) != (b is None) for s, b in zip(small, big))
        downloaded = self.workflow_populator.download_workflow(summary.workflow_id, style="ga")
        assert _step_by_label(downloaded["steps"], "loop")["loop"]["inputs"]["i1"] == rule

    def test_loop_multi_source_input_first_non_null(self):
        rule = {"output_source": ["osmall", "obig"], "pick_value": "first_non_null"}
        workflow = self._two_branch_loop(rule, "$(inputs.a < 5)", "$(inputs.a >= 5)", "last_iteration")
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert self._output_value(summary, "obig") == 20
        assert len(self._iterations(summary.invocation_id)) == 9

    def test_loop_multi_source_input_the_only_non_null_fails_with_two_values(self):
        # At i1 = 3 both branches run.
        rule = {"output_source": ["osmall", "obig"], "pick_value": "the_only_non_null"}
        workflow = self._two_branch_loop(rule, "$(inputs.a < 5)", "$(inputs.a >= 3)", "last_iteration")
        invocation = self._run_failing(workflow, {"i1": {"value": 1, "type": "raw"}})
        assert invocation["messages"][0]["reason"] == "loop_failed"
        assert invocation["messages"][0]["details"] == (
            "Loop input 'i1': more than one output it is fed from is not null, the_only_non_null needs one."
        )
        assert self._outcomes(invocation["id"]) == ["continue", "continue", "failed"]

    def test_loop_multi_source_input_datasets(self):
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1: int
  d: data
steps:
  loop:
    in:
      i1: i1
      d: d
    when: $(inputs.i1 < 5)
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
        d: data
      outputs:
        o1:
          outputSource: count/sum
        oa:
          outputSource: small/out_file1
        ob:
          outputSource: big/out_file1
      steps:
        count:
          tool_id: expression_add_int
          in:
            a: i1
        small:
          tool_id: cat1
          when: $(inputs.n < 3)
          in:
            input1: d
            n: i1
        big:
          tool_id: cat1
          when: $(inputs.n >= 3)
          in:
            input1: d
            n: i1
""",
            {
                "loop": {
                    "inputs": {
                        "i1": {"output_source": "o1"},
                        "d": {"output_source": ["oa", "ob"], "pick_value": "first_non_null"},
                    }
                }
            },
        )
        summary = self._run(
            workflow, {"i1": {"value": 1, "type": "raw"}, "d": {"value": "simple_line.txt", "type": "File"}}
        )
        iterations = [
            self.workflow_populator.get_invocation(iteration["subworkflow_invocation_id"])
            for iteration in self._iterations(summary.invocation_id)
        ]
        assert len(iterations) == 4
        # Each iteration's d is the dataset of the branch that ran in the iteration before it.
        for previous, iteration, branch in zip(iterations, iterations[1:], ["oa", "oa", "ob"]):
            dataset_input = next(item for item in iteration["inputs"].values() if item["label"] == "d")
            assert dataset_input["id"] == previous["outputs"][branch]["id"]

    def test_validate_loop_fail_list_output_source(self):
        for rule, message in (
            ({"output_source": ["osmall", "missing"], "pick_value": "first_non_null"}, "'missing' is not an output"),
            ({"output_source": "osmall", "link_merge": "merge_nested"}, "need a list output_source"),
            ({"output_source": ["osmall", "obig"], "pick_value": "any_non_null"}, "Invalid loop definition"),
        ):
            workflow = self._two_branch_loop(rule, "$(inputs.a < 5)", "$(inputs.a >= 5)", "last_iteration")
            response = self.workflow_populator.create_workflow_response(workflow)
            self._assert_status_code_is(response, 400)
            assert message in response.json()["err_msg"]

    def test_loop_fail_loop_when_exception(self):
        invocation = self._run_failing(
            single_loop_workflow('${ throw new Error("failed"); }'), {"i1": {"value": 1, "type": "raw"}}
        )
        assert invocation["messages"][0]["reason"] == "expression_evaluation_failed"
        assert self._outcomes(invocation["id"]) == ["failed"]
        # The first iteration never ran; it must not be left waiting to be scheduled.
        assert self._iteration_states(invocation["id"]) == ["failed"]
        first_iteration_id = self._iterations(invocation["id"])[0]["subworkflow_invocation_id"]
        messages = self.workflow_populator.get_invocation(first_iteration_id)["messages"]
        assert messages[0]["details"] == "The loop ended before this iteration started."

    def test_loop_fail_loop_when_exception_third_iteration(self):
        when = '${ if (inputs.i1 >= 3) { throw new Error("failed"); } return true; }'
        invocation = self._run_failing(single_loop_workflow(when), {"i1": {"value": 1, "type": "raw"}})
        assert invocation["messages"][0]["reason"] == "expression_evaluation_failed"
        # The first two iterations ran and stay recorded.
        assert self._outcomes(invocation["id"]) == ["continue", "failed"]

    def test_loop_fail_non_boolean_loop_when(self):
        invocation = self._run_failing(single_loop_workflow("$(inputs.i1)"), {"i1": {"value": 1, "type": "raw"}})
        assert invocation["messages"][0]["reason"] == "when_not_boolean"
        assert self._outcomes(invocation["id"]) == ["failed"]

    def test_loop_fail_non_boolean_loop_when_third_iteration(self):
        invocation = self._run_failing(
            single_loop_workflow('$(inputs.i1 < 3 ? true : "I am a string")'), {"i1": {"value": 1, "type": "raw"}}
        )
        assert invocation["messages"][0]["reason"] == "when_not_boolean"
        assert self._outcomes(invocation["id"]) == ["continue", "failed"]

    def test_validate_loop_fail_no_loop_when(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        del _step_by_label(workflow["steps"], "loop")["when"]
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "needs a 'when' expression" in response.json()["err_msg"]

    def test_validate_loop_fail_scatter(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
steps:
  loop:
    in:
      i1: i1
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_ONE_BODY, " " * 6)}
""",
            SINGLE_VARIABLE_LOOP,
        )
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "mapping over a loop step is not supported" in response.json()["err_msg"]

    def test_validate_loop_fail_scatter_enclosing_subworkflow(self):
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
steps:
  outer:
    in:
      i1: i1
    run:
      class: GalaxyWorkflow
      inputs:
        i1: int
      steps:
        loop:
          in:
            i1: i1
          when: $(inputs.i1 < 10)
          run:
{indent(ADD_ONE_BODY, " " * 12)}
""",
            {"outer/loop": SINGLE_VARIABLE_LOOP["loop"]},
        )
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "mapping over a subworkflow that contains a loop is not supported" in response.json()["err_msg"]

    def test_loop_mapped_over_at_run_time_fails(self):
        # A collection made by a mapped-over step is only known when the workflow runs.
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  numbers:
    type: collection
    collection_type: list
steps:
  plus_one:
    tool_id: expression_add_int
    in:
      a: numbers
  loop:
    in:
      i1: plus_one/sum
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_ONE_BODY, " " * 6)}
""",
            SINGLE_VARIABLE_LOOP,
        )
        elements = [{"identifier": "e1", "content": "1", "ext": "expression.json"}]
        invocation = self._run_failing(workflow, {"numbers": {"collection_type": "list", "elements": elements}})
        assert invocation["messages"][0]["reason"] == "loop_failed"
        assert invocation["messages"][0]["details"] == "Mapping over a loop step is not supported."
        assert self._outcomes(invocation["id"]) == ["failed"]
        assert self._iteration_states(invocation["id"]) == ["failed"]

    def test_validate_loop_fail_on_tool_step(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        tool_step = _step_by_label(workflow["steps"], "loop")["subworkflow"]["steps"]["1"]
        tool_step["loop"] = {"inputs": {"a": {"output_source": "sum"}}}
        tool_step["when"] = "$(true)"
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "a loop is only allowed on a subworkflow step" in response.json()["err_msg"]

    def test_validate_loop_fail_all_iterations_of_parameter(self):
        # The body's o2 passes the parameter i2 through; a list of parameters is not supported yet.
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  i2: int
steps:
  loop:
    in:
      i1: i1
      i2: i2
    when: $(inputs.i1 < 10)
    run:
{indent(ADD_TWO_BODY, " " * 6)}
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1"}}, "output_method": "all_iterations"}},
        )
        response = self.workflow_populator.create_workflow_response(workflow)
        self._assert_status_code_is(response, 400)
        assert "output 'o2' is a parameter" in response.json()["err_msg"]

    def test_validate_loop(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        workflow_id = self.workflow_populator.create_workflow(workflow)
        downloaded = self.workflow_populator.download_workflow(workflow_id, style="ga")
        loop_step = _step_by_label(downloaded["steps"], "loop")
        assert loop_step["loop"] == {"inputs": {"i1": {"output_source": "o1"}}, "output_method": "last_iteration"}
        assert loop_step["when"] == "$(inputs.i1 < 10)"
        reimported_id = self.workflow_populator.create_workflow(downloaded)
        reimported = self.workflow_populator.download_workflow(reimported_id, style="ga")
        assert _step_by_label(reimported["steps"], "loop")["loop"] == loop_step["loop"]
        response = self.workflow_populator.download_workflow_raw(workflow_id, style="format2")
        self._assert_status_code_is(response, 400)
        assert "cannot be exported to format2 yet" in response.json()["err_msg"]

    def test_validate_loop_fail_no_ext(self):
        workflow = single_loop_workflow("$(inputs.i1 < 10)")
        workflow_id = self.workflow_populator.create_workflow(workflow)
        with patch.object(self._app.config, "enable_beta_workflow_loop", False):
            # The switch is checked before the loop's contents.
            _step_by_label(workflow["steps"], "loop")["loop"] = {"unknown": True}
            response = self.workflow_populator.create_workflow_response(workflow)
            self._assert_status_code_is(response, 403)
            assert "workflow loops are not enabled" in response.json()["err_msg"]
            history_id = self.dataset_populator.new_history()
            response = self.workflow_populator.invoke_workflow_raw(
                workflow_id, {"history_id": history_id, "inputs": {"0": 1}, "inputs_by": "step_index"}
            )
            self._assert_status_code_is(response, 403)
            assert "workflow loops are not enabled" in response.json()["err_msg"]

    def test_loop_nesting_depth_limit(self):
        self.workflow_populator.create_workflow(nested_loops_workflow(4))
        response = self.workflow_populator.create_workflow_response(nested_loops_workflow(5))
        self._assert_status_code_is(response, 400)
        assert "nested at most 4 deep" in response.json()["err_msg"]

    def test_loop_iteration_limit(self):
        with patch.object(self._app.config, "workflow_loop_max_iterations", 3):
            invocation = self._run_failing(
                single_loop_workflow("$(inputs.i1 < 10)"), {"i1": {"value": 1, "type": "raw"}}
            )
        assert invocation["messages"][0]["reason"] == "loop_failed"
        assert invocation["messages"][0]["details"] == "Loop reached the limit of 3 iterations set by the server."
        assert self._outcomes(invocation["id"]) == ["continue", "continue", "limit"]

    def test_loop_failed_body_job(self):
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
outputs:
  o1:
    outputSource: add/sum
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
  fail:
    tool_id: job_properties
    state:
      thebool: true
      failbool: true
"""
        invocation = self._run_failing(
            single_loop_workflow("$(inputs.i1 < 10)", body=body), {"i1": {"value": 1, "type": "raw"}}
        )
        assert invocation["messages"][0]["reason"] == "job_failed"
        assert self._outcomes(invocation["id"]) == ["failed"]

    def _run_collection_feedback(self, body_steps: str, elements: list[dict[str, Any]]) -> dict[str, Any]:
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
outputs:
  o1:
    outputSource: loop/o1
steps:
  loop:
    in:
      i1: i1
    when: $(true)
    run:
      class: GalaxyWorkflow
      inputs:
        i1:
          type: collection
          collection_type: list
      outputs:
        o1:
          outputSource: change/output
      steps:
        change:
{indent(body_steps, " " * 10)}
""",
            SINGLE_VARIABLE_LOOP,
        )
        invocation = self._run_failing(workflow, {"i1": {"collection_type": "list", "elements": elements}})
        assert invocation["messages"][0]["reason"] == "loop_failed"
        assert self._outcomes(invocation["id"]) == ["failed"]
        return invocation["messages"][0]

    def test_loop_collection_feedback_must_keep_order(self):
        message = self._run_collection_feedback(
            "tool_id: __SORTLIST__\nin:\n  input: i1\n",
            [{"identifier": identifier, "content": "1"} for identifier in ("b", "a")],
        )
        assert (
            message["details"] == "Loop input 'i1' must keep its collection type, element identifiers and their order."
        )

    def test_loop_collection_feedback_must_keep_identifiers(self):
        # The empty element is dropped.
        message = self._run_collection_feedback(
            "tool_id: __FILTER_EMPTY_DATASETS__\nin:\n  input: i1\n",
            [{"identifier": "a", "content": "1"}, {"identifier": "b", "content": ""}],
        )
        assert (
            message["details"] == "Loop input 'i1' must keep its collection type, element identifiers and their order."
        )

    def test_loop_collection_feedback_must_stay_a_collection(self):
        message = self._run_collection_feedback(
            "tool_id: __EXTRACT_DATASET__\nin:\n  input: i1\n",
            [{"identifier": "a", "content": "1"}],
        )
        assert message["details"] == "Loop input 'i1' takes a dataset collection, output 'o1' is not one."

    def test_loop_mapped_over_refused_at_run_request(self):
        # The saved types match, the supplied collection is nested deeper than the loop takes.
        workflow = loop_workflow(
            """
class: GalaxyWorkflow
inputs:
  i1:
    type: collection
    collection_type: list
steps:
  loop:
    in:
      i1: i1
    when: $(true)
    run:
      class: GalaxyWorkflow
      inputs:
        i1:
          type: collection
          collection_type: list
      outputs:
        o1:
          outputSource: sort/output
      steps:
        sort:
          tool_id: __SORTLIST__
          in:
            input: i1
""",
            SINGLE_VARIABLE_LOOP,
        )
        workflow_id = self.workflow_populator.create_workflow(workflow)
        history_id = self.dataset_populator.new_history()
        hdca = self.dataset_collection_populator.create_list_of_list_in_history(history_id, wait=True).json()
        response = self.workflow_populator.invoke_workflow_raw(
            workflow_id,
            {
                "history_id": history_id,
                "inputs": {"0": {"src": "hdca", "id": hdca["id"]}},
                "inputs_by": "step_index",
            },
        )
        self._assert_status_code_is(response, 400)
        assert "mapping over a loop step is not supported" in response.json()["err_msg"]

    def test_validate_loop_fail_step_input_default_and_value_from(self):
        for step_input in ({"default": 5}, {"valueFrom": "$(inputs.i1 + 1)"}):
            workflow = single_loop_workflow("$(inputs.i1 < 10)")
            _step_by_label(workflow["steps"], "loop")["in"] = {"i1": step_input}
            response = self.workflow_populator.create_workflow_response(workflow)
            self._assert_status_code_is(response, 400)
            assert "of a loop step is not supported yet" in response.json()["err_msg"]

    def _run_sleeping_loop(self, output_method: str = "last_iteration") -> RunJobsSummary:
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
  data: data
outputs:
  o1:
    outputSource: add/sum
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
  sleep:
    tool_id: cat_data_and_sleep
    state:
      sleep_time: 15
    in:
      input1: data
"""
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  data: data
steps:
  loop:
    in:
      i1: i1
      data: data
    when: $(inputs.i1 < 10)
    run:
{indent(body, " " * 6)}
""",
            {"loop": {**SINGLE_VARIABLE_LOOP["loop"], "output_method": output_method}},
        )
        summary = self._run(
            workflow,
            {"i1": {"value": 1, "type": "raw"}, "data": {"value": "1.txt", "type": "File"}},
            assert_ok=False,
            wait=False,
        )

        def second_iteration_started():
            invocation = self.workflow_populator.get_invocation(summary.invocation_id, step_details=True)
            steps = [step for step in invocation["steps"] if step["workflow_step_label"] == "loop"]
            return steps[0]["iterations"] if steps and len(steps[0]["iterations"]) >= 2 else None

        wait_on(second_iteration_started, "second loop iteration")
        return summary

    def _assert_newest_iteration_cancelled(self, summary: RunJobsSummary, iterations_at_cancel: int) -> None:
        iterations = self._iterations(summary.invocation_id)
        # The iteration allocated in the pass during which the cancellation arrived may exist.
        assert iterations_at_cancel <= len(iterations) <= iterations_at_cancel + 1
        newest = iterations[-1]["subworkflow_invocation_id"]
        assert self.workflow_populator.get_invocation(newest)["state"] == "cancelled"
        body_jobs = self.dataset_populator.invocation_jobs(newest)
        assert "deleted" in {job["state"] for job in body_jobs}, body_jobs
        for job in self.dataset_populator.history_jobs(summary.history_id):
            assert job["state"] in ("ok", "skipped", "deleted"), job

    def test_cancel_loop(self):
        summary = self._run_sleeping_loop()
        iterations_at_cancel = len(self._iterations(summary.invocation_id))
        self.workflow_populator.cancel_invocation(summary.invocation_id)
        self.workflow_populator.wait_for_invocation(None, summary.invocation_id, assert_ok=False)
        self.dataset_populator.wait_for_history_jobs(summary.history_id)
        assert self.workflow_populator.get_invocation(summary.invocation_id)["state"] == "cancelled"
        self._assert_newest_iteration_cancelled(summary, iterations_at_cancel)

    def test_cancel_all_iterations_loop_builds_nothing(self):
        summary = self._run_sleeping_loop("all_iterations")
        self.workflow_populator.cancel_invocation(summary.invocation_id)
        self.workflow_populator.wait_for_invocation(None, summary.invocation_id, assert_ok=False)
        self.dataset_populator.wait_for_history_jobs(summary.history_id)
        assert self.workflow_populator.get_invocation(summary.invocation_id)["state"] == "cancelled"
        assert self._all_iterations_collections(summary.history_id) == []

    def test_cancel_loop_iteration(self):
        # Cancelling the subworkflow invocation of the running iteration cancels the loop.
        summary = self._run_sleeping_loop()
        iterations = self._iterations(summary.invocation_id)
        self.workflow_populator.cancel_invocation(iterations[-1]["subworkflow_invocation_id"])
        self.workflow_populator.wait_for_invocation(None, summary.invocation_id, assert_ok=False)
        self.dataset_populator.wait_for_history_jobs(summary.history_id)
        assert self.workflow_populator.get_invocation(summary.invocation_id)["state"] == "cancelled"
        self._assert_newest_iteration_cancelled(summary, len(iterations))


class TestWorkflowLoopExport(BaseWorkflowLoopIntegrationTestCase, UsesCeleryTasks):
    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        UsesCeleryTasks.handle_galaxy_config_kwds(config)

    def test_export_import_keeps_iterations(self):
        summary = self._run(single_loop_workflow("$(inputs.i1 < 4)"), {"i1": {"value": 1, "type": "raw"}})
        store_path = self.workflow_populator.download_invocation_to_store(summary.invocation_id, extension="tgz")
        history_id = self.dataset_populator.new_history()
        imported = self.workflow_populator.create_invocation_from_store(history_id, store_path=store_path)
        # The store holds the invocation and its three iterations.
        assert len(imported) == 4
        imported_root = next(
            invocation
            for invocation in imported
            if any(
                step["workflow_step_label"] == "loop"
                for step in self.workflow_populator.get_invocation(invocation["id"], step_details=True)["steps"]
            )
        )
        imported_iterations = self._iterations(imported_root["id"])
        original_iterations = self._iterations(summary.invocation_id)
        assert [(iteration["iteration"], iteration["loop_outcome"]) for iteration in imported_iterations] == [
            (iteration["iteration"], iteration["loop_outcome"]) for iteration in original_iterations
        ]
        assert {iteration["subworkflow_invocation_id"] for iteration in imported_iterations}.isdisjoint(
            iteration["subworkflow_invocation_id"] for iteration in original_iterations
        )

    def test_export_import_keeps_all_iterations_output(self):
        workflow = single_loop_workflow("$(inputs.i1 < 4)")
        _step_by_label(workflow["steps"], "loop")["loop"]["output_method"] = "all_iterations"
        summary = self._run(workflow, {"i1": {"value": 1, "type": "raw"}})
        store_path = self.workflow_populator.download_invocation_to_store(summary.invocation_id, extension="tgz")
        history_id = self.dataset_populator.new_history()
        imported = self.workflow_populator.create_invocation_from_store(history_id, store_path=store_path)
        imported_root = next(
            invocation
            for invocation in imported
            if self.workflow_populator.get_invocation(invocation["id"])["output_collections"]
        )
        output = self.workflow_populator.get_invocation(imported_root["id"])["output_collections"]["o1"]
        # The archive holds no files, so the imported datasets are not ok; read the collection as it is.
        hdca = self._get(f"histories/{history_id}/contents/dataset_collections/{output['id']}").json()
        assert hdca["collection_type"] == "list"
        assert [element["element_identifier"] for element in hdca["elements"]] == ["0", "1", "2"]


class TestWorkflowLoopEmbeddedPulsar(BaseWorkflowLoopIntegrationTestCase):
    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["job_config_file"] = EMBEDDED_PULSAR_JOB_CONFIG_FILE

    def test_loop_on_pulsar(self):
        # Feeds a dataset made on the Pulsar destination back into the next iteration.
        body = """
class: GalaxyWorkflow
inputs:
  i1: int
  data: data
outputs:
  o1:
    outputSource: add/sum
  data:
    outputSource: cat/out_file1
steps:
  add:
    tool_id: expression_add_int
    in:
      a: i1
  cat:
    tool_id: cat
    in:
      input1: data
      queries_0|input2: data
"""
        workflow = loop_workflow(
            f"""
class: GalaxyWorkflow
inputs:
  i1: int
  data: data
outputs:
  o1:
    outputSource: loop/o1
  data:
    outputSource: loop/data
steps:
  loop:
    in:
      i1: i1
      data: data
    when: $(inputs.i1 < 4)
    run:
{indent(body, " " * 6)}
""",
            {"loop": {"inputs": {"i1": {"output_source": "o1"}, "data": {"output_source": "data"}}}},
        )
        summary = self._run(
            workflow, {"i1": {"value": 1, "type": "raw"}, "data": {"value": "simple_line.txt", "type": "File"}}
        )
        assert self._output_value(summary, "o1") == 4
        invocation = self.workflow_populator.get_invocation(summary.invocation_id)
        content = self.dataset_populator.get_history_dataset_content(
            summary.history_id, dataset_id=invocation["outputs"]["data"]["id"]
        )
        assert content == "This is a line of text.\n" * 8
        # Expression tools always run in the Galaxy process, the cat jobs run on Pulsar.
        history_id = self._app.security.decode_id(summary.history_id)
        destinations = self._app.model.session.scalars(
            select(Job.destination_id).where(Job.tool_id == "cat", Job.history_id == history_id)
        ).all()
        assert destinations == ["pulsar_embed"] * 3
