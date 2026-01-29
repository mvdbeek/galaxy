from dataclasses import dataclass

from .cwl_union_parameter_model_input_parameters import CwlUnionParameterModelInputParameters

__all__ = ["CwlUnionParameterModelInput2"]


@dataclass
class CwlUnionParameterModelInput2:
    """
    CwlUnionParameterModelInput2 dataclass

    Args:
        name (str)               : Parameter name. Used when referencing parameter in
                                   workflows or inside command templating.
        parameters (CwlUnionParameterModelInputParameters)
                                 :
        parameter_type (str | None)
                                 :
    """

    name: str  # Parameter name. Used when referencing parameter in workflows or inside command templating.
    parameters: CwlUnionParameterModelInputParameters
    parameter_type: str | None = "cwl_union"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "parameter_type": "parameter_type",
            "parameters": "parameters",
        }
        key_transform_with_dump = {
            "name": "name",
            "parameter_type": "parameter_type",
            "parameters": "parameters",
        }
