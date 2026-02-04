# Implementation Plan: Workflow Invocation Output Queuing

## Overview

This plan outlines the implementation for queuing a new workflow invocation that uses outputs from another invocation as inputs, even when the source invocation has not yet scheduled/produced those outputs.

---

## 1. API Payload Design

### 1.1 New Input Source Type: `invocation_output`

Extend the existing input specification to support a new source type that references another invocation's output.

**Current input format:**
```json
{
  "inputs": {
    "0": {"id": "abc123", "src": "hda"}
  }
}
```

**New format for invocation output references:**
```json
{
  "inputs": {
    "0": {
      "src": "invocation_output",
      "invocation_id": "encoded_invocation_id",
      "output_name": "output_label"
    }
  }
}
```

**Alternative: Reference by step + output name (for unlabeled outputs):**
```json
{
  "inputs": {
    "0": {
      "src": "invocation_step_output",
      "invocation_id": "encoded_invocation_id",
      "step_id": "encoded_step_id",
      "output_name": "output"
    }
  }
}
```

### 1.2 Schema Changes

**File:** `lib/galaxy/schema/workflows.py`

Add new Pydantic models for invocation output references:

```python
class InvocationOutputReference(Model):
    """Reference to an output from another workflow invocation."""
    src: Literal["invocation_output"] = "invocation_output"
    invocation_id: EncodedDatabaseIdField
    output_name: str = Field(
        ...,
        description="The label of the workflow output to use as input"
    )

class InvocationStepOutputReference(Model):
    """Reference to a specific step output from another workflow invocation."""
    src: Literal["invocation_step_output"] = "invocation_step_output"
    invocation_id: EncodedDatabaseIdField
    step_id: EncodedDatabaseIdField
    output_name: str = Field(
        ...,
        description="The name of the step output to use as input"
    )

# Update the input union type to include new reference types
WorkflowInput = Union[
    DatasetInput,           # {"src": "hda", "id": "..."}
    DatasetCollectionInput, # {"src": "hdca", "id": "..."}
    InvocationOutputReference,
    InvocationStepOutputReference,
]
```

**File:** `lib/galaxy/schema/invocation.py`

Add new invocation state:

```python
class InvocationState(str, Enum):
    NEW = "new"
    REQUIRES_MATERIALIZATION = "requires_materialization"
    WAITING_FOR_INPUT = "waiting_for_input"  # NEW: Waiting for upstream invocation
    READY = "ready"
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    FAILED = "failed"
    COMPLETED = "completed"
```

---

## 2. ORM Model Changes

### 2.1 New Model: `WorkflowInvocationInputDependency`

**File:** `lib/galaxy/model/__init__.py`

```python
class WorkflowInvocationInputDependency(Base, RepresentById):
    """
    Tracks dependencies between workflow invocations where one invocation
    uses outputs from another as inputs.
    """
    __tablename__ = "workflow_invocation_input_dependency"

    id: Mapped[int] = mapped_column(primary_key=True)

    # The invocation that is waiting for input
    workflow_invocation_id: Mapped[int] = mapped_column(
        ForeignKey("workflow_invocation.id"),
        index=True
    )

    # The workflow step that needs the input
    workflow_step_id: Mapped[int] = mapped_column(
        ForeignKey("workflow_step.id"),
        index=True
    )

    # Input name on the step
    input_name: Mapped[str] = mapped_column(String(255))

    # The source invocation providing the output
    source_invocation_id: Mapped[int] = mapped_column(
        ForeignKey("workflow_invocation.id"),
        index=True
    )

    # The workflow output ID (if referencing labeled output)
    source_workflow_output_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("workflow_output.id"),
        index=True,
        nullable=True
    )

    # Alternative: reference step output directly
    source_step_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("workflow_step.id"),
        index=True,
        nullable=True
    )
    source_output_name: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )

    # Resolved dataset/collection when available
    resolved_dataset_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("history_dataset_association.id"),
        index=True,
        nullable=True
    )
    resolved_collection_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("history_dataset_collection_association.id"),
        index=True,
        nullable=True
    )

    # Timestamps
    create_time: Mapped[datetime] = mapped_column(default=now)
    update_time: Mapped[datetime] = mapped_column(default=now, onupdate=now)

    # Relationships
    workflow_invocation = relationship(
        "WorkflowInvocation",
        foreign_keys=[workflow_invocation_id],
        back_populates="input_dependencies"
    )
    source_invocation = relationship(
        "WorkflowInvocation",
        foreign_keys=[source_invocation_id],
        back_populates="dependent_invocations"
    )
    workflow_step = relationship("WorkflowStep")
    resolved_dataset = relationship("HistoryDatasetAssociation")
    resolved_collection = relationship("HistoryDatasetCollectionAssociation")
```

### 2.2 Update WorkflowInvocation Model

**File:** `lib/galaxy/model/__init__.py`

Add relationships to `WorkflowInvocation`:

