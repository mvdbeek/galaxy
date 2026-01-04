from dataclasses import dataclass

from .expression_lib import ExpressionLib

__all__ = ["JavascriptRequirement"]


@dataclass
class JavascriptRequirement:
    """
    JavascriptRequirement dataclass.

    Args:
        expression_lib (Optional[ExpressionLib])
                                 :
        type_ (str)              :
    """

    expression_lib: ExpressionLib | None
    type_: str
