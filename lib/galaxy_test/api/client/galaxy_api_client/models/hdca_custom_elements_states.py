from typing import TypeAlias

from .elements_states_dict import ElementsStatesDict

__all__ = ["HdcaCustomElementsStates"]

HdcaCustomElementsStates: TypeAlias = ElementsStatesDict | None
"""Alias for A dictionary containing counts for each dataset state in the collection."""
