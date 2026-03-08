import { createApp, defineComponent, h, reactive, ref, computed, type PropType, type VNode } from "vue"
import builtinSchemas from "./test_tool_schemas.json"

// ============================================================
// Types
// ============================================================

interface ToolSchema {
    [key: string]: unknown
}

interface GxOption {
    label: string
    value: string
    selected?: boolean
}

interface BranchInfo {
    schema: any
    discrimProp: string
    discrimValue: any
    label: string
    isAbsent: boolean
    fields: Array<{ name: string; schema: any }>
}

// ============================================================
// Schema utilities
// ============================================================

function stripSchemaDialect(schema: ToolSchema): ToolSchema {
    const { $schema, ...rest } = schema
    return rest
}

/** Recursively resolve all $ref references inline. Handles circular refs by
 *  replacing them with a simple object placeholder. */
function resolveRefs(schema: ToolSchema): ToolSchema {
    const defs = (schema.$defs || schema.definitions || {}) as Record<string, any>

    function resolve(node: any, visiting: Set<string>): any {
        if (node === null || node === undefined || typeof node !== "object") return node
        if (Array.isArray(node)) return node.map((item) => resolve(item, visiting))

        if (typeof node.$ref === "string") {
            const match = node.$ref.match(/^#\/\$defs\/(.+)$/) || node.$ref.match(/^#\/definitions\/(.+)$/)
            if (match) {
                const defName = match[1]
                if (visiting.has(defName)) {
                    // Circular reference — return a safe placeholder
                    const { $ref, ...siblings } = node
                    return { type: "object", title: `${defName} (circular ref)`, ...siblings }
                }
                const def = defs[defName]
                if (def) {
                    const next = new Set(visiting)
                    next.add(defName)
                    const { $ref, ...siblings } = node
                    const resolved = resolve(def, next)
                    return { ...resolved, ...siblings }
                }
            }
        }

        const out: any = {}
        for (const [k, v] of Object.entries(node)) {
            if (k === "$defs" || k === "definitions") continue
            out[k] = resolve(v, visiting)
        }
        return out
    }

    return resolve(schema, new Set())
}

function prepareSchema(schema: ToolSchema): ToolSchema {
    return resolveRefs(stripSchemaDialect(schema))
}

// ============================================================
// Built-in examples
// ============================================================

const BUILTIN_EXAMPLES: Record<string, ToolSchema> = Object.fromEntries(
    Object.entries(builtinSchemas as Record<string, ToolSchema>).map(([id, s]) => [id, s])
)

// ============================================================
// Schema inspection helpers
// ============================================================

function hasStringType(schema: any): boolean {
    if (schema.type === "string") return true
    if (schema.anyOf) return schema.anyOf.some((s: any) => s.type === "string")
    return false
}

function isConditional(schema: any): boolean {
    return schema?.gx_type === "gx_conditional" || (schema?.oneOf && !schema?.enum)
}

function isRepeat(schema: any): boolean {
    return schema?.gx_type === "gx_repeat" || (schema?.type === "array" && schema?.items)
}

/** Parse oneOf branches to extract discriminator info. */
function parseBranches(schema: any): BranchInfo[] {
    const oneOf = schema.oneOf as any[]
    if (!oneOf) return []

    return oneOf.map((branch) => {
        const props = branch.properties || {}
        let discrimProp = ""
        let discrimValue: any = undefined

        for (const [key, propSchema] of Object.entries(props) as [string, any][]) {
            if (propSchema.const !== undefined) {
                discrimProp = key
                discrimValue = propSchema.const
                break
            }
        }

        const isAbsent = !discrimProp
        const label = isAbsent ? "(default)" : String(discrimValue)
        const fields: BranchInfo["fields"] = []
        for (const [name, propSchema] of Object.entries(props) as [string, any][]) {
            if (name === discrimProp) continue
            fields.push({ name, schema: propSchema })
        }

        return { schema: branch, discrimProp, discrimValue, label, isAbsent, fields }
    })
}

function findDefaultBranchIndex(branches: BranchInfo[]): number {
    // Prefer first non-absent branch
    const idx = branches.findIndex((b) => !b.isAbsent)
    return idx >= 0 ? idx : 0
}

// ============================================================
// Field rendering
// ============================================================

function fieldTitle(name: string, schema: any): string {
    return schema.title || name
}

function renderTextField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    const title = fieldTitle(name, schema)
    if (schema.gx_area) {
        return h("div", { class: "control" }, [
            h("label", title),
            h("textarea", {
                value: value || "",
                rows: 3,
                onInput: (e: Event) => onChange((e.target as HTMLTextAreaElement).value),
            }),
        ])
    }
    return h("div", { class: "control" }, [
        h("label", title),
        h("input", {
            type: "text",
            value: value || "",
            onInput: (e: Event) => onChange((e.target as HTMLInputElement).value),
        }),
    ])
}

