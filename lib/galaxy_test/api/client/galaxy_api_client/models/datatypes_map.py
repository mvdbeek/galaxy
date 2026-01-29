from dataclasses import dataclass

from .datatypes_map_class_to_classes import DatatypesMapClassToClasses
from .datatypes_map_ext_to_class_name import DatatypesMapExtToClassName

__all__ = ["DatatypesMap"]


@dataclass
class DatatypesMap:
    """
    DatatypesMap dataclass

    Args:
        class_to_classes (DatatypesMapClassToClasses)
                                 : Dictionary mapping datatype's classes with their base
                                   classes
        ext_to_class_name (DatatypesMapExtToClassName)
                                 : Dictionary mapping datatype's extensions with
                                   implementation classes
    """

    class_to_classes: DatatypesMapClassToClasses  # Dictionary mapping datatype's classes with their base classes
    ext_to_class_name: (
        DatatypesMapExtToClassName  # Dictionary mapping datatype's extensions with implementation classes
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class_to_classes": "class_to_classes",
            "ext_to_class_name": "ext_to_class_name",
        }
        key_transform_with_dump = {
            "class_to_classes": "class_to_classes",
            "ext_to_class_name": "ext_to_class_name",
        }
