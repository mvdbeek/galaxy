"""Sentinel signals for Galaxy job handler and runner threads."""


class _StopSignal:
    """Sentinel type for signaling monitor/worker threads to shut down.

    Using a dedicated class instead of a bare ``object()`` ensures the
    queue type annotation (``Queue[Union[T, _StopSignal]]``) is
    expressible and prevents subclasses from accidentally shadowing the
    sentinel with their own ``object()`` instance.
    """

    pass


STOP_SIGNAL = _StopSignal()