```python
class WorkflowInvocation:
    # ... existing fields ...

    # New relationships
    input_dependencies: Mapped[list["WorkflowInvocationInputDependency"]] = relationship(
        "WorkflowInvocationInputDependency",
        foreign_keys="WorkflowInvocationInputDependency.workflow_invocation_id",
        back_populates="workflow_invocation",
        cascade="all, delete-orphan"
    )

    dependent_invocations: Mapped[list["WorkflowInvocationInputDependency"]] = relationship(
        "WorkflowInvocationInputDependency",
        foreign_keys="WorkflowInvocationInputDependency.source_invocation_id",
        back_populates="source_invocation"
    )

    def has_unresolved_input_dependencies(self) -> bool:
        """Check if any input dependencies are still unresolved."""
        return any(
            dep.resolved_dataset_id is None and dep.resolved_collection_id is None
            for dep in self.input_dependencies
        )

    def get_unresolved_dependencies(self) -> list["WorkflowInvocationInputDependency"]:
        """Return list of unresolved input dependencies."""
        return [
            dep for dep in self.input_dependencies
            if dep.resolved_dataset_id is None and dep.resolved_collection_id is None
        ]
```

### 2.3 Database Migration

**File:** `lib/galaxy/model/migrations/alembic/versions/XXXX_add_invocation_input_dependency.py`

```python
"""Add workflow_invocation_input_dependency table

Revision ID: XXXX
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'workflow_invocation_input_dependency',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('workflow_invocation_id', sa.Integer(),
                  sa.ForeignKey('workflow_invocation.id'), nullable=False, index=True),
        sa.Column('workflow_step_id', sa.Integer(),
                  sa.ForeignKey('workflow_step.id'), nullable=False, index=True),
        sa.Column('input_name', sa.String(255), nullable=False),
        sa.Column('source_invocation_id', sa.Integer(),
                  sa.ForeignKey('workflow_invocation.id'), nullable=False, index=True),
        sa.Column('source_workflow_output_id', sa.Integer(),
                  sa.ForeignKey('workflow_output.id'), nullable=True, index=True),
        sa.Column('source_step_id', sa.Integer(),
                  sa.ForeignKey('workflow_step.id'), nullable=True, index=True),
        sa.Column('source_output_name', sa.String(255), nullable=True),
        sa.Column('resolved_dataset_id', sa.Integer(),
                  sa.ForeignKey('history_dataset_association.id'), nullable=True, index=True),
        sa.Column('resolved_collection_id', sa.Integer(),
                  sa.ForeignKey('history_dataset_collection_association.id'), nullable=True, index=True),
        sa.Column('create_time', sa.DateTime(), default=sa.func.now()),
        sa.Column('update_time', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    op.drop_table('workflow_invocation_input_dependency')
```

---

## 3. Workflow Scheduler Changes

### 3.1 Input Resolution During Invocation Creation

**File:** `lib/galaxy/workflow/run_request.py`

Modify `build_workflow_run_configs()` to handle invocation output references:

```python
def _resolve_invocation_output_reference(
    trans,
    input_dict: dict,
    workflow_invocation: WorkflowInvocation,
    step: WorkflowStep,
    input_name: str,
) -> Optional[Union[HistoryDatasetAssociation, HistoryDatasetCollectionAssociation]]:
    """
    Resolve an invocation output reference to an actual dataset/collection.

    Returns the resolved object if available, or None if the source invocation
    hasn't produced the output yet.
    """
    src = input_dict.get("src")
    if src not in ("invocation_output", "invocation_step_output"):
        return None  # Not an invocation reference

    sa_session = trans.sa_session

    # Decode and fetch source invocation
    source_invocation_id = trans.security.decode_id(input_dict["invocation_id"])
    source_invocation = sa_session.get(WorkflowInvocation, source_invocation_id)

    if source_invocation is None:
        raise RequestParameterInvalidException(
            f"Source invocation {input_dict['invocation_id']} not found"
        )

    # Verify user has access to source invocation
    if source_invocation.user_id != trans.user.id:
        raise ItemAccessibilityException(
            f"Cannot access invocation {input_dict['invocation_id']}"
        )

    # Create dependency record
    dependency = WorkflowInvocationInputDependency(
        workflow_invocation=workflow_invocation,
        workflow_step=step,
        input_name=input_name,
        source_invocation=source_invocation,
    )

    if src == "invocation_output":
        # Reference by workflow output label
        output_name = input_dict["output_name"]

        # Find the workflow output definition
        workflow_output = None
        for wo in source_invocation.workflow.workflow_outputs:
            if wo.label == output_name:
                workflow_output = wo
                break

        if workflow_output is None:
            raise RequestParameterInvalidException(
                f"Output '{output_name}' not found in source workflow"
            )

        dependency.source_workflow_output_id = workflow_output.id

        # Try to resolve immediately if output is already available
        output_assoc = source_invocation.get_output_object(output_name)
        if output_assoc:
            if hasattr(output_assoc, 'dataset'):
                dependency.resolved_dataset_id = output_assoc.id
                return output_assoc
            else:
                dependency.resolved_collection_id = output_assoc.id
                return output_assoc

    elif src == "invocation_step_output":
        # Reference by step + output name
        source_step_id = trans.security.decode_id(input_dict["step_id"])
        dependency.source_step_id = source_step_id
        dependency.source_output_name = input_dict["output_name"]

        # Try to resolve immediately
        for step_inv in source_invocation.steps:
            if step_inv.workflow_step_id == source_step_id:
                for output in step_inv.output_datasets:
                    if output.output_name == input_dict["output_name"]:
                        dependency.resolved_dataset_id = output.dataset_id
                        return output.dataset
                for output in step_inv.output_dataset_collections:
                    if output.output_name == input_dict["output_name"]:
                        dependency.resolved_collection_id = output.dataset_collection_id
                        return output.dataset_collection

    # Output not yet available - add dependency and return None
    sa_session.add(dependency)
    return None
```

### 3.2 Scheduler State Management

