import { createTestingPinia } from "@pinia/testing";
import { getLocalVue, withPlugins } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { useServerMock } from "@/api/client/__mocks__";
import type {
    InvocationState,
    InvocationStep,
    InvocationStepIteration,
    WorkflowInvocationElementView,
} from "@/api/invocations";
import type { WorkflowStepTyped } from "@/api/workflows";

import invocationData from "../Workflow/test/json/invocation.json";

import WorkflowInvocationStep from "./WorkflowInvocationStep.vue";

const localVue = getLocalVue();
const { server, http } = useServerMock();

const SELECTORS = {
    SUBWORKFLOW_ALERT: "[data-description='subworkflow alert']",
    LOOP_ITERATIONS: ".workflow-loop-iterations",
    ITERATION: "[data-description='loop iteration']",
};

const SUBWORKFLOW_STEP = {
    id: 0,
    type: "subworkflow",
    input_steps: {},
    annotation: null,
} as unknown as WorkflowStepTyped;

/** Mount an expanded subworkflow step; `stepFetches` counts the requests for the step's details. */
async function mountSubworkflowStep(
    iterations: InvocationStepIteration[],
    stepState: InvocationStep["state"] = "scheduled",
    invocationState: InvocationState = "scheduled",
) {
    const invocationStep = {
        ...invocationData.steps[0],
        workflow_step_label: "subworkflow",
        subworkflow_invocation_id: "newest-child",
        state: stepState,
        iterations,
    } as InvocationStep;
    const stepFetches = { count: 0 };
    server.use(
        http.get("/api/invocations/steps/{step_id}", ({ response }) => {
            stepFetches.count++;
            return response(200).json(invocationStep);
        }),
    );
    const invocation = {
        ...invocationData,
        state: invocationState,
        steps: [invocationStep],
    } as unknown as WorkflowInvocationElementView;
    const wrapper = mount(WorkflowInvocationStep as object, {
        props: { invocation, workflowStep: SUBWORKFLOW_STEP, expanded: true },
        global: {
            ...withPlugins(localVue, createTestingPinia({ createSpy: vi.fn, stubActions: false })),
            stubs: {
                ...localVue.stubs,
                WorkflowInvocationStepHeader: true,
                GTabs: true,
                GTab: true,
                SubworkflowAlert: { template: "<div data-description='subworkflow alert' />" },
            },
        },
    });
    await flushPromises();
    return { wrapper, stepFetches };
}

/** Wait past the step's 3 second poll interval */
async function afterPollInterval() {
    await vi.advanceTimersByTimeAsync(3500);
    await flushPromises();
}

describe("WorkflowInvocationStep", () => {
    it("shows the subworkflow alert and no iteration list for a subworkflow step that is not a loop", async () => {
        const { wrapper } = await mountSubworkflowStep([]);
        expect(wrapper.find(SELECTORS.SUBWORKFLOW_ALERT).exists()).toBe(true);
        expect(wrapper.find(SELECTORS.LOOP_ITERATIONS).exists()).toBe(false);
    });

    it("shows the iterations of a loop step in place of the subworkflow alert", async () => {
        const { wrapper } = await mountSubworkflowStep([
            { iteration: 0, subworkflow_invocation_id: "first-child", loop_outcome: "continue" },
            { iteration: 1, subworkflow_invocation_id: "newest-child", loop_outcome: "stop" },
        ]);
        expect(wrapper.find(SELECTORS.SUBWORKFLOW_ALERT).exists()).toBe(false);
        expect(wrapper.findAll(SELECTORS.ITERATION)).toHaveLength(2);
    });

    describe("polling", () => {
        const failedLoop: InvocationStepIteration[] = [
            { iteration: 0, subworkflow_invocation_id: "first-child", loop_outcome: "failed" },
        ];

        beforeEach(() => {
            vi.useFakeTimers({ toFake: ["setTimeout", "clearTimeout"] });
        });

        afterEach(() => {
            vi.useRealTimers();
        });

        it("keeps polling a loop step that is new while the invocation is active", async () => {
            const { stepFetches } = await mountSubworkflowStep(failedLoop, "new", "ready");
            const fetchesAfterMount = stepFetches.count;
            await afterPollInterval();
            expect(stepFetches.count).toBeGreaterThan(fetchesAfterMount);
        });

        it("stops polling a loop step that stayed new once the invocation failed", async () => {
            const { stepFetches } = await mountSubworkflowStep(failedLoop, "new", "failed");
            const fetchesAfterMount = stepFetches.count;
            await afterPollInterval();
            expect(stepFetches.count).toBe(fetchesAfterMount);
        });

        it("keeps polling an ordinary subworkflow step that is new, whatever the invocation's state", async () => {
            const { stepFetches } = await mountSubworkflowStep([], "new", "failed");
            const fetchesAfterMount = stepFetches.count;
            await afterPollInterval();
            expect(stepFetches.count).toBeGreaterThan(fetchesAfterMount);
        });
    });
});
