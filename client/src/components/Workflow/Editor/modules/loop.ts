/**
 * Workflow loops on subworkflow steps, as saved in `step.loop`.
 *
 * The server validates loops at save (`lib/galaxy/workflow/loop.py`) and stays the authority;
 * `loopErrors` repeats the checks the editor can make without the subworkflow, so the step
 * form can show them before a save is refused.
 */

import type { InputTerminalSource, Step } from "@/stores/workflowStepStore";
import localize from "@/utils/localization";

export type LoopPickValue = "first_non_null" | "the_only_non_null" | "all_non_null";
export type LoopOutputMethod = "last_iteration" | "all_iterations";

export interface LoopInputRule {
    output_source?: string | string[];
    link_merge?: string;
    pick_value?: LoopPickValue;
    default?: unknown;
    value_from?: string;
}

export interface WorkflowLoop {
    inputs: Record<string, LoopInputRule>;
    output_method?: LoopOutputMethod;
}

export interface LoopInputErrors {
    outputSource?: string;
    /** An output the editor does not list; the server may still know it, so this is a warning. */
    unknownOutput?: string;
    pickValue?: string;
    default?: string;
    valueFrom?: string;
}

export interface LoopErrors {
    when?: string;
    /** A connection to a name that is no input of the subworkflow and that no expression reads. */
    whenWarning?: string;
    /** A loop without any rule. */
    loop?: string;
    /** Rules for names that are not inputs of the step, e.g. after the subworkflow was upgraded. */
    staleInputs: { name: string; message: string }[];
    inputs: Record<string, LoopInputErrors>;
}

/** `inputs.name` or `inputs["name"]` in an expression, as `INPUT_REFERENCE` in loop.py. */
const INPUT_REFERENCE = /inputs(?:\.([A-Za-z_]\w*)|\[\s*["']([^"']+)["']\s*\])/g;

/**
 * Whether a subworkflow input has no label: the step then names it "N:name" (modules.py), and loops
 * address inputs by label only, so the server refuses a rule for it.
 */
export function isUnlabelledInput(input: InputTerminalSource): boolean {
    return (
        input.input_subworkflow_step_id !== undefined && input.name.startsWith(`${input.input_subworkflow_step_id}:`)
    );
}

export function getLoop(step: Step): WorkflowLoop | null {
    const loop = step.loop as WorkflowLoop | null | undefined;
    return loop ? { ...loop, inputs: loop.inputs ?? {} } : null;
}

export function ruleSources(rule: LoopInputRule | undefined): string[] {
    const source = rule?.output_source;
    if (source === undefined || source === null) {
        return [];
    }
    return Array.isArray(source) ? source : [source];
}

/** Returns `loop` with the rule of `inputName` changed; unset fields are dropped, and an empty rule is removed. */
export function withRule(loop: WorkflowLoop, inputName: string, changes: Partial<LoopInputRule>): WorkflowLoop {
    const rule: LoopInputRule = { ...loop.inputs[inputName], ...changes };
    if (ruleSources(rule).length < 2) {
        // pick_value and link_merge only apply to several outputs.
        delete rule.pick_value;
        delete rule.link_merge;
    }
    const cleaned = Object.fromEntries(
        Object.entries(rule).filter(([, value]) => value !== undefined && value !== null && value !== ""),
    ) as LoopInputRule;
    const inputs = { ...loop.inputs };
    if (Object.keys(cleaned).length) {
        inputs[inputName] = cleaned;
    } else {
        delete inputs[inputName];
    }
    return { ...loop, inputs };
}

/** The `output_source` for a selection of outputs: one label, a list of two or more, or none. */
export function sourcesToOutputSource(sources: string[]): string | string[] | undefined {
    if (sources.length === 0) {
        return undefined;
    }
    return sources.length === 1 ? sources[0] : sources;
}

/** Converts the text of a default to the type of the parameter it feeds; text that does not convert is kept. */
export function parseDefault(text: string, parameterType: string | undefined): unknown {
    const trimmed = text.trim();
    if (parameterType === "integer" && /^-?\d+$/.test(trimmed)) {
        return Number(trimmed);
    }
    if (parameterType === "float" && trimmed !== "" && Number.isFinite(Number(trimmed))) {
        return Number(trimmed);
    }
    if (parameterType === "boolean" && (trimmed === "true" || trimmed === "false")) {
        return trimmed === "true";
    }
    return text;
}

function defaultMatchesType(value: unknown, parameterType: string | undefined): boolean {
    switch (parameterType) {
        case "integer":
            return typeof value === "number" && Number.isInteger(value);
        case "float":
            return typeof value === "number";
        case "boolean":
            return typeof value === "boolean";
        case "text":
            return typeof value === "string";
        default:
            return true;
    }
}

/** Localizes `text`, then puts `values` in place of `{0}`, `{1}`, ... */
function message(text: string, ...values: string[]): string {
    return values.reduce((result, value, index) => result.replace(`{${index}}`, value), localize(text));
}

/** The help of the condition field, with an example on a connected parameter input of `step`. */
export function whenHelp(step: Step): string {
    const connected = connectedInputs(step);
    const input = step.inputs.find(
        (input) => input.input_type === "parameter" && connected.has(input.name) && /^[A-Za-z_]\w*$/.test(input.name),
    );
    const help = localize(
        "Expression evaluated before every iteration, including the first, on the inputs of the iteration about to run. The loop stops when it is false; if it is false before the first iteration, the step is skipped. It may only use connected inputs",
    );
    return input
        ? message("{0}, for example $(inputs.{1} < 10).", help, input.name)
        : message("{0}, for example $(inputs.x < 10) where x is a connected parameter input.", help);
}

