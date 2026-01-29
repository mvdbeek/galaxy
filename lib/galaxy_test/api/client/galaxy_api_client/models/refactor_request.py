from dataclasses import dataclass

from .refactor_request_actions import RefactorRequestActions

__all__ = ["RefactorRequest"]


@dataclass
class RefactorRequest:
    """
    RefactorRequest dataclass

    Args:
        actions (RefactorRequestActions)
                                 :
        dry_run (bool | None)    :
        style (str | None)       :
    """

    actions: RefactorRequestActions
    dry_run: bool | None = False
    style: str | None = "export"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "actions": "actions",
            "dry_run": "dry_run",
            "style": "style",
        }
        key_transform_with_dump = {
            "actions": "actions",
            "dry_run": "dry_run",
            "style": "style",
        }
