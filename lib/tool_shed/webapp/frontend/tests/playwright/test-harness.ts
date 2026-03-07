import { createApp, defineComponent, h, reactive } from "vue"
import { JsonForms } from "@jsonforms/vue"
import { vanillaRenderers } from "@jsonforms/vue-vanilla"
import type { JsonFormsChangeEvent, JsonFormsRendererRegistryEntry } from "@jsonforms/core"
import rawSchemas from "./test_tool_schemas.json"

const renderers: JsonFormsRendererRegistryEntry[] = [...vanillaRenderers]

interface ToolSchema {
    [key: string]: unknown
}

// Strip $schema field - AJV in JsonForms doesn't support draft 2020-12 $schema URIs
function stripSchemaDialect(schema: ToolSchema): ToolSchema {
    const { $schema, ...rest } = schema
    return rest
}

const schemas = Object.fromEntries(
    Object.entries(rawSchemas as Record<string, ToolSchema>).map(([id, s]) => [id, stripSchemaDialect(s)])
)

const SchemaFormCard = defineComponent({
    name: "SchemaFormCard",
    props: {
        toolId: { type: String, required: true },
        schema: { type: Object, required: true },
    },
    setup(props) {
        const data = reactive<Record<string, unknown>>({})
        const onChange = (event: JsonFormsChangeEvent) => {
            Object.assign(data, event.data)
        }
        return () =>
            h("div", { class: "tool-card", id: `tool-${props.toolId}` }, [
                h("h2", `Tool: ${props.toolId}`),
                h(JsonForms, {
                    data,
                    schema: props.schema,
                    renderers,
                    onChange,
                }),
            ])
    },
})

const App = defineComponent({
    name: "App",
    setup() {
        return () =>
            h("div", [
                h("h1", "Galaxy Tool Parameter Schema Forms"),
                ...Object.entries(schemas).map(([toolId, schema]) =>
                    h(SchemaFormCard, { toolId, schema, key: toolId })
                ),
            ])
    },
})

createApp(App).mount("#app")
