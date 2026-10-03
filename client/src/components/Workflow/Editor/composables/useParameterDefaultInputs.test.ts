import "@/composables/__mocks__/filter";

import { createTestingPinia } from "@pinia/testing";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import { getActivePinia, PiniaVuePlugin, setActivePinia } from "pinia";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { computed, nextTick } from "vue";

import type { FormInputNode } from "@/components/Form/composables/useFormState";
import { visitAllInputs } from "@/components/Form/utilities";
import { useConnectionStore } from "@/stores/workflowConnectionStore";
import { type Step, useWorkflowStepStore } from "@/stores/workflowStepStore";

import { useParameterDefaultInputs } from "./useParameterDefaultInputs";

import FormSelect from "@/components/Form/Elements/FormSelect.vue";
import FormDefault from "@/components/Workflow/Editor/Forms/FormDefault.vue";

const defaultName = "parameter_definition|optional|specify_default|default";
const localVue = getLocalVue();
localVue.use(PiniaVuePlugin);

function conditional(name: string, value: string | boolean, cases: FormInputNode["cases"]): FormInputNode {
    return {
        name,
        type: "conditional",
        test_param: { name, type: typeof value === "boolean" ? "boolean" : "text", value },
        cases,
    };
}

function parameterInputs(): FormInputNode[] {
    const optionalCases = ["true", "false"].map((value) => ({
        value,
        inputs: [
            conditional("specify_default", true, [
                { value: "true", inputs: [{ name: "default", type: "text", value: "vertebrata_odb10" }] },
                { value: "false", inputs: [] },
            ]),
        ],
    }));
    return [
        conditional("parameter_definition", "text", [
            {
                value: "text",
                inputs: [
                    { name: "multiple", type: "boolean", value: false },
                    conditional("optional", false, optionalCases),
                    conditional("restrictions", "onConnections", [{ value: "onConnections", inputs: [] }]),
                ],
            },
            {
                value: "integer",
                inputs: [{ name: "default", type: "integer", value: 3 }],
            },
        ]),
    ];
}

function step(id: number, type: Step["type"], inputs: FormInputNode[]): Step {
    return {
        id,
        type,
        name: "Input",
        content_id: null,
        tool_state: {},
        input_connections: {},
        inputs: [],
        outputs: [],
        config_form: { inputs },
    };
}

function select(name = "lineage", options = [["Vertebrata", "vertebrata_odb10", false]]): FormInputNode {
    return { name, type: "select", options };
}

function defaults(inputs: FormInputNode[]) {
    const result: FormInputNode[] = [];
    visitAllInputs(inputs, (input: FormInputNode, name: string) => {
        if (name === defaultName) {
            result.push(input);
        }
    });
    return result;
}

