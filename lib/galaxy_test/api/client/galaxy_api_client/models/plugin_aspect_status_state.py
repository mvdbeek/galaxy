from enum import Enum


class PluginAspectStatusState(str, Enum):
    NOT_OK = "not_ok"
    OK = "ok"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
