<template>
    <div data-state="waiting">
        <nav class="content-top-menu d-flex align-items-center justify-content-between">
            <h5 class="flex-grow-1 overflow-hidden mr-auto text-nowrap text-truncate">
                <span class="hid">{{ item.hid }}</span
                >: (<span>{{ item.index }}</span
                >)
                <span>Loading...</span>
            </h5>
        </nav>
    </div>
</template>

<script>
export default {
    props: {
        index: { type: Number, required: true },
        selected: { type: Boolean, required: true },
        expanded: { type: Boolean, required: true },
    },
};
</script>
