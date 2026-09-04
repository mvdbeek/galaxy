"""Standalone worker that evaluates one JavaScript program in an embedded V8 isolate.

This module is deliberately dependency-light: it imports only the standard library
at module load and ``py_mini_racer`` lazily, so it starts quickly and can run inside
a restrictive jail (for example ``bubblewrap``) that has little more than the Python
interpreter and its site-packages available read-only.

Protocol: read one JSON object ``{"program", "timeout", "memory_limit"}`` from stdin
and write one JSON object ``{"result": <value>}`` or ``{"error": <message>}`` to
stdout. ``program`` must yield a JSON string (i.e. end in ``JSON.stringify(...)``) so
its result round-trips as JSON.
"""

import json
import sys
from typing import Any


def run_program(program: str, timeout: float, memory_limit: int) -> Any:
    """Evaluate ``program`` in a fresh, isolated V8 context and return its value.

    Raises the underlying ``py_mini_racer`` exception on a JS error, timeout, or
    out-of-memory; the caller is responsible for translating those.
    """
    # lazy import: keep worker module import light so it starts quickly in the jail
    from py_mini_racer import MiniRacer

    ctx = MiniRacer()
    ctx.set_hard_memory_limit(memory_limit)
    try:
        raw = ctx.eval(program, timeout_sec=timeout)
    finally:
        ctx.close()
    if not isinstance(raw, (str, bytes, bytearray)):
        # JSON.stringify(undefined) yields JS ``undefined``; treat as null.
        return None
    return json.loads(raw)


def main() -> None:
    request = json.load(sys.stdin)
    try:
        result = run_program(request["program"], request["timeout"], request["memory_limit"])
        response = {"result": result}
    except Exception as e:
        response = {"error": str(e)}
    json.dump(response, sys.stdout)


if __name__ == "__main__":
    main()
