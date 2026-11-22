<script setup lang="ts">
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { computed, ref } from "vue";

import type { InvocationState, InvocationStepIteration } from "@/api/invocations";
import { iconClasses, LOOP_ENDED_INVOCATION_STATES, loopIterationState } from "@/composables/useInvocationGraph";
import localize from "@/utils/localization";
import { withPrefix } from "@/utils/redirect";

import ExternalLink from "../ExternalLink.vue";
import GAlert from "@/components/BaseComponents/GAlert.vue";
import GButton from "@/components/BaseComponents/GButton.vue";

/** How many of the newest iterations are listed while the list is collapsed. */
const COLLAPSED_COUNT = 5;

const props = defineProps<{
    /** The iterations of the loop step, in order */
    iterations: InvocationStepIteration[];
    /** The state of the invocation the loop step belongs to */
    invocationState: InvocationState;
}>();

const showAll = ref(false);

const invocationEnded = computed(() => LOOP_ENDED_INVOCATION_STATES.includes(props.invocationState));

const isCollapsible = computed(() => props.iterations.length > COLLAPSED_COUNT);

const shownIterations = computed(() =>
    isCollapsible.value && !showAll.value ? props.iterations.slice(-COLLAPSED_COUNT) : props.iterations,
);

/** Localize a message, then put a number in place of its `{n}`. */
function localizeWithNumber(message: string, n: number): string {
    return localize(message).replace("{n}", String(n));
}

/** The loop's outcome, from that of its newest iteration */
const summary = computed(() => {
    const newest = props.iterations[props.iterations.length - 1];
    // Only iterations that ran to an outcome count, not a running or skipped one.
    const ranCount = props.iterations.filter((each) => each.loop_outcome && each.loop_outcome !== "skipped").length;
    switch (newest?.loop_outcome) {
        case "stop":
            return ranCount === 1
                ? localize("Loop stopped after 1 iteration")
                : localizeWithNumber("Loop stopped after {n} iterations", ranCount);
        case "skipped":
            return localize("Loop did not run: its condition was false");
        case "failed":
            return localizeWithNumber("Loop failed in iteration {n}", newest.iteration);
        case "limit":
            return ranCount === 1
                ? localize("Loop stopped at the iteration limit after 1 iteration")
                : localizeWithNumber("Loop stopped at the iteration limit after {n} iterations", ranCount);
        default:
            if (invocationEnded.value) {
                return localize("Loop did not finish");
            }
            if (!newest || (newest.iteration === 0 && !newest.loop_outcome)) {
                return localize("Loop not finished yet");
            }
            // The next iteration starts in the pass that records "continue".
            return localizeWithNumber(
                "Loop running: iteration {n}",
                newest.loop_outcome ? newest.iteration + 1 : newest.iteration,
            );
    }
});

function outcomeText(iteration: InvocationStepIteration): string {
    switch (iteration.loop_outcome) {
        case "continue":
            return localize("completed, loop continued");
        case "stop":
            return localize("completed, loop stopped");
        case "skipped":
            return localize("skipped: condition was false");
        case "failed":
            return localize("failed");
        case "limit":
            return localize("completed; loop failed: iteration limit reached");
        default:
            if (invocationEnded.value) {
                return localize("did not finish");
            }
            return iteration.iteration === 0 ? localize("not finished yet") : localize("running");
    }
}

function iterationIcon(iteration: InvocationStepIteration) {
    return iconClasses[loopIterationState(iteration, props.invocationState)];
}
</script>

<template>
    <GAlert variant="secondary" show class="workflow-loop-iterations">
        <div class="d-flex align-items-center justify-content-between flex-wrap">
            <span data-description="loop iterations summary">{{ summary }}</span>
            <GButton
                v-if="isCollapsible"
                size="small"
                transparent
                :aria-expanded="showAll ? 'true' : 'false'"
                data-description="toggle loop iterations"
                @click="showAll = !showAll">
                <template v-if="showAll">{{
                    localizeWithNumber("Show only the newest {n}", COLLAPSED_COUNT)
                }}</template>
                <template v-else>{{ localizeWithNumber("Show all {n}", props.iterations.length) }}</template>
            </GButton>
        </div>
        <ul class="list-unstyled mb-0 mt-1">
            <li
                v-for="iteration in shownIterations"
                :key="iteration.iteration"
                class="d-flex align-items-center flex-gapx-1"
                data-description="loop iteration"
                :data-iteration="iteration.iteration"
                :data-outcome="iteration.loop_outcome ?? ''">
                <FontAwesomeIcon
                    :icon="iterationIcon(iteration).icon"
                    :class="iterationIcon(iteration).class"
                    :spin="iterationIcon(iteration).spin"
                    fixed-width />
                <span data-description="loop iteration label">
                    <b>{{ localizeWithNumber("Iteration {n}", iteration.iteration) }}</b
                    >:
                    {{ outcomeText(iteration) }}
                </span>
                <ExternalLink
                    :href="withPrefix(`/workflows/invocations/${iteration.subworkflow_invocation_id}`)"
                    :aria-label="localizeWithNumber('View iteration {n}', iteration.iteration)">
                    {{ localize("View") }}
                </ExternalLink>
            </li>
        </ul>
    </GAlert>
</template>
