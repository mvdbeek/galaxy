<template>
    <div>
        <h3 v-if="includeTitle">Job Information</h3>
        <b-table small :items="jobProperties" :fields="fields" v-if="job" @row-clicked="toggleDetails">
            <template v-slot:cell(value)="data">
                <span v-html="formatPreview(data)"/>
            </template>
            <template v-slot:row-details="row">
                <b-card>
                    <pre class="text-white bg-dark"><code class="break-word">{{row.item.value}}</code></pre>
                </b-card>
            </template>
        </b-table>
    </div>
</template>
<script>
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";

Vue.use(BootstrapVue);

export default {
    props: {
        job: Object,
        includeTitle: {
            type: Boolean, required: false, default: false,
        }
    },
    data() {
        return {
            fields: [
                {key: 'jobProperty', label: 'Job Information'},
                {key: 'value', label: ''}
            ],
            formatted: ['Tool Standard Output:', 'Tool Standard Error:', 'Job Standard Output:', 'Job Standard Error:', 'Command Line:'],
        }
    },
    computed: {
        jobProperties() {
            const properties = [
                {jobProperty: 'Galaxy Tool ID:', value: this.job.tool_id},
                {jobProperty: 'Galaxy Tool Version:', value: this.job.tool_version},
            ]
            if (this.job.command_version) {
                properties.push({jobProperty: 'Tool Version:', value: this.job.command_version});
            }
            if (this.job.command_line) {
                properties.push({jobProperty: 'Command Line:', value: this.job.command_line});
            }
            if (this.job.tool_stdout) {
                properties.push({jobProperty: 'Tool Standard Output:', value: this.job.tool_stdout});
            }
            if (this.job.tool_stderr) {
                properties.push({jobProperty: 'Tool Standard Error:', value: this.job.tool_stderr});
            }
            if (this.job.job_stdout) {
                properties.push({jobProperty: 'Job Standard Output:', value: this.job.job_stdout});
            }
            if (this.job.job_stderr) {
                properties.push({jobProperty: 'Job Standard Error:', value: this.job.job_stderr});
            }
            if (this.job.exit_code) {
                properties.push({jobProperty: 'Tool Exit Code:', value: this.job.exit_code});
            }
            console.log(this.job);
            console.log(properties);
            return properties;
        },
    },
    methods: {
        toggleDetails: function(item) {
            if (this.formatted.includes(item.jobProperty) && item.value) {
                this.$set(item, '_showDetails', !item._showDetails)
            }
        },
        formatPreview: function(data) {
            if (this.formatted.includes(data.item.jobProperty)) {
                let truncatedData = data.value;
                if (data.value.length > 40) {
                    truncatedData = data.value.substring(0, 40) + '...'
                }
                return `<code>${truncatedData}</code>`
            }
            return data.value;
        },
        formatter: function(data) {
            if (this.formatted.includes(data.item.jobProperty)) {
                return `<pre><code>${data.value}</code></pre>`
            }
            return data.value;
        },
        showDetails: function(row) {
            if (this.formatted.includes(row.item.jobProperty)) {
                row.item._showDetails != row.item._showDetails ;
            }
        },
    }
}
</script>