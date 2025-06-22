<script setup lang="ts">
import { computed, watch, ref } from "vue";
import { fetchCollectionElements, fetchCollectionSummary } from "@/api/datasetCollections";

interface CollectionElementPickerProps {
    hdcaId: string;
}
const props = defineProps<CollectionElementPickerProps>();
const dceToId = ref<{
    [k: string]: string | undefined;
}>()
const selectedValue = ref<string>()

watch(() => props.hdcaId, async () => {
    const collectionSummary = await fetchCollectionSummary({ hdca_id: props.hdcaId })
    const collectionElements = await fetchCollectionElements({ hdcaId: props.hdcaId, collectionId: collectionSummary.collection_id, limit: 10 })
    const identifierAndIds = Object.fromEntries(collectionElements.map((element) => {
        return [element.object?.id, element.element_identifier]
    }))
    dceToId.value = identifierAndIds
}, {immediate: true})
const value = computed(() => selectedValue.value || Object.keys(dceToId.value || {}).at(0))

function handleInput(value: string) {
    console.log("got value", value)
    selectedValue.value = value
}

</script>

<template>
    <div>
        <b-navbar>
            <b-collapse id="nav-text-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-text>Select Element</b-nav-text>
                </b-navbar-nav>
                <b-nav-form>
                    <b-input-group size="sm">
                        <b-form-select
                            :value="value"
                            class="text-right"
                            :options="dceToId"
                            @input="handleInput"></b-form-select>
                    </b-input-group>
                </b-nav-form>
            </b-collapse>
        </b-navbar>
        <slot name="element" :element="value"></slot>
    </div>
</template>