function renderIntegerField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    return h("div", { class: "control" }, [
        h("label", fieldTitle(name, schema)),
        h("input", {
            type: "number",
            step: "1",
            value: value ?? "",
            onInput: (e: Event) => {
                const v = (e.target as HTMLInputElement).value
                onChange(v === "" ? null : parseInt(v))
            },
        }),
    ])
}

function renderFloatField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    return h("div", { class: "control" }, [
        h("label", fieldTitle(name, schema)),
        h("input", {
            type: "number",
            step: "any",
            value: value ?? "",
            onInput: (e: Event) => {
                const v = (e.target as HTMLInputElement).value
                onChange(v === "" ? null : parseFloat(v))
            },
        }),
    ])
}

function renderBooleanField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    return h("div", { class: "control" }, [
        h("label", [
            h("input", {
                type: "checkbox",
                checked: !!value,
                onChange: (e: Event) => onChange((e.target as HTMLInputElement).checked),
            }),
            ` ${fieldTitle(name, schema)}`,
        ]),
    ])
}

function renderSelectField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    const options = (schema.gx_options || []) as GxOption[]
    const defaultVal = options.find((o) => o.selected)?.value || options[0]?.value || ""
    const currentVal = value ?? defaultVal

    // If no gx_options, try to extract from anyOf/const
    const effectiveOptions =
        options.length > 0
            ? options
            : extractConstOptions(schema)

    return h("div", { class: "control" }, [
        h("label", fieldTitle(name, schema)),
        h(
            "select",
            {
                value: currentVal,
                onChange: (e: Event) => onChange((e.target as HTMLSelectElement).value),
            },
            effectiveOptions.map((opt: GxOption) => h("option", { value: opt.value }, opt.label))
        ),
    ])
}

function extractConstOptions(schema: any): GxOption[] {
    const sources = schema.anyOf || schema.oneOf || []
    return sources
        .filter((s: any) => s.const !== undefined)
        .map((s: any) => ({
            label: String(s.const),
            value: String(s.const),
            selected: false,
        }))
}

function renderColorField(name: string, schema: any, value: any, onChange: (v: any) => void): VNode {
    return h("div", { class: "control" }, [
        h("label", fieldTitle(name, schema)),
        h("input", {
            type: "color",
            value: value || "#000000",
            onInput: (e: Event) => onChange((e.target as HTMLInputElement).value),
        }),
    ])
}

function renderDataPlaceholder(name: string, schema: any): VNode {
    const exts = (schema.gx_extensions || []).join(", ") || "any"
    const multiple = schema.gx_multiple ? " (multiple)" : ""
    const kind = schema.gx_type === "gx_data_collection" ? "Collection" : "Dataset"
    return h("div", { class: "control" }, [
        h("label", fieldTitle(name, schema)),
        h("div", { class: "data-placeholder" }, `${kind} selector: ${exts}${multiple}`),
    ])
}

// ============================================================
// GxField — dispatches to the right renderer
// ============================================================

