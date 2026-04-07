import tempfile
from typing import Optional
from unittest.mock import MagicMock

import pytest
from social_core.utils import setting_name

from galaxy.authnz.managers import AuthnzManager
from galaxy.util import asbool


@pytest.fixture
def mock_app():
    yield MagicMock()


OIDC_BACKEND_CONFIG_TEMPLATE = """<?xml version="1.0"?>
<OIDC>
    <provider name="{provider_name}">
        <url>{url}</url>
        <client_id>{client_id}</client_id>
        <client_secret>{client_secret}</client_secret>
        <redirect_uri>$galaxy_url/authnz/keycloak/callback</redirect_uri>
        <enable_idp_logout>{enable_idp_logout}</enable_idp_logout>
        <require_create_confirmation>{require_create_confirmation}</require_create_confirmation>
        <accepted_audiences>{accepted_audiences}</accepted_audiences>
        <username_key>{username_key}</username_key>
    </provider>
</OIDC>
"""

OIDC_BACKEND_CONFIG_WITH_IDP_ID_TEMPLATE = """<?xml version="1.0"?>
<OIDC>
    <provider name="{provider_name}" idp_id="{idp_id}">
        <url>{url}</url>
        <client_id>test_client_id</client_id>
        <client_secret>test_client_secret</client_secret>
        <redirect_uri>http://localhost/authnz/{idp_id}/callback</redirect_uri>
        <enable_idp_logout>{enable_idp_logout}</enable_idp_logout>
    </provider>
</OIDC>
"""

OIDC_BACKEND_CONFIG_TWO_PROVIDERS_TEMPLATE = """<?xml version="1.0"?>
<OIDC>
    <provider name="{provider_name1}" idp_id="{idp_id1}">
        <url>{url1}</url>
        <client_id>client_id_1</client_id>
        <client_secret>client_secret_1</client_secret>
        <redirect_uri>http://localhost/authnz/{idp_id1}/callback</redirect_uri>
        <enable_idp_logout>false</enable_idp_logout>
        <label>{label1}</label>
    </provider>
    <provider name="{provider_name2}" idp_id="{idp_id2}">
        <url>{url2}</url>
        <client_id>client_id_2</client_id>
        <client_secret>client_secret_2</client_secret>
        <redirect_uri>http://localhost/authnz/{idp_id2}/callback</redirect_uri>
        <enable_idp_logout>false</enable_idp_logout>
        <label>{label2}</label>
    </provider>
</OIDC>
"""


OIDC_CONFIG_TEMPLATE = """
<OIDC>
    <Setter Property="VERIFY_SSL" Value="False" Type="bool"/>
    {extra_properties}
</OIDC>
"""


def create_oidc_config(extra_properties: str = "") -> tuple[str, str]:
    contents = OIDC_CONFIG_TEMPLATE.format(extra_properties=extra_properties)
    file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    file.write(contents)
    return contents, file.name


def create_backend_config(
    provider_name="oidc",
    url="https://example.com",
    client_id="client_id",
    client_secret="client_secret",
    enable_idp_logout="true",
    require_create_confirmation="false",
    accepted_audiences="https://audience.example.com",
    username_key="custom_username",
) -> tuple[str, str]:
    contents = OIDC_BACKEND_CONFIG_TEMPLATE.format(
        provider_name=provider_name,
        url=url,
        client_id=client_id,
        client_secret=client_secret,
        enable_idp_logout=enable_idp_logout,
        require_create_confirmation=require_create_confirmation,
        accepted_audiences=accepted_audiences,
        username_key=username_key,
    )
    file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    file.write(contents)
    return contents, file.name


def create_backend_config_with_idp_id(
    provider_name="keycloak",
    idp_id="my_keycloak",
    url="https://example.com",
    enable_idp_logout="true",
) -> tuple[str, str]:
    contents = OIDC_BACKEND_CONFIG_WITH_IDP_ID_TEMPLATE.format(
        provider_name=provider_name,
        idp_id=idp_id,
        url=url,
        enable_idp_logout=enable_idp_logout,
    )
    file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".xml")
    file.write(contents)
    file.flush()
    return contents, file.name


def create_backend_config_two_providers(
    provider_name1="keycloak",
    idp_id1="keycloak1",
    url1="https://keycloak1.example.com",
    label1="Keycloak 1",
    provider_name2="keycloak",
    idp_id2="keycloak2",
    url2="https://keycloak2.example.com",
    label2="Keycloak 2",
) -> tuple[str, str]:
    contents = OIDC_BACKEND_CONFIG_TWO_PROVIDERS_TEMPLATE.format(
        provider_name1=provider_name1,
        idp_id1=idp_id1,
        url1=url1,
        label1=label1,
        provider_name2=provider_name2,
        idp_id2=idp_id2,
        url2=url2,
        label2=label2,
    )
    file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".xml")
    file.write(contents)
    file.flush()
    return contents, file.name


