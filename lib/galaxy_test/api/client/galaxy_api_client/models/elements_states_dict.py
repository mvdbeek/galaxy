from dataclasses import dataclass

__all__ = ["ElementsStatesDict"]


@dataclass
class ElementsStatesDict:
    """
    ElementsStatesDict dataclass

    Args:
        deferred (int | None)    :
        discarded (int | None)   :
        empty (int | None)       :
        error (int | None)       :
        failed_metadata (int | None)
                                 :
        new (int | None)         :
        ok (int | None)          :
        paused (int | None)      :
        queued (int | None)      :
        running (int | None)     :
        setting_metadata (int | None)
                                 :
        upload (int | None)      :
    """

    deferred: int | None = None
    discarded: int | None = None
    empty: int | None = None
    error: int | None = None
    failed_metadata: int | None = None
    new: int | None = None
    ok: int | None = None
    paused: int | None = None
    queued: int | None = None
    running: int | None = None
    setting_metadata: int | None = None
    upload: int | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deferred": "deferred",
            "discarded": "discarded",
            "empty": "empty",
            "error": "error",
            "failed_metadata": "failed_metadata",
            "new": "new",
            "ok": "ok",
            "paused": "paused",
            "queued": "queued",
            "running": "running",
            "setting_metadata": "setting_metadata",
            "upload": "upload",
        }
        key_transform_with_dump = {
            "deferred": "deferred",
            "discarded": "discarded",
            "empty": "empty",
            "error": "error",
            "failed_metadata": "failed_metadata",
            "new": "new",
            "ok": "ok",
            "paused": "paused",
            "queued": "queued",
            "running": "running",
            "setting_metadata": "setting_metadata",
            "upload": "upload",
        }