const GxField = defineComponent({
    name: "GxField",
    props: {
        name: { type: String, required: true },
        schema: { type: Object, required: true },
        modelValue: { default: undefined },
    },
    emits: ["update:modelValue"],
    setup(props, { emit }) {
        function onChange(val: any) {
            emit("update:modelValue", val)
        }

        return () => {
            const schema = props.schema as any
            const gxType = schema.gx_type
            const value = props.modelValue

            // Conditional
            if (isConditional(schema)) {
                return h(GxConditional, {
                    name: props.name,
                    schema,
                    modelValue: value,
                    "onUpdate:modelValue": onChange,
                })
            }

            // Repeat
            if (isRepeat(schema)) {
                return h(GxRepeat, {
                    name: props.name,
                    schema,
                    modelValue: value,
                    "onUpdate:modelValue": onChange,
                })
            }

            // Select (gx_select or anyOf with const values but no oneOf)
            if (gxType === "gx_select") {
                return renderSelectField(props.name, schema, value, onChange)
            }

            // Data / collection
            if (gxType === "gx_data" || gxType === "gx_data_collection") {
                return renderDataPlaceholder(props.name, schema)
            }

            // Color
            if (gxType === "gx_color") {
                return renderColorField(props.name, schema, value, onChange)
            }

            // Boolean
            if (gxType === "gx_boolean" || schema.type === "boolean") {
                return renderBooleanField(props.name, schema, value, onChange)
            }

            // Integer
            if (gxType === "gx_integer" || schema.type === "integer") {
                return renderIntegerField(props.name, schema, value, onChange)
            }

            // Float
            if (gxType === "gx_float" || schema.type === "number") {
                return renderFloatField(props.name, schema, value, onChange)
            }

            // Text / string
            if (gxType === "gx_text" || schema.type === "string" || hasStringType(schema)) {
                return renderTextField(props.name, schema, value, onChange)
            }

            // Nested object
            if (schema.type === "object" && schema.properties) {
                return h(GxObjectFields, {
                    name: props.name,
                    schema,
                    modelValue: value || {},
                    "onUpdate:modelValue": onChange,
                })
            }

            // Fallback
            return h("div", { class: "control" }, [
                h("label", fieldTitle(props.name, schema)),
                h("div", { class: "data-placeholder" }, `[${gxType || schema.type || "complex"}]`),
            ])
        }
    },
})

// ============================================================
// GxObjectFields — renders all properties of an object schema
// ============================================================

const GxObjectFields = defineComponent({
    name: "GxObjectFields",
    props: {
        name: { type: String, default: "" },
        schema: { type: Object as PropType<any>, required: true },
        modelValue: { type: Object, default: () => ({}) },
        showBorder: { type: Boolean, default: false },
    },
    emits: ["update:modelValue"],
    setup(props, { emit }) {
        function updateField(fieldName: string, value: any) {
            const newData = { ...(props.modelValue as any), [fieldName]: value }
            emit("update:modelValue", newData)
        }

        return () => {
            const properties = (props.schema as any).properties || {}
            const data = (props.modelValue || {}) as any
            const entries = Object.entries(properties) as [string, any][]

            const children = entries.map(([name, propSchema]) =>
                h(GxField, {
                    key: name,
                    name,
                    schema: propSchema,
                    modelValue: data[name],
                    "onUpdate:modelValue": (v: any) => updateField(name, v),
                })
            )

            if (props.showBorder && props.name) {
                return h("fieldset", { class: "gx-section" }, [
                    h("legend", props.name),
                    ...children,
                ])
            }
            return h("div", { class: "gx-fields" }, children)
        }
    },
})

// ============================================================
// GxConditional — renders a conditional (oneOf with discriminator)
// ============================================================

