#!/usr/bin/env python
"""Summarize where integration test time goes.

Integration tests build a Galaxy application per test class, so most of the suite's
runtime is instance startup and teardown rather than the test bodies. This reports
that split from either of two sources:

``summarize_test_timings.py timings.jsonl``
    Records written by ``lib/galaxy_test/driver/timing.py`` when a run sets
    ``GALAXY_TEST_TIMING_FILE``. Gives the per-phase breakdown of every launch.

``summarize_test_timings.py --ci-log job.log``
    Raw GitHub Actions logs (``gh run view --job=<id> --log``). No instrumentation
    needed, so this works on runs that predate it, but timings are inferred from the
    interval between reported test results and are therefore coarse.

Pass ``--json-report`` alongside either to add per-test durations from a run that
used ``--structured_data_report_file``.
"""

import argparse
import json
import os
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from typing import Any

CI_TIMESTAMP = re.compile(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{6})\d*Z")
CI_TEST_RESULT = re.compile(
    r"(test/\S+\.py)::(\S+?)\s+(?:<- \S+\s+)?(PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)",
)


def parse_timing_records(paths: list[str]) -> list[dict[str, Any]]:
    records = []
    for path in paths:
        with open(path) as fh:
            for line_number, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"{path}:{line_number}: skipping unparseable record", file=sys.stderr)
    return records


def summarize_timing_records(records: list[dict[str, Any]]) -> None:
    startups = [r for r in records if r["kind"] in ("startup", "restart")]
    teardowns = [r for r in records if r["kind"] == "teardown"]
    if not startups:
        print("No startup records found.")
        return

    startup_total = sum(r["total"] for r in startups)
    teardown_total = sum(r["total"] for r in teardowns)
    print(f"{len(startups)} instance launches, {len(teardowns)} teardowns")
    print(f"  startup  {startup_total / 60:7.1f}m  {_distribution([r['total'] for r in startups])}")
    if teardowns:
        print(f"  teardown {teardown_total / 60:7.1f}m  {_distribution([r['total'] for r in teardowns])}")
    print(f"  combined {(startup_total + teardown_total) / 60:7.1f}m")

    _print_phase_totals("startup phases", startups)
    _print_phase_totals("teardown phases", teardowns)
    _print_app_stage_totals("application startup stages", startups, "app_startup_stages")
    _print_app_stage_totals("application shutdown stages", teardowns, "app_shutdown_stages")
    _print_slowest_launches(startups)
    _print_shareable_instances(startups)


def _distribution(values: list[float]) -> str:
    ordered = sorted(values)
    p90 = ordered[min(int(0.9 * len(ordered)), len(ordered) - 1)]
    return f"mean {statistics.mean(values):5.1f}s  median {statistics.median(values):5.1f}s  p90 {p90:5.1f}s"


def _print_phase_totals(title: str, records: list[dict[str, Any]]) -> None:
    if not records:
        return
    totals: dict[str, float] = defaultdict(float)
    for record in records:
        for name, seconds in record.get("phases", {}).items():
            totals[name] += seconds
    print(f"\n{title} (phases nest, so they do not sum to the total):")
    for name, seconds in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"  {seconds / 60:7.1f}m  mean {seconds / len(records):6.2f}s  {name}")


def _print_app_stage_totals(title: str, records: list[dict[str, Any]], field: str) -> None:
    totals: dict[str, float] = defaultdict(float)
    counted = 0
    for record in records:
        stages = record.get(field)
        if not stages:
            continue
        counted += 1
        for name, seconds in stages.items():
            totals[name] += seconds
    if not counted:
        return
    print(f"\n{title} ({counted} records):")
    for name, seconds in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"  {seconds / 60:7.1f}m  mean {seconds / counted:6.2f}s  {name}")


def _print_slowest_launches(startups: list[dict[str, Any]], limit: int = 15) -> None:
    print(f"\nslowest {limit} launches:")
    for record in sorted(startups, key=lambda r: r["total"], reverse=True)[:limit]:
        cache = record.get("fast_app_cache", "?")
        print(f"  {record['total']:7.1f}s  fast_app={cache:16s}  {record.get('instance', '?')}")


