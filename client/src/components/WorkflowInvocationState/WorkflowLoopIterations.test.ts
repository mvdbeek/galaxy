import { faCheckCircle, faClock, faSpinner } from "@fortawesome/free-solid-svg-icons";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";

import type { InvocationState, InvocationStepIteration } from "@/api/invocations";

import WorkflowLoopIterations from "./WorkflowLoopIterations.vue";

const localVue = getLocalVue();

const SELECTORS = {
    SUMMARY: "[data-description='loop iterations summary']",
    ITERATION: "[data-description='loop iteration']",
    LABEL: "[data-description='loop iteration label']",
    TOGGLE: "[data-description='toggle loop iterations']",
};

function iterations(...outcomes: InvocationStepIteration["loop_outcome"][]): InvocationStepIteration[] {
    return outcomes.map((loop_outcome, iteration) => ({
        iteration,
        subworkflow_invocation_id: `child-${iteration}`,
        loop_outcome,
    }));
}

function mountIterations(loopIterations: InvocationStepIteration[], invocationState: InvocationState = "scheduled") {
    return mount(WorkflowLoopIterations as object, {
        props: { iterations: loopIterations, invocationState },
        global: localVue,
    });
}

type Wrapper = ReturnType<typeof mountIterations>;

function summary(wrapper: Wrapper) {
    return wrapper.find(SELECTORS.SUMMARY).text();
}

function rowTexts(wrapper: Wrapper) {
    return wrapper.findAll(SELECTORS.LABEL).map((label) => label.text().replace(/\s+/g, " "));
}

/** The icon name of each row and whether it spins */
function rowIcons(wrapper: Wrapper) {
    return wrapper.findAll(`${SELECTORS.ITERATION} > svg`).map((icon) => ({
        icon: icon.attributes("data-icon"),
        spin: icon.classes().includes("fa-spin"),
    }));
}

describe("WorkflowLoopIterations", () => {
    it("shows a later iteration without outcome as running", () => {
        const wrapper = mountIterations(iterations("continue", null), "ready");
        expect(summary(wrapper)).toBe("Loop running: iteration 1");
        expect(rowTexts(wrapper)).toEqual(["Iteration 0: completed, loop continued", "Iteration 1: running"]);
        expect(rowIcons(wrapper)[1]).toEqual({ icon: faSpinner.iconName, spin: true });
        expect(wrapper.find(SELECTORS.TOGGLE).exists()).toBe(false);
    });

    it("shows iteration 0 without outcome as not finished yet, since it may wait for the step's inputs", () => {
        const wrapper = mountIterations(iterations(null), "ready");
        expect(summary(wrapper)).toBe("Loop not finished yet");
        expect(rowTexts(wrapper)).toEqual(["Iteration 0: not finished yet"]);
        expect(rowIcons(wrapper)).toEqual([{ icon: faClock.iconName, spin: false }]);
    });

    it.each<InvocationState>(["cancelled", "cancelling", "failed", "scheduled", "completed"])(
        "shows an iteration without outcome as not finished once the invocation is %s",
        (invocationState) => {
            const wrapper = mountIterations(iterations("continue", null), invocationState);
            expect(summary(wrapper)).toBe("Loop did not finish");
            expect(rowTexts(wrapper)[1]).toBe("Iteration 1: did not finish");
            expect(rowIcons(wrapper)[1]?.spin).toBe(false);
        },
    );

    it("shows a loop that stopped", () => {
        const wrapper = mountIterations(iterations("continue", "continue", "stop"));
        expect(summary(wrapper)).toBe("Loop stopped after 3 iterations");
        expect(rowTexts(wrapper)[2]).toBe("Iteration 2: completed, loop stopped");
    });

    it("says iteration in the singular for a loop that stopped after one", () => {
        expect(summary(mountIterations(iterations("stop")))).toBe("Loop stopped after 1 iteration");
    });

    it("shows a loop whose condition was false before the first iteration", () => {
        const wrapper = mountIterations(iterations("skipped"));
        expect(summary(wrapper)).toBe("Loop did not run: its condition was false");
        expect(rowTexts(wrapper)).toEqual(["Iteration 0: skipped: condition was false"]);
    });

    it("shows a failed iteration", () => {
        const wrapper = mountIterations(iterations("continue", "failed"), "failed");
        expect(summary(wrapper)).toBe("Loop failed in iteration 1");
        expect(rowTexts(wrapper)[1]).toBe("Iteration 1: failed");
    });

    it("shows the iteration that reached the limit as completed and the loop as failed", () => {
        const wrapper = mountIterations(iterations("continue", "limit"), "failed");
        expect(summary(wrapper)).toBe("Loop stopped at the iteration limit after 2 iterations");
        expect(rowTexts(wrapper)[1]).toBe("Iteration 1: completed; loop failed: iteration limit reached");
        expect(rowIcons(wrapper)[1]).toEqual({ icon: faCheckCircle.iconName, spin: false });
    });

    it("links each iteration to its subworkflow invocation", () => {
        const wrapper = mountIterations(iterations("continue", "stop"));
        const links = wrapper.findAll(`${SELECTORS.ITERATION} a`);
        expect(links.map((link) => link.attributes("href"))).toEqual([
            "/workflows/invocations/child-0",
            "/workflows/invocations/child-1",
        ]);
        expect(links.map((link) => link.attributes("aria-label"))).toEqual(["View iteration 0", "View iteration 1"]);
        expect(links[0]!.attributes("target")).toBe("_blank");
    });

    it("lists only the newest iterations of a long loop until expanded", async () => {
        const outcomes: InvocationStepIteration["loop_outcome"][] = Array(63).fill("continue");
        const wrapper = mountIterations(iterations(...outcomes, "limit"), "failed");
        expect(summary(wrapper)).toBe("Loop stopped at the iteration limit after 64 iterations");

        let rows = wrapper.findAll(SELECTORS.ITERATION);
        expect(rows.map((row) => row.attributes("data-iteration"))).toEqual(["59", "60", "61", "62", "63"]);
        expect(wrapper.find(SELECTORS.TOGGLE).text()).toBe("Show all 64");
        expect(wrapper.find(SELECTORS.TOGGLE).attributes("aria-expanded")).toBe("false");

        await wrapper.find(SELECTORS.TOGGLE).trigger("click");
        rows = wrapper.findAll(SELECTORS.ITERATION);
        expect(rows).toHaveLength(64);
        expect(wrapper.find(SELECTORS.TOGGLE).text()).toBe("Show only the newest 5");
        expect(wrapper.find(SELECTORS.TOGGLE).attributes("aria-expanded")).toBe("true");
    });
});