**File:** `lib/galaxy/workflow/scheduling_manager.py`

Modify `WorkflowRequestMonitor` to handle the `WAITING_FOR_INPUT` state:

```python
class WorkflowRequestMonitor:

    def __attempt_resolve_input_dependencies(
        self,
        workflow_invocation: WorkflowInvocation
    ) -> bool:
        """
        Attempt to resolve any pending input dependencies from upstream invocations.

        Returns True if all dependencies are resolved, False otherwise.
        """
        sa_session = self.app.model.context.current
        all_resolved = True

        for dependency in workflow_invocation.get_unresolved_dependencies():
            source_invocation = dependency.source_invocation

            # Check if source invocation has failed
            if source_invocation.state == InvocationState.FAILED:
                # Fail this invocation too
                workflow_invocation.add_message(
                    InvocationFailureInputDependencyFailed(
                        workflow_step_id=dependency.workflow_step_id,
                        input_name=dependency.input_name,
                        source_invocation_id=source_invocation.id,
                        reason="Source invocation failed"
                    )
                )
                workflow_invocation.set_state(InvocationState.FAILED)
                return False

            # Try to resolve the output
            resolved = self.__try_resolve_dependency(dependency)
            if not resolved:
                all_resolved = False

        return all_resolved

    def __try_resolve_dependency(
        self,
        dependency: WorkflowInvocationInputDependency
    ) -> bool:
        """Try to resolve a single dependency."""
        source_invocation = dependency.source_invocation

        if dependency.source_workflow_output_id:
            # Resolve by workflow output label
            workflow_output = self.app.model.context.current.get(
                WorkflowOutput,
                dependency.source_workflow_output_id
            )
            output_obj = source_invocation.get_output_object(workflow_output.label)
            if output_obj:
                if isinstance(output_obj, HistoryDatasetAssociation):
                    dependency.resolved_dataset_id = output_obj.id
                else:
                    dependency.resolved_collection_id = output_obj.id
                return True

        elif dependency.source_step_id:
            # Resolve by step output
            for step_inv in source_invocation.steps:
                if step_inv.workflow_step_id == dependency.source_step_id:
                    for output in step_inv.output_datasets:
                        if output.output_name == dependency.source_output_name:
                            dependency.resolved_dataset_id = output.dataset_id
                            return True
                    for output in step_inv.output_dataset_collections:
                        if output.output_name == dependency.source_output_name:
                            dependency.resolved_collection_id = output.dataset_collection_id
                            return True

        return False

    def __monitor(self):
        # ... existing monitoring code ...

        # Handle WAITING_FOR_INPUT state
        waiting_invocations = self.app.model.context.current.scalars(
            select(WorkflowInvocation).where(
                WorkflowInvocation.state == InvocationState.WAITING_FOR_INPUT
            )
        ).all()

        for workflow_invocation in waiting_invocations:
            if self.__attempt_resolve_input_dependencies(workflow_invocation):
                # All dependencies resolved - transition to READY
                workflow_invocation.set_state(InvocationState.READY)
                self.__schedule(workflow_invocation)
```

### 3.3 Invocation Execution with Dependencies

**File:** `lib/galaxy/workflow/run.py`

Modify the workflow invocation process to use resolved dependencies:

```python
class WorkflowProgress:

    def replacement_for_input_dependency(
        self,
        step: WorkflowStep,
        input_name: str,
    ) -> Optional[Union[HistoryDatasetAssociation, HistoryDatasetCollectionAssociation]]:
        """
        Get the resolved input from an invocation dependency.
        """
        for dependency in self.workflow_invocation.input_dependencies:
            if (dependency.workflow_step_id == step.id and
                dependency.input_name == input_name):
                if dependency.resolved_dataset_id:
                    return self.sa_session.get(
                        HistoryDatasetAssociation,
                        dependency.resolved_dataset_id
                    )
                elif dependency.resolved_collection_id:
                    return self.sa_session.get(
                        HistoryDatasetCollectionAssociation,
                        dependency.resolved_collection_id
                    )
        return None
```

---

## 4. User Communication: Waiting Status

### 4.1 API Response Schema Updates

**File:** `lib/galaxy/schema/invocation.py`

Add input dependency information to invocation responses:

```python
class InvocationInputDependencyView(Model):
    """View model for an input dependency on another invocation."""

    workflow_step_id: EncodedDatabaseIdField
    input_name: str
    source_invocation_id: EncodedDatabaseIdField
    source_invocation_state: InvocationState
    output_name: Optional[str] = None
    step_id: Optional[EncodedDatabaseIdField] = None
    resolved: bool = Field(
        description="Whether the dependency has been resolved to an actual dataset/collection"
    )
    resolved_id: Optional[EncodedDatabaseIdField] = None
    resolved_src: Optional[Literal["hda", "hdca"]] = None


class WorkflowInvocationElementView(WorkflowInvocationCollectionView):
    # ... existing fields ...

    # New field for input dependencies
    input_dependencies: list[InvocationInputDependencyView] = Field(
        default_factory=list,
        description="Input dependencies on other workflow invocations"
    )

    # New field indicating what the invocation is waiting for
    waiting_for: Optional[list[WaitingForInfo]] = Field(
        default=None,
        description="Information about what the invocation is waiting for (if in WAITING_FOR_INPUT state)"
    )


class WaitingForInfo(Model):
    """Information about what an invocation is waiting for."""

    type: Literal["invocation_output"] = "invocation_output"
    invocation_id: EncodedDatabaseIdField
    invocation_state: InvocationState
    workflow_name: str
    output_name: str
    estimated_completion: Optional[datetime] = None
```

