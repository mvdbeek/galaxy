import { createTestingPinia } from "@pinia/testing";
import { shallowMount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";

import type { InvocationMessage as InvocationMessageType } from "@/api/invocations";

import InvocationMessage from "./InvocationMessage.vue";

const STRUCTURE_MISMATCH_DETAILS =
    "Collections 'lines' (no elements) and 'populated collection' (2 elements) have different element " +
    "structures. To map them together, use collections with the same number and nesting of elements.";

function mountMessage(invocationMessage: InvocationMessageType) {
    return shallowMount(InvocationMessage as object, {
        propsData: { invocationMessage },
        pinia: createTestingPinia({ createSpy: vi.fn }),
    });
}

describe("InvocationMessage", () => {
    it("explains how to resolve a collection structure mismatch", () => {
        const wrapper = mountMessage({
            reason: "collection_structure_mismatch",
            workflow_step_id: 3,
            details: STRUCTURE_MISMATCH_DETAILS,
        });

        expect(wrapper.classes()).toContain("errormessage");
        expect(wrapper.text()).toBe(
            "Invocation scheduling failed because step 4 cannot map over its inputs. " + STRUCTURE_MISMATCH_DETAILS,
        );
    });

    it("renders step-path messages without a doubled separator", () => {
        const wrapper = mountMessage({
            reason: "when_not_boolean",
            workflow_step_id: 1,
            details: "",
        });

        expect(wrapper.text()).toBe(
            "Invocation scheduling failed because step 2 is a conditional step and the result of the " +
                "when expression is not a boolean type.",
        );
    });
});
