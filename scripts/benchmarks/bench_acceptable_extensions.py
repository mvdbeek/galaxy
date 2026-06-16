#!/usr/bin/env python
"""Standalone micro-benchmark for the datatypes-registry work performed while
building the workflow *Run* form (issue #22927).

The run form's ``data`` / ``data_collection`` inputs compute an "acceptable
extensions" set (formats union implicit-conversion sources) via
``BaseDataToolParameter._acceptable_extensions``
(``lib/galaxy/tools/parameters/basic.py``), which loops over *every* extension in
the datatypes registry calling
``Registry.find_conversion_destination_for_dataset_by_extensions``
(``lib/galaxy/datatypes/registry.py``).

This script loads a *real* datatypes registry (no DB / web server needed) and
times that exact work, so we can cheaply rule the registry in or out as the cause
of the "Loading workflow run data" slowness, and see how it scales as the registry
grows toward production size (usegalaxy.org/.eu install many tool-shed datatypes
and converters).

Run (from the Galaxy root, with the venv active)::

    PYTHONPATH=lib python scripts/benchmarks/bench_acceptable_extensions.py
    PYTHONPATH=lib python scripts/benchmarks/bench_acceptable_extensions.py \
        --extra-datatypes 4000 --extra-converters-per-type 4 --profile

``--extra-datatypes`` / ``--extra-converters-per-type`` synthetically inflate the
registry to probe scaling without a production instance.
"""

import argparse
import cProfile
import os
import pstats
import sys
import time
from statistics import median

# Allow running directly from a source checkout without installing galaxy.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "lib"))

from galaxy.datatypes.registry import Registry  # noqa: E402

DEFAULT_CONFIG = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
    "lib",
    "galaxy",
    "config",
    "sample",
    "datatypes_conf.xml.sample",
)

# Formats representative of common workflow data inputs (broad -> narrow).
SAMPLE_FORMATS = [
    ["data"],
    ["tabular"],
    ["txt"],
    ["fastqsanger"],
    ["bam"],
    ["vcf"],
    ["tabular", "txt", "interval"],
]


def load_registry(config: str) -> Registry:
    registry = Registry()
    registry.load_datatypes(root_dir=".", config=config)
    return registry


def inflate_registry(registry: Registry, extra_datatypes: int, extra_converters_per_type: int) -> None:
    """Synthetically grow the registry to probe scaling.

    New extensions reuse an existing datatype *instance* (so ``matches_any`` /
    ``issubclass`` keep working) and optionally get synthetic converter targets,
    expanding both ``datatypes_by_extension`` and ``datatype_converters`` the way a
    large tool-shed install would.
    """
    if extra_datatypes <= 0:
        return
    base_instance = registry.get_datatype_by_extension("tabular") or registry.get_datatype_by_extension("data")
    existing_targets = list(registry.datatypes_by_extension.keys())
    new_exts = []
    for i in range(extra_datatypes):
        ext = f"synthetic_ext_{i}"
        registry.datatypes_by_extension[ext] = base_instance
        new_exts.append(ext)
    # Clear the memoized converter cache so freshly added extensions are considered.
    registry._converters_by_datatype = {}
    if extra_converters_per_type > 0:
        for ext in new_exts:
            targets = {}
            for j in range(extra_converters_per_type):
                target = existing_targets[(hash(ext) + j) % len(existing_targets)]
                targets[target] = ("synthetic_converter.xml", {})
            registry.datatype_converters[ext] = targets


def acceptable_extensions(registry: Registry, formats):
    """Replicates ``BaseDataToolParameter._acceptable_extensions`` without needing
    a constructed tool parameter instance."""
    accepted = set(formats)
    for ext in list(registry.datatypes_by_extension.keys()):
        if ext in accepted:
            continue
        direct, converted, _ = registry.find_conversion_destination_for_dataset_by_extensions(ext, formats)
        if direct or converted:
            accepted.add(ext)
    return accepted


def time_call(fn, repeats):
    timings = []
    result = None
    for _ in range(repeats):
        t0 = time.perf_counter()
        result = fn()
        timings.append((time.perf_counter() - t0) * 1000.0)
    return result, timings


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="datatypes_conf.xml to load")
    parser.add_argument("--extra-datatypes", type=int, default=0, help="synthetic extra extensions to register")
    parser.add_argument(
        "--extra-converters-per-type", type=int, default=0, help="synthetic converters per added extension"
    )
    parser.add_argument("--repeats", type=int, default=5, help="timed repeats per format set")
    parser.add_argument("--profile", action="store_true", help="dump a cProfile of one cold + warm pass")
    args = parser.parse_args()

    t0 = time.perf_counter()
    registry = load_registry(args.config)
    load_ms = (time.perf_counter() - t0) * 1000.0
    inflate_registry(registry, args.extra_datatypes, args.extra_converters_per_type)
    num_exts = len(registry.datatypes_by_extension)

    print(f"loaded {args.config} in {load_ms:.0f} ms")
    print(f"registry extensions: {num_exts}")
    print(f"datatype_converters entries: {len(registry.datatype_converters)}")
    print()
    print(f"{'formats':<32}{'cold (ms)':>12}{'warm median (ms)':>20}{'accepted':>12}")
    print("-" * 76)

    profiler = cProfile.Profile() if args.profile else None
    for formats in SAMPLE_FORMATS:
        # Each call recomputes from scratch (mirrors a fresh per-request param
        # instance); the registry-level converter cache persists between calls.
        if profiler is not None:
            profiler.enable()
        accepted, timings = time_call(lambda formats=formats: acceptable_extensions(registry, formats), args.repeats)
        if profiler is not None:
            profiler.disable()
        cold = timings[0]
        warm = median(timings[1:]) if len(timings) > 1 else timings[0]
        print(f"{','.join(formats):<32}{cold:>12.1f}{warm:>20.1f}{len(accepted):>12}")

    if profiler is not None:
        print()
        print("=== cProfile (cumulative, top 25) ===")
        pstats.Stats(profiler).sort_stats("cumulative").print_stats(25)


if __name__ == "__main__":
    main()
