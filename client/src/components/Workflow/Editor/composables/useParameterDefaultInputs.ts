import { computed, type Ref } from "vue";

import type { FormInputNode } from "@/components/Form/composables/useFormState";
import { visitAllInputs, visitInputs } from "@/components/Form/utilities";
import type { WorkflowConnectionStore } from "@/stores/workflowConnectionStore";
import type { Step, WorkflowStepStore } from "@/stores/workflowStepStore";

type Option = [string, string, boolean];

/** Use the current connected tool forms to offer labels while storing option values. */
export function useParameterDefaultInputs(
    step: Ref<Step>,
    stepStore: WorkflowStepStore,
    connectionStore: WorkflowConnectionStore,
) {
    return computed<FormInputNode[]>(() => {
        const inputs: FormInputNode[] = step.value.config_form?.inputs ?? [];
        if (step.value.type !== "parameter_input") {
            return inputs;
        }

        const definition = inputs.find((input) => input.name === "parameter_definition");
        const textCase = definition?.cases?.find((item) => item.value === "text");
        if (definition?.test_param?.value !== "text" || !textCase) {
            return inputs;
        }
        const restrictions = textCase.inputs.find((input) => input.name === "restrictions");
        if (restrictions?.test_param?.value !== "onConnections") {
            return inputs;
        }
        // Multiple defaults use the existing text serialization, rather than an array of selections.
        if (textCase.inputs.find((input) => input.name === "multiple")?.value === true) {
            return inputs;
        }

        const optionLists: Option[][] = [];
        const connections = connectionStore.getConnectionsForStep(step.value.id);
        for (const connection of connections) {
            if (connection.output.stepId !== step.value.id || connection.output.name !== "output") {
                continue;
            }
            const connectedInputs = stepStore.getStep(connection.input.stepId)?.config_form?.inputs;
            if (!connectedInputs) {
                return inputs;
            }
            let options: Option[] | undefined;
            let isSelect = false;
            visitInputs(connectedInputs, (input: FormInputNode, name: string) => {
                if (name === connection.input.name && input.type === "select") {
                    isSelect = true;
                    if (Array.isArray(input.options)) {
                        options = input.options as Option[];
                    }
                }
            });
            if (isSelect && !options) {
                return inputs;
            }
            if (options) {
                optionLists.push(options);
            }
        }
        const firstOptions = optionLists[0];
        if (!firstOptions) {
            return inputs;
        }

        let options = firstOptions;
        if (optionLists.length > 1) {
            const allowedValues = optionLists.map((list) => new Set(list.map((option) => option[1])));
            const labels = new Map<string, Set<string>>();
            for (const list of optionLists) {
                for (const [label, value] of list) {
                    if (allowedValues.every((values) => values.has(value))) {
                        if (!labels.has(value)) {
                            labels.set(value, new Set());
                        }
                        labels.get(value)!.add(label);
                    }
                }
            }
            options = Array.from(labels, ([value, labels]): Option => [Array.from(labels).join(", "), value, false]);
            options.sort((a, b) => a[0].localeCompare(b[0]));
        }

        // Config forms belong to the step store; decorate a copy for this editor only.
        const result: FormInputNode[] = JSON.parse(JSON.stringify(inputs));
        const resultTextCase = result
            .find((input) => input.name === "parameter_definition")!
            .cases!.find((item) => item.value === "text")!;
        visitAllInputs(resultTextCase.inputs, (input: FormInputNode, name: string) => {
            if (name === "optional|specify_default|default") {
                input.type = "select";
                input.options = options;
            }
        });
        return result;
    });
}