def _print_shareable_instances(startups: list[dict[str, Any]]) -> None:
    """Instances configured identically could in principle share one application."""
    by_fingerprint: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in startups:
        fingerprint = record.get("config_fingerprint")
        if fingerprint and fingerprint != "none":
            by_fingerprint[fingerprint].append(record)
    if not by_fingerprint:
        return
    shared = {f: rs for f, rs in by_fingerprint.items() if len(rs) > 1}
    redundant = sum(sum(r["total"] for r in rs[1:]) for rs in shared.values())
    print(f"\n{len(by_fingerprint)} distinct configs across {len(startups)} launches")
    print(f"  {len(shared)} configs are launched more than once, costing {redundant / 60:.1f}m in repeat launches")
    for fingerprint, records in sorted(shared.items(), key=lambda item: len(item[1]), reverse=True)[:10]:
        instances = ", ".join(sorted({r.get("instance", "?") for r in records}))
        print(f"  {len(records):3d}x {fingerprint}  {instances[:110]}")


def parse_ci_logs(paths: list[str]) -> dict[tuple[str, str, str], list[float]]:
    """Infer per-test timings from GitHub Actions logs, keyed by (log, file, class).

    Each reported test result carries a timestamp, so the interval since the previous
    result approximates that test's duration - including whatever setup ran first. The
    first test of a class therefore absorbs that class's instance startup, which is what
    makes the boot cost visible without any instrumentation.
    """
    groups: dict[tuple[str, str, str], list[float]] = {}
    for path in paths:
        previous = None
        for line in open(path, errors="replace"):
            match = CI_TIMESTAMP.search(line)
            if not match:
                continue
            timestamp = datetime.strptime(match.group(1), "%Y-%m-%dT%H:%M:%S.%f")
            if "test session starts" in line:
                previous = timestamp
            result = CI_TEST_RESULT.search(line)
            if result and previous is not None:
                duration = (timestamp - previous).total_seconds()
                previous = timestamp
                node_id = result.group(2)
                class_name = node_id.split("::")[0] if "::" in node_id else "<module>"
                groups.setdefault((path, result.group(1), class_name), []).append(duration)
    return groups


def shard_group_key(test_file: str, class_name: str) -> str:
    """Build the key ``galaxy_test.shard`` uses: the test's module name, then its class."""
    module = test_file.removeprefix("test/").removesuffix(".py").replace("/", ".")
    return module if class_name == "<module>" else f"{module}::{class_name}"


def write_shard_durations(groups: dict[tuple[str, str, str], list[float]], path: str) -> None:
    """Record what each group would cost run in one place, for duration-weighted packing.

    Hash sharding splits a group across shards and each slice pays a full instance
    startup, so the slices summed overstate the group. Estimate what one shard would spend
    on the whole group by charging that startup once instead of once per slice.
    """
    observed: dict[str, list[list[float]]] = defaultdict(list)
    for (_, test_file, class_name), values in groups.items():
        observed[shard_group_key(test_file, class_name)].append(values)

    durations = {}
    for key, slices in observed.items():
        overheads = [_boot_overhead(values) for values in slices]
        redundant_boots = (len(slices) - 1) * statistics.mean(overheads)
        durations[key] = round(max(sum(sum(values) for values in slices) - redundant_boots, 0.1), 1)

    with open(path, "w") as fh:
        json.dump(dict(sorted(durations.items())), fh, indent=2)
        fh.write("\n")
    print(f"\nwrote {len(durations)} group durations to {path}")


def _boot_overhead(durations: list[float]) -> float:
    """Estimate the instance startup absorbed by a group's first test.

    Sibling tests run against the already-booted instance, so their median is the best
    available estimate of what the first test would have cost without the boot.
    """
    baseline = statistics.median(durations[1:]) if len(durations) > 1 else 0.0
    return max(durations[0] - baseline, 0.0)


