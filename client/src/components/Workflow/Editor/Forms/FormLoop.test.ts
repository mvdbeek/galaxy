import { createTestingPinia } from "@pinia/testing";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount, shallowMount, type VueWrapper } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { createPinia, setActivePinia } from "pinia";
import { describe, expect, it, vi } from "vitest";

import { useUndoRedoStore } from "@/stores/undoRedoStore";
import { useConnectionStore } from "@/stores/workflowConnectionStore";
import { useWorkflowStateStore } from "@/stores/workflowEditorStateStore";
import { type Step, useWorkflowStepStore, type WorkflowStepStore } from "@/stores/workflowStepStore";

import { useStepActions } from "../Actions/stepActions";

import FormLoop from "./FormLoop.vue";
import GButton from "@/components/BaseComponents/GButton.vue";
import FormError from "@/components/Form/Elements/FormError.vue";
import FormElement from "@/components/Form/FormElement.vue";

const localVue = getLocalVue();

const LOOP = { inputs: { i1: { output_source: "o1" } }, output_method: "last_iteration" };

function makeStep(overrides: Partial<Step> = {}): Step {
    return {
        id: 3,
        name: "Body",
        type: "subworkflow",
        inputs: [
            { name: "i1", label: "i1", input_type: "parameter", type: "integer", multiple: false, optional: false },
            { name: "reads", label: "reads", input_type: "dataset", multiple: false, optional: false },
        ],
        outputs: [
            { name: "o1", extensions: ["input"], optional: false },
            { name: "o2", extensions: ["input"], optional: false },
        ],
        input_connections: { i1: { id: 0, output_name: "output" } },
        position: { left: 0, top: 0 },
        tool_state: {},
        workflow_outputs: [],
        ...overrides,
    } as Step;
}

function mountLoop(step: Step): VueWrapper {
    return shallowMount(FormLoop as any, {
        props: { step },
        global: localVue,
        pinia: createTestingPinia({ createSpy: vi.fn }),
    });
}

function field(wrapper: VueWrapper, id: string) {
    return wrapper.findAllComponents(FormElement).find((element) => element.props("id") === id);
}

function setField(wrapper: VueWrapper, id: string, value: unknown) {
    const element = field(wrapper, id);
    expect(element, `field ${id}`).toBeDefined();
    element!.vm.$emit("update:modelValue", value);
}

function updates(wrapper: VueWrapper): Partial<Step>[] {
    return (wrapper.emitted("onUpdateStep") ?? []).map((args) => args[1] as Partial<Step>);
}

function lastUpdate(wrapper: VueWrapper): Partial<Step> {
    const all = updates(wrapper);
    expect(all.length).toBeGreaterThan(0);
    return all[all.length - 1]!;
}

/** Types into a text field and leaves it, which writes the text to the step. */
async function typeAndLeave(wrapper: VueWrapper, id: string, value: string) {
    setField(wrapper, id, value);
    await field(wrapper, id)!.element.parentElement!.dispatchEvent(new FocusEvent("focusout", { bubbles: true }));
}

function lastSetting(wrapper: VueWrapper): [string, unknown] {
    const all = wrapper.emitted("onSetLoopSetting") ?? [];
    expect(all.length).toBeGreaterThan(0);
    const args = all[all.length - 1]!;
    return [args[1] as string, args[2]];
}

function staleMessages(wrapper: VueWrapper): string[][] {
    return wrapper
        .findAll(".form-loop-stale")
        .map((stale) => stale.findComponent(FormError).props("alerts") as string[]);
}

const WHEN = "$(inputs.i1 < 10)";

