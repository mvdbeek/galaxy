"""Profiling helpers shared by the performance tests.

These wrap a callable (typically an in-process server-side method such as
``WorkflowContentsManager._workflow_to_dict_run``) in ``cProfile`` and persist a
``.pstats`` file plus a printed cumulative-time table, so a slow endpoint can be
diagnosed by *where* the time goes rather than guessed at.
"""

import cProfile
import io
import os
import pstats
import time
from collections.abc import Callable
from contextlib import contextmanager
from typing import Optional

DEFAULT_PROFILE_DIR = os.environ.get("GALAXY_TEST_PROFILE_OUTPUT_DIR", "run_form_profiles")
PROFILE_TOP_N = int(os.environ.get("GALAXY_TEST_PROFILE_TOP_N", "40"))


def profile_output_dir() -> str:
    os.makedirs(DEFAULT_PROFILE_DIR, exist_ok=True)
    return DEFAULT_PROFILE_DIR


def dump_stats(profiler: cProfile.Profile, label: str, top_n: int = PROFILE_TOP_N) -> str:
    """Write a ``.pstats`` file for ``profiler`` and print/return the top-N
    cumulative-time table. Returns the printed table for assertions/logging."""
    out_dir = profile_output_dir()
    pstats_path = os.path.join(out_dir, f"{label}.pstats")
    profiler.dump_stats(pstats_path)

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(top_n)
    table = stream.getvalue()

    print(f"\n=== cProfile [{label}] -> {pstats_path} (cumulative, top {top_n}) ===")
    print(table)
    return table


class MethodProfiler:
    """Profile an *in-process* method by monkeypatching it on its owner for the
    duration of a ``with`` block.

    The wrapper runs in whatever thread actually invokes the method, so when the
    method is the handler for an embedded-server HTTP request, ``enable()`` /
    ``disable()`` happen on that handler thread and cProfile captures the genuine
    server-side call (with its real ``trans``), not the test client.

    Only safe when a single request exercises the method at a time -- which is the
    case for these serial benchmarks.
    """

    def __init__(self, owner: object, method_name: str, label: str):
        self.owner = owner
        self.method_name = method_name
        self.label = label
        self.profiler = cProfile.Profile()
        self.call_count = 0
        self.wall_seconds = 0.0
        self._original: Optional[Callable] = None

    def __enter__(self) -> "MethodProfiler":
        self._original = getattr(self.owner, self.method_name)
        original = self._original

        def wrapped(*args, **kwargs):
            self.call_count += 1
            t0 = time.perf_counter()
            self.profiler.enable()
            try:
                return original(*args, **kwargs)
            finally:
                self.profiler.disable()
                self.wall_seconds += time.perf_counter() - t0

        setattr(self.owner, self.method_name, wrapped)
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._original is not None:
            setattr(self.owner, self.method_name, self._original)
        if self.call_count:
            dump_stats(self.profiler, self.label)


@contextmanager
def timed(label: str):
    """Time a block and print a single wall-clock line."""
    t0 = time.perf_counter()
    try:
        yield
    finally:
        print(f"[timing] {label}: {(time.perf_counter() - t0) * 1000.0:.1f} ms")
