from dataclasses import dataclass

from .parameters import Parameters

__all__ = ["CwlUnionParameterModelOutput"]


@dataclass
class CwlUnionParameterModelOutput:
    """
    CwlUnionParameterModelOutput dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (Parameters)  :
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: Parameters
    parameter_type: str | None = "cwl_union"
