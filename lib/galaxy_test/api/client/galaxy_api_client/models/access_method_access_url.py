from typing import TypeAlias

from .access_url import AccessUrl

__all__ = ["AccessMethodAccessUrl"]

AccessMethodAccessUrl: TypeAlias = AccessUrl | None
