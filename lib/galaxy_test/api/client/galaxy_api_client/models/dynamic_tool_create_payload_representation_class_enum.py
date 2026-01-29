from enum import Enum, unique

__all__ = ["DynamicToolCreatePayloadRepresentationClassEnum"]


@unique
class DynamicToolCreatePayloadRepresentationClassEnum(str, Enum):
    """
    Discriminator enum for DynamicToolCreatePayloadRepresentation union types.

    Args:
        GalaxyTool (str)         : Value for GALAXYTOOL
    """

    GALAXYTOOL = "GalaxyTool"
