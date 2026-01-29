from dataclasses import dataclass

__all__ = ["OAuth2Info"]


@dataclass
class OAuth2Info:
    """
    OAuth2Info dataclass

    Args:
        authorize_url (str)      :
    """

    authorize_url: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "authorize_url": "authorize_url",
        }
        key_transform_with_dump = {
            "authorize_url": "authorize_url",
        }
