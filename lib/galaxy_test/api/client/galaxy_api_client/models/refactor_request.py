from dataclasses import dataclass

from .actions import Actions

__all__ = ["RefactorRequest"]


@dataclass
class RefactorRequest:
    """
    RefactorRequest dataclass.

    Args:
        actions (Actions)        :
        dry_run (Optional[bool]) :
        style (Optional[str])    :
    """

    actions: Actions
    dry_run: bool | None = False
    style: str | None = "export"