### 4.2 Invocation Messages

**File:** `lib/galaxy/schema/invocation.py`

Add new message types for dependency status:

```python
class InvocationWaitingForInputMessage(Model):
    """Message indicating invocation is waiting for upstream output."""

    reason: Literal["waiting_for_invocation_output"] = "waiting_for_invocation_output"
    source_invocation_id: EncodedDatabaseIdField
    source_workflow_name: str
    output_name: str
    source_invocation_state: InvocationState


class InvocationFailureInputDependencyFailed(InvocationFailureMessageBase):
    """Message when a source invocation that this invocation depends on has failed."""

    reason: Literal["input_dependency_failed"] = "input_dependency_failed"
    source_invocation_id: EncodedDatabaseIdField
    input_name: str
    details: Optional[str] = None
```

---

## 5. User Interface Changes

### 5.1 New Data Source Variant

**File:** `client/src/components/Form/Elements/FormData/variants.ts`

Add new source type for invocation outputs:

```typescript
export const SOURCE_VARIANTS = {
  // ... existing variants ...

  INVOCATION_OUTPUT: {
    id: "invocation_output",
    label: "Workflow Invocation Output",
    icon: "fa-sitemap",
    description: "Use output from another workflow invocation",
    multiple: false,
  },
} as const;

export type DataSourceType =
  | "hda"
  | "hdca"
  | "ldda"
  | "invocation_output"
  | "invocation_step_output";
```

### 5.2 Invocation Output Selector Component

**File:** `client/src/components/Form/Elements/FormData/FormDataInvocationOutput.vue`

```vue
<template>
  <div class="invocation-output-selector">
    <div class="mb-3">
      <label class="form-label">Select Source Invocation</label>
      <BFormSelect
        v-model="selectedInvocationId"
        :options="invocationOptions"
        @change="onInvocationChange"
      >
        <template #first>
          <option :value="null">-- Select an invocation --</option>
        </template>
      </BFormSelect>
    </div>

    <div v-if="selectedInvocation" class="mb-3">
      <div class="invocation-info alert alert-info">
        <div class="d-flex align-items-center">
          <span class="me-2">
            <InvocationStateIcon :state="selectedInvocation.state" />
          </span>
          <div>
            <strong>{{ selectedInvocation.workflow_name }}</strong>
            <br />
            <small class="text-muted">
              Started: {{ formatDate(selectedInvocation.create_time) }}
              <span v-if="selectedInvocation.state !== 'scheduled'">
                · Status: {{ selectedInvocation.state }}
              </span>
            </small>
          </div>
        </div>

        <div v-if="!isInvocationComplete" class="mt-2 text-warning">
          <FontAwesomeIcon icon="clock" />
          This invocation is still running. Your workflow will wait for it to complete.
        </div>
      </div>
    </div>

    <div v-if="selectedInvocationId && availableOutputs.length > 0" class="mb-3">
      <label class="form-label">Select Output</label>
      <BFormSelect
        v-model="selectedOutput"
        :options="outputOptions"
        @change="onOutputChange"
      >
        <template #first>
          <option :value="null">-- Select an output --</option>
        </template>
      </BFormSelect>
    </div>

    <div v-if="selectedOutput" class="selected-output-preview">
      <OutputPreview
        :output="selectedOutput"
        :invocation="selectedInvocation"
        :show-pending-warning="!isOutputAvailable"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from "vue";
import { BFormSelect } from "bootstrap-vue-next";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { useInvocationsStore } from "@/stores/invocationsStore";
import InvocationStateIcon from "@/components/WorkflowInvocationState/InvocationStateIcon.vue";
import OutputPreview from "./OutputPreview.vue";

interface Props {
  historyId: string;
  extensions?: string[];
  collectionTypes?: string[];
}

const props = defineProps<Props>();

const emit = defineEmits<{
  (e: "update:value", value: InvocationOutputSelection | null): void;
}>();

interface InvocationOutputSelection {
  src: "invocation_output" | "invocation_step_output";
  invocation_id: string;
  output_name?: string;
  step_id?: string;
}

const invocationsStore = useInvocationsStore();

const selectedInvocationId = ref<string | null>(null);
const selectedOutput = ref<OutputOption | null>(null);

const invocationOptions = computed(() => {
  return invocationsStore.getInvocationsForHistory(props.historyId).map(inv => ({
    value: inv.id,
    text: `${inv.workflow_name} (${formatDate(inv.create_time)}) - ${inv.state}`,
  }));
});

const selectedInvocation = computed(() => {
  if (!selectedInvocationId.value) return null;
  return invocationsStore.getInvocation(selectedInvocationId.value);
});

const isInvocationComplete = computed(() => {
  return selectedInvocation.value?.state === "scheduled" ||
         selectedInvocation.value?.state === "completed";
});

const availableOutputs = computed(() => {
  if (!selectedInvocation.value) return [];

  const outputs: OutputOption[] = [];

  // Add labeled workflow outputs
  for (const [label, output] of Object.entries(selectedInvocation.value.outputs || {})) {
    outputs.push({
      type: "workflow_output",
      label,
      output,
      available: output.id != null,
    });
  }

  // Add output collections
  for (const [label, output] of Object.entries(selectedInvocation.value.output_collections || {})) {
    outputs.push({
      type: "workflow_output_collection",
      label,
      output,
      available: output.id != null,
    });
  }

  return outputs;
});

const outputOptions = computed(() => {
  return availableOutputs.value.map(output => ({
    value: output,
    text: `${output.label}${output.available ? '' : ' (pending)'}`,
  }));
});

const isOutputAvailable = computed(() => {
  return selectedOutput.value?.available ?? false;
});

function onInvocationChange() {
  selectedOutput.value = null;
  emitValue();
}

function onOutputChange() {
  emitValue();
}

function emitValue() {
  if (!selectedInvocationId.value || !selectedOutput.value) {
    emit("update:value", null);
    return;
  }

  emit("update:value", {
    src: "invocation_output",
    invocation_id: selectedInvocationId.value,
    output_name: selectedOutput.value.label,
  });
}

function formatDate(dateStr: string): string {
  return new Date(dateStr).toLocaleString();
}

onMounted(async () => {
  // Load recent invocations for the current history
  await invocationsStore.fetchInvocationsForHistory(props.historyId);
});
</script>

<style scoped>
.invocation-info {
  font-size: 0.9rem;
}
.selected-output-preview {
  border: 1px solid var(--border-color);
  border-radius: 4px;
  padding: 1rem;
}
</style>
```