describe("workflow parameter default options", () => {
    let stepStore: ReturnType<typeof useWorkflowStepStore>;
    let connectionStore: ReturnType<typeof useConnectionStore>;
    let parameter: Step;

    function updateStep(id: number, updates: Partial<Step>) {
        stepStore.updateStep({ ...stepStore.getStep(id)!, ...updates });
    }

    function connect(id = 1, name = "lineage") {
        connectionStore.addConnection({
            input: { stepId: id, name, connectorType: "input" },
            output: { stepId: 0, name: "output", connectorType: "output" },
        });
    }

    function formInputs() {
        return useParameterDefaultInputs(
            computed(() => stepStore.getStep(0)!),
            stepStore,
            connectionStore,
        );
    }

    beforeEach(() => {
        setActivePinia(createTestingPinia({ createSpy: vi.fn, stubActions: false }));
        stepStore = useWorkflowStepStore("default-options");
        connectionStore = useConnectionStore("default-options");
        parameter = stepStore.addStep(step(0, "parameter_input", parameterInputs()));
        stepStore.addStep(step(1, "tool", [select()]));
    });

    it("uses labels and values in both optional branches without modifying stored forms", () => {
        connect();
        const inputs = formInputs().value;
        expect(defaults(inputs)).toHaveLength(2);
        for (const input of defaults(inputs)) {
            expect(input).toMatchObject({ type: "select", value: "vertebrata_odb10", options: select().options });
        }
        expect(defaults(parameter.config_form!.inputs)[0]!.type).toBe("text");
        expect(inputs[0]!.cases![1]!.inputs[0]!.type).toBe("integer");
    });

    it("intersects values, combines differing labels, and sorts the intersection", () => {
        updateStep(1, {
            config_form: {
                inputs: [
                    select("lineage", [
                        ["Vertebrata", "v", false],
                        ["Bacteria", "b", false],
                        ["Excluded", "excluded", false],
                    ]),
                ],
            },
        });
        stepStore.addStep(
            step(2, "tool", [
                select("lineage", [
                    ["Vertebrates", "v", false],
                    ["Bacteria", "b", false],
                    ["Other", "o", false],
                ]),
            ]),
        );
        connect();
        connect(2);
        expect(defaults(formInputs().value)[0]!.options).toEqual([
            ["Bacteria", "b", false],
            ["Vertebrata, Vertebrates", "v", false],
        ]);
    });

    it("falls back when a connected select has unavailable options", () => {
        stepStore.addStep(step(2, "tool", [{ name: "lineage", type: "select" }]));
        connect();
        connect(2);
        expect(formInputs().value).toBe(parameter.config_form!.inputs);
    });

    it("ignores connected text inputs when collecting select restrictions", () => {
        stepStore.addStep(step(2, "tool", [{ name: "lineage", type: "text" }]));
        connect();
        connect(2);
        expect(defaults(formInputs().value)[0]!.options).toEqual(select().options);
    });

    it("keeps an empty intersection as a select with no permitted options", () => {
        stepStore.addStep(step(2, "tool", [select("lineage", [["Other", "other", false]])]));
        connect();
        connect(2);
        expect(defaults(formInputs().value)[0]).toMatchObject({ type: "select", options: [] });
    });

    it("looks up the full input path through active conditionals, sections, and repeats", () => {
        updateStep(1, {
            config_form: {
                inputs: [
                    conditional("mode", "active", [
                        { value: "inactive", inputs: [select("lineage", [["Wrong", "wrong", false]])] },
                        {
                            value: "active",
                            inputs: [
                                {
                                    name: "section",
                                    type: "section",
                                    inputs: [{ name: "repeat", type: "repeat", cache: [[select()]] }],
                                },
                            ],
                        },
                    ]),
                ],
            },
        });
        connect(1, "mode|section|repeat_0|lineage");
        expect(defaults(formInputs().value)[0]!.options).toEqual(select().options);
    });

    it("updates options when connected tool state changes and falls back after disconnection", () => {
        connect();
        const inputs = formInputs();
        expect(defaults(inputs.value)[0]!.type).toBe("select");
        const updatedOptions = [["Updated", "updated", false]];
        updateStep(1, { config_form: { inputs: [select("lineage", updatedOptions)] } });
        expect(defaults(inputs.value)[0]!.options).toEqual(updatedOptions);
        expect(defaults(inputs.value)[0]!.value).toBe("vertebrata_odb10");
        connectionStore.removeConnection("1-lineage-0-output");
        expect(defaults(inputs.value)[0]!.type).toBe("text");
    });

    it.each(["no connections", "text connection", "missing tool form", "unrestricted", "other parameter type"])(
        "retains the original form for %s",
        (scenario) => {
            if (scenario !== "no connections") {
                connect();
            }
            if (scenario === "text connection") {
                updateStep(1, { config_form: { inputs: [{ name: "lineage", type: "text" }] } });
            } else if (scenario === "missing tool form") {
                updateStep(1, { config_form: undefined });
            } else if (scenario === "unrestricted") {
                parameter.config_form!.inputs[0].cases[0].inputs[2].test_param.value = "none";
            } else if (scenario === "other parameter type") {
                parameter.config_form!.inputs[0].test_param.value = "integer";
            }
            expect(formInputs().value).toBe(parameter.config_form!.inputs);
        },
    );

    it("preserves text serialization for multiple defaults", () => {
        parameter.config_form!.inputs[0].cases[0].inputs[0].value = true;
        connect();
        expect(formInputs().value).toBe(parameter.config_form!.inputs);
    });

    it("renders the saved default label and submits the selected underlying value", async () => {
        updateStep(1, {
            config_form: {
                inputs: [
                    select("lineage", [
                        ["Vertebrata", "vertebrata_odb10", false],
                        ["Bacteria", "bacteria_odb10", false],
                    ]),
                ],
            },
        });
        connect();
        const wrapper = mount(FormDefault as object, {
            localVue,
            pinia: getActivePinia(),
            propsData: { step: parameter, datatypes: [] },
            provide: { workflowId: "default-options" },
        });
        const selector = wrapper.findComponent(FormSelect);
        expect(selector.props("value")).toBe("vertebrata_odb10");
        expect(selector.text()).toContain("Vertebrata");
        expect(wrapper.emitted("onSetData")).toBeUndefined();
        selector.vm.$emit("input", "bacteria_odb10");
        await nextTick();
        expect(wrapper.emitted("onSetData")![0]![1]).toMatchObject({ inputs: { [defaultName]: "bacteria_odb10" } });
        wrapper.destroy();
    });

    it("switches between text and select without losing a locally edited default", async () => {
        const wrapper = mount(FormDefault as object, {
            localVue,
            pinia: getActivePinia(),
            propsData: { step: parameter, datatypes: [] },
            provide: { workflowId: "default-options" },
        });
        expect(wrapper.findComponent(FormSelect).exists()).toBe(false);
        connect();
        await nextTick();
        expect(wrapper.findComponent(FormSelect).props("value")).toBe("vertebrata_odb10");
        expect(wrapper.emitted("onSetData")).toBeUndefined();
        wrapper.findComponent(FormSelect).vm.$emit("input", "edited-default");
        await nextTick();
        connectionStore.removeConnection("1-lineage-0-output");
        await nextTick();
        expect(wrapper.findComponent(FormSelect).exists()).toBe(false);
        expect(wrapper.emitted("onSetData")).toHaveLength(1);
        expect((wrapper.find(`input[id='${defaultName}']`).element as HTMLInputElement).value).toBe("edited-default");
        wrapper.destroy();
    });
});
