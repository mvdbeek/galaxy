"""Profileable benchmark for the workflow *Run* form endpoint (issue #22927).

The Run interface ("Loading workflow run data") is bound to a single request:
``GET /api/workflows/{id}/download?style=run`` -> ``WorkflowContentsManager._workflow_to_dict_run``
(``lib/galaxy/managers/workflows.py``). In 26.1 this can take *minutes*, independent
of history size. This test boots a real (framework) Galaxy, builds a workflow whose
size is controllable, and:

* times the end-to-end ``style=run`` HTTP download, and
* captures a **server-side cProfile** of ``_workflow_to_dict_run`` by monkeypatching
  it on the in-process app for the duration of the request (see ``MethodProfiler``),

so the slow region can be *seen* in the cumulative-time table rather than guessed.

Scaling knobs (env vars), all default small so the standard suite stays fast::

    GALAXY_TEST_RUNFORM_DEPTH=50          # extra chained tool steps
    GALAXY_TEST_RUNFORM_DATA_INPUTS=10    # number of data input steps
    GALAXY_TEST_RUNFORM_DISTINCT_TOOLS=1  # cycle distinct tools across data-input steps
    GALAXY_TEST_RUNFORM_HISTORY_ITEMS=0   # datasets to add (probe history-independence)
    GALAXY_TEST_RUNFORM_REPEATS=3         # timed HTTP repeats
    GALAXY_TEST_PERFORMANCE_TIMEOUT=5000  # ms; soft assertion on median

Run::

    ./run_tests.sh -api lib/galaxy_test/performance/test_workflow_run_form_performance.py
"""

import os
from statistics import median

from galaxy_test.base.populators import (
    DatasetPopulator,
    WorkflowPopulator,
)
from ._framework import PerformanceTestCase
from ._profiling import MethodProfiler

RUNFORM_DEPTH = int(os.environ.get("GALAXY_TEST_RUNFORM_DEPTH", "5"))
RUNFORM_DATA_INPUTS = int(os.environ.get("GALAXY_TEST_RUNFORM_DATA_INPUTS", "3"))
RUNFORM_DISTINCT_TOOLS = os.environ.get("GALAXY_TEST_RUNFORM_DISTINCT_TOOLS", "0") not in ("0", "", "false")
RUNFORM_HISTORY_ITEMS = int(os.environ.get("GALAXY_TEST_RUNFORM_HISTORY_ITEMS", "0"))
RUNFORM_REPEATS = int(os.environ.get("GALAXY_TEST_RUNFORM_REPEATS", "3"))
PERFORMANCE_TIMEOUT = int(os.environ.get("GALAXY_TEST_PERFORMANCE_TIMEOUT", "5000"))

# Framework tools that take a single ``input1`` data parameter and emit ``out_file1``.
# Filtered against the live toolbox at runtime; falls back to ``cat1`` only.
CANDIDATE_DATA_TOOLS = ["cat1", "cat", "head", "tail", "wc_gnu"]


class TestWorkflowRunFormPerformance(PerformanceTestCase):
    framework_tool_and_types = True

    def setUp(self):
        super().setUp()
        self.workflow_populator = WorkflowPopulator(self.galaxy_interactor)
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

    def _galaxy_app(self):
        """Return the in-process app object for embedded servers, else ``None``."""
        driver = self._test_driver
        wrappers = getattr(driver, "server_wrappers", None) if driver else None
        if not wrappers:
            return None
        try:
            return wrappers[0].app
        except (IndexError, NotImplementedError):
            return None

    def _data_tools(self):
        app = self._galaxy_app()
        if not (RUNFORM_DISTINCT_TOOLS and app is not None):
            return ["cat1"]
        available = [tid for tid in CANDIDATE_DATA_TOOLS if app.toolbox.has_tool(tid)]
        return available or ["cat1"]

    def _build_workflow_yaml(self):
        tools = self._data_tools()
        num_inputs = max(RUNFORM_DATA_INPUTS, 1)
        lines = ["class: GalaxyWorkflow", "inputs:"]
        for i in range(num_inputs):
            lines.append(f"  in_{i}: data")
        lines.append("steps:")
        # One tool step per data input.
        for i in range(num_inputs):
            tool = tools[i % len(tools)]
            lines.append(f"  step_{i}:")
            lines.append(f"    tool_id: {tool}")
            lines.append("    in:")
            lines.append(f"      input1: in_{i}")
        # Chain extra cat1 steps off the first input's step to scale step count.
        prev = "step_0"
        for j in range(RUNFORM_DEPTH):
            label = f"chain_{j}"
            lines.append(f"  {label}:")
            lines.append("    tool_id: cat1")
            lines.append("    in:")
            lines.append(f"      input1: {prev}/out_file1")
            prev = label
        return "\n".join(lines) + "\n"

    def _populate_history(self, history_id, count):
        for i in range(count):
            self.dataset_populator.new_dataset(history_id, content=f"line {i}\n", wait=False)
        if count:
            self.dataset_populator.wait_for_history(history_id)

    def test_run_form_download(self):
        workflow_yaml = self._build_workflow_yaml()
        workflow_id = self.workflow_populator.upload_yaml_workflow(workflow_yaml)
        history_id = self.dataset_populator.new_history()
        self._populate_history(history_id, RUNFORM_HISTORY_ITEMS)

        num_steps = max(RUNFORM_DATA_INPUTS, 1) + RUNFORM_DEPTH
        label = f"runform_steps{num_steps}_inputs{RUNFORM_DATA_INPUTS}_hist{RUNFORM_HISTORY_ITEMS}"
        print(
            f"\n[run-form benchmark] steps={num_steps} data_inputs={RUNFORM_DATA_INPUTS} "
            f"distinct_tools={self._data_tools()} history_items={RUNFORM_HISTORY_ITEMS} repeats={RUNFORM_REPEATS}"
        )

        app = self._galaxy_app()
        timings_ms = []

        def _download_all():
            for _ in range(RUNFORM_REPEATS):
                import time

                t0 = time.perf_counter()
                run_data = self.workflow_populator.download_workflow(workflow_id, style="run", history_id=history_id)
                timings_ms.append((time.perf_counter() - t0) * 1000.0)
                assert run_data.get("steps"), "run-form download returned no steps"

        if app is not None:
            # Profile the genuine server-side handler with its real trans/toolbox.
            with MethodProfiler(app.workflow_contents_manager, "_workflow_to_dict_run", label) as prof:
                _download_all()
            print(
                f"[run-form benchmark] server-side _workflow_to_dict_run: "
                f"{prof.call_count} calls, {prof.wall_seconds * 1000.0:.1f} ms total"
            )
        else:
            # External target: only end-to-end timing is available.
            print("[run-form benchmark] no in-process app; skipping server-side cProfile")
            _download_all()

        med = median(timings_ms)
        print(
            f"[run-form benchmark] HTTP style=run download: "
            f"min={min(timings_ms):.1f} median={med:.1f} max={max(timings_ms):.1f} ms"
        )
        # Soft assertion: keep the default (small) configuration under the timeout.
        # Scaling sweeps are expected to exceed this and surface the hotspot in the
        # cProfile table -- raise the timeout via env when sweeping.
        assert med < PERFORMANCE_TIMEOUT, f"style=run median {med:.0f} ms exceeded {PERFORMANCE_TIMEOUT} ms"