### 5.3 Update FormData Component

**File:** `client/src/components/Form/Elements/FormData/FormData.vue`

Add the invocation output tab to the data source tabs:

```vue
<template>
  <!-- Add new tab for invocation outputs -->
  <BTab
    v-if="allowInvocationOutputs"
    title="From Invocation"
    :title-link-class="tabTitleClass('invocation_output')"
  >
    <FormDataInvocationOutput
      :history-id="historyId"
      :extensions="extensions"
      :collection-types="collectionTypes"
      @update:value="onInvocationOutputSelect"
    />
  </BTab>
</template>

<script>
// Add to props
props: {
  // ... existing props
  allowInvocationOutputs: {
    type: Boolean,
    default: true,
  },
}
</script>
```

### 5.4 Workflow Run Form Updates

**File:** `client/src/components/Workflow/Run/WorkflowRunFormSimple.vue`

Update the form to support invocation output inputs:

```vue
<script setup>
// Add support for serializing invocation output references
function buildInvocationPayload() {
  const inputs = {};

  for (const [inputName, inputValue] of Object.entries(formData.value)) {
    if (inputValue?.src === "invocation_output" ||
        inputValue?.src === "invocation_step_output") {
      // Invocation output reference - pass through as-is
      inputs[inputName] = inputValue;
    } else {
      // Regular dataset/collection input
      inputs[inputName] = inputValue;
    }
  }

  return {
    // ... other payload fields
    inputs,
  };
}
</script>
```

### 5.5 Invocation Status Display

**File:** `client/src/components/WorkflowInvocationState/WorkflowInvocationState.vue`

Update to show waiting status:

```vue
<template>
  <div class="workflow-invocation-state">
    <span v-if="invocation.state === 'waiting_for_input'" class="state-waiting">
      <FontAwesomeIcon icon="clock" spin />
      Waiting for upstream invocation
      <BTooltip>
        This workflow is waiting for outputs from another workflow invocation
        to become available before it can proceed.
      </BTooltip>
    </span>
    <!-- ... other states ... -->
  </div>
</template>
```

### 5.6 Invocation Details Panel

**File:** `client/src/components/WorkflowInvocationState/WorkflowInvocationDetails.vue`

Add section showing input dependencies:

```vue
<template>
  <div v-if="invocation.input_dependencies?.length > 0" class="input-dependencies mt-3">
    <h5>Input Dependencies</h5>
    <BTable :items="dependencyItems" :fields="dependencyFields" small striped>
      <template #cell(source_invocation)="data">
        <RouterLink :to="invocationLink(data.item.source_invocation_id)">
          {{ data.item.source_workflow_name }}
        </RouterLink>
        <InvocationStateIcon :state="data.item.source_invocation_state" />
      </template>
      <template #cell(status)="data">
        <span v-if="data.item.resolved" class="text-success">
          <FontAwesomeIcon icon="check-circle" /> Resolved
        </span>
        <span v-else class="text-warning">
          <FontAwesomeIcon icon="clock" /> Pending
        </span>
      </template>
    </BTable>
  </div>
</template>
```

---

## 6. Test Plan

### 6.1 API Tests

**File:** `lib/galaxy_test/api/test_workflow_invocation_queuing.py`

