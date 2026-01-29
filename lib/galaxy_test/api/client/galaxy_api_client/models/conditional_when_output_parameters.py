from typing import TypeAlias

from .conditional_when_output_parameters_item import ConditionalWhenOutputParametersItem

__all__ = ["ConditionalWhenOutputParameters"]

ConditionalWhenOutputParameters: TypeAlias = list[ConditionalWhenOutputParametersItem]
