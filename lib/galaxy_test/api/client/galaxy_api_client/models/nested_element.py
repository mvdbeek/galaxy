from dataclasses import dataclass

__all__ = ["NestedElement"]


@dataclass
class NestedElement:
    """
    [Circular reference detected: NestedElement -> NestedElementElements ->
    NestedElementElementsItem -> NestedElement]
    """

    # No properties defined in schema
    pass
