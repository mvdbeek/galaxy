<template>
    <div class="invocations-list">
        <h2 class="mb-3">
            <span id="invocations-title">Workflow Invocations</span>
        </h2>
        <b-alert variant="info" show v-if="headerMessage">
            {{ headerMessage }}
        </b-alert>
        <b-table
            id="invocation-list-table"
            :fields="invocationFields"
            :items="provider"
            v-model="invocationItemsModel"
            :per-page="perPage"
            :current-page="currentPage"
            hover
            striped
            caption-top
            fixed
            show-empty
        >
            <template v-slot:empty>
                <b-alert id="no-invocations" variant="info" show>
                    {{ noInvocationsMessage }}
                </b-alert>
            </template>
            <template v-slot:row-details="row">
                <b-card>
                    <small class="float-right" :data-invocation-id="row.item.id">
                        <b>Invocation: {{ row.item.id }}</b>
                    </small>
                    <workflow-invocation-state :invocation-id="row.item.id" @invocation-cancelled="refresh" />
                </b-card>
            </template>
            <template v-slot:cell(workflow_id)="data">
                <b-link
                    class="toggle-invocation-details"
                    v-b-tooltip
                    title="Show Invocation details"
                    href="#"
                    @click.stop="swapRowDetails(data)"
                >
                    <b>{{ getWorkflowNameByInstanceId(data.item.workflow_id) }}</b>
                </b-link>
            </template>
            <template v-slot:cell(history_id)="data">
                <b-link
                    id="switch-to-history"
                    v-b-tooltip
                    title="Switch to History"
                    href="#"
                    @click.stop="switchHistory(data.item.history_id)"
                >
                    <b>{{ getHistoryNameById(data.item.history_id) }}</b>
                </b-link>
            </template>
            <template v-slot:cell(create_time)="data">
                <UtcDate :date="data.value" mode="elapsed" />
            </template>
            <template v-slot:cell(update_time)="data">
                <UtcDate :date="data.value" mode="elapsed" />
            </template>
            <template v-slot:cell(execute)="data">
                <b-button
                    v-b-tooltip.hover.bottom
                    id="run-workflow"
                    title="Run Workflow"
                    class="workflow-run btn-sm btn-primary fa fa-play"
                    @click.stop="executeWorkflow(getWorkflowByInstanceId(data.item.workflow_id).id)"
                />
            </template>
        </b-table>
        <b-pagination
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            aria-controls="my-table"
        ></b-pagination>
    </div>
</template>

<script>
import { getAppRoot } from "onload/loadConfig";
import { getGalaxyInstance } from "app";
import { invocationsProvider } from "components/providers/InvocationsProvider";
import { WorkflowInvocationState } from "components/WorkflowInvocationState";
import UtcDate from "components/UtcDate";
import LoadingSpan from "components/LoadingSpan";
import { mapCacheActions } from "vuex-cache";
import { mapGetters } from "vuex";

export default {
    components: {
        UtcDate,
        WorkflowInvocationState,
        LoadingSpan,
    },
    props: {
        noInvocationsMessage: { type: String, default: "No Workflow Invocations to display" },
        headerMessage: { type: String, default: "" },
        ownerGrid: { type: Boolean, default: true },
    },
    data() {
        const fields = [
            { key: "workflow_id", label: "Workflow" },
            { key: "history_id", label: "History" },
            { key: "create_time", label: "Invoked" },
            { key: "update_time", label: "Updated" },
            { key: "state" },
            { key: "execute", label: "" },
        ];
        return {
            invocationItems: [],
            invocationItemsModel: [],
            invocationFields: fields,
            status: "",
            currentPage: 1,
            perPage: 50,
            rows: 0,
        };
    },
    computed: {
        ...mapGetters([
            "getWorkflowNameByInstanceId",
            "getWorkflowByInstanceId",
            "getHistoryById",
            "getHistoryNameById",
        ]),
        invocationItemsComputed() {
            return this.computeItems(this.invocationItems);
        },
        apiUrl() {
            return `${getAppRoot()}api/invocations`;
        },
    },
    watch: {
        invocationItems: function (promise) {
            promise.then((invocations) => {
                const historyIds = new Set();
                const workflowIds = new Set();
                invocations.map((invocation) => {
                    historyIds.add(invocation.history_id);
                    workflowIds.add(invocation.workflow_id);
                });
                historyIds.forEach(
                    (history_id) => this.getHistoryById(history_id) || this.fetchHistoryForId(history_id)
                );
                workflowIds.forEach(
                    (workflow_id) =>
                        this.getWorkflowByInstanceId(workflow_id) || this.fetchWorkflowForInstanceId(workflow_id)
                );
            });
        },
    },
    methods: {
        ...mapCacheActions(["fetchWorkflowForInstanceId", "fetchHistoryForId"]),
        provider(ctx) {
            ctx.apiUrl = this.apiUrl;
            const extraParams = this.ownerGrid ? {} : { include_terminal: false };
            this.invocationItems = invocationsProvider(ctx, this.setRows, extraParams);
            return this.invocationItems;
        },
        refresh() {
            this.$root.$emit("bv::refresh::table", "invocation-list-table");
        },
        setRows(data) {
            this.rows = data.headers.total_matches;
        },
        swapRowDetails(row) {
            row.toggleDetails();
        },
        executeWorkflow: function (workflowId) {
            window.location = `${getAppRoot()}workflows/run?id=${workflowId}`;
        },
        switchHistory(historyId) {
            const Galaxy = getGalaxyInstance();
            Galaxy.currHistoryPanel.switchToHistory(historyId);
        },
    },
};
</script>
