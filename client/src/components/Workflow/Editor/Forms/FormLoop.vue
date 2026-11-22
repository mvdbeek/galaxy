<script setup lang="ts">
import isEqual from "lodash.isequal";
import { computed, onBeforeUnmount, ref, watch } from "vue";

import type { InputTerminalSource, Step } from "@/stores/workflowStepStore";
import localize from "@/utils/localization";

import {
    getLoop,
    isUnlabelledInput,
    loopErrors,
    type LoopInputRule,
    type LoopOutputMethod,
    type LoopPickValue,
    parseDefault,
    ruleSources,
    sourcesToOutputSource,
    whenHelp,
    withRule,
    type WorkflowLoop,
} from "../modules/loop";

import GButton from "@/components/BaseComponents/GButton.vue";
import Heading from "@/components/Common/Heading.vue";
import FormError from "@/components/Form/Elements/FormError.vue";
import FormElement from "@/components/Form/FormElement.vue";

const props = defineProps<{
    step: Step;
}>();

const emit = defineEmits<{
    /** A discrete edit: one undo entry each. */
    (e: "onUpdateStep", id: number, value: Partial<Step>): void;
    /** Typing in a text field: merged into one undo entry while the user types. */
    (e: "onSetLoopSetting", id: number, key: "when" | "loop", value: unknown): void;
}>();

const loop = computed(() => getLoop(props.step));
/**
 * Text typed in "Run while" and "Value from", written to the step when the user leaves the field or presses
 * Enter, so the step never holds a half-typed expression (each name in the condition draws a port).
 */
const whenDraft = ref<string | null>(null);
const valueFromDrafts = ref<Record<string, string>>({});
/** The step as the user sees it, with the text not written yet, so messages follow the typing. */
const shownStep = computed(() => {
    let shown = props.step;
    if (whenDraft.value !== null) {
        shown = { ...shown, when: whenDraft.value || undefined };
    }
    if (loop.value && Object.keys(valueFromDrafts.value).length) {
        shown = { ...shown, loop: withValueFromDrafts(loop.value) as unknown as Step["loop"] };
    }
    return shown;
});
const errors = computed(() => loopErrors(shownStep.value));
// A change from elsewhere, such as undo, replaces what was typed.
watch(
    () => props.step.when,
    () => (whenDraft.value = null),
);
watch(
    () => props.step.loop,
    () => (valueFromDrafts.value = {}),
);
onBeforeUnmount(commitDrafts);
/** Inputs without a rule whose fields the user opened with "Add feedback". */
const opened = ref<string[]>([]);

const outputMethodOptions = [
    [localize("Last iteration"), "last_iteration"],
    [localize("All iterations, as a list"), "all_iterations"],
];
const pickValueOptions = [
    [localize("First non-null"), "first_non_null"],
    [localize("The only non-null"), "the_only_non_null"],
];
const booleanOptions = [
    [localize("Yes"), "true"],
    [localize("No"), "false"],
];

const conditionHelp = computed(() => whenHelp(props.step));

/** The subworkflow's outputs, and any output a rule names that the editor does not list, so it can be deselected. */
function outputOptions(inputName: string) {
    const names = props.step.outputs.map((output) => output.name);
    const missing = ruleSources(rule(inputName)).filter((source) => !names.includes(source));
    return [...names, ...missing].map((name) => [name, name]);
}

function rule(inputName: string): LoopInputRule | undefined {
    return loop.value?.inputs[inputName];
}

function isOpen(input: InputTerminalSource): boolean {
    return !isUnlabelledInput(input) && (Boolean(rule(input.name)) || opened.value.includes(input.name));
}

/**
 * Before the editor's undo or redo, write what was typed, so the shortcut reverts the typing as in other
 * fields. The input's own undo is prevented: it would put the typed text back after the editor's undo.
 */
function onDraftKeydown(event: KeyboardEvent, commit: () => void) {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "z") {
        event.preventDefault();
        commit();
    } else if (event.key === "Enter") {
        commit();
    }
}

function parameterType(input: InputTerminalSource): string | undefined {
    return input.input_type === "parameter" ? input.type : undefined;
}

function hasDefault(inputName: string): boolean {
    const value = rule(inputName)?.default;
    return value !== undefined && value !== null;
}

function defaultText(inputName: string): string {
    return hasDefault(inputName) ? String(rule(inputName)?.default) : "";
}

