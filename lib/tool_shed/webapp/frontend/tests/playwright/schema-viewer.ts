import { createApp, defineComponent, h, reactive, ref, computed, watch, type PropType } from "vue"
import { JsonForms } from "@jsonforms/vue"
import { vanillaRenderers } from "@jsonforms/vue-vanilla"
import type { JsonFormsChangeEvent, JsonFormsRendererRegistryEntry } from "@jsonforms/core"
import builtinSchemas from "./test_tool_schemas.json"

const renderers: JsonFormsRendererRegistryEntry[] = [...vanillaRenderers]

interface ToolSchema {
    [key: string]: unknown
}

function stripSchemaDialect(schema: ToolSchema): ToolSchema {
    const { $schema, ...rest } = schema
    return rest
}

// --- Example schemas (built-in) ---
const BUILTIN_EXAMPLES: Record<string, ToolSchema> = Object.fromEntries(
    Object.entries(builtinSchemas as Record<string, ToolSchema>).map(([id, s]) => [id, stripSchemaDialect(s)])
)

// --- Form renderer component ---
const SchemaForm = defineComponent({
    name: "SchemaForm",
    props: {
        schema: { type: Object as PropType<ToolSchema>, required: true },
    },
    setup(props) {
        const data = reactive<Record<string, unknown>>({})
        const onChange = (event: JsonFormsChangeEvent) => {
            Object.keys(data).forEach((k) => delete data[k])
            Object.assign(data, event.data)
        }
        return () =>
            h(JsonForms, {
                data,
                schema: props.schema,
                renderers,
                onChange,
            })
    },
})

// --- JSON data viewer component ---
const JsonDataViewer = defineComponent({
    name: "JsonDataViewer",
    props: {
        schema: { type: Object as PropType<ToolSchema>, required: true },
    },
    setup(props) {
        const data = reactive<Record<string, unknown>>({})
        const formRef = ref<InstanceType<typeof JsonForms> | null>(null)

        const onChange = (event: JsonFormsChangeEvent) => {
            Object.keys(data).forEach((k) => delete data[k])
            Object.assign(data, event.data)
        }

        const jsonText = computed(() => JSON.stringify(data, null, 2))

        return () =>
            h("div", { class: "output-grid" }, [
                h("div", { class: "panel" }, [
                    h("div", { class: "panel-header" }, "Form"),
                    h("div", { class: "panel-body" }, [
                        h(JsonForms, {
                            ref: formRef,
                            data,
                            schema: props.schema,
                            renderers,
                            onChange,
                        }),
                    ]),
                ]),
                h("div", { class: "panel" }, [
                    h("div", { class: "panel-header" }, "Form Data (JSON)"),
                    h("div", { class: "panel-body" }, [h("pre", { class: "json-output" }, jsonText.value)]),
                ]),
            ])
    },
})

