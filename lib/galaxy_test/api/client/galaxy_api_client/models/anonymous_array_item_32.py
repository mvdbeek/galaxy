from dataclasses import dataclass, field
from typing import Any

__all__ = ["AnonymousArrayItem32"]


@dataclass
class AnonymousArrayItem32:
    """
    AnonymousArrayItem32 dataclass

    Args:
        items (List[dict[str, Any]] | None)
                                 : A list of dict[str, Any] items.
    """

    items: list[dict[str, Any]] | None = field(default_factory=list)  # A list of dict[str, Any] items.
