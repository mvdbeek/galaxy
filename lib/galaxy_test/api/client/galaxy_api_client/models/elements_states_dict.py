from dataclasses import dataclass

__all__ = ["ElementsStatesDict"]


@dataclass
class ElementsStatesDict:
    """
    ElementsStatesDict dataclass.

    Args:
        deferred (Optional[int]) :
        discarded (Optional[int]):
        empty (Optional[int])    :
        error (Optional[int])    :
        failed_metadata (Optional[int])
                                 :
        new (Optional[int])      :
        ok (Optional[int])       :
        paused (Optional[int])   :
        queued (Optional[int])   :
        running (Optional[int])  :
        setting_metadata (Optional[int])
                                 :
        upload (Optional[int])   :
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
