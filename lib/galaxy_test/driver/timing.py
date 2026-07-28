"""Optional instrumentation of Galaxy test instance startup and teardown.

Integration tests build a full Galaxy application per test class, so the fixed
cost of a launch/teardown cycle dominates the suite's runtime. Set
``GALAXY_TEST_TIMING_FILE`` to a path to append one JSON object per cycle,
recording how long each phase took. When the variable is unset every entry
point here is a cheap no-op.

Records are consumed by ``scripts/summarize_test_timings.py``.
"""

import hashlib
import json
import os
import re
import threading
import time
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

TIMING_FILE_ENV_VAR = "GALAXY_TEST_TIMING_FILE"

# Values that necessarily differ between two otherwise identical launches. They are
# masked out before fingerprinting a config so that two test classes that configure
# Galaxy the same way produce the same fingerprint.
VOLATILE_CONFIG_KEYS = frozenset(
    {
        "database_connection",
        "install_database_connection",
        "amqp_internal_connection",
        "id_secret",
        "global_conf",
    }
)
# Directories ``setup_galaxy_config`` creates with ``tempfile.mkdtemp``, so their names
# carry per-launch randomness. Their values are masked wherever they appear, not just
# under these keys, since other settings embed them.
VOLATILE_PATH_KEYS = (
    "config_dir",
    "data_dir",
    "galaxy_data_manager_data_path",
    "job_working_directory",
    "new_file_path",
    "template_cache_path",
    "file_path",
    "tool_data_path",
    "shed_tool_data_path",
)
TEMPORARY_DATABASE_NAME = re.compile(r"gxtest[A-Za-z0-9]+")

_write_lock = threading.Lock()


class Timings:
    """Collects phase durations for a single instance launch or teardown."""

    def __init__(self, kind: str, **fields: Any) -> None:
        self.kind = kind
        self.fields: dict[str, Any] = dict(fields)
        self.phases: dict[str, float] = {}
        self._started = time.perf_counter()

    @contextmanager
    def phase(self, name: str) -> Iterator[None]:
        started = time.perf_counter()
        try:
            yield
        finally:
            self.record(name, time.perf_counter() - started)

    def record(self, name: str, seconds: float) -> None:
        # Phases can repeat within a cycle (one wrapper stopped per server), so accumulate.
        self.phases[name] = round(self.phases.get(name, 0.0) + seconds, 4)

    def set(self, key: str, value: Any) -> None:
        self.fields[key] = value

    def as_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "total": round(time.perf_counter() - self._started, 4),
            "phases": self.phases,
            **self.fields,
        }


class NullTimings(Timings):
    """Stand-in used when timing is disabled or no cycle is active."""

    def __init__(self) -> None:
        super().__init__("null")

    @contextmanager
    def phase(self, name: str) -> Iterator[None]:
        yield

    def record(self, name: str, seconds: float) -> None:
        pass

    def set(self, key: str, value: Any) -> None:
        pass


NULL_TIMINGS = NullTimings()

_active: Timings = NULL_TIMINGS


def enabled() -> bool:
    return bool(os.environ.get(TIMING_FILE_ENV_VAR))


def current() -> Timings:
    """Return the cycle being timed, or a no-op recorder outside of one."""
    return _active


@contextmanager
def phase(name: str) -> Iterator[None]:
    """Time a phase of whichever cycle is active, if any."""
    with _active.phase(name):
        yield


@contextmanager
def timed_cycle(kind: str, **fields: Any) -> Iterator[Timings]:
    """Time one launch (``kind="startup"``) or teardown (``kind="teardown"``).

    The record is written on exit, including when the body raises, so a launch that
    fails partway through still reports the phases that completed.
    """
    global _active
    if not enabled():
        yield NULL_TIMINGS
        return
    previous = _active
    timings = Timings(kind, **fields)
    _active = timings
    try:
        yield timings
    finally:
        _active = previous
        _write(timings)


def _write(timings: Timings) -> None:
    path = os.environ.get(TIMING_FILE_ENV_VAR)
    if not path:
        return
    line = f"{json.dumps(timings.as_dict())}\n"
    with _write_lock:
        with open(path, "a") as fh:
            fh.write(line)


def record_config_fingerprint(galaxy_config: dict[str, Any] | None, volatile_paths: list[str] | None = None) -> None:
    """Attach the fingerprint of a launch's config to the active record, if timing is on."""
    if not enabled():
        return
    _active.set("config_fingerprint", config_fingerprint(galaxy_config, volatile_paths))


def config_fingerprint(galaxy_config: dict[str, Any] | None, volatile_paths: list[str] | None = None) -> str:
    """Hash a Galaxy config, ignoring values that differ between every launch.

    Two test classes sharing a fingerprint configure Galaxy identically and could in
    principle share a single application instance.
    """
    if galaxy_config is None:
        return "none"
    normalized = _normalize(galaxy_config, _volatile_paths(galaxy_config, volatile_paths), top_level=True)
    serialized = json.dumps(normalized, sort_keys=True, default=repr)
    return hashlib.sha256(serialized.encode()).hexdigest()[:12]


def _volatile_paths(galaxy_config: dict[str, Any], extra: list[str] | None) -> list[str]:
    """Every per-launch directory to mask, longest first so nested paths go first.

    Both the path and its realpath are masked - on macOS the temp root resolves under
    ``/private``, and the config mixes the two forms.
    """
    paths = set(extra or [])
    for key in VOLATILE_PATH_KEYS:
        value = galaxy_config.get(key)
        if isinstance(value, str) and value:
            paths.add(value)
    paths.update(os.path.realpath(path) for path in list(paths))
    return sorted(paths, key=len, reverse=True)


def _normalize(value: Any, volatile_paths: list[str], top_level: bool = False) -> Any:
    if isinstance(value, dict):
        return {
            key: "<volatile>" if top_level and key in VOLATILE_CONFIG_KEYS else _normalize(item, volatile_paths)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [_normalize(item, volatile_paths) for item in value]
    if isinstance(value, str):
        for volatile_path in volatile_paths:
            if volatile_path and volatile_path in value:
                value = value.replace(volatile_path, "<tmp>")
        return TEMPORARY_DATABASE_NAME.sub("<db>", value)
    return value
