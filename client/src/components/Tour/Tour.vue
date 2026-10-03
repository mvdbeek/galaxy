<script setup lang="ts">
import { BAlert } from "bootstrap-vue";
import { storeToRefs } from "pinia";
import { computed, nextTick, onUnmounted, ref, watch } from "vue";
import { useRouter } from "vue-router/composables";

import { isAdminUser, isAnonymousUser } from "@/api";
import type { TourRequirements, TourStep as TourStepType } from "@/api/tours";
import { useHistoryStore } from "@/stores/historyStore";
import { useTourStore } from "@/stores/tourStore";
import { useUserStore } from "@/stores/userStore";
import { errorMessageAsString } from "@/utils/simple-error";

import GModal from "../BaseComponents/GModal.vue";
import LoadingSpan from "../LoadingSpan.vue";
import TourStep from "./TourStep.vue";

/** Allow time to read even short steps when auto-playing the tour. */
const MIN_PLAY_DELAY = 10000;
/** Reading time per word at 200 words per minute, plus time to orient to each step. */
const WORD_DELAY = 300;
const STEP_DELAY = 2000;

const props = defineProps<{
    steps: TourStepType[];
    requirements: TourRequirements;
    tourId: string;
    waitingOnElement?: string | null;
    onBefore: (step: TourStepType) => Promise<void>;
    onNext: (step: TourStepType) => Promise<void>;
}>();

const emit = defineEmits(["end-tour"]);

const router = useRouter();

const errorMessage = ref("");
const isPlaying = ref(false);
const isAdvancing = ref(false);
let playTimeout: ReturnType<typeof setTimeout> | undefined;
let isActive = true;

// Store variables
const historyStore = useHistoryStore();
const { currentHistory } = storeToRefs(historyStore);
const { currentUser } = storeToRefs(useUserStore());
const tourStore = useTourStore();
const { currentTour } = storeToRefs(tourStore);

/** The current step index
 *
 * This is set and updated based on the currently active tour in the `tourStore`.
 * Is `-1` if no tour is currently active (or has ended).
 */
const currentIndex = computed({
    get: () => (currentTour.value?.step !== undefined ? currentTour.value?.step : -1),
    set: (val: number) => {
        // We still check if there's a current tour, because this setter might be called
        // after the tour has ended and currentTour is unset.
        if (currentTour.value) {
            tourStore.setTour(props.tourId, val);
        }
    },
});

// Local step variables
const currentStep = computed(() => props.steps[currentIndex.value]);
const numberOfSteps = computed(() => props.steps.length);
const isFirst = computed(() => currentIndex.value === 0);
const isLast = computed(() => currentIndex.value === props.steps.length - 1);

/** On some conditions here, a message modal is shown and the tour doesn't start
 * when these conditions are met. This returns the contents of the modal if it should be shown.
 */
const modalContents = computed<{
    title: string;
    message: string;
    variant: "danger" | "info";
    loading?: boolean;
    okText?: string;
    cancelText?: "End Tour";
    ok?: () => Promise<void>;
} | null>(() => {
    if (errorMessage.value) {
        return {
            title: "Tour Failed",
            message: errorMessage.value,
            variant: "danger",
            ok: async () => {
                errorMessage.value = "";
                pause();
            },
        };
    }

    if (!currentHistory.value || !currentUser.value) {
        return {
            title: "Preparing Tour",
            message: "Evaluating Requirements",
            variant: "info",
            loading: true,
        };
    }

    if (isFirst.value) {
        if (props.requirements.indexOf("logged_in") >= 0 && isAnonymousUser(currentUser.value)) {
            return {
                title: "Requires Login",
                message: "You must log in to Galaxy to use this tour.",
                variant: "info",
                okText: router ? "Login or Register" : undefined,
                cancelText: "End Tour",
                ok: async () => {
                    endTour();
                    if (router) {
                        router.push(`/login/start?redirect=/tours/${props.tourId}`);
                    }
                },
            };
        }
        if (props.requirements.indexOf("admin") >= 0 && !isAdminUser(currentUser.value)) {
            return {
                title: "Requires Admin",
                message: "You must be an admin to use this tour.",
                variant: "info",
                okText: router ? "Exit Tour" : undefined,
                cancelText: "End Tour",
                ok: async () => {
                    endTour();
                    if (router) {
                        if (isAnonymousUser(currentUser.value)) {
                            router.push(`/login/start?redirect=/tours/${props.tourId}`);
                        } else {
                            router.push("/");
                        }
                    }
                },
            };
        }
        // TODO: better estimate for whether the history is new.
        if (props.requirements.indexOf("new_history") >= 0 && currentHistory.value && currentHistory.value.size !== 0) {
            return {
                title: "Requires New History",
                message:
                    "This tour is designed to run on a new history, please create a new history before running it.",
                variant: "info",
                okText: "Create New History",
                cancelText: "End Tour",
                ok: async () => {
                    await historyStore.createNewHistory();
                },
            };
        }
    }
    return null;
});

