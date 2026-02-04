<script setup lang="ts">
import { computed, ref, watch } from "vue";

import { GalaxyApi } from "@/api";
import type { WorkflowInvocation } from "@/api/invocations";
import { useHistoryStore } from "@/stores/historyStore";

interface InvocationOutputOption {
    label: string;
    src: string;
    id: string | null;
    available: boolean;
}

interface InvocationOutputSelection {
    src: "invocation_output" | "invocation_step_output";
    invocation_id: string;
    output_name?: string;
    step_id?: string;
}

const props = defineProps<{
    extensions?: string[];
}>();

const emit = defineEmits<{
    (e: "update:value", value: InvocationOutputSelection | null): void;
}>();

const historyStore = useHistoryStore();

const invocations = ref<WorkflowInvocation[]>([]);
const selectedInvocationId = ref<string | null>(null);
const selectedOutput = ref<InvocationOutputOption | null>(null);
const loading = ref(false);
const error = ref<string | null>(null);

const currentHistoryId = computed(() => historyStore.currentHistoryId);

const selectedInvocation = computed(() => {
    if (!selectedInvocationId.value) return null;
    return invocations.value.find((inv) => inv.id === selectedInvocationId.value) || null;
});

const isInvocationComplete = computed(() => {
    if (!selectedInvocation.value) return false;
    return selectedInvocation.value.state === "scheduled" || selectedInvocation.value.state === "completed";
});

const availableOutputs = computed<InvocationOutputOption[]>(() => {
    if (!selectedInvocation.value) return [];

    const outputs: InvocationOutputOption[] = [];

    // Add labeled workflow outputs
    if (selectedInvocation.value.outputs) {
        for (const [label, output] of Object.entries(selectedInvocation.value.outputs)) {
            outputs.push({
                label,
                src: "hda",
                id: output.id || null,
                available: output.id != null,
            });
        }
    }

    // Add output collections
    if (selectedInvocation.value.output_collections) {
        for (const [label, output] of Object.entries(selectedInvocation.value.output_collections)) {
            outputs.push({
                label,
                src: "hdca",
                id: output.id || null,
                available: output.id != null,
            });
        }
    }

    return outputs;
});

async function fetchInvocations() {
    if (!currentHistoryId.value) return;

    loading.value = true;
    error.value = null;

    try {
        const { data, error: apiError } = await GalaxyApi().GET("/api/invocations", {
            params: {
                query: {
                    history_id: currentHistoryId.value,
                    view: "element",
                    limit: 50,
                },
            },
        });

        if (apiError) {
            error.value = "Failed to load workflow invocations";
            return;
        }

        invocations.value = data as WorkflowInvocation[];
    } catch (e) {
        error.value = "Failed to load workflow invocations";
    } finally {
        loading.value = false;
    }
}

function formatDate(dateStr: string): string {
    return new Date(dateStr).toLocaleString();
}

function onInvocationChange() {
    selectedOutput.value = null;
    emitValue();
}

function onOutputChange() {
    emitValue();
}

function emitValue() {
    if (!selectedInvocationId.value || !selectedOutput.value) {
        emit("update:value", null);
        return;
    }

    emit("update:value", {
        src: "invocation_output",
        invocation_id: selectedInvocationId.value,
        output_name: selectedOutput.value.label,
    });
}

function getWorkflowName(invocation: WorkflowInvocation): string {
    // The invocation may have a workflow_id but not the full workflow info
    // Return a formatted string
    return `Workflow Invocation`;
}

function getStateClass(state: string): string {
    switch (state) {
        case "scheduled":
        case "completed":
            return "text-success";
        case "failed":
            return "text-danger";
        case "cancelled":
        case "cancelling":
            return "text-warning";
        default:
            return "text-info";
    }
}

// Watch for history changes
watch(
    currentHistoryId,
    () => {
        fetchInvocations();
    },
    { immediate: true }
);
</script>

<template>
    <div class="invocation-output-selector">
        <div v-if="loading" class="text-center p-3">
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
            Loading invocations...
        </div>

        <div v-else-if="error" class="alert alert-danger">
            {{ error }}
        </div>

        <div v-else-if="invocations.length === 0" class="alert alert-info">
            No workflow invocations found in current history. Run a workflow first to use its outputs as input.
        </div>

        <div v-else>
            <div class="mb-3">
                <label class="form-label fw-bold">Select Source Invocation</label>
                <select
                    v-model="selectedInvocationId"
                    class="form-select"
                    data-description="invocation selector"
                    @change="onInvocationChange">
                    <option :value="null">-- Select an invocation --</option>
                    <option v-for="inv in invocations" :key="inv.id" :value="inv.id">
                        {{ getWorkflowName(inv) }} ({{ formatDate(inv.create_time) }}) -
                        <span :class="getStateClass(inv.state)">{{ inv.state }}</span>
                    </option>
                </select>
            </div>

            <div v-if="selectedInvocation" class="mb-3">
                <div class="alert" :class="isInvocationComplete ? 'alert-success' : 'alert-warning'">
                    <div class="d-flex align-items-center">
                        <div>
                            <strong>{{ getWorkflowName(selectedInvocation) }}</strong>
                            <br />
                            <small class="text-muted">
                                Started: {{ formatDate(selectedInvocation.create_time) }}
                                <span v-if="!isInvocationComplete"> - Status: {{ selectedInvocation.state }} </span>
                            </small>
                        </div>
                    </div>

                    <div v-if="!isInvocationComplete" class="mt-2">
                        <i class="fa fa-clock"></i>
                        This invocation is still running. Your workflow will wait for it to complete.
                    </div>
                </div>
            </div>

            <div v-if="selectedInvocationId && availableOutputs.length > 0" class="mb-3">
                <label class="form-label fw-bold">Select Output</label>
                <select
                    v-model="selectedOutput"
                    class="form-select"
                    data-description="invocation output selector"
                    @change="onOutputChange">
                    <option :value="null">-- Select an output --</option>
                    <option v-for="output in availableOutputs" :key="output.label" :value="output">
                        {{ output.label }}
                        <span v-if="!output.available">(pending)</span>
                    </option>
                </select>
            </div>

            <div
                v-if="selectedInvocationId && availableOutputs.length === 0 && selectedInvocation"
                class="alert alert-info">
                This invocation has no labeled outputs yet. The workflow may still be running or has no workflow
                outputs defined.
            </div>

            <div v-if="selectedOutput" class="selected-output-info p-3 border rounded">
                <strong>Selected Output:</strong> {{ selectedOutput.label }}
                <br />
                <span class="text-muted">
                    Type: {{ selectedOutput.src === "hda" ? "Dataset" : "Collection" }}
                    <span v-if="selectedOutput.available" class="text-success"> (Available) </span>
                    <span v-else class="text-warning"> (Will be available when invocation completes) </span>
                </span>
            </div>
        </div>
    </div>
</template>

<style scoped>
.invocation-output-selector {
    min-height: 200px;
}
.selected-output-info {
    background-color: var(--bs-light);
}
</style>
