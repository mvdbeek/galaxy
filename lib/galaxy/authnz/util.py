from .psa_authnz import BACKENDS_NAME


def provider_name_to_backend(provider):
    """
    Convert a provider name (config key / idp_id) to the value used to look up
    social auth tokens in the database (UserAuthnzToken.provider).

    Since the migration that introduced idp_id, UserAuthnzToken.provider stores
    the idp_id (which defaults to the lowercased provider name, e.g. 'google').
    This function returns the lowercased provider name when it matches a known
    backend key, which is the same as the default idp_id for single-instance setups.

    For multi-instance setups with explicit idp_id values, callers should use
    the idp_id directly rather than relying on this function.
    """
    for k in BACKENDS_NAME:
        if k.lower() == provider.lower():
            return k.lower()
    return None


def debug_access_token_data(access_token, social, **kwargs):
    """
    Debug auth pipeline step to add decoded access token data
    to extra_data field. Should only be used for testing,
    but needs to be at an importable path to use in the auth pipeline
    """
    social.set_extra_data({"access_token_decoded": access_token})