```python
"""
Tests for workflow invocation queuing with dependencies on other invocations.
"""

from galaxy_test.api._framework import ApiTestCase
from galaxy_test.base.populators import DatasetPopulator, WorkflowPopulator


class TestWorkflowInvocationQueuing(ApiTestCase):
    """Test cases for queuing workflows with invocation output dependencies."""

    dataset_populator: DatasetPopulator
    workflow_populator: WorkflowPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)

    def test_invoke_with_invocation_output_reference(self):
        """Test invoking a workflow with an output from another invocation."""
        with self.dataset_populator.test_history() as history_id:
            # Create and run first workflow
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")
            hda = self.dataset_populator.new_dataset(history_id, content="test content")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Create second workflow and invoke with reference to first invocation's output
            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            # Invoke before first workflow completes
            invocation2_response = self.workflow_populator.invoke_workflow_raw(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            )

            self._assert_status_code_is(invocation2_response, 200)
            invocation2 = invocation2_response.json()

            # Verify invocation is in waiting state
            assert invocation2["state"] in ("new", "waiting_for_input", "ready")

            # Wait for first invocation to complete
            self.workflow_populator.wait_for_invocation(invocation1["id"])

            # Wait for second invocation to complete
            self.workflow_populator.wait_for_invocation(invocation2["id"])

            # Verify second invocation completed successfully
            final_state = self.workflow_populator.get_invocation(invocation2["id"])
            assert final_state["state"] == "scheduled"

    def test_invoke_with_step_output_reference(self):
        """Test invoking a workflow referencing a specific step output."""
        with self.dataset_populator.test_history() as history_id:
            # Run first workflow
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")
            hda = self.dataset_populator.new_dataset(history_id, content="test")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Get step ID from first invocation
            invocation1_details = self.workflow_populator.get_invocation(
                invocation1["id"],
                step_details=True
            )
            cat_step = next(
                s for s in invocation1_details["steps"]
                if s["workflow_step_label"] == "cat"
            )

            # Create and invoke second workflow
            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            invocation2 = self.workflow_populator.invoke_workflow(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_step_output",
                        "invocation_id": invocation1["id"],
                        "step_id": cat_step["workflow_step_id"],
                        "output_name": "out_file1",
                    }
                },
                history_id=history_id,
                wait=True,
            )

            assert invocation2["state"] == "scheduled"

    def test_invocation_fails_when_source_fails(self):
        """Test that dependent invocation fails when source invocation fails."""
        with self.dataset_populator.test_history() as history_id:
            # Create workflow that will fail
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: fail/out_file1
steps:
  fail:
    tool_id: exit_code_std
    tool_state:
      exit_code: 1
    in:
      input: input1
""")
            hda = self.dataset_populator.new_dataset(history_id, content="test")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Create dependent workflow
            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            invocation2 = self.workflow_populator.invoke_workflow_raw(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # Wait and check both invocations
            self.workflow_populator.wait_for_invocation(
                invocation1["id"],
                assert_ok=False
            )
            self.workflow_populator.wait_for_invocation(
                invocation2["id"],
                assert_ok=False
            )

            final_state = self.workflow_populator.get_invocation(invocation2["id"])
            assert final_state["state"] == "failed"

            # Check for failure message
            messages = final_state.get("messages", [])
            dep_failed_messages = [
                m for m in messages
                if m.get("reason") == "input_dependency_failed"
            ]
            assert len(dep_failed_messages) > 0

    def test_invocation_output_reference_invalid_output_name(self):
        """Test error handling for invalid output name reference."""
        with self.dataset_populator.test_history() as history_id:
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")
            hda = self.dataset_populator.new_dataset(history_id, content="test")
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            # Try to reference non-existent output
            response = self.workflow_populator.invoke_workflow_raw(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": invocation1["id"],
                        "output_name": "nonexistent_output",
                    }
                },
                history_id=history_id,
            )

            self._assert_status_code_is(response, 400)
            assert "not found" in response.json()["err_msg"].lower()

    def test_invocation_with_collection_output_reference(self):
        """Test referencing a collection output from another invocation."""
        with self.dataset_populator.test_history() as history_id:
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output_collection:
    outputSource: split/split_output
steps:
  split:
    tool_id: collection_split_on_column
    in:
      input1: input1
""")
            hda = self.dataset_populator.new_dataset(
                history_id,
                content="a\tb\nc\td\n"
            )
            invocation1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Workflow that consumes a collection
            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input_collection:
    type: collection
    collection_type: list
steps:
  process:
    tool_id: cat_collection
    in:
      input1: input_collection
""")

            invocation2 = self.workflow_populator.invoke_workflow(
                workflow2["id"],
                inputs={
                    "input_collection": {
                        "src": "invocation_output",
                        "invocation_id": invocation1["id"],
                        "output_name": "output_collection",
                    }
                },
                history_id=history_id,
                wait=True,
            )

            assert invocation2["state"] == "scheduled"

    def test_chained_invocations(self):
        """Test chaining multiple invocations together."""
        with self.dataset_populator.test_history() as history_id:
            # Create three identical workflows
            workflow_yaml = """
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
"""
            workflow1 = self._upload_yaml_workflow(workflow_yaml)
            workflow2 = self._upload_yaml_workflow(workflow_yaml)
            workflow3 = self._upload_yaml_workflow(workflow_yaml)

            # Start first workflow
            hda = self.dataset_populator.new_dataset(history_id, content="initial")
            inv1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Chain second workflow to first (before first completes)
            inv2 = self.workflow_populator.invoke_workflow_raw(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv1["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # Chain third workflow to second (before either completes)
            inv3 = self.workflow_populator.invoke_workflow_raw(
                workflow3["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv2["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # Wait for all to complete
            self.workflow_populator.wait_for_invocation(inv3["id"], timeout=120)

            # Verify all completed
            for inv_id in [inv1["id"], inv2["id"], inv3["id"]]:
                state = self.workflow_populator.get_invocation(inv_id)
                assert state["state"] == "scheduled"

    def test_input_dependencies_in_response(self):
        """Test that input dependencies are returned in invocation response."""
        with self.dataset_populator.test_history() as history_id:
            workflow1 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")
            hda = self.dataset_populator.new_dataset(history_id, content="test")
            inv1 = self.workflow_populator.invoke_workflow(
                workflow1["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            workflow2 = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            inv2 = self.workflow_populator.invoke_workflow_raw(
                workflow2["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv1["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # Check input_dependencies in response
            inv2_details = self.workflow_populator.get_invocation(inv2["id"])
            assert "input_dependencies" in inv2_details
            assert len(inv2_details["input_dependencies"]) == 1

            dep = inv2_details["input_dependencies"][0]
            assert dep["source_invocation_id"] == inv1["id"]
            assert dep["output_name"] == "output1"
```