// We use this ref to control the modal visibility
const showModal = ref(false);
const modalRef = ref<InstanceType<typeof GModal> | null>(null);

// Wait for GModal to render and then force show
// (We needed this, without this the GModal wouldn't show via the .sync prop)
watch(
    () => modalContents.value,
    async (newValue) => {
        if (Boolean(newValue) !== showModal.value) {
            showModal.value = Boolean(newValue);

            if (showModal.value) {
                pause();
                await nextTick();
                modalRef.value?.showModal?.();
            }
        }
    },
    { immediate: true },
);

start();

onUnmounted(() => {
    isActive = false;
    pause();
    window.removeEventListener("pointerdown", pause, true);
    window.removeEventListener("keydown", pause, true);
    window.removeEventListener("keyup", handleKeyup);
});

function start() {
    window.addEventListener("pointerdown", pause, true);
    window.addEventListener("keydown", pause, true);
    window.addEventListener("keyup", handleKeyup);
}

function play(isCurrentlyPlaying: boolean) {
    clearPlayTimeout();
    isPlaying.value = isCurrentlyPlaying;
    if (isPlaying.value) {
        scheduleNext();
    }
}

function clearPlayTimeout() {
    clearTimeout(playTimeout);
    playTimeout = undefined;
}

function pause() {
    isPlaying.value = false;
    clearPlayTimeout();
}

function scheduleNext() {
    if (!isPlaying.value || isAdvancing.value || isLast.value || !currentStep.value || modalContents.value) {
        return;
    }

    const { title, content } = currentStep.value;
    const text = new DOMParser().parseFromString(`${title || ""} ${content || ""}`, "text/html").body.textContent || "";
    const wordCount = text.trim().split(/\s+/).length;
    playTimeout = setTimeout(next, Math.max(MIN_PLAY_DELAY, wordCount * WORD_DELAY + STEP_DELAY));
}

async function next() {
    if (!isActive || isAdvancing.value || modalContents.value) {
        return;
    }
    clearPlayTimeout();
    isAdvancing.value = true;
    try {
        // do post-actions
        if (currentStep.value) {
            await props.onNext(currentStep.value);
        }
        if (!isActive) {
            return;
        }
        // do pre-actions
        const nextIndex = currentIndex.value + 1;
        if (nextIndex < numberOfSteps.value && currentIndex.value !== -1) {
            const nextStep = props.steps[nextIndex];
            if (nextStep) {
                await props.onBefore(nextStep);
            }
        } else {
            // End Tour
            endTour();
        }
        // go to next step
        if (isActive) {
            currentIndex.value = nextIndex;
        }
    } catch (e) {
        pause();
        errorMessage.value = errorMessageAsString(e);
    } finally {
        isAdvancing.value = false;
    }
    scheduleNext();
}

/** Ends the tour
 *
 * _In the case that_ `TourRunner` _is the parent, this will unmount the component._
 */
function endTour() {
    isActive = false;
    tourStore.setTour(undefined);
    pause();
    errorMessage.value = "";

    emit("end-tour");
}

async function handleKeyup(e: KeyboardEvent) {
    switch (e.keyCode) {
        case 39:
            await next();
            break;
        case 27:
            endTour();
            break;
    }
}

function modalDismiss(ok = true) {
    if (modalContents.value?.ok && (ok || errorMessage.value)) {
        modalContents.value.ok();
    } else if (modalContents.value?.cancelText === "End Tour") {
        endTour();
    }
}
</script>

<template>
    <div class="d-flex flex-column">
        <GModal
            v-if="modalContents !== null"
            id="tour-requirement"
            ref="modalRef"
            show
            :confirm="!errorMessage && modalContents.ok !== undefined"
            :ok-text="modalContents.okText"
            :cancel-text="modalContents.cancelText"
            :title="modalContents.title"
            size="small"
            :footer="Boolean(errorMessage)"
            @ok="modalDismiss"
            @cancel="modalDismiss(false)">
            <BAlert :variant="modalContents.variant" show>
                <span v-if="!modalContents.loading">{{ modalContents.message }}</span>
                <LoadingSpan v-else :message="modalContents.message" />
            </BAlert>
            <div v-if="errorMessage">
                The tour encountered an issue and cannot continue to the next step. This may be due to:
                <ul class="mb-2">
                    <li>Required interface elements not being visible or accessible</li>
                    <li>Page content still loading</li>
                    <li>Browser or network connectivity issues</li>
                </ul>
            </div>
            <template v-slot:footer>
                <span v-if="errorMessage">Exit to retry the current step.</span>
                <span v-else-if="modalContents.cancelText === 'End Tour'">Closing this modal ends the tour.</span>
            </template>
        </GModal>
        <TourStep
            v-if="modalContents === null && currentHistory && currentStep && currentUser"
            :key="currentIndex"
            :step="currentStep"
            :is-playing="isPlaying"
            :is-advancing="isAdvancing"
            :is-last="isLast"
            :waiting-on-element="waitingOnElement"
            @next="next"
            @end="endTour"
            @play="play" />
    </div>
</template>
