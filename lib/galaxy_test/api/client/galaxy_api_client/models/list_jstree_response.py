from dataclasses import dataclass, field
from typing import Any

__all__ = ["ListJstreeResponse"]


@dataclass
class ListJstreeResponse:
    """
    List of files in Jstree format.

    Args:
        items (List[dict[str, Any]] | None)
                                 : List of files in Jstree format.
    """

    items: list[dict[str, Any]] | None = field(default_factory=list)  # List of files in Jstree format.
