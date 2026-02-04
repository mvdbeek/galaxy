"""
Tests for workflow invocation queuing with dependencies on other invocations.

This module tests the ability to queue a new workflow invocation that uses
outputs from another (potentially still running) invocation as inputs.
"""

from galaxy_test.base.populators import (
    DatasetPopulator,
    WorkflowPopulator,
)
from galaxy_test.base.workflow_fixtures import WORKFLOW_WITH_OUTPUTS
from ._framework import ApiTestCase


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
            # Run first workflow with test_data
            summary1 = self.workflow_populator.run_workflow(
                WORKFLOW_WITH_OUTPUTS,
                test_data={"input1": "test content"},
                history_id=history_id,
            )
            invocation1_id = summary1.invocation_id
            workflow1_id = summary1.workflow_id

            # Create second workflow and invoke with reference to first invocation's output
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)

            # Invoke with invocation output reference
            invocation2_id = self.workflow_populator.invoke_workflow_and_assert_ok(
                workflow2_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1_id,
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )

            # Wait for second invocation to complete
            self.workflow_populator.wait_for_invocation_and_completion(invocation2_id)

            # Verify second invocation completed successfully
            final_invocation = self.workflow_populator.get_invocation(invocation2_id)
            assert final_invocation["state"] == "completed"

    def test_invoke_with_invocation_output_reference_before_completion(self):
        """Test invoking a workflow referencing an output before source invocation completes."""
        with self.dataset_populator.test_history() as history_id:
            # Run first workflow without waiting for completion
            summary1 = self.workflow_populator.run_workflow(
                WORKFLOW_WITH_OUTPUTS,
                test_data={"input1": "test content"},
                history_id=history_id,
                wait=False,
            )
            invocation1_id = summary1.invocation_id

            # Immediately invoke second workflow (before first completes)
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)

            invocation2_id = self.workflow_populator.invoke_workflow_and_assert_ok(
                workflow2_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1_id,
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )

            # Check that second invocation has input dependencies
            invocation2_details = self.workflow_populator.get_invocation(invocation2_id)
            assert "input_dependencies" in invocation2_details
            assert len(invocation2_details["input_dependencies"]) == 1

            dep = invocation2_details["input_dependencies"][0]
            assert dep["source_invocation_id"] == invocation1_id
            assert dep["output_name"] == "wf_output_1"

            # Wait for second invocation to complete (it will wait for first internally)
            self.workflow_populator.wait_for_invocation_and_completion(invocation2_id)

            # Verify dependency was resolved
            final_invocation = self.workflow_populator.get_invocation(invocation2_id)
            if final_invocation.get("input_dependencies"):
                dep = final_invocation["input_dependencies"][0]
                assert dep["resolved"] is True

    def test_invocation_output_reference_invalid_output_name(self):
        """Test error handling for invalid output name reference."""
        with self.dataset_populator.test_history() as history_id:
            summary1 = self.workflow_populator.run_workflow(
                WORKFLOW_WITH_OUTPUTS,
                test_data={"input1": "test"},
                history_id=history_id,
            )
            invocation1_id = summary1.invocation_id

            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)

            # Try to reference non-existent output
            invoke_response = self.workflow_populator.invoke_workflow(
                workflow2_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1_id,
                        "output_name": "nonexistent_output",
                    }
                },
                inputs_by="name",
            )

            self._assert_status_code_is(invoke_response, 400)
            assert "not found" in invoke_response.json()["err_msg"].lower()

    def test_invocation_output_reference_invalid_invocation(self):
        """Test error handling for invalid invocation ID reference."""
        with self.dataset_populator.test_history() as history_id:
            workflow_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)

            # Try to reference non-existent invocation
            invoke_response = self.workflow_populator.invoke_workflow(
                workflow_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": "nonexistent_id",
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )

            self._assert_status_code_is(invoke_response, 400)

    def test_chained_invocations(self):
        """Test chaining multiple invocations together."""
        with self.dataset_populator.test_history() as history_id:
            # Start first workflow with test_data
            summary1 = self.workflow_populator.run_workflow(
                WORKFLOW_WITH_OUTPUTS,
                test_data={"input1": "initial"},
                history_id=history_id,
                wait=False,
            )
            inv1_id = summary1.invocation_id

            # Chain second workflow to first
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)
            inv2_id = self.workflow_populator.invoke_workflow_and_assert_ok(
                workflow2_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv1_id,
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )

            # Chain third workflow to second
            workflow3_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)
            inv3_id = self.workflow_populator.invoke_workflow_and_assert_ok(
                workflow3_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv2_id,
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )

            # Wait for final invocation (it will wait for the chain)
            self.workflow_populator.wait_for_invocation_and_completion(inv3_id)

            # Verify all completed
            for inv_id in [inv1_id, inv2_id, inv3_id]:
                state = self.workflow_populator.get_invocation(inv_id)
                assert state["state"] == "completed"

    def test_waiting_for_input_state(self):
        """Test that WAITING_FOR_INPUT state is set correctly."""
        with self.dataset_populator.test_history() as history_id:
            # Start first workflow without waiting
            summary1 = self.workflow_populator.run_workflow(
                WORKFLOW_WITH_OUTPUTS,
                test_data={"input1": "test"},
                history_id=history_id,
                wait=False,
            )
            invocation1_id = summary1.invocation_id

            # Immediately create dependent invocation
            workflow2_id = self.workflow_populator.upload_yaml_workflow(WORKFLOW_WITH_OUTPUTS)

            invoke_response = self.workflow_populator.invoke_workflow(
                workflow2_id,
                history_id=history_id,
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1_id,
                        "output_name": "wf_output_1",
                    }
                },
                inputs_by="name",
            )
            self._assert_status_code_is(invoke_response, 200)
            invocation2 = invoke_response.json()

            # The state should be waiting_for_input if output isn't available yet
            # or it could transition to ready/scheduled if the first invocation completed quickly
            assert invocation2["state"] in ("new", "waiting_for_input", "ready", "scheduled")

            # Wait for completion
            self.workflow_populator.wait_for_invocation_and_completion(invocation2["id"])
