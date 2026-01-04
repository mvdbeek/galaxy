from dataclasses import dataclass

__all__ = ["CwlBooleanParameterModel"]


@dataclass
class CwlBooleanParameterModel:
    """
    CwlBooleanParameterModel dataclass.

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameter_type (Optional[str])
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameter_type: str | None = "cwl_boolean"
