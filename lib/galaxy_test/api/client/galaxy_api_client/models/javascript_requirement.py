from dataclasses import dataclass

from .javascript_requirement_expression_lib import JavascriptRequirementExpressionLib

__all__ = ["JavascriptRequirement"]


@dataclass
class JavascriptRequirement:
    """
    JavascriptRequirement dataclass

    Args:
        expression_lib (JavascriptRequirementExpressionLib)
                                 :
        type_ (str)              : Maps from 'type'
    """

    expression_lib: JavascriptRequirementExpressionLib
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "expression_lib": "expression_lib",
            "type": "type_",
        }
        key_transform_with_dump = {
            "expression_lib": "expression_lib",
            "type_": "type",
        }