### 6.2 Selenium/Playwright Tests

**File:** `lib/galaxy_test/selenium/test_workflow_invocation_queuing.py`

```python
"""
Selenium tests for workflow invocation queuing UI.
"""

from galaxy_test.base.workflow_fixtures import WORKFLOW_SIMPLE_CAT_TWICE
from .framework import (
    managed_history,
    selenium_test,
    SeleniumTestCase,
)


class TestWorkflowInvocationQueuingUI(SeleniumTestCase):
    """UI tests for selecting invocation outputs as workflow inputs."""

    ensure_registered = True

    @selenium_test
    @managed_history
    def test_invocation_output_tab_visible(self):
        """Test that the 'From Invocation' tab is visible in workflow run form."""
        # Upload a dataset and run a workflow first
        self.perform_upload(self.get_filename("1.fasta"))
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)

        # Verify the invocation output tab exists
        self.wait_for_selector_visible('[data-description="invocation output tab"]')

    @selenium_test
    @managed_history
    def test_select_invocation_output_as_input(self):
        """Test selecting an output from a previous invocation as input."""
        # Run first workflow
        self.perform_upload(self.get_filename("1.fasta"))
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)
        self.workflow_run_submit()
        self.workflow_run_wait_for_ok(hid=2)

        # Open workflow run form again
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)

        # Click on "From Invocation" tab
        self.click_selector('[data-description="invocation output tab"]')

        # Select the previous invocation
        invocation_select = self.wait_for_selector_visible(
            '[data-description="invocation selector"]'
        )
        self.select_option(invocation_select, index=0)  # Most recent invocation

        # Select output
        output_select = self.wait_for_selector_visible(
            '[data-description="invocation output selector"]'
        )
        self.select_option(output_select, text="output1")

        # Submit workflow
        self.workflow_run_submit()

        # Verify workflow was submitted (will see new invocation)
        self.wait_for_history_to_have_invocation()

    @selenium_test
    @managed_history
    def test_waiting_status_displayed(self):
        """Test that waiting status is displayed for queued invocations."""
        # This test runs a long-running workflow and immediately queues another
        # that depends on it, then verifies the UI shows waiting status

        self.perform_upload(self.get_filename("1.fasta"))

        # Run a workflow (simulating a slow one)
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)
        self.workflow_run_submit()

        # Immediately queue another workflow dependent on the first
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)
        self.click_selector('[data-description="invocation output tab"]')
        invocation_select = self.wait_for_selector_visible(
            '[data-description="invocation selector"]'
        )
        self.select_option(invocation_select, index=0)
        output_select = self.wait_for_selector_visible(
            '[data-description="invocation output selector"]'
        )
        self.select_option(output_select, text="output1")
        self.workflow_run_submit()

        # Check invocation list for waiting status
        self.navigate_to_invocations()

        # Look for waiting indicator
        self.wait_for_selector_visible('[data-state="waiting_for_input"]')

    @selenium_test
    @managed_history
    def test_invocation_details_shows_dependencies(self):
        """Test that invocation details page shows input dependencies."""
        # Setup and run chained workflows
        self.perform_upload(self.get_filename("1.fasta"))
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)
        self.workflow_run_submit()

        # Queue dependent workflow
        self.workflow_run_open_workflow(WORKFLOW_SIMPLE_CAT_TWICE)
        self.click_selector('[data-description="invocation output tab"]')
        invocation_select = self.wait_for_selector_visible(
            '[data-description="invocation selector"]'
        )
        self.select_option(invocation_select, index=0)
        output_select = self.wait_for_selector_visible(
            '[data-description="invocation output selector"]'
        )
        self.select_option(output_select, text="output1")
        self.workflow_run_submit()

        # Navigate to invocation details
        self.navigate_to_invocations()
        self.click_selector('[data-description="invocation-link"]:first-child')

        # Verify dependencies section is shown
        self.wait_for_selector_visible('[data-description="input-dependencies"]')

        # Verify source invocation link is present
        self.wait_for_selector_visible(
            '[data-description="source-invocation-link"]'
        )
```

### 6.3 Integration Tests

**File:** `lib/galaxy_test/api/test_workflow_invocation_queuing_integration.py`

