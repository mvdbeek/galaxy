import os
import string
import tempfile
from unittest.mock import (
    MagicMock,
    patch,
)

import pytest
from cryptography.fernet import InvalidToken

from galaxy.model.unittest_utils.data_app import (
    GalaxyDataTestApp,
    GalaxyDataTestConfig,
)
from galaxy.security.vault import (
    HashicorpVault,
    InvalidVaultKeyException,
    Vault,
    VaultFactory,
)
from galaxy.util.unittest import TestCase


class AbstractTestCases:
    """Test classes that should not be collected.

    Classes derived from unittest.TestCase are collected only if they are at the
    module level: https://stackoverflow.com/a/25695512/4503125

    This workaround is needed because unittest/pytest try to collect test
    classes even if they are abstract, and therefore their tests fails.
    """

    class VaultTestBase(TestCase):
        vault: Vault

        def test_read_write_secret(self):
            self.vault.write_secret("my/test/secret", "hello world")
            assert self.vault.read_secret("my/test/secret") == "hello world"

        def test_overwrite_secret(self):
            self.vault.write_secret("my/new/secret", "hello world")
            self.vault.write_secret("my/new/secret", "hello overwritten")
            assert self.vault.read_secret("my/new/secret") == "hello overwritten"

        def test_valid_paths(self):
            with self.assertRaises(InvalidVaultKeyException):
                self.vault.write_secret("", "hello world")
            with self.assertRaises(InvalidVaultKeyException):
                self.vault.write_secret("my//new/secret", "hello world")
            with self.assertRaises(InvalidVaultKeyException):
                self.vault.write_secret("my/ /new/secret", "hello world")
            # leading and trailing slashes should be ignored
            self.vault.write_secret("/my/new/secret with space/", "hello overwritten")
            assert self.vault.read_secret("my/new/secret with space") == "hello overwritten"


VAULT_CONF_HASHICORP = os.path.join(os.path.dirname(__file__), "fixtures/vault_conf_hashicorp.yml")


@pytest.mark.skipif(
    not os.environ.get("VAULT_ADDRESS") or not os.environ.get("VAULT_TOKEN"),
    reason="VAULT_ADDRESS and VAULT_TOKEN env vars not set",
)
class TestHashicorpVault(AbstractTestCases.VaultTestBase):
    def setUp(self) -> None:
        with (
            tempfile.NamedTemporaryFile(mode="w", prefix="vault_hashicorp", delete=False) as tempconf,
            open(VAULT_CONF_HASHICORP) as f,
        ):
            content = string.Template(f.read()).safe_substitute(
                vault_address=os.environ.get("VAULT_ADDRESS"), vault_token=os.environ.get("VAULT_TOKEN")
            )
            tempconf.write(content)
            self.vault_temp_conf = tempconf.name
        config = GalaxyDataTestConfig(vault_config_file=self.vault_temp_conf)
        app = GalaxyDataTestApp(config=config)
        self.vault = VaultFactory.from_app(app)

    def tearDown(self) -> None:
        os.remove(self.vault_temp_conf)


VAULT_CONF_DATABASE = os.path.join(os.path.dirname(__file__), "fixtures/vault_conf_database.yml")
VAULT_CONF_DATABASE_ROTATED = os.path.join(os.path.dirname(__file__), "fixtures/vault_conf_database_rotated.yml")
VAULT_CONF_DATABASE_INVALID = os.path.join(os.path.dirname(__file__), "fixtures/vault_conf_database_invalid_keys.yml")


class TestDatabaseVault(AbstractTestCases.VaultTestBase):
    def setUp(self) -> None:
        config = GalaxyDataTestConfig(vault_config_file=VAULT_CONF_DATABASE)
        app = GalaxyDataTestApp(config=config)
        self.vault = VaultFactory.from_app(app)

    def test_rotate_keys(self):
        config = GalaxyDataTestConfig(vault_config_file=VAULT_CONF_DATABASE)
        app = GalaxyDataTestApp(config=config)
        vault = VaultFactory.from_app(app)
        vault.write_secret("my/rotated/secret", "hello rotated")

        # should succeed after rotation
        app.config.vault_config_file = VAULT_CONF_DATABASE_ROTATED  # type: ignore[attr-defined]
        vault = VaultFactory.from_app(app)
        assert vault.read_secret("my/rotated/secret") == "hello rotated"

    def test_wrong_keys(self):
        config = GalaxyDataTestConfig(vault_config_file=VAULT_CONF_DATABASE)
        app = GalaxyDataTestApp(config=config)
        vault = VaultFactory.from_app(app)
        vault.write_secret("my/incorrect/secret", "hello incorrect")

        # should fail because decryption keys are the wrong
        app.config.vault_config_file = VAULT_CONF_DATABASE_INVALID  # type: ignore[attr-defined]
        vault = VaultFactory.from_app(app)
        with self.assertRaises(InvalidToken):
            vault.read_secret("my/incorrect/secret")


