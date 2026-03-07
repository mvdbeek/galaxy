import { vanillaRenderers } from "@jsonforms/vue-vanilla"
import type { JsonFormsRendererRegistryEntry } from "@jsonforms/core"

export const renderers: JsonFormsRendererRegistryEntry[] = [...vanillaRenderers]
