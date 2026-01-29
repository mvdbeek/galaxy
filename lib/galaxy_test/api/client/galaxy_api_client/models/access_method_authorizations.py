from typing import TypeAlias

from .authorizations import Authorizations

__all__ = ["AccessMethodAuthorizations"]

AccessMethodAuthorizations: TypeAlias = Authorizations | None