const GxConditional = defineComponent({
    name: "GxConditional",
    props: {
        name: { type: String, required: true },
        schema: { type: Object as PropType<any>, required: true },
        modelValue: { default: undefined },
    },
    emits: ["update:modelValue"],
    setup(props, { emit }) {
        const branches = computed(() => parseBranches(props.schema))
        const selectedIdx = ref(findDefaultBranchIndex(branches.value))

        // Get discriminator prop name (same across all non-absent branches)
        const discrimProp = computed(() => {
            const nonAbsent = branches.value.filter((b) => !b.isAbsent)
            return nonAbsent[0]?.discrimProp || ""
        })

        // Selectable options (non-absent branches)
        const options = computed(() => branches.value.filter((b) => !b.isAbsent))

        // Is this a boolean conditional?
        const isBooleanDiscrim = computed(() => {
            return options.value.every(
                (b) => b.discrimValue === true || b.discrimValue === false
            )
        })

        function selectBranch(idx: number) {
            selectedIdx.value = idx
            const branch = branches.value[idx]
            const newData: any = {}
            if (branch.discrimProp) {
                newData[branch.discrimProp] = branch.discrimValue
            }
            emit("update:modelValue", newData)
        }

        function onFieldUpdate(fieldName: string, value: any) {
            const current = (props.modelValue as any) || {}
            emit("update:modelValue", { ...current, [fieldName]: value })
        }

        return () => {
            const branch = branches.value[selectedIdx.value]
            if (!branch) return h("div", "(no conditional branches)")

            const data = (props.modelValue as any) || {}

            // For boolean discriminators, render as checkbox
            if (isBooleanDiscrim.value && discrimProp.value) {
                const trueIdx = branches.value.findIndex((b) => b.discrimValue === true)
                const falseIdx = branches.value.findIndex((b) => b.discrimValue === false)
                const isTrue = selectedIdx.value === trueIdx

                return h("div", { class: "gx-conditional" }, [
                    h("div", { class: "control" }, [
                        h("label", [
                            h("input", {
                                type: "checkbox",
                                checked: isTrue,
                                onChange: () => selectBranch(isTrue ? falseIdx : trueIdx),
                            }),
                            ` ${fieldTitle(discrimProp.value, branch.schema?.properties?.[discrimProp.value] || {})}`,
                        ]),
                    ]),
                    ...branch.fields.map((f) =>
                        h(GxField, {
                            key: `${selectedIdx.value}-${f.name}`,
                            name: f.name,
                            schema: f.schema,
                            modelValue: data[f.name],
                            "onUpdate:modelValue": (v: any) => onFieldUpdate(f.name, v),
                        })
                    ),
                ])
            }

            // For string-based discriminators, render as select
            return h("div", { class: "gx-conditional" }, [
                options.value.length > 0
                    ? h("div", { class: "control" }, [
                          h("label", fieldTitle(discrimProp.value || props.name, {})),
                          h(
                              "select",
                              {
                                  value: selectedIdx.value,
                                  onChange: (e: Event) =>
                                      selectBranch(Number((e.target as HTMLSelectElement).value)),
                              },
                              options.value.map((b, i) => {
                                  const globalIdx = branches.value.indexOf(b)
                                  return h("option", { value: globalIdx }, b.label)
                              })
                          ),
                      ])
                    : null,
                ...branch.fields.map((f) =>
                    h(GxField, {
                        key: `${selectedIdx.value}-${f.name}`,
                        name: f.name,
                        schema: f.schema,
                        modelValue: data[f.name],
                        "onUpdate:modelValue": (v: any) => onFieldUpdate(f.name, v),
                    })
                ),
            ])
        }
    },
})

// ============================================================
// GxRepeat — renders a repeat section (array of objects)
// ============================================================

