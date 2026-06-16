# Performance benchmarks

Profileable benchmarks for diagnosing slow endpoints.

## Workflow Run form (`GET /api/workflows/{id}/download?style=run`)

`test_workflow_run_form_performance.py` boots a framework Galaxy, builds a
size-controllable workflow, times the `style=run` download, and dumps a
**server-side cProfile** of `WorkflowContentsManager._workflow_to_dict_run`
(see issue #22927 — "Loading workflow run data" taking minutes).

```bash
# sanity run (small, fast)
./run_tests.sh -api lib/galaxy_test/performance/test_workflow_run_form_performance.py

# scaling sweep — compare DEPTH 5 / 20 / 50 and read the cumulative table
GALAXY_TEST_RUNFORM_DEPTH=50 \
GALAXY_TEST_RUNFORM_DATA_INPUTS=10 \
GALAXY_TEST_RUNFORM_DISTINCT_TOOLS=1 \
GALAXY_TEST_PERFORMANCE_TIMEOUT=600000 \
./run_tests.sh -api lib/galaxy_test/performance/test_workflow_run_form_performance.py

# history-independence check (issue says size doesn't matter): 0 vs 200
GALAXY_TEST_RUNFORM_HISTORY_ITEMS=200 ./run_tests.sh -api \
    lib/galaxy_test/performance/test_workflow_run_form_performance.py
```

`.pstats` files land in `GALAXY_TEST_PROFILE_OUTPUT_DIR` (default
`run_form_profiles/`); inspect interactively with:

```bash
python -m pstats run_form_profiles/<label>.pstats   # then: sort cumulative / stats 40
# or snakeviz run_form_profiles/<label>.pstats
```

### Datatypes-registry micro-benchmark (no server)

`scripts/benchmarks/bench_acceptable_extensions.py` isolates the registry work the
run form performs per `data` input (`_acceptable_extensions` ->
`find_conversion_destination_for_dataset_by_extensions`). Useful to rule the
registry in/out and to see how it scales as the converter graph grows:

```bash
PYTHONPATH=lib python scripts/benchmarks/bench_acceptable_extensions.py
PYTHONPATH=lib python scripts/benchmarks/bench_acceptable_extensions.py \
    --extra-datatypes 5000 --extra-converters-per-type 4 --profile
```

## Profiling a live / production Galaxy

The default framework toolbox is small. The minutes-long behavior on
usegalaxy.org / usegalaxy.eu depends on the production toolbox + datatypes
registry, so capture a profile there too.

### Sampling (recommended — no code change, safe in production)

[`py-spy`](https://github.com/benfred/py-spy) attaches to a running worker and
samples the stack; ideal for a process that is *stuck* for minutes:

```bash
pip install py-spy
# find a Galaxy gunicorn/uvicorn worker PID, then while a user loads the Run form:
py-spy record -o runform.svg --pid <worker_pid> --duration 60 --subprocesses
# instantaneous snapshot of what every thread is doing right now:
py-spy dump --pid <worker_pid>
```

[`austin`](https://github.com/P403n1x87/austin) is an alternative sampler with the
same workflow.

### In-request profiling

- `pyinstrument` can wrap the ASGI app to emit a per-request flame graph
  (statistical, low overhead).
- The bundled cProfile `ProfileMiddleware`
  (`lib/galaxy/web/framework/middleware/profile.py`) is **not** wired into the
  default ASGI stack, so prefer the samplers above for production; use it only in a
  dev instance where you can add it to the middleware stack.

### What to look for

In the cumulative-time table / flame graph, attribute time within
`_workflow_to_dict_run` across:

- `Tool.to_json` (per tool step — built fresh every request),
- `WorkflowModuleInjector.inject_all` / `compute_runtime_state`,
- datatypes-registry calls (`get_converters_by_datatype`,
  `find_conversion_destination_for_dataset_by_extensions`),
- the data-parameter option/initial-value building.