def test_parse_backend_config(mock_app):
    config_values = {
        "url": "https://example.com",
        "client_id": "example_app",
        "client_secret": "abcd1234",
        "enable_idp_logout": "true",
        "require_create_confirmation": "false",
        "accepted_audiences": "https://audience.example.com",
        "username_key": "custom_username",
    }
    oidc_contents, oidc_path = create_oidc_config()
    backend_contents, backend_path = create_backend_config(provider_name="oidc", **config_values)
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    assert isinstance(manager.oidc_backends_config["oidc"], dict)
    parsed = manager.oidc_backends_config["oidc"]
    assert parsed["url"] == config_values["url"]
    assert parsed["client_id"] == config_values["client_id"]
    assert parsed["client_secret"] == config_values["client_secret"]
    assert parsed["accepted_audiences"] == config_values["accepted_audiences"]
    assert parsed["username_key"] == config_values["username_key"]
    # Boolean values should be parsed into bools
    assert parsed["enable_idp_logout"] == asbool(config_values["enable_idp_logout"])
    assert parsed["require_create_confirmation"] == asbool(config_values["require_create_confirmation"])
    # provider_name should be stored in config for backend class lookup
    assert parsed["provider_name"] == "oidc"


def test_psa_authnz_config(mock_app):
    """
    Test config values are set correctly in PSAAuthnz
    """
    config_values = {
        "url": "https://example.com",
        "client_id": "example_app",
        "client_secret": "abcd1234",
        "enable_idp_logout": "true",
        "require_create_confirmation": "false",
        "accepted_audiences": "https://audience.example.com",
        "username_key": "custom_username",
    }
    oidc_contents, oidc_path = create_oidc_config()
    backend_contents, backend_path = create_backend_config(provider_name="oidc", **config_values)
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    from galaxy.authnz.psa_authnz import PSAAuthnz

    psa_authnz = PSAAuthnz(
        provider="oidc",
        oidc_config=manager.oidc_config,
        oidc_backend_config=manager.oidc_backends_config["oidc"],
        app_config=mock_app.config,
    )
    assert psa_authnz.config[setting_name("USERNAME_KEY")] == config_values["username_key"]


def _create_backend_config_with_idphint(idphint_value: Optional[str] = None) -> tuple[str, str]:
    """Create a Keycloak backend config, optionally including an <idphint> element."""
    idphint_element = f"        <idphint>{idphint_value}</idphint>" if idphint_value else ""
    contents = f"""<?xml version="1.0"?>
<OIDC>
    <provider name="keycloak">
        <url>https://auth.example.org/realms/MyRealm/</url>
        <client_id>galaxy-oidc</client_id>
        <client_secret>secret</client_secret>
        <redirect_uri>https://galaxy.example.org/authnz/keycloak/callback</redirect_uri>
        <enable_idp_logout>true</enable_idp_logout>
{idphint_element}
    </provider>
</OIDC>
"""
    file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".xml")
    file.write(contents)
    file.flush()
    return contents, file.name


def test_parse_idphint_from_xml(mock_app):
    """
    Regression test: <idphint> in oidc_backends_config.xml must be parsed into
    the oidc_backend_config dict so that PSAAuthnz can forward it as IDPHINT to
    the Keycloak/CILogon backends (which use it to set kc_idp_hint).

    Previously, _parse_idp_config() had no branch for <idphint>, so the element
    was silently ignored and oidc_backend_config.get("idphint") always returned
    None, causing kc_idp_hint to never be sent to Keycloak.
    """
    _, oidc_path = create_oidc_config()
    _, backend_path = _create_backend_config_with_idphint(idphint_value="my-switch-edu-id")
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    parsed = manager.oidc_backends_config["keycloak"]
    assert "idphint" in parsed, "<idphint> element must be parsed into oidc_backend_config dict"
    assert parsed["idphint"] == "my-switch-edu-id"


def test_idphint_propagated_to_psa_config(mock_app):
    """
    When <idphint> is configured, PSAAuthnz must expose it as IDPHINT in its
    config so the Keycloak/CILogon PSA backend can add kc_idp_hint to the
    authorization URL.
    """
    from galaxy.authnz.psa_authnz import PSAAuthnz

    _, oidc_path = create_oidc_config()
    _, backend_path = _create_backend_config_with_idphint(idphint_value="stage")
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    psa = PSAAuthnz(
        provider="keycloak",
        oidc_config=manager.oidc_config,
        oidc_backend_config=manager.oidc_backends_config["keycloak"],
        app_config=mock_app.config,
    )
    assert psa.config.get("IDPHINT") == "stage", "IDPHINT must be 'stage' when <idphint>stage</idphint> is in XML"


def test_missing_idphint_is_none(mock_app):
    """
    When <idphint> is absent from the XML, IDPHINT must be None (not a hardcoded
    default string like 'oidc'), so the Keycloak backend omits kc_idp_hint
    entirely rather than sending a wrong value.
    """
    from galaxy.authnz.psa_authnz import PSAAuthnz

    _, oidc_path = create_oidc_config()
    _, backend_path = _create_backend_config_with_idphint(idphint_value=None)
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    psa = PSAAuthnz(
        provider="keycloak",
        oidc_config=manager.oidc_config,
        oidc_backend_config=manager.oidc_backends_config["keycloak"],
        app_config=mock_app.config,
    )
    assert psa.config.get("IDPHINT") is None, "IDPHINT must be None when <idphint> is absent from XML"


