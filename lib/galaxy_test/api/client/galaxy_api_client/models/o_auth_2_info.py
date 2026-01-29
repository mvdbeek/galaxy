from dataclasses import dataclass

__all__ = ["OAuth2Info"]


@dataclass
class OAuth2Info:
    """
    OAuth2Info dataclass.

    Args:
        authorize_url (str)      :
    """

    authorize_url: str
