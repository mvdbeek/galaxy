from dataclasses import dataclass

__all__ = ["CwlNullParameterModel"]


@dataclass
class CwlNullParameterModel:
    """
    CwlNullParameterModel dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameter_type: str | None = "cwl_null"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "parameter_type": "parameter_type",
        }
        key_transform_with_dump = {
            "name": "name",
            "parameter_type": "parameter_type",
        }