def test_idp_id_used_as_config_key(mock_app):
    """
    When idp_id is specified, it should be used as the key in oidc_backends_config
    instead of the lowercased provider name.
    """
    _, oidc_path = create_oidc_config()
    _, backend_path = create_backend_config_with_idp_id(
        provider_name="keycloak",
        idp_id="my_keycloak_instance",
        url="https://keycloak.example.org/realms/master/",
    )
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    # Config should be keyed by idp_id, not provider name
    assert "my_keycloak_instance" in manager.oidc_backends_config
    assert "keycloak" not in manager.oidc_backends_config
    parsed = manager.oidc_backends_config["my_keycloak_instance"]
    assert parsed["provider_name"] == "keycloak"
    assert parsed["url"] == "https://keycloak.example.org/realms/master/"


def test_idp_id_default_is_lowercased_name(mock_app):
    """
    When idp_id is not specified, the config key should default to the lowercased
    provider name (backward compatible behavior).
    """
    _, oidc_path = create_oidc_config()
    _, backend_path = create_backend_config(provider_name="keycloak")
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    assert "keycloak" in manager.oidc_backends_config
    assert manager.oidc_backends_config["keycloak"]["provider_name"] == "keycloak"


def test_two_providers_same_type_different_idp_id(mock_app):
    """
    Two providers of the same type (e.g., Keycloak) with different idp_ids
    should both be parsed and stored independently.
    """
    _, oidc_path = create_oidc_config()
    _, backend_path = create_backend_config_two_providers(
        provider_name1="keycloak",
        idp_id1="keycloak_uni",
        url1="https://keycloak.university.example.org/realms/uni/",
        label1="University Keycloak",
        provider_name2="keycloak",
        idp_id2="keycloak_corp",
        url2="https://keycloak.corp.example.org/realms/corp/",
        label2="Corporate Keycloak",
    )
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    # Both providers should be in the config
    assert "keycloak_uni" in manager.oidc_backends_config
    assert "keycloak_corp" in manager.oidc_backends_config
    # Each should have the correct URL
    assert manager.oidc_backends_config["keycloak_uni"]["url"] == "https://keycloak.university.example.org/realms/uni/"
    assert manager.oidc_backends_config["keycloak_corp"]["url"] == "https://keycloak.corp.example.org/realms/corp/"
    # Both should have the same provider_name for backend class lookup
    assert manager.oidc_backends_config["keycloak_uni"]["provider_name"] == "keycloak"
    assert manager.oidc_backends_config["keycloak_corp"]["provider_name"] == "keycloak"
    # Labels should be set correctly
    assert manager.oidc_backends_config["keycloak_uni"]["label"] == "University Keycloak"
    assert manager.oidc_backends_config["keycloak_corp"]["label"] == "Corporate Keycloak"


def test_duplicate_idp_id_raises_error(mock_app):
    """
    Two providers with the same idp_id should raise a ConfigurationError.
    """
    from galaxy import exceptions

    _, oidc_path = create_oidc_config()
    # Both have the same idp_id (default = name.lower() = "keycloak")
    contents = """<?xml version="1.0"?>
<OIDC>
    <provider name="keycloak">
        <url>https://first.example.org/</url>
        <client_id>c1</client_id>
        <client_secret>s1</client_secret>
        <redirect_uri>http://localhost/authnz/keycloak/callback</redirect_uri>
        <enable_idp_logout>false</enable_idp_logout>
    </provider>
    <provider name="keycloak">
        <url>https://second.example.org/</url>
        <client_id>c2</client_id>
        <client_secret>s2</client_secret>
        <redirect_uri>http://localhost/authnz/keycloak/callback</redirect_uri>
        <enable_idp_logout>false</enable_idp_logout>
    </provider>
</OIDC>
"""
    import tempfile

    f = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".xml")
    f.write(contents)
    f.flush()
    with pytest.raises(exceptions.ConfigurationError, match="Duplicate provider idp_id"):
        AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=f.name)


def test_psa_authnz_uses_idp_id_in_config(mock_app):
    """
    PSAAuthnz should store idp_id and provider_name separately in its config.
    idp_id is used for token storage, provider is used for backend class lookup.
    """
    from galaxy.authnz.psa_authnz import PSAAuthnz

    _, oidc_path = create_oidc_config()
    _, backend_path = create_backend_config_with_idp_id(
        provider_name="keycloak",
        idp_id="my_keycloak_instance",
        url="https://keycloak.example.org/realms/master/",
    )
    manager = AuthnzManager(app=mock_app, oidc_config_file=oidc_path, oidc_backends_config_file=backend_path)
    psa = PSAAuthnz(
        provider="my_keycloak_instance",
        oidc_config=manager.oidc_config,
        oidc_backend_config=manager.oidc_backends_config["my_keycloak_instance"],
        app_config=mock_app.config,
    )
    # idp_id should be set for token storage
    assert psa.config["idp_id"] == "my_keycloak_instance"
    # provider should be the backend type name for class lookup
    assert psa.config["provider"] == "keycloak"

