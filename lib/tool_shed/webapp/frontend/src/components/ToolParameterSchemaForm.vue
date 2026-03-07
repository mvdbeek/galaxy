<script setup lang="ts">
import { ref, watch } from "vue"
import { JsonForms } from "@jsonforms/vue"
import type { JsonFormsChangeEvent } from "@jsonforms/vue"
import type { JsonSchema } from "@jsonforms/core"

import { getToolParameterRequestSchema } from "@/api"
import { errorMessageAsString } from "@/util"
import { renderers } from "@/components/jsonforms/renderers"
import LoadingDiv from "@/components/LoadingDiv.vue"
import ErrorBanner from "@/components/ErrorBanner.vue"

interface Props {
    trsToolId: string
    version: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
    (e: "change", data: Record<string, unknown>): void
}>()

const schema = ref<JsonSchema | null>(null)
const formData = ref<Record<string, unknown>>({})
const loading = ref(true)
const errorMessage = ref<string | null>(null)

function onChange(event: JsonFormsChangeEvent) {
    formData.value = event.data as Record<string, unknown>
    emit("change", formData.value)
}

watch(
    () => [props.trsToolId, props.version],
    async () => {
        loading.value = true
        errorMessage.value = null
        schema.value = null
        formData.value = {}
        try {
            schema.value = (await getToolParameterRequestSchema(
                props.trsToolId,
                props.version
            )) as JsonSchema
        } catch (e) {
            errorMessage.value = errorMessageAsString(e)
        }
        loading.value = false
    },
    { immediate: true }
)
</script>

<template>
    <div class="tool-parameter-schema-form">
        <loading-div v-if="loading" message="Loading parameter schema..." />
        <error-banner v-else-if="errorMessage" :error="errorMessage" />
        <json-forms
            v-else-if="schema"
            :data="formData"
            :schema="schema"
            :renderers="renderers"
            :config="{ hideRequiredAsterisk: false }"
            @change="onChange"
        />
        <div v-if="schema && Object.keys(formData).length > 0" class="q-mt-md">
            <q-expansion-item label="Form Data (Debug)" dense>
                <pre class="q-pa-sm bg-grey-2" style="font-size: 0.85em; overflow: auto">{{
                    JSON.stringify(formData, null, 2)
                }}</pre>
            </q-expansion-item>
        </div>
    </div>
</template>
