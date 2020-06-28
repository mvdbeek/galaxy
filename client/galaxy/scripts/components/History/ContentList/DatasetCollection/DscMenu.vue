<template>
    <PriorityMenu :starting-height="27">

        <PriorityMenuItem
            key="delete-collection"
            title="Delete Collection Only"
            icon="fas fa-trash"
            @click.stop="$emit('deleteCollection')"
        />

        <PriorityMenuItem
            key="delete-with-datasets""
            title="Delete Contained Datasets"
            icon="fas fa-trash"
            @click.stop="$emit('deleteCollection', { recursive: true, })"
        />

        <PriorityMenuItem
            key="purge-datasets"
            title="Purge Contained Datasets"
            icon="fas fa-burn"
            @click.stop="$emit('deleteCollection', { recursive: true, purge: true })"
        />

    </PriorityMenu>
</template>

<script>

import { DatasetCollection, deleteCollection } from "../../model";
import { PriorityMenu, PriorityMenuItem } from "components/PriorityMenu";

export default {
    components: {
        PriorityMenu,
        PriorityMenuItem
    }
};

</script>
