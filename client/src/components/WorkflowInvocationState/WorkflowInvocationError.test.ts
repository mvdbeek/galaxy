import { createTestingPinia } from "@pinia/testing";
import { shallowMount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";

import type { InvocationMessage, WorkflowInvocationElementView } from "@/api/invocations";

import WorkflowInvocationError from "./WorkflowInvocationError.vue";

vi.mock("@/composables/useWorkflowInstance", () => ({
    useWorkflowInstance: () => ({ workflow: { value: undefined } }),
}));

describe("WorkflowInvocationError", () => {
    it("renders an item card for each mismatched collection reference", () => {
        const invocationMessage: InvocationMessage = {
            reason: "collection_structure_mismatch",
            workflow_step_id: 3,
            details:
                "Collections 'lines' (no elements) and 'populated collection' (2 elements) have different element " +
                "structures. To map them together, use collections with the same number and nesting of elements.",
            collection_references: [
                { src: "hdca", id: "abc123" },
                { src: "dce", id: "def456" },
            ],
        };
        const wrapper = shallowMount(WorkflowInvocationError as object, {
            propsData: {
                invocationMessage,
                invocation: { id: "", workflow_id: "", steps: [] } as unknown as WorkflowInvocationElementView,
                storeId: "invocation-test",
            },
            pinia: createTestingPinia({ createSpy: vi.fn }),
        });

        const items = wrapper.findAll("[itemsrc]");
        expect(items).toHaveLength(2);
        expect(items.at(0).attributes("itemid")).toBe("abc123");
        expect(items.at(0).attributes("itemsrc")).toBe("hdca");
        expect(items.at(1).attributes("itemid")).toBe("def456");
        expect(items.at(1).attributes("itemsrc")).toBe("dce");
        expect(wrapper.text()).toContain("Mismatched collection:");
    });
});