function unconnectedReference(expression: string, connected: Set<string>): string | null {
    for (const match of expression.matchAll(INPUT_REFERENCE)) {
        const name = match[1] ?? match[2];
        if (name && !connected.has(name)) {
            return name;
        }
    }
    return null;
}

function connectedInputs(step: Step): Set<string> {
    return new Set(
        Object.entries(step.input_connections ?? {})
            .filter(([, links]) => (Array.isArray(links) ? links.length > 0 : Boolean(links)))
            .map(([name]) => name),
    );
}

/** The problems the server would refuse at save in the loop of `step`, keyed by where the form shows them. */
export function loopErrors(step: Step): LoopErrors {
    const errors: LoopErrors = { staleInputs: [], inputs: {} };
    const loop = getLoop(step);
    if (!loop) {
        return errors;
    }
    const connected = connectedInputs(step);
    if (!step.when) {
        // The example is in the help: an error is shown as escaped text, so it keeps no "<".
        errors.when = localize("A loop needs a condition.");
    } else {
        const unconnected = unconnectedReference(step.when, connected);
        if (unconnected) {
            errors.when = message("The condition uses input '{0}', which is not connected.", unconnected);
        }
    }
    const read = new Set(
        [step.when, ...Object.values(loop.inputs).map((rule) => rule.value_from)].flatMap((expression) =>
            [...(expression ?? "").matchAll(INPUT_REFERENCE)].map((match) => match[1] ?? match[2]),
        ),
    );
    const unused = [...connected].find((name) => !read.has(name) && !step.inputs.some((input) => input.name === name));
    if (unused) {
        errors.whenWarning = message(
            "Input '{0}' is connected, but neither the condition nor a value from uses it. Its port stays on the step until you remove the connection.",
            unused,
        );
    }
    if (Object.keys(loop.inputs).length === 0) {
        errors.loop = localize("Feed back at least one input from an output of the subworkflow.");
    }
    const stepInputs = new Map(step.inputs.map((input) => [input.name, input]));
    const outputNames = new Set(step.outputs.map((output) => output.name));
    Object.entries(loop.inputs).forEach(([inputName, rule]) => {
        const stepInput = stepInputs.get(inputName);
        if (!stepInput) {
            errors.staleInputs.push({
                name: inputName,
                message: message("Loop input '{0}' is not an input of the subworkflow.", inputName),
            });
            return;
        }
        if (isUnlabelledInput(stepInput)) {
            errors.staleInputs.push({
                name: inputName,
                message: message(
                    "Input '{0}' has no label in the subworkflow, and only labelled inputs can be fed back.",
                    inputName,
                ),
            });
            return;
        }
        const inputErrors: LoopInputErrors = {};
        const sources = ruleSources(rule);
        // The editor does not list an output of the subworkflow that is one of its input steps.
        const unknown = sources.find((source) => !outputNames.has(source));
        if (unknown) {
            inputErrors.unknownOutput = message(
                "'{0}' is not among the outputs listed for this subworkflow. If it is a workflow output on one of the subworkflow's input steps the server accepts it; otherwise remove it here, or saving fails.",
                unknown,
            );
        }
        if (sources.length === 0 && (rule.default === undefined || rule.default === null) && !rule.value_from) {
            inputErrors.outputSource = localize(
                "Feed this input back from an output, or give it a default or a value from.",
            );
        } else if (Array.isArray(rule.output_source) && sources.length < 2) {
            inputErrors.outputSource = localize("A list of outputs needs two or more outputs.");
        } else if (!Array.isArray(rule.output_source) && (rule.pick_value || rule.link_merge)) {
            inputErrors.outputSource = localize(
                "pick_value and link_merge need two or more outputs; changing the outputs here removes them.",
            );
        } else if (rule.link_merge === "merge_flattened") {
            inputErrors.outputSource = localize(
                "link_merge 'merge_flattened' is not supported yet; remove link_merge from this input's rule in the workflow file.",
            );
        }
        if (sources.length >= 2 && rule.pick_value !== "first_non_null" && rule.pick_value !== "the_only_non_null") {
            inputErrors.pickValue = localize("Choose how one value is picked among the outputs.");
        }
        if (rule.default !== undefined && rule.default !== null) {
            if (stepInput.input_type !== "parameter") {
                inputErrors.default = localize("A dataset or collection input cannot have a default; clear it.");
            } else if (!defaultMatchesType(rule.default, stepInput.type)) {
                inputErrors.default = message(
                    "{0} is not a valid {1} value.",
                    JSON.stringify(rule.default),
                    stepInput.type,
                );
            }
        }
        if (rule.value_from) {
            const unconnected = unconnectedReference(rule.value_from, connected);
            if (unconnected) {
                inputErrors.valueFrom = message(
                    "The expression uses input '{0}', which is not connected.",
                    unconnected,
                );
            }
        }
        if (Object.keys(inputErrors).length) {
            errors.inputs[inputName] = inputErrors;
        }
    });
    return errors;
}
