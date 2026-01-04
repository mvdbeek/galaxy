from enum import Enum


class HelpContentFormat(str, Enum):
    MARKDOWN = "markdown"
    PLAIN_TEXT = "plain_text"
    RESTRUCTUREDTEXT = "restructuredtext"

    def __str__(self) -> str:
        return str(self.value)