function updateLoop(newLoop: WorkflowLoop, typing = false) {
    if (isEqual(newLoop, loop.value)) {
        return;
    }
    if (typing) {
        emit("onSetLoopSetting", props.step.id, "loop", newLoop);
    } else {
        emit("onUpdateStep", props.step.id, { loop: newLoop as unknown as Step["loop"] });
    }
}

function onLoopSwitch(value: boolean) {
    if (value && !loop.value) {
        // An existing `when` becomes the condition; without one the condition field asks for one.
        emit("onUpdateStep", props.step.id, { loop: { inputs: {}, output_method: "last_iteration" } });
    } else if (!value && loop.value) {
        // The condition stays: the step is then conditionally skipped, as the conditional switch shows.
        emit("onUpdateStep", props.step.id, { loop: undefined });
    }
}

function withValueFromDrafts(current: WorkflowLoop): WorkflowLoop {
    return Object.entries(valueFromDrafts.value).reduce(
        (result, [inputName, text]) => withRule(result, inputName, { value_from: text }),
        current,
    );
}

function commitWhen() {
    if (whenDraft.value !== null) {
        const when = whenDraft.value || undefined;
        whenDraft.value = null;
        if (when !== (props.step.when || undefined)) {
            emit("onSetLoopSetting", props.step.id, "when", when);
        }
    }
}

function commitValueFrom() {
    if (loop.value && Object.keys(valueFromDrafts.value).length) {
        const newLoop = withValueFromDrafts(loop.value);
        valueFromDrafts.value = {};
        updateLoop(newLoop, true);
    }
}

/** Writes all typed text, when the form goes away, e.g. on another step or leaving the editor. */
function commitDrafts() {
    commitWhen();
    commitValueFrom();
}

function valueFromText(inputName: string): string {
    return valueFromDrafts.value[inputName] ?? rule(inputName)?.value_from ?? "";
}

function onOutputMethod(value: LoopOutputMethod) {
    if (loop.value && value !== (loop.value.output_method ?? "last_iteration")) {
        updateLoop({ ...loop.value, output_method: value });
    }
}

function onRule(inputName: string, changes: Partial<LoopInputRule>, typing = false) {
    if (!opened.value.includes(inputName)) {
        // Keep the fields open when their last value is cleared while editing.
        opened.value.push(inputName);
    }
    if (loop.value) {
        updateLoop(withRule(loop.value, inputName, changes), typing);
    }
}

function onSources(inputName: string, value: string[] | string | null) {
    const sources = value === null ? [] : Array.isArray(value) ? value : [value];
    const changes: Partial<LoopInputRule> = { output_source: sourcesToOutputSource(sources) };
    if (sources.length > 1 && !rule(inputName)?.pick_value) {
        // Several outputs need a pick_value; start from the first one offered.
        changes.pick_value = "first_non_null";
    }
    onRule(inputName, changes);
}

function onDefault(input: InputTerminalSource, value: string | null, typing: boolean) {
    const text = value ?? "";
    onRule(input.name, { default: text === "" ? undefined : parseDefault(text, parameterType(input)) }, typing);
}

function onRemoveStale(inputName: string) {
    if (loop.value) {
        const inputs = { ...loop.value.inputs };
        delete inputs[inputName];
        updateLoop({ ...loop.value, inputs });
    }
}
</script>