describe("FormLoop", () => {
    it("shows only the switch when the step has no loop", () => {
        const wrapper = mountLoop(makeStep());
        expect(field(wrapper, "__loop")!.props("modelValue")).toBe(false);
        expect(field(wrapper, "__loop_when")).toBeUndefined();
        expect(field(wrapper, "__loop_source__0")).toBeUndefined();
    });

    it("switches a loop on, keeping an existing condition", () => {
        const wrapper = mountLoop(makeStep({ when: WHEN }));
        setField(wrapper, "__loop", true);
        expect(lastUpdate(wrapper)).toEqual({ loop: { inputs: {}, output_method: "last_iteration" } });
    });

    it("switches a loop on without a condition and asks for one, with no gate input", async () => {
        const step = makeStep();
        const wrapper = mountLoop(step);
        setField(wrapper, "__loop", true);
        const update = lastUpdate(wrapper);
        expect(update).toEqual({ loop: { inputs: {}, output_method: "last_iteration" } });
        await wrapper.setProps({ step: { ...step, ...update } });
        expect(field(wrapper, "__loop_when")!.props("modelValue")).toBe("");
        expect(field(wrapper, "__loop_when")!.props("error")).toBe("A loop needs a condition.");
        expect(field(wrapper, "__loop_when")!.props("help")).toContain(
            "connected inputs, for example $(inputs.i1 < 10).",
        );
    });

    it("switches a loop off and leaves the condition", () => {
        const wrapper = mountLoop(makeStep({ when: WHEN, loop: LOOP }));
        setField(wrapper, "__loop", false);
        expect(lastUpdate(wrapper)).toEqual({ loop: undefined });
    });

    it("edits the condition as free text", async () => {
        const wrapper = mountLoop(makeStep({ when: "$(inputs.i1 < 5)", loop: LOOP }));
        expect(field(wrapper, "__loop_when")!.props("modelValue")).toBe("$(inputs.i1 < 5)");
        await typeAndLeave(wrapper, "__loop_when", WHEN);
        expect(lastSetting(wrapper)).toEqual(["when", WHEN]);
    });

    it("emits nothing for an edit that changes nothing", async () => {
        const wrapper = mountLoop(makeStep({ when: WHEN, loop: LOOP }));
        await typeAndLeave(wrapper, "__loop_when", WHEN);
        setField(wrapper, "__loop_source__0", ["o1"]);
        setField(wrapper, "__loop_output_method", "last_iteration");
        await typeAndLeave(wrapper, "__loop_value_from__0", "");
        expect(wrapper.emitted("onUpdateStep")).toBeUndefined();
        expect(wrapper.emitted("onSetLoopSetting")).toBeUndefined();
    });

    it("emits nothing for an existing loop until something is edited", () => {
        const loop = {
            inputs: { i1: { output_source: ["o1", "o2"], pick_value: "the_only_non_null", default: 1 } },
            output_method: "all_iterations",
        };
        const wrapper = mountLoop(makeStep({ when: WHEN, loop }));
        expect(wrapper.emitted("onUpdateStep")).toBeUndefined();
        expect(field(wrapper, "__loop_source__0")!.props("modelValue")).toEqual(["o1", "o2"]);
        expect(field(wrapper, "__loop_pick_value__0")!.props("modelValue")).toBe("the_only_non_null");
        expect(field(wrapper, "__loop_default__0")!.props("modelValue")).toBe("1");
        expect(field(wrapper, "__loop_output_method")!.props("modelValue")).toBe("all_iterations");
    });

    it("keeps link_merge and fields it does not know through an edit", async () => {
        const loop = {
            inputs: { i1: { output_source: ["o1", "o2"], link_merge: "merge_nested", pick_value: "first_non_null" } },
            output_method: "last_iteration",
            future_loop_field: 1,
        };
        const wrapper = mountLoop(makeStep({ when: WHEN, loop }));
        await typeAndLeave(wrapper, "__loop_value_from__0", "$(self + 1)");
        expect(lastSetting(wrapper)).toEqual([
            "loop",
            {
                inputs: {
                    i1: {
                        output_source: ["o1", "o2"],
                        link_merge: "merge_nested",
                        pick_value: "first_non_null",
                        value_from: "$(self + 1)",
                    },
                },
                output_method: "last_iteration",
                future_loop_field: 1,
            },
        ]);
    });

    it("writes a rule from the fields of an input", async () => {
        const step = makeStep({ when: WHEN, loop: { inputs: {}, output_method: "last_iteration" } });
        const wrapper = mountLoop(step);
        wrapper.find(".form-loop-input-closed").findComponent(GButton).vm.$emit("click");
        await wrapper.vm.$nextTick();
        setField(wrapper, "__loop_source__0", ["o1"]);
        let loop = lastUpdate(wrapper).loop;
        expect(loop).toEqual({ inputs: { i1: { output_source: "o1" } }, output_method: "last_iteration" });

        await wrapper.setProps({ step: { ...step, loop } });
        setField(wrapper, "__loop_default__0", "5");
        loop = lastSetting(wrapper)[1] as Step["loop"];
        await wrapper.setProps({ step: { ...step, loop } });
        await typeAndLeave(wrapper, "__loop_value_from__0", "$(self + 1)");
        loop = lastSetting(wrapper)[1] as Step["loop"];
        expect(loop).toEqual({
            inputs: { i1: { output_source: "o1", default: 5, value_from: "$(self + 1)" } },
            output_method: "last_iteration",
        });

        await wrapper.setProps({ step: { ...step, loop } });
        setField(wrapper, "__loop_output_method", "all_iterations");
        expect(lastUpdate(wrapper).loop).toEqual({ ...loop, output_method: "all_iterations" });
    });

    it("removes a rule whose fields are all cleared", () => {
        const wrapper = mountLoop(makeStep({ when: WHEN, loop: LOOP }));
        setField(wrapper, "__loop_source__0", []);
        expect(lastUpdate(wrapper).loop).toEqual({ inputs: {}, output_method: "last_iteration" });
    });

    it("sets pick_value when a second output is chosen, and drops it for one", async () => {
        const step = makeStep({ when: WHEN, loop: LOOP });
        const wrapper = mountLoop(step);
        expect(field(wrapper, "__loop_pick_value__0")).toBeUndefined();

        setField(wrapper, "__loop_source__0", ["o1", "o2"]);
        const several = lastUpdate(wrapper).loop;
        expect(several).toEqual({
            inputs: { i1: { output_source: ["o1", "o2"], pick_value: "first_non_null" } },
            output_method: "last_iteration",
        });
        await wrapper.setProps({ step: { ...step, loop: several } });
        const pickValue = field(wrapper, "__loop_pick_value__0")!;
        expect(pickValue.props("error")).toBeUndefined();
        expect(pickValue.props("attributes")?.optional).toBe(false);

        setField(wrapper, "__loop_pick_value__0", "the_only_non_null");
        const picked = lastUpdate(wrapper).loop;
        expect(picked).toEqual({
            inputs: { i1: { output_source: ["o1", "o2"], pick_value: "the_only_non_null" } },
            output_method: "last_iteration",
        });
        await wrapper.setProps({ step: { ...step, loop: picked } });

        setField(wrapper, "__loop_source__0", ["o2"]);
        expect(lastUpdate(wrapper).loop).toEqual({
            inputs: { i1: { output_source: "o2" } },
            output_method: "last_iteration",
        });
    });

    it("asks for pick_value on a list of outputs without one", () => {
        const loop = { inputs: { i1: { output_source: ["o1", "o2"] } } };
        const wrapper = mountLoop(makeStep({ when: WHEN, loop }));
        expect(field(wrapper, "__loop_pick_value__0")!.props("error")).toBe(
            "Choose how one value is picked among the outputs.",
        );
    });

    it("keeps inputs without a rule on one line until feedback is added", async () => {
        const wrapper = mountLoop(makeStep({ when: WHEN, loop: LOOP }));
        expect(field(wrapper, "__loop_source__1")).toBeUndefined();
        const closed = wrapper.find(".form-loop-input-closed");
        expect(closed.text()).toContain("reads");
        closed.findComponent(GButton).vm.$emit("click");
        await wrapper.vm.$nextTick();
        expect(field(wrapper, "__loop_source__1")).toBeDefined();
        expect(field(wrapper, "__loop_value_from__1")).toBeDefined();
        expect(wrapper.emitted("onUpdateStep")).toBeUndefined();
    });

    it("offers a default for parameter inputs only, as yes/no for a boolean", () => {
        const step = makeStep({
            when: WHEN,
            loop: { inputs: { i1: { output_source: "o1" }, reads: { output_source: "o2" } } },
        });
        const wrapper = mountLoop(step);
        expect(field(wrapper, "__loop_default__0")!.props("type")).toBeUndefined();
        expect(field(wrapper, "__loop_default__1")).toBeUndefined();
        expect(field(wrapper, "__loop_value_from__1")).toBeDefined();

        const booleanStep = makeStep({
            when: WHEN,
            inputs: [
                {
                    name: "go",
                    label: "go",
                    input_type: "parameter",
                    type: "boolean",
                    multiple: false,
                    optional: false,
                    extensions: [],
                },
            ],
            loop: { inputs: { go: { output_source: "o1" } } },
        });
        const booleanWrapper = mountLoop(booleanStep);
        expect(field(booleanWrapper, "__loop_default__0")!.props("type")).toBe("select");
        setField(booleanWrapper, "__loop_default__0", "false");
        expect(lastUpdate(booleanWrapper).loop).toEqual({ inputs: { go: { output_source: "o1", default: false } } });
    });

    it("shows what the server would refuse", () => {
        const loop = {
            inputs: {
                i1: { output_source: "o9", default: "five", value_from: "$(inputs.missing)" },
                reads: { output_source: "o1", default: 1 },
            },
        };
        const wrapper = mountLoop(makeStep({ when: "$(inputs.unconnected)", loop }));
        expect(field(wrapper, "__loop_when")!.props("error")).toBe(
            "The condition uses input 'unconnected', which is not connected.",
        );
        const source = field(wrapper, "__loop_source__0")!;
        expect(source.props("warning")).toBe(
            "'o9' is not among the outputs listed for this subworkflow. If it is a workflow output on one of the subworkflow's input steps the server accepts it; otherwise remove it here, or saving fails.",
        );
        expect(source.props("attributes")?.options).toEqual([
            ["o1", "o1"],
            ["o2", "o2"],
            ["o9", "o9"],
        ]);
        expect(field(wrapper, "__loop_default__0")!.props("error")).toBe('"five" is not a valid integer value.');
        expect(field(wrapper, "__loop_value_from__0")!.props("error")).toBe(
            "The expression uses input 'missing', which is not connected.",
        );
        expect(field(wrapper, "__loop_default__1")!.props("error")).toBe(
            "A dataset or collection input cannot have a default; clear it.",
        );
    });

    it("asks for a condition and at least one rule", () => {
        const wrapper = mountLoop(
            makeStep({ when: undefined, input_connections: {}, loop: { inputs: {}, output_method: "last_iteration" } }),
        );
        expect(field(wrapper, "__loop_when")!.props("error")).toBe("A loop needs a condition.");
        expect(field(wrapper, "__loop_when")!.props("help")).toContain(
            "for example $(inputs.x < 10) where x is a connected parameter input.",
        );
        expect(field(wrapper, "__loop")!.props("error")).toBeUndefined();
        expect(wrapper.find(".form-loop-no-rule").findComponent(FormError).props("alerts")).toEqual([
            "Feed back at least one input from an output of the subworkflow.",
        ]);
    });

    it("refuses a list output_source without two outputs, pick_value on one output, and merge_flattened", () => {
        const loop = {
            inputs: {
                i1: { output_source: ["o1"], pick_value: "first_non_null" },
                reads: { output_source: ["o1", "o2"], pick_value: "first_non_null", link_merge: "merge_flattened" },
            },
        };
        const wrapper = mountLoop(makeStep({ when: WHEN, loop }));
        expect(field(wrapper, "__loop_source__0")!.props("error")).toBe("A list of outputs needs two or more outputs.");
        expect(field(wrapper, "__loop_source__1")!.props("error")).toBe(
            "link_merge 'merge_flattened' is not supported yet; remove link_merge from this input's rule in the workflow file.",
        );
        const single = mountLoop(
            makeStep({ when: WHEN, loop: { inputs: { i1: { output_source: "o2", pick_value: "first_non_null" } } } }),
        );
        expect(field(single, "__loop_source__0")!.props("error")).toBe(
            "pick_value and link_merge need two or more outputs; changing the outputs here removes them.",
        );
    });

    it("refuses an empty rule", () => {
        const wrapper = mountLoop(makeStep({ when: WHEN, loop: { inputs: { i1: {} } } }));
        expect(field(wrapper, "__loop_source__0")!.props("error")).toBe(
            "Feed this input back from an output, or give it a default or a value from.",
        );
    });

    it("keeps an input open when its last field is cleared", async () => {
        const step = makeStep({ when: WHEN, loop: LOOP });
        const wrapper = mountLoop(step);
        setField(wrapper, "__loop_source__0", []);
        const loop = lastUpdate(wrapper).loop;
        expect(loop).toEqual({ inputs: {}, output_method: "last_iteration" });
        await wrapper.setProps({ step: { ...step, loop } });
        expect(field(wrapper, "__loop_source__0")).toBeDefined();
    });

    it("offers no feedback for an unlabelled subworkflow input, and reports a rule on one", async () => {
        const unlabelled = {
            name: "2:Input dataset",
            label: "2:Input dataset",
            input_type: "dataset",
            input_subworkflow_step_id: 2,
            multiple: false,
            optional: false,
            extensions: ["data"],
        };
        const step = makeStep({ when: WHEN, loop: LOOP });
        const wrapper = mountLoop({ ...step, inputs: [...step.inputs, unlabelled] } as Step);
        const closed = wrapper
            .findAll(".form-loop-input-closed")
            .find((line) => line.text().includes("2:Input dataset"))!;
        expect(closed.find(".form-loop-unlabelled").text()).toBe("Label this input in the subworkflow to feed it back");
        expect(closed.findComponent(GButton).exists()).toBe(false);

        const withRule = mountLoop({
            ...step,
            inputs: [...step.inputs, unlabelled],
            loop: { inputs: { i1: { output_source: "o1" }, "2:Input dataset": { output_source: "o2" } } },
        } as Step);
        expect(field(withRule, "__loop_source__2")).toBeUndefined();
        expect(staleMessages(withRule)).toEqual([
            ["Input '2:Input dataset' has no label in the subworkflow, and only labelled inputs can be fed back."],
        ]);
        withRule.find(".form-loop-stale").findComponent(GButton).vm.$emit("click");
        expect(lastUpdate(withRule).loop).toEqual({ inputs: { i1: { output_source: "o1" } } });
    });

    it("removes a rule for an input the step no longer has", () => {
        const loop = { inputs: { i1: { output_source: "o1" }, gone: { output_source: "o2" } } };
        const wrapper = mountLoop(makeStep({ when: WHEN, loop }));
        expect(staleMessages(wrapper)).toEqual([["Loop input 'gone' is not an input of the subworkflow."]]);
        wrapper.find(".form-loop-stale").findComponent(GButton).vm.$emit("click");
        expect(lastUpdate(wrapper).loop).toEqual({ inputs: { i1: { output_source: "o1" } } });
    });
});