const GxRepeat = defineComponent({
    name: "GxRepeat",
    props: {
        name: { type: String, required: true },
        schema: { type: Object as PropType<any>, required: true },
        modelValue: { default: undefined },
    },
    emits: ["update:modelValue"],
    setup(props, { emit }) {
        function items(): any[] {
            return Array.isArray(props.modelValue) ? props.modelValue : []
        }

        function addItem() {
            emit("update:modelValue", [...items(), {}])
        }

        function removeItem(idx: number) {
            const arr = [...items()]
            arr.splice(idx, 1)
            emit("update:modelValue", arr)
        }

        function updateItem(idx: number, value: any) {
            const arr = [...items()]
            arr[idx] = value
            emit("update:modelValue", arr)
        }

        return () => {
            const itemSchema = (props.schema as any).items || {}
            const arr = items()
            const title = fieldTitle(props.name, props.schema)

            return h("fieldset", { class: "gx-repeat" }, [
                h("legend", [
                    title,
                    h(
                        "button",
                        {
                            class: "btn-add",
                            onClick: addItem,
                            title: "Add item",
                        },
                        "+"
                    ),
                ]),
                arr.length === 0
                    ? h("div", { class: "repeat-empty" }, "No items. Click + to add.")
                    : null,
                ...arr.map((item, idx) =>
                    h("div", { class: "repeat-item", key: idx }, [
                        h("div", { class: "repeat-item-header" }, [
                            h("span", `#${idx + 1}`),
                            h(
                                "button",
                                {
                                    class: "btn-remove",
                                    onClick: () => removeItem(idx),
                                    title: "Remove",
                                },
                                "\u00d7"
                            ),
                        ]),
                        h(GxObjectFields, {
                            schema: itemSchema,
                            modelValue: item || {},
                            "onUpdate:modelValue": (v: any) => updateItem(idx, v),
                        }),
                    ])
                ),
            ])
        }
    },
})

// ============================================================
// GxFormViewer — form + JSON data side by side
// ============================================================

const GxFormViewer = defineComponent({
    name: "GxFormViewer",
    props: {
        schema: { type: Object as PropType<ToolSchema>, required: true },
    },
    setup(props) {
        const prepared = computed(() => prepareSchema(props.schema))
        const formData = ref<Record<string, any>>({})

        const jsonText = computed(() => JSON.stringify(formData.value, null, 2))

        return () =>
            h("div", { class: "output-grid" }, [
                h("div", { class: "panel" }, [
                    h("div", { class: "panel-header" }, "Form"),
                    h("div", { class: "panel-body" }, [
                        h(GxObjectFields, {
                            schema: prepared.value,
                            modelValue: formData.value,
                            "onUpdate:modelValue": (v: any) => {
                                formData.value = v
                            },
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

// ============================================================
// Main App
// ============================================================

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
                activeSchema.value = parsed
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
                activeSchema.value = parsed
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
                    h(
                        "p",
                        "Paste a JSON Schema, provide a URL, or pick a built-in example to render the tool parameter form."
                    ),
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
                              onInput: (e: Event) =>
                                  (jsonInput.value = (e.target as HTMLTextAreaElement).value),
                              placeholder:
                                  '{\n  "type": "object",\n  "properties": {\n    "name": { "type": "string", "title": "Name" }\n  }\n}',
                          })
                        : h("div", { class: "url-row" }, [
                              h("input", {
                                  type: "text",
                                  value: urlInput.value,
                                  onInput: (e: Event) =>
                                      (urlInput.value = (e.target as HTMLInputElement).value),
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
                            ? h(
                                  "button",
                                  { class: "btn btn-primary", onClick: tryParseAndRender },
                                  "Render"
                              )
                            : null,
                        h("button", { class: "btn btn-secondary", onClick: clear }, "Clear"),
                        errorMsg.value ? h("span", { class: "error-msg" }, errorMsg.value) : null,
                        successMsg.value
                            ? h("span", { class: "success-msg" }, successMsg.value)
                            : null,
                    ]),

                    // Built-in examples
                    h("div", { class: "examples" }, [
                        h(
                            "span",
                            { style: "font-size:0.8rem;color:#6c757d;margin-right:4px" },
                            "Examples:"
                        ),
                        ...Object.keys(BUILTIN_EXAMPLES).map((id) =>
                            h("button", { class: "chip", onClick: () => loadExample(id) }, id)
                        ),
                    ]),
                ]),

                // Output
                activeSchema.value
                    ? h(GxFormViewer, {
                          schema: activeSchema.value,
                          key: JSON.stringify(activeSchema.value),
                      })
                    : h("div", { class: "empty-state" }, [
                          h("p", "Paste a schema or pick an example to get started"),
                      ]),
            ])
    },
})

createApp(App).mount("#app")
