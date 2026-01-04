from dataclasses import dataclass

__all__ = ["CwlFloatParameterModel"]


@dataclass
class CwlFloatParameterModel:
    """
    CwlFloatParameterModel dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameter_type: str | None = "cwl_float"