describe("FormLoop with its fields mounted", () => {
    it("shows a change of the step in a focused field, as after an undo from the keyboard", async () => {
        const step = makeStep({ when: WHEN, loop: LOOP });
        const wrapper = mount(FormLoop as any, {
            props: { step },
            global: localVue,
            pinia: createTestingPinia({ createSpy: vi.fn }),
            attachTo: document.body,
        });
        const input = wrapper.find("input#__loop_when");
        (input.element as HTMLInputElement).focus();
        await input.setValue("$(inputs.i1 < 11)");
        await input.trigger("keydown", { key: "z", ctrlKey: true });
        expect(wrapper.emitted("onSetLoopSetting")).toEqual([[3, "when", "$(inputs.i1 < 11)"]]);
        await wrapper.setProps({ step: { ...step, when: "$(inputs.i1 < 11)" } });
        await wrapper.setProps({ step: { ...step, when: WHEN } });
        expect(document.activeElement).toBe(input.element);
        expect((input.element as HTMLInputElement).value).toBe(WHEN);
        wrapper.unmount();
    });

    it("emits nothing on open, with the select fields filling in their values", async () => {
        const loop = {
            inputs: {
                i1: { output_source: ["o1", "o2"], pick_value: "the_only_non_null", default: 1 },
                reads: { output_source: ["o1", "o9"], link_merge: "merge_nested" },
            },
            output_method: "all_iterations",
        };
        const wrapper = mount(FormLoop as any, {
            props: { step: makeStep({ when: WHEN, loop }) },
            global: localVue,
            pinia: createTestingPinia({ createSpy: vi.fn }),
        });
        await flushPromises();
        expect(wrapper.find("#__loop_when").exists()).toBe(true);
        // Loop outputs, then feed back from and pick value of each input; reads has no pick_value yet.
        expect(wrapper.findAll(".multiselect")).toHaveLength(5);
        expect(wrapper.emitted("onUpdateStep")).toBeUndefined();
        expect(wrapper.emitted("onSetLoopSetting")).toBeUndefined();
    });
});