// --- Main App ---
const App = defineComponent({
    name: "App",
    setup() {
        type InputMode = "json" | "url"
        const mode = ref<InputMode>("json")
        const jsonInput = ref("")
        const urlInput = ref("")
        const errorMsg = ref("")
        const successMsg = ref("")
        const loading = ref(false)
        const activeSchema = ref<ToolSchema | null>(null)

        function tryParseAndRender() {
            errorMsg.value = ""
            successMsg.value = ""
            const text = jsonInput.value.trim()
            if (!text) {
                errorMsg.value = "Please paste a JSON schema"
                return
            }
            try {
                const parsed = JSON.parse(text) as ToolSchema
                activeSchema.value = stripSchemaDialect(parsed)
                successMsg.value = "Schema loaded"
            } catch (e) {
                errorMsg.value = `Invalid JSON: ${(e as Error).message}`
            }
        }

        async function fetchAndRender() {
            errorMsg.value = ""
            successMsg.value = ""
            const url = urlInput.value.trim()
            if (!url) {
                errorMsg.value = "Please enter a URL"
                return
            }
            loading.value = true
            try {
                const resp = await fetch(url)
                if (!resp.ok) throw new Error(`HTTP ${resp.status}: ${resp.statusText}`)
                const text = await resp.text()
                const parsed = JSON.parse(text) as ToolSchema
                activeSchema.value = stripSchemaDialect(parsed)
                jsonInput.value = JSON.stringify(parsed, null, 2)
                successMsg.value = "Schema fetched and loaded"
            } catch (e) {
                errorMsg.value = `Fetch failed: ${(e as Error).message}`
            } finally {
                loading.value = false
            }
        }

        function loadExample(id: string) {
            const schema = BUILTIN_EXAMPLES[id]
            if (schema) {
                activeSchema.value = schema
                jsonInput.value = JSON.stringify(schema, null, 2)
                errorMsg.value = ""
                successMsg.value = `Loaded example: ${id}`
                mode.value = "json"
            }
        }

        function clear() {
            activeSchema.value = null
            jsonInput.value = ""
            urlInput.value = ""
            errorMsg.value = ""
            successMsg.value = ""
        }

        // Check for ?url= or ?schema= query params on load
        const params = new URLSearchParams(window.location.search)
        const paramUrl = params.get("url")
        const paramSchema = params.get("schema")
        if (paramUrl) {
            urlInput.value = paramUrl
            mode.value = "url"
            // Auto-fetch on load
            setTimeout(() => fetchAndRender(), 100)
        } else if (paramSchema) {
            jsonInput.value = paramSchema
            mode.value = "json"
            setTimeout(() => tryParseAndRender(), 100)
        }

        return () =>
            h("div", [
                // Header
                h("div", { class: "header" }, [
                    h("h1", "Galaxy Tool Schema Viewer"),
                    h("p", "Paste a JSON Schema, provide a URL, or pick a built-in example to render the tool parameter form."),
                ]),

                // Input panel
                h("div", { class: "input-panel" }, [
                    // Tabs
                    h("div", { class: "tabs" }, [
                        h(
                            "button",
                            {
                                class: ["tab", mode.value === "json" ? "active" : ""],
                                onClick: () => (mode.value = "json"),
                            },
                            "Paste JSON"
                        ),
                        h(
                            "button",
                            {
                                class: ["tab", mode.value === "url" ? "active" : ""],
                                onClick: () => (mode.value = "url"),
                            },
                            "From URL"
                        ),
                    ]),

                    // JSON input
                    mode.value === "json"
                        ? h("textarea", {
                              value: jsonInput.value,
                              onInput: (e: Event) => (jsonInput.value = (e.target as HTMLTextAreaElement).value),
                              placeholder: '{\n  "type": "object",\n  "properties": {\n    "name": { "type": "string", "title": "Name" }\n  }\n}',
                          })
                        : h("div", { class: "url-row" }, [
                              h("input", {
                                  type: "text",
                                  value: urlInput.value,
                                  onInput: (e: Event) => (urlInput.value = (e.target as HTMLInputElement).value),
                                  onKeydown: (e: KeyboardEvent) => {
                                      if (e.key === "Enter") fetchAndRender()
                                  },
                                  placeholder: "https://example.com/tool-schema.json",
                              }),
                              h(
                                  "button",
                                  {
                                      class: "btn btn-primary",
                                      onClick: fetchAndRender,
                                      disabled: loading.value,
                                  },
                                  loading.value ? "Fetching..." : "Fetch"
                              ),
                          ]),

                    // Actions
                    h("div", { class: "actions" }, [
                        mode.value === "json"
                            ? h("button", { class: "btn btn-primary", onClick: tryParseAndRender }, "Render")
                            : null,
                        h("button", { class: "btn btn-secondary", onClick: clear }, "Clear"),
                        errorMsg.value ? h("span", { class: "error-msg" }, errorMsg.value) : null,
                        successMsg.value ? h("span", { class: "success-msg" }, successMsg.value) : null,
                    ]),

                    // Built-in examples
                    h("div", { class: "examples" }, [
                        h("span", { style: "font-size:0.8rem;color:#6c757d;margin-right:4px" }, "Examples:"),
                        ...Object.keys(BUILTIN_EXAMPLES).map((id) =>
                            h("button", { class: "chip", onClick: () => loadExample(id) }, id)
                        ),
                    ]),
                ]),

                // Output
                activeSchema.value
                    ? h(JsonDataViewer, { schema: activeSchema.value, key: JSON.stringify(activeSchema.value) })
                    : h("div", { class: "empty-state" }, [
                          h("div", { class: "icon" }, "\u{1F4CB}"),
                          h("p", "Paste a schema or pick an example to get started"),
                      ]),
            ])
    },
})

createApp(App).mount("#app")
