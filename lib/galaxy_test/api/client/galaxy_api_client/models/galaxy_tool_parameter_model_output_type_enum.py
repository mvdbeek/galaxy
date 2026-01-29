from enum import Enum, unique

__all__ = ["GalaxyToolParameterModelOutputTypeEnum"]


@unique
class GalaxyToolParameterModelOutputTypeEnum(str, Enum):
    """
    Discriminator enum for GalaxyToolParameterModelOutput union types.

    Args:
        text (str)               : Value for TEXT
        integer (str)            : Value for INTEGER
        float (str)              : Value for FLOAT
        boolean (str)            : Value for BOOLEAN
        hidden (str)             : Value for HIDDEN
        select (str)             : Value for SELECT
        data (str)               : Value for DATA
        data_collection (str)    : Value for DATA_COLLECTION
        data_column (str)        : Value for DATA_COLUMN
        directory (str)          : Value for DIRECTORY
        rules (str)              : Value for RULES
        group_tag (str)          : Value for GROUP_TAG
        baseurl (str)            : Value for BASEURL
        genomebuild (str)        : Value for GENOMEBUILD
        color (str)              : Value for COLOR
    """

    TEXT = "text"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    HIDDEN = "hidden"
    SELECT = "select"
    DATA = "data"
    DATA_COLLECTION = "data_collection"
    DATA_COLUMN = "data_column"
    DIRECTORY = "directory"
    RULES = "rules"
    GROUP_TAG = "group_tag"
    BASEURL = "baseurl"
    GENOMEBUILD = "genomebuild"
    COLOR = "color"