describe("FormLoop undo", () => {
    function setup() {
        setActivePinia(createPinia());
        const workflowId = "loop-undo";
        const stepStore = useWorkflowStepStore(workflowId);
        const undoRedoStore = useUndoRedoStore(workflowId);
        const stepActions = useStepActions(
            stepStore,
            undoRedoStore,
            useWorkflowStateStore(workflowId),
            useConnectionStore(workflowId),
        );
        const step = stepStore.addStep(makeStep({ when: WHEN, loop: LOOP }), false, false);
        return { stepStore, undoRedoStore, stepActions, step };
    }

    it("restores the previous loop and condition", () => {
        const { stepStore, undoRedoStore, stepActions, step } = setup();
        const wrapper = mountLoop(step);
        setField(wrapper, "__loop_source__0", ["o1", "o2"]);
        stepActions.updateStep(step.id, lastUpdate(wrapper));
        expect(stepStore.getStep(step.id)!.loop).toEqual({
            inputs: { i1: { output_source: ["o1", "o2"], pick_value: "first_non_null" } },
            output_method: "last_iteration",
        });
        undoRedoStore.undo();
        expect(stepStore.getStep(step.id)!.loop).toEqual(LOOP);

        setField(wrapper, "__loop", false);
        stepActions.updateStep(step.id, lastUpdate(wrapper));
        expect(stepStore.getStep(step.id)!.loop).toBeUndefined();
        expect(stepStore.getStep(step.id)!.when).toBe(WHEN);
        undoRedoStore.undo();
        expect(stepStore.getStep(step.id)!.loop).toEqual(LOOP);
    });

    /** Mounts the form on the store's step and applies what it emits, as the editor does. */
    function connect(
        wrapper: VueWrapper,
        stepActions: ReturnType<typeof useStepActions>,
        stepStore: WorkflowStepStore,
        stepId: number,
    ) {
        // The emitted list is not kept across unmount, so remember the emissions already applied.
        const applied = new Set<unknown[]>();
        return async () => {
            for (const args of wrapper.emitted("onSetLoopSetting") ?? []) {
                if (!applied.has(args)) {
                    applied.add(args);
                    const [, key, value] = args;
                    stepActions.setLoopSetting(stepStore.getStep(stepId)!, key as "when", value as string);
                }
            }
            await wrapper.setProps({ step: stepStore.getStep(stepId)! });
        };
    }

    it("writes typed text when the field is left, as one named undo step, and no port for partial names", async () => {
        const { stepStore, undoRedoStore, stepActions, step } = setup();
        const wrapper = mountLoop(step);
        const apply = connect(wrapper, stepActions, stepStore, step.id);
        const typed = "$(inputs.limit < 20)";
        for (let end = 1; end <= typed.length; end++) {
            setField(wrapper, "__loop_when", typed.slice(0, end));
            await apply();
            // Nothing reaches the step while typing: no port for "l", "li", ...
            expect(stepStore.getStep(step.id)!.when).toBe(WHEN);
            expect(stepStore.getStepExtraInputs(step.id)).toEqual([]);
        }
        expect(field(wrapper, "__loop_when")!.props("modelValue")).toBe(typed);
        expect(field(wrapper, "__loop_when")!.props("error")).toBe(
            "The condition uses input 'limit', which is not connected.",
        );
        wrapper.find(".form-loop-when").element.dispatchEvent(new FocusEvent("focusout", { bubbles: true }));
        await apply();
        undoRedoStore.flushLazyAction();
        expect(stepStore.getStep(step.id)!.when).toBe(typed);
        expect(stepStore.getStepExtraInputs(step.id).map((input) => input.name)).toEqual(["limit"]);
        expect(undoRedoStore.undoActionStack).toHaveLength(1);
        expect(undoRedoStore.undoActionStack[0]!.name).toBe('edit loop condition of step "4: Body"');
        undoRedoStore.undo();
        await apply();
        expect(stepStore.getStep(step.id)!.when).toBe(WHEN);
        expect(stepStore.getStepExtraInputs(step.id)).toEqual([]);
    });

    it("writes typed text before undo and redo, so the shortcut reverts the typing", async () => {
        const { stepStore, undoRedoStore, stepActions, step } = setup();
        const wrapper = mountLoop(step);
        const apply = connect(wrapper, stepActions, stepStore, step.id);
        setField(wrapper, "__loop_when", "$(inputs.i1 < 30)");
        const undoKey = new KeyboardEvent("keydown", { key: "z", ctrlKey: true, bubbles: true, cancelable: true });
        wrapper.find(".form-loop-when").element.dispatchEvent(undoKey);
        // The input's own undo would put the typed text back after the editor's undo.
        expect(undoKey.defaultPrevented).toBe(true);
        await apply();
        expect(stepStore.getStep(step.id)!.when).toBe("$(inputs.i1 < 30)");
        undoRedoStore.undo();
        await apply();
        expect(stepStore.getStep(step.id)!.when).toBe(WHEN);
        expect(field(wrapper, "__loop_when")!.props("modelValue")).toBe(WHEN);

        setField(wrapper, "__loop_value_from__0", "$(self + 3)");
        await wrapper.find(".form-loop-value-from").trigger("keydown", { key: "Z", metaKey: true, shiftKey: true });
        await apply();
        expect((stepStore.getStep(step.id)!.loop as any).inputs.i1.value_from).toBe("$(self + 3)");
    });

    it("lets the port of a name in a loop condition take any parameter, unlike a conditional step's", () => {
        const { stepStore, step } = setup();
        stepStore.updateStep({ ...step, when: "$(inputs.i1 < inputs.limit)" });
        expect(stepStore.getStepExtraInputs(step.id)).toEqual([
            expect.objectContaining({ name: "limit", acceptedTypes: ["boolean", "integer", "float", "text"] }),
        ]);
        stepStore.updateStep({ ...stepStore.getStep(step.id)!, loop: undefined });
        expect(stepStore.getStepExtraInputs(step.id)).toEqual([
            expect.not.objectContaining({ acceptedTypes: expect.anything() }),
        ]);
    });

    it("writes typed text on Enter, and when the form goes away", async () => {
        const { stepStore, stepActions, step } = setup();
        const wrapper = mountLoop(step);
        const apply = connect(wrapper, stepActions, stepStore, step.id);
        setField(wrapper, "__loop_value_from__0", "$(self + 1)");
        await wrapper.find(".form-loop-value-from").trigger("keydown", { key: "Enter" });
        await apply();
        expect(stepStore.getStep(step.id)!.loop).toEqual({
            inputs: { i1: { output_source: "o1", value_from: "$(self + 1)" } },
            output_method: "last_iteration",
        });

        setField(wrapper, "__loop_when", "$(inputs.i1 < 3)");
        setField(wrapper, "__loop_value_from__0", "$(self + 2)");
        wrapper.unmount();
        await apply();
        expect(stepStore.getStep(step.id)!.when).toBe("$(inputs.i1 < 3)");
        expect(stepStore.getStep(step.id)!.loop).toEqual({
            inputs: { i1: { output_source: "o1", value_from: "$(self + 2)" } },
            output_method: "last_iteration",
        });
    });

    it("drops typed text when the step changes underneath, e.g. by undo", async () => {
        const { stepStore, step } = setup();
        const wrapper = mountLoop(step);
        setField(wrapper, "__loop_when", "$(inputs.i1 <");
        stepStore.updateStep({ ...stepStore.getStep(step.id)!, when: "$(inputs.i1 < 4)" });
        await wrapper.setProps({ step: stepStore.getStep(step.id)! });
        expect(field(wrapper, "__loop_when")!.props("modelValue")).toBe("$(inputs.i1 < 4)");
        wrapper.unmount();
        expect(wrapper.emitted("onSetLoopSetting")).toBeUndefined();
    });

    it("keeps the port and connection of a name the condition no longer reads, with a warning", async () => {
        const { stepStore, stepActions, step } = setup();
        stepStore.updateStep({
            ...step,
            when: "$(inputs.i1 < inputs.limit)",
            input_connections: { ...step.input_connections, limit: { id: 1, output_name: "output" } },
        });
        expect(stepStore.getStepExtraInputs(step.id).map((input) => input.name)).toEqual(["limit"]);
        const wrapper = mountLoop(stepStore.getStep(step.id)!);
        const apply = connect(wrapper, stepActions, stepStore, step.id);
        await typeAndLeave(wrapper, "__loop_when", WHEN);
        await apply();
        expect(stepStore.getStep(step.id)!.input_connections.limit).toEqual({ id: 1, output_name: "output" });
        expect(stepStore.getStepExtraInputs(step.id).map((input) => input.name)).toEqual(["limit"]);
        expect(field(wrapper, "__loop_when")!.props("warning")).toBe(
            "Input 'limit' is connected, but neither the condition nor a value from uses it. Its port stays on the step until you remove the connection.",
        );

        // A step that is only conditional loses the port as before; the loop changes nothing there.
        stepStore.updateStep({ ...stepStore.getStep(step.id)!, loop: undefined });
        expect(stepStore.getStepExtraInputs(step.id)).toEqual([]);
    });
});
