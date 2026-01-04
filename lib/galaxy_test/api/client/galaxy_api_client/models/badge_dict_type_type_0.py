from enum import Enum


class BadgeDictTypeType0(str, Enum):
    BACKED_UP = "backed_up"
    FASTER = "faster"
    LESS_SECURE = "less_secure"
    LESS_STABLE = "less_stable"
    MORE_SECURE = "more_secure"
    MORE_STABLE = "more_stable"
    NOT_BACKED_UP = "not_backed_up"
    SHORT_TERM = "short_term"
    SLOWER = "slower"

    def __str__(self) -> str:
        return str(self.value)
