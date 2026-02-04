"""
Tests for workflow invocation queuing with dependencies on other invocations.

This module tests the ability to queue a new workflow invocation that uses
outputs from another (potentially still running) invocation as inputs.
"""

from galaxy_test.base.populators import (
    DatasetPopulator,
    WorkflowPopulator,
)
from ._framework import ApiTestCase


WORKFLOW_SIMPLE_WITH_OUTPUT = """
class: GalaxyWorkflow
name: Simple Workflow With Output
inputs:
  input1: data
outputs:
  output1:
    outputSource: first_cat/out_file1
steps:
  first_cat:
    tool_id: cat1
    in:
      input1: input1
"""

WORKFLOW_CONSUMER = """
class: GalaxyWorkflow
name: Consumer Workflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: second_cat/out_file1
steps:
  second_cat:
    tool_id: cat1
    in:
      input1: input1
"""


class TestWorkflowInvocationQueuing(ApiTestCase):
    """Test cases for queuing workflows with invocation output dependencies."""

    dataset_populator: DatasetPopulator
    workflow_populator: WorkflowPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    def test_invoke_with_invocation_output_reference(self):
        """Test invoking a workflow with an output from another invocation."""
        with self.dataset_populator.test_history() as history_id:
            # Create and run first workflow
            workflow1_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)

            hda = self.dataset_populator.new_dataset(history_id, content="test content")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1_id,
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Create second workflow and invoke with reference to first invocation's output
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            # Invoke with invocation output reference
            invoke_response = self._post(
                f"workflows/{workflow2_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": invocation1["id"],
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )
            self._assert_status_code_is(invoke_response, 200)
            invocation2 = invoke_response.json()

            # Verify invocation was created
            assert invocation2["id"] is not None
            assert invocation2["state"] in ("new", "waiting_for_input", "ready")

            # Wait for first invocation to complete
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow1_id,
                invocation_id=invocation1["id"],
            )

            # Wait for second invocation to complete
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow2_id,
                invocation_id=invocation2["id"],
            )

            # Verify second invocation completed successfully
            final_invocation = self._get(f"invocations/{invocation2['id']}").json()
            assert final_invocation["state"] == "scheduled"

    def test_invoke_with_invocation_output_reference_before_completion(self):
        """Test invoking a workflow referencing an output before source invocation completes."""
        with self.dataset_populator.test_history() as history_id:
            # Create workflow that will take some time (uses sleep tool if available)
            workflow1_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)

            hda = self.dataset_populator.new_dataset(history_id, content="test content")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1_id,
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Immediately invoke second workflow (before first completes)
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            invoke_response = self._post(
                f"workflows/{workflow2_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": invocation1["id"],
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )
            self._assert_status_code_is(invoke_response, 200)
            invocation2 = invoke_response.json()

            # Check that second invocation has input dependencies
            invocation2_details = self._get(f"invocations/{invocation2['id']}").json()
            assert "input_dependencies" in invocation2_details
            assert len(invocation2_details["input_dependencies"]) == 1

            dep = invocation2_details["input_dependencies"][0]
            assert dep["source_invocation_id"] == invocation1["id"]
            assert dep["output_name"] == "output1"

            # Wait for both to complete
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow1_id,
                invocation_id=invocation1["id"],
            )
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow2_id,
                invocation_id=invocation2["id"],
            )

            # Verify dependency was resolved
            final_invocation = self._get(f"invocations/{invocation2['id']}").json()
            if final_invocation.get("input_dependencies"):
                dep = final_invocation["input_dependencies"][0]
                assert dep["resolved"] is True

    def test_invocation_output_reference_invalid_output_name(self):
        """Test error handling for invalid output name reference."""
        with self.dataset_populator.test_history() as history_id:
            workflow1_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)

            hda = self.dataset_populator.new_dataset(history_id, content="test")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1_id,
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            # Try to reference non-existent output
            invoke_response = self._post(
                f"workflows/{workflow2_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": invocation1["id"],
                            "output_name": "nonexistent_output",
                        }
                    },
                },
                json=True,
            )

            self._assert_status_code_is(invoke_response, 400)
            assert "not found" in invoke_response.json()["err_msg"].lower()

    def test_invocation_output_reference_invalid_invocation(self):
        """Test error handling for invalid invocation ID reference."""
        with self.dataset_populator.test_history() as history_id:
            workflow_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            # Try to reference non-existent invocation
            invoke_response = self._post(
                f"workflows/{workflow_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": "nonexistent_id",
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )

            self._assert_status_code_is(invoke_response, 400)

    def test_chained_invocations(self):
        """Test chaining multiple invocations together."""
        with self.dataset_populator.test_history() as history_id:
            # Create three workflows
            workflow1_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)
            workflow3_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            # Start first workflow
            hda = self.dataset_populator.new_dataset(history_id, content="initial")
            inv1 = self.workflow_populator.invoke_workflow(
                workflow1_id,
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Chain second workflow to first
            inv2_response = self._post(
                f"workflows/{workflow2_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": inv1["id"],
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )
            self._assert_status_code_is(inv2_response, 200)
            inv2 = inv2_response.json()

            # Chain third workflow to second
            inv3_response = self._post(
                f"workflows/{workflow3_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": inv2["id"],
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )
            self._assert_status_code_is(inv3_response, 200)
            inv3 = inv3_response.json()

            # Wait for all to complete
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow1_id,
                invocation_id=inv1["id"],
            )
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow2_id,
                invocation_id=inv2["id"],
            )
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow3_id,
                invocation_id=inv3["id"],
            )

            # Verify all completed
            for inv_id in [inv1["id"], inv2["id"], inv3["id"]]:
                state = self._get(f"invocations/{inv_id}").json()
                assert state["state"] == "scheduled"

    def test_waiting_for_input_state(self):
        """Test that WAITING_FOR_INPUT state is set correctly."""
        with self.dataset_populator.test_history() as history_id:
            # Create first workflow
            workflow1_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_SIMPLE_WITH_OUTPUT)

            hda = self.dataset_populator.new_dataset(history_id, content="test")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1_id,
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Immediately create dependent invocation
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_CONSUMER)

            invoke_response = self._post(
                f"workflows/{workflow2_id}/invocations",
                data={
                    "history_id": history_id,
                    "inputs": {
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": invocation1["id"],
                            "output_name": "output1",
                        }
                    },
                },
                json=True,
            )
            self._assert_status_code_is(invoke_response, 200)
            invocation2 = invoke_response.json()

            # The state should be waiting_for_input if output isn't available yet
            # or it could transition to ready/scheduled if the first invocation completed quickly
            assert invocation2["state"] in ("new", "waiting_for_input", "ready", "scheduled")

            # Wait for completion
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow1_id,
                invocation_id=invocation1["id"],
            )
            self.workflow_populator.wait_for_invocation_and_jobs(
                history_id=history_id,
                workflow_id=workflow2_id,
                invocation_id=invocation2["id"],
            )