def summarize_ci_logs(paths: list[str], durations_out: str | None = None) -> None:
    groups = parse_ci_logs(paths)
    if not groups:
        print("No test results found in the supplied logs.")
        return

    total = sum(sum(durations) for durations in groups.values())
    tests = sum(len(durations) for durations in groups.values())
    overheads = [_boot_overhead(durations) for durations in groups.values()]
    overhead = sum(overheads)
    unique_classes = len({(f, c) for _, f, c in groups})

    print(f"{tests} tests over {total / 60:.0f}m in {len(paths)} log(s)")
    print(f"instance boots: {len(groups)} for {unique_classes} distinct classes ({len(groups) / unique_classes:.2f}x)")
    print(f"estimated boot + teardown cost: {overhead / 60:.0f}m ({overhead / total * 100:.0f}% of run time)")
    print(f"  per boot: {_distribution(overheads)}")
    single = [g for g, durations in groups.items() if len(durations) == 1]
    print(f"boots serving a single test: {len(single)}")

    print("\nslowest 20 test files:")
    per_file: dict[str, float] = defaultdict(float)
    per_file_count: dict[str, int] = defaultdict(int)
    for (_, test_file, _), durations in groups.items():
        per_file[test_file] += sum(durations)
        per_file_count[test_file] += len(durations)
    for test_file, seconds in sorted(per_file.items(), key=lambda item: item[1], reverse=True)[:20]:
        count = per_file_count[test_file]
        print(f"  {seconds / 60:7.1f}m  n={count:4d}  mean={seconds / count:6.1f}s  {test_file}")

    if durations_out:
        write_shard_durations(groups, durations_out)


def summarize_json_report(path: str) -> None:
    with open(path) as fh:
        report = json.load(fh)
    tests = report.get("tests", [])
    if not tests:
        print("\nNo tests in JSON report.")
        return
    # Setup is where a test class's Galaxy instance is built, so it is the phase that
    # matters most here - reporting the call phase alone would hide the boot cost.
    durations = []
    for test in tests:
        phases = {phase: test.get(phase, {}).get("duration", 0.0) for phase in ("setup", "call", "teardown")}
        durations.append((sum(phases.values()), phases, test["nodeid"]))
    total = sum(d for d, _, _ in durations)
    setup_total = sum(p["setup"] for _, p, _ in durations)
    teardown_total = sum(p["teardown"] for _, p, _ in durations)
    print(f"\n{len(durations)} tests in JSON report, {total / 60:.1f}m total")
    print(f"  setup    {setup_total / 60:7.1f}m ({setup_total / total * 100:.0f}%)")
    print(f"  call     {(total - setup_total - teardown_total) / 60:7.1f}m")
    print(f"  teardown {teardown_total / 60:7.1f}m ({teardown_total / total * 100:.0f}%)")
    print("slowest 20 tests:")
    for duration, phases, node_id in sorted(durations, key=lambda item: item[0], reverse=True)[:20]:
        detail = " ".join(f"{phase}={seconds:.1f}s" for phase, seconds in phases.items() if seconds >= 0.05)
        print(f"  {duration:7.1f}s  {node_id}  [{detail}]")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("timing_files", nargs="*", help="JSONL files written via GALAXY_TEST_TIMING_FILE")
    parser.add_argument("--ci-log", action="append", default=[], help="raw GitHub Actions job log to analyze instead")
    parser.add_argument("--json-report", help="pytest-json-report output to add per-test durations from")
    parser.add_argument(
        "--write-shard-durations",
        metavar="PATH",
        help="write per-group durations for lib/galaxy_test/shard_durations.json (requires --ci-log)",
    )
    args = parser.parse_args()

    if args.write_shard_durations and not args.ci_log:
        parser.error("--write-shard-durations needs --ci-log to measure from")

    if not args.timing_files and not args.ci_log:
        parser.error("supply at least one timing file or --ci-log")

    for path in args.timing_files + args.ci_log + ([args.json_report] if args.json_report else []):
        if not os.path.exists(path):
            parser.error(f"no such file: {path}")

    if args.timing_files:
        summarize_timing_records(parse_timing_records(args.timing_files))
    if args.ci_log:
        if args.timing_files:
            print()
        summarize_ci_logs(args.ci_log, args.write_shard_durations)
    if args.json_report:
        summarize_json_report(args.json_report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