<template>
    <div class="form-loop">
        <Heading h2 separator bold size="sm">{{ localize("Loop") }}</Heading>
        <FormElement
            id="__loop"
            :model-value="Boolean(loop)"
            :title="localize('Run this step in a loop')"
            :help="
                localize(
                    'Run the subworkflow again and again while the condition is true, feeding outputs of one iteration into inputs of the next; inputs without feedback keep their first value. Switching the loop off keeps the condition: the step is then skipped when it is false.',
                )
            "
            type="boolean"
            @update:model-value="onLoopSwitch" />
        <div v-if="loop">
            <!-- The text fields have no type, so FormElement gives the plain input the step label uses: FormText
                 would keep showing the typed text after an undo from the keyboard until the field is left. -->
            <div class="form-loop-when" @focusout="commitWhen" @keydown="onDraftKeydown($event, commitWhen)">
                <FormElement
                    id="__loop_when"
                    :model-value="whenDraft ?? step.when ?? ''"
                    :title="localize('Run while')"
                    :help="conditionHelp"
                    :error="errors.when"
                    :warning="errors.whenWarning"
                    @update:model-value="(value: unknown) => (whenDraft = String(value ?? ''))" />
            </div>
            <FormElement
                id="__loop_output_method"
                :model-value="loop.output_method ?? 'last_iteration'"
                :title="localize('Loop outputs')"
                :help="localize('Output the last iteration, or a list of the output of every iteration.')"
                type="select"
                :attributes="{ options: outputMethodOptions }"
                @update:model-value="onOutputMethod" />
            <div
                v-for="stale in errors.staleInputs"
                :key="stale.name"
                class="form-loop-stale ui-form-element section-row alert alert-info">
                <FormError :alerts="[stale.message]" />
                <GButton size="small" outline color="blue" class="mt-1" @click="onRemoveStale(stale.name)">
                    {{ localize("Remove") }}
                </GButton>
            </div>
            <div v-if="errors.loop" class="form-loop-no-rule ui-form-element section-row alert alert-info">
                <FormError :alerts="[errors.loop]" />
            </div>
            <div v-for="(input, index) in step.inputs" :key="input.name" class="form-loop-input">
                <div v-if="!isOpen(input)" class="form-loop-input-closed d-flex align-items-center mb-2">
                    <span class="flex-grow-1">{{ input.label || input.name }}</span>
                    <span v-if="isUnlabelledInput(input)" class="form-loop-unlabelled text-muted small text-right">
                        {{ localize("Label this input in the subworkflow to feed it back") }}
                    </span>
                    <GButton v-else size="small" outline color="blue" @click="opened.push(input.name)">
                        {{ localize("Add feedback") }}
                    </GButton>
                </div>
                <template v-else>
                    <Heading h3 size="sm">{{ input.label || input.name }}</Heading>
                    <FormElement
                        :id="`__loop_source__${index}`"
                        :model-value="ruleSources(rule(input.name))"
                        :title="localize('Feed back from')"
                        :help="localize('Subworkflow output that gives this input its value in the next iteration.')"
                        :error="errors.inputs[input.name]?.outputSource"
                        :warning="errors.inputs[input.name]?.unknownOutput"
                        type="select"
                        :attributes="{
                            options: outputOptions(input.name),
                            multiple: true,
                            optional: true,
                            display: 'simple',
                        }"
                        @update:model-value="
                            (value: unknown) => onSources(input.name, value as string[] | string | null)
                        " />
                    <FormElement
                        v-if="ruleSources(rule(input.name)).length > 1"
                        :id="`__loop_pick_value__${index}`"
                        :model-value="rule(input.name)?.pick_value ?? null"
                        :title="localize('Pick value')"
                        :help="localize('How one value is picked among the outputs.')"
                        :error="errors.inputs[input.name]?.pickValue"
                        type="select"
                        :attributes="{ options: pickValueOptions, optional: !rule(input.name)?.pick_value }"
                        @update:model-value="
                            (value: unknown) =>
                                onRule(input.name, { pick_value: (value as LoopPickValue | null) ?? undefined })
                        " />
                    <FormElement
                        v-if="parameterType(input) === 'boolean'"
                        :id="`__loop_default__${index}`"
                        :model-value="hasDefault(input.name) ? defaultText(input.name) : null"
                        :title="localize('Default')"
                        :help="localize('Value used when the fed-back value is null or skipped.')"
                        :error="errors.inputs[input.name]?.default"
                        type="select"
                        :attributes="{ options: booleanOptions, optional: true }"
                        @update:model-value="(value: unknown) => onDefault(input, value as string | null, false)" />
                    <FormElement
                        v-else-if="input.input_type === 'parameter' || hasDefault(input.name)"
                        :id="`__loop_default__${index}`"
                        :model-value="defaultText(input.name)"
                        :title="localize('Default')"
                        :help="localize('Value used when the fed-back value is null or skipped.')"
                        :error="errors.inputs[input.name]?.default"
                        @update:model-value="(value: unknown) => onDefault(input, String(value ?? ''), true)" />
                    <div
                        class="form-loop-value-from"
                        @focusout="commitValueFrom"
                        @keydown="onDraftKeydown($event, commitValueFrom)">
                        <FormElement
                            :id="`__loop_value_from__${index}`"
                            :model-value="valueFromText(input.name)"
                            :title="localize('Value from')"
                            :help="
                                localize(
                                    'Expression that computes the value for the next iteration: self is the fed-back value after the default, inputs the inputs of the iteration that just ran, for example $(self + 1).',
                                )
                            "
                            :error="errors.inputs[input.name]?.valueFrom"
                            @update:model-value="
                                (value: unknown) =>
                                    (valueFromDrafts = { ...valueFromDrafts, [input.name]: String(value ?? '') })
                            " />
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>
