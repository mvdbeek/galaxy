from dataclasses import dataclass
from typing import Any

__all__ = ["CwlUnionParameterModelInput"]


@dataclass
class CwlUnionParameterModelInput:
    """
    CwlUnionParameterModelInput dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (Dict[str, Any])
                                 : [Circular reference detected: Parameters ->
                                   ParametersItem -> CwlUnionParameterModel-Input ->
                                   Parameters]
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: dict[
        str, Any
    ]  # [Circular reference detected: Parameters -> ParametersItem -> CwlUnionParameterModel-Input -> Parameters]
    parameter_type: str | None = "cwl_union"
