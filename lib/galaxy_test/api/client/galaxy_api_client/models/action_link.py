from dataclasses import dataclass

__all__ = ["ActionLink"]


@dataclass
class ActionLink:
    """
    An action link to be displayed in the notification as a button.

    Args:
        action_name (str)        : The name of the action, will be the button title.
        link (str)               : The link to be opened when the button is clicked.
    """

    action_name: str  # The name of the action, will be the button title.
    link: str  # The link to be opened when the button is clicked.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_name": "action_name",
            "link": "link",
        }
        key_transform_with_dump = {
            "action_name": "action_name",
            "link": "link",
        }