```python
"""
Integration tests for workflow invocation queuing.
Tests realistic scenarios with actual workflow execution.
"""

from galaxy_test.api._framework import ApiTestCase
from galaxy_test.base.populators import DatasetPopulator, WorkflowPopulator


class TestWorkflowInvocationQueuingIntegration(ApiTestCase):
    """Integration tests for real-world queuing scenarios."""

    def test_parallel_workflows_with_shared_dependency(self):
        """Test multiple workflows depending on the same source invocation."""
        with self.dataset_populator.test_history() as history_id:
            # Source workflow
            source_workflow = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            hda = self.dataset_populator.new_dataset(history_id, content="shared")
            source_inv = self.workflow_populator.invoke_workflow(
                source_workflow["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Dependent workflows
            dep_workflow = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            # Queue multiple dependents
            dep_invs = []
            for i in range(3):
                inv = self.workflow_populator.invoke_workflow_raw(
                    dep_workflow["id"],
                    inputs={
                        "input1": {
                            "src": "invocation_output",
                            "invocation_id": source_inv["id"],
                            "output_name": "output1",
                        }
                    },
                    history_id=history_id,
                ).json()
                dep_invs.append(inv)

            # Wait for all to complete
            for inv in dep_invs:
                self.workflow_populator.wait_for_invocation(inv["id"])
                state = self.workflow_populator.get_invocation(inv["id"])
                assert state["state"] == "scheduled"

    def test_complex_dag_of_invocations(self):
        """
        Test a DAG structure of dependent invocations:

            A
           / \
          B   C
           \ /
            D
        """
        with self.dataset_populator.test_history() as history_id:
            workflow = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: cat/out_file1
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            workflow_two_inputs = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
  input2: data
outputs:
  output1:
    outputSource: cat_list/out_file1
steps:
  cat_list:
    tool_id: cat_list
    in:
      input1:
        - input1
        - input2
""")

            # A: Initial workflow
            hda = self.dataset_populator.new_dataset(history_id, content="root")
            inv_a = self.workflow_populator.invoke_workflow(
                workflow["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # B and C: Depend on A
            inv_b = self.workflow_populator.invoke_workflow_raw(
                workflow["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv_a["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            inv_c = self.workflow_populator.invoke_workflow_raw(
                workflow["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv_a["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # D: Depends on both B and C
            inv_d = self.workflow_populator.invoke_workflow_raw(
                workflow_two_inputs["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": inv_b["id"],
                        "output_name": "output1",
                    },
                    "input2": {
                        "src": "invocation_output",
                        "invocation_id": inv_c["id"],
                        "output_name": "output1",
                    },
                },
                history_id=history_id,
            ).json()

            # Wait for D to complete (should cascade wait for all)
            self.workflow_populator.wait_for_invocation(inv_d["id"], timeout=180)

            # Verify all completed
            for inv_id in [inv_a["id"], inv_b["id"], inv_c["id"], inv_d["id"]]:
                state = self.workflow_populator.get_invocation(inv_id)
                assert state["state"] == "scheduled"

    def test_cancellation_propagation(self):
        """Test that cancelling a source invocation affects dependents."""
        with self.dataset_populator.test_history() as history_id:
            # Long-running workflow
            workflow = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
outputs:
  output1:
    outputSource: sleep/output
steps:
  sleep:
    tool_id: __SLEEP__
    tool_state:
      sleep_time: 30
    in:
      input: input1
""")

            hda = self.dataset_populator.new_dataset(history_id, content="test")
            source_inv = self.workflow_populator.invoke_workflow(
                workflow["id"],
                inputs={"input1": {"src": "hda", "id": hda["id"]}},
                history_id=history_id,
            )

            # Queue dependent
            dep_workflow = self._upload_yaml_workflow("""
class: GalaxyWorkflow
inputs:
  input1: data
steps:
  cat:
    tool_id: cat1
    in:
      input1: input1
""")

            dep_inv = self.workflow_populator.invoke_workflow_raw(
                dep_workflow["id"],
                inputs={
                    "input1": {
                        "src": "invocation_output",
                        "invocation_id": source_inv["id"],
                        "output_name": "output1",
                    }
                },
                history_id=history_id,
            ).json()

            # Cancel source invocation
            self._delete(f"invocations/{source_inv['id']}")

            # Wait and check dependent failed/cancelled
            self.workflow_populator.wait_for_invocation(
                dep_inv["id"],
                assert_ok=False
            )

            state = self.workflow_populator.get_invocation(dep_inv["id"])
            assert state["state"] in ("failed", "cancelled")
```

---

## 7. Implementation Order

### Phase 1: Backend Foundation
1. Create database migration for `workflow_invocation_input_dependency` table
2. Add ORM model and relationships
3. Update schema with new input types and invocation state

### Phase 2: Core Logic
4. Implement input reference resolution in `run_request.py`
5. Update scheduler to handle `WAITING_FOR_INPUT` state
6. Implement dependency resolution logic in `scheduling_manager.py`

### Phase 3: API Updates
7. Update invocation serialization to include dependencies
8. Add new message types for dependency status
9. Update API documentation

### Phase 4: Frontend
10. Create `FormDataInvocationOutput.vue` component
11. Update `FormData.vue` to include invocation output tab
12. Update workflow run form to serialize new input types
13. Update invocation status display components
14. Add dependencies section to invocation details

### Phase 5: Testing
15. Implement API tests
16. Implement Selenium/Playwright tests
17. Implement integration tests

### Phase 6: Documentation
18. Update API documentation
19. Add user documentation for the feature
20. Update developer documentation

---

## 8. Considerations and Edge Cases

### 8.1 Access Control
- Users can only reference invocations they have access to
- Verify history/invocation ownership during resolution

### 8.2 Cross-History Dependencies
- Should dependencies work across histories?
- If yes, need to copy/reference datasets appropriately

### 8.3 Cycle Detection
- Prevent circular dependencies between invocations
- Validate dependency graph before accepting invocation

### 8.4 Performance
- Index foreign keys for efficient dependency queries
- Consider batching dependency resolution checks

### 8.5 UI/UX
- Clear indication of pending vs available outputs
- Show estimated wait time if possible
- Allow filtering invocations by workflow/status in selector

### 8.6 Cleanup
- Handle orphaned dependencies when invocations are deleted
- Consider cascade delete behavior