@patch("galaxy.security.vault.hvac")
class TestHashicorpVaultTokenRenewal:
    def _make_vault(self, hvac_mock, config_overrides=None, token_lookup_data=None):
        mock_client = MagicMock()
        hvac_mock.Client.return_value = mock_client
        if token_lookup_data is not None:
            mock_client.auth.token.lookup_self.return_value = {"data": token_lookup_data}
        config = {
            "vault_address": "http://localhost:8200",
            "vault_token": "s.test-token",
        }
        if config_overrides:
            config.update(config_overrides)
        vault = HashicorpVault(config)
        return vault, mock_client

    def test_renewable_token_starts_renewal_thread(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            token_lookup_data={"renewable": True, "ttl": 3600},
        )
        try:
            assert vault._token_renewable is True
            assert vault._token_ttl == 3600
            assert vault._renewal_thread is not None
            assert vault._renewal_thread.is_alive()
        finally:
            vault.shutdown()

    def test_non_renewable_token_no_thread(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            token_lookup_data={"renewable": False, "ttl": 3600},
        )
        assert vault._token_renewable is False
        assert vault._renewal_thread is None

    def test_zero_ttl_token_no_thread(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            token_lookup_data={"renewable": True, "ttl": 0},
        )
        assert vault._renewal_thread is None

    def test_token_renewal_disabled_by_config(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            config_overrides={"token_renewal": False},
            token_lookup_data={"renewable": True, "ttl": 3600},
        )
        mock_client.auth.token.lookup_self.assert_not_called()
        assert vault._renewal_thread is None

    def test_token_lookup_failure_disables_renewal(self, hvac_mock):
        mock_client = MagicMock()
        hvac_mock.Client.return_value = mock_client
        mock_client.auth.token.lookup_self.side_effect = Exception("connection refused")
        config = {
            "vault_address": "http://localhost:8200",
            "vault_token": "s.test-token",
        }
        vault = HashicorpVault(config)
        assert vault._renewal_thread is None

    def test_renewal_interval_override(self, hvac_mock):
        vault, _ = self._make_vault(
            hvac_mock,
            config_overrides={"token_renewal_interval": 600},
            token_lookup_data={"renewable": True, "ttl": 3600},
        )
        try:
            assert vault._compute_renewal_interval(3600) == 600
        finally:
            vault.shutdown()

    def test_renewal_interval_minimum_enforced(self, hvac_mock):
        vault, _ = self._make_vault(
            hvac_mock,
            config_overrides={"token_renewal_interval": 2},
            token_lookup_data={"renewable": True, "ttl": 10},
        )
        try:
            assert vault._compute_renewal_interval(10) == HashicorpVault.MIN_RENEWAL_INTERVAL_SECONDS
        finally:
            vault.shutdown()

    def test_shutdown_stops_thread(self, hvac_mock):
        vault, _ = self._make_vault(
            hvac_mock,
            token_lookup_data={"renewable": True, "ttl": 3600},
        )
        assert vault._renewal_thread is not None
        vault.shutdown()
        assert not vault._renewal_thread.is_alive()

    def test_read_secret_forbidden_returns_none(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            config_overrides={"token_renewal": False},
        )
        mock_client.secrets.kv.read_secret_version.side_effect = hvac_mock.exceptions.Forbidden
        result = vault.read_secret("some/key")
        assert result is None

    def test_write_secret_forbidden_raises(self, hvac_mock):
        vault, mock_client = self._make_vault(
            hvac_mock,
            config_overrides={"token_renewal": False},
        )
        mock_client.secrets.kv.v2.create_or_update_secret.side_effect = hvac_mock.exceptions.Forbidden
        with pytest.raises(hvac_mock.exceptions.Forbidden):
            vault.write_secret("some/key", "value")
