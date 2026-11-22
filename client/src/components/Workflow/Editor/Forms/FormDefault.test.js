import { createTestingPinia } from "@pinia/testing";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { h } from "vue";

import { resetMockConfig, setMockConfig } from "@/composables/__mocks__/config";
import { useRefreshFromStore } from "@/stores/refreshFromStore";

import FormCollectionType from "./FormCollectionType.vue";
import FormConditional from "./FormConditional.vue";
import FormDefault from "./FormDefault.vue";
import FormInputCollection from "./FormInputCollection.vue";
import FormLoop from "./FormLoop.vue";

vi.mock("./FormDatatype.vue", () => ({ default: { render: () => h("div") } }));
vi.mock("@/composables/config");

const localVue = getLocalVue();

describe("FormDefault", () => {
    let wrapper;
    const outputs = [
        { name: "output-name", label: "output-label" },
        { name: "other-name", label: "other-label" },
    ];

    beforeEach(() => {
        wrapper = mount(FormDefault, {
            props: {
                datatypes: [],
                step: {
                    id: 0,
                    contentId: "id",
                    annotation: "annotation",
                    label: "label",
                    name: "name",
                    type: "subworkflow",
                    configForm: {
                        inputs: [],
                    },
                    inputs: [],
                    outputs,
                },
            },
            global: { ...localVue, provide: { workflowId: "mock-workflow" } },
            pinia: createTestingPinia({ createSpy: vi.fn }),
        });
    });

    it("re-seeds the collection input form from the step on refresh", async () => {
        const collectionStep = {
            id: 0,
            content_id: null,
            annotation: "annotation",
            label: "label",
            name: "name",
            type: "data_collection_input",
            config_form: { inputs: [] },
            inputs: [],
            outputs: [],
            tool_state: { collection_type: '"list"' },
        };
        const collectionWrapper = mount(FormDefault, {
            propsData: { datatypes: [], step: collectionStep },
            global: { ...localVue, provide: { workflowId: "mock-workflow" } },
            pinia: createTestingPinia({ createSpy: vi.fn, stubActions: false }),
        });
        const collectionTypeField = () =>
            collectionWrapper.findComponent(FormInputCollection).findComponent(FormCollectionType);

        collectionTypeField().vm.$emit("onChange", "paired");
        await collectionWrapper.vm.$nextTick();
        expect(collectionTypeField().props("value")).toBe("paired");
        expect(collectionWrapper.emitted("onSetData")).toHaveLength(1);

        useRefreshFromStore().refresh();
        await collectionWrapper.vm.$nextTick();
        expect(collectionTypeField().props("value")).toBe("list");
        expect(collectionWrapper.emitted("onSetData")).toHaveLength(1);

        collectionTypeField().vm.$emit("onChange", "list:paired");
        expect(collectionWrapper.emitted("onSetData")).toHaveLength(2);
        expect(collectionWrapper.emitted("onSetData")[1][1].inputs.collection_type).toBe("list:paired");
        collectionWrapper.unmount();
    });

    it("check initial value and value change", async () => {
        const title = wrapper.find(".portlet-title-text").text();
        expect(title).toBe("name");
        const inputCount = wrapper.findAll("input").length;
        expect(inputCount).toBe(4);
        const outputLabelCount = wrapper.findAll("#__label__output-name").length;
        expect(outputLabelCount).toBe(1);
        const otherLabelCount = wrapper.findAll("#__label__other-name").length;
        expect(otherLabelCount).toBe(1);
    });

    describe("loop section", () => {
        const loop = { inputs: { i1: { output_source: "o1" } }, output_method: "last_iteration" };

        function mountStep(step) {
            return mount(FormDefault, {
                props: {
                    datatypes: [],
                    step: {
                        id: 0,
                        name: "name",
                        type: "subworkflow",
                        config_form: { inputs: [] },
                        inputs: [],
                        outputs,
                        input_connections: {},
                        ...step,
                    },
                },
                global: { ...localVue, provide: { workflowId: "mock-workflow" } },
                pinia: createTestingPinia({ createSpy: vi.fn }),
            });
        }

        afterEach(() => {
            resetMockConfig();
        });

        it("is hidden while workflow loops are disabled, and the conditional switch is kept", () => {
            const loopWrapper = mountStep({ when: "$(inputs.i1 < 10)", loop });
            expect(loopWrapper.findComponent(FormLoop).exists()).toBe(false);
            expect(loopWrapper.findComponent(FormConditional).exists()).toBe(true);
        });

        it("is shown on a subworkflow step when workflow loops are enabled", () => {
            setMockConfig({ enable_beta_workflow_loop: true });
            const loopWrapper = mountStep({});
            expect(loopWrapper.findComponent(FormLoop).exists()).toBe(true);
            expect(loopWrapper.findComponent(FormConditional).exists()).toBe(true);
        });

        it("replaces the conditional switch on a loop step", () => {
            setMockConfig({ enable_beta_workflow_loop: true });
            const loopWrapper = mountStep({ when: "$(inputs.i1 < 10)", loop });
            expect(loopWrapper.findComponent(FormLoop).exists()).toBe(true);
            expect(loopWrapper.findComponent(FormConditional).exists()).toBe(false);
            expect(loopWrapper.emitted("onUpdateStep")).toBeUndefined();
        });

        it("is hidden on a step that is not a subworkflow", () => {
            setMockConfig({ enable_beta_workflow_loop: true });
            const loopWrapper = mountStep({ type: "tool", content_id: "cat1" });
            expect(loopWrapper.findComponent(FormLoop).exists()).toBe(false);
        });
    });
});
