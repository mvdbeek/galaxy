<script setup lang="ts">
import { faFileAlt, faSquare } from "@fortawesome/free-regular-svg-icons";
import { faCheckSquare, faInfoCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { computed } from "vue";

import type { SecondaryFileSelection } from "./model";

import Popper from "@/components/Popper/Popper.vue";

interface Props {
    secondaryFiles: SecondaryFileSelection[];
    disabled?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
    disabled: false,
});

const emit = defineEmits<{
    (e: "toggle", index: number): void;
}>();

const selectedCount = computed(() => props.secondaryFiles.filter((f) => f.selected).length);
const hasSecondaryFiles = computed(() => props.secondaryFiles.length > 0);

function toggleFile(index: number) {
    if (!props.disabled) {
        emit("toggle", index);
    }
}

function getFileName(path: string): string {
    return path.split("/").pop() || path;
}
</script>

<template>
    <Popper
        v-if="hasSecondaryFiles"
        placement="bottom"
        title="Detected Index Files"
        mode="primary-title"
        trigger="click">
        <template v-slot:reference>
            <span class="secondary-files-indicator cursor-pointer" :class="{ 'has-selected': selectedCount > 0 }">
                <FontAwesomeIcon :icon="faFileAlt" />
                <span v-if="selectedCount > 0" class="badge badge-info ml-1">{{ selectedCount }}</span>
            </span>
        </template>
        <div class="secondary-files-content px-2 py-2 no-highlight">
            <div class="mb-2 text-muted small">
                <FontAwesomeIcon :icon="faInfoCircle" class="mr-1" />
                <span v-localize>
                    Index files detected alongside your data. Select which to import instead of regenerating.
                </span>
            </div>
            <table class="secondary-files-table grid w-100">
                <tbody>
                    <tr
                        v-for="(file, index) in secondaryFiles"
                        :key="file.path"
                        class="secondary-file-row"
                        :class="{ disabled: disabled }"
                        @click="toggleFile(index)">
                        <td class="checkbox-cell">
                            <FontAwesomeIcon
                                v-if="file.selected"
                                class="px-2 text-success"
                                :icon="faCheckSquare"
                                fa-fw />
                            <FontAwesomeIcon v-else class="px-2" :icon="faSquare" fa-fw />
                        </td>
                        <td class="description-cell text-left">
                            <span class="pr-2">{{ file.description }}</span>
                        </td>
                        <td class="filename-cell text-muted small text-left">
                            <span class="pr-2">{{ getFileName(file.path) }}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div v-if="disabled" class="secondary-files-cover" />
        </div>
    </Popper>
</template>

<style lang="scss" scoped>
@import "@/style/scss/theme/blue.scss";

.secondary-files-indicator {
    color: $text-muted;
    &.has-selected {
        color: $brand-info;
    }
}

.secondary-files-content {
    position: relative;
    min-width: 300px;

    .secondary-files-cover {
        background: $white;
        cursor: no-drop;
        height: 100%;
        left: 0;
        opacity: 0.25;
        position: absolute;
        top: 0;
        width: 100%;
    }

    .secondary-files-table {
        tr {
            cursor: pointer;
            &:hover:not(.disabled) {
                background-color: lighten($brand-info, 35%);
            }
            &.disabled {
                cursor: not-allowed;
                opacity: 0.6;
            }
        }

        .checkbox-cell {
            width: 40px;
        }

        .description-cell {
            font-weight: 500;
        }

        .filename-cell {
            font-size: 0.85em;
        }
    }
}
</style>
