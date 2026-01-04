from enum import Enum


class RequestDataType(str, Enum):
    CONVERTED_DATASETS_STATE = "converted_datasets_state"
    DATA = "data"
    FEATURES = "features"
    GENOME_DATA = "genome_data"
    IN_USE_STATE = "in_use_state"
    RAW_DATA = "raw_data"
    STATE = "state"
    TRACK_CONFIG = "track_config"

    def __str__(self) -> str:
        return str(self.value)
