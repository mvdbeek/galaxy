from enum import Enum, unique

__all__ = ["RequestDataType"]


@unique
class RequestDataType(str, Enum):
    """
    Particular pieces of information that can be requested for a dataset.

    Args:
        state (str)              : Value for STATE
        converted_datasets_state (str)
                                 : Value for CONVERTED_DATASETS_STATE
        data (str)               : Value for DATA
        features (str)           : Value for FEATURES
        raw_data (str)           : Value for RAW_DATA
        track_config (str)       : Value for TRACK_CONFIG
        genome_data (str)        : Value for GENOME_DATA
        in_use_state (str)       : Value for IN_USE_STATE
    """

    STATE = "state"
    CONVERTED_DATASETS_STATE = "converted_datasets_state"
    DATA = "data"
    FEATURES = "features"
    RAW_DATA = "raw_data"
    TRACK_CONFIG = "track_config"
    GENOME_DATA = "genome_data"
    IN_USE_STATE = "in_use_state"
