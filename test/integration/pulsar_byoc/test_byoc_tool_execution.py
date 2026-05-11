"""End-to-end BYOC tool-execution test.

This is the heavy sibling of ``test_byoc_e2e.py``. It brings up the full
stack — Keycloak (via docker compose) → pulsar-relay (subprocess) →
Pulsar daemon (subprocess) → Galaxy (in-process via
``IntegrationTestCase``) — drives the BYOC bootstrap, then submits a real
framework tool and asserts that:

1. TPV routes the job to the ``pulsar_byoc`` runner.
2. The multi-tenant runner materialises a client manager bound to the
   BYOC user's relay + manager_name.
3. The Pulsar daemon picks up the ``job_setup_<manager>`` message,
   executes the tool, and publishes a ``job_status_update_<manager>``
   completion.
4. Galaxy collects the outputs and marks the job ``ok``.

Skipped automatically when Docker / the pulsar-relay checkout / the
pulsar checkout aren't reachable — see the suite README.

This test is intentionally instrumented for debugging. Failures dump the
relay + Pulsar subprocess logs to stdout so a tester can diagnose without
re-running.
"""

from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import (
    ClassVar,
    Optional,
)

import httpx
import pytest
from pulsar_relay_client import CredentialsFile

from galaxy import model
from galaxy.managers.pulsar_byoc import STATUS_ACTIVE
from galaxy.security.vault import UserVaultWrapper
from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util

from ._keycloak_bootstrap import (
    KeycloakSetup,
    provision,
)
from ._keycloak_login import login_via_keycloak

pytestmark = pytest.mark.e2e

HERE = Path(__file__).parent
COMPOSE_FILE = HERE / "docker-compose.yml"
JOB_CONF_TEMPLATE = HERE / "byoc_job_conf.yml.template"
TPV_CONFIG_TEMPLATE = HERE / "byoc_tpv_config.yml.template"
PULSAR_APP_TEMPLATE = HERE / "pulsar_app.yml.template"

_DEVICE_GRANT = "urn:ietf:params:oauth:grant-type:device_code"


# --- Helpers (mirrored from conftest so this file is grep-able standalone) ---


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return int(s.getsockname()[1])


def _compose_cmd() -> Optional[list[str]]:
    docker = shutil.which("docker")
    if docker is not None:
        try:
            subprocess.run([docker, "compose", "version"], check=True, capture_output=True, timeout=5)
            return [docker, "compose"]
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
            pass
    legacy = shutil.which("docker-compose")
    if legacy is not None:
        return [legacy]
    return None


def _docker_running() -> bool:
    docker = shutil.which("docker")
    if docker is None:
        return False
    try:
        subprocess.run([docker, "info"], check=True, capture_output=True, timeout=5)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False


def _drive_device_flow_with_pair(relay: str, keycloak_setup) -> dict:
    """Drive device-flow + Keycloak sign-in + token exchange.

    Returns the ``/auth/device/token`` JSON body, which carries
    ``access_token`` / ``refresh_token`` / ``refresh_token_secondary``.
    """
    with httpx.Client(timeout=10.0) as client:
        dev = client.post(
            f"{relay}/auth/device/code",
            data={"client_hint": "byoc-tool-execution", "pair": "true"},
        )
        assert dev.status_code == 200, dev.text
        body = dev.json()
        device_code = body["device_code"]
        user_code = body["user_code"]
        interval = max(int(body["interval"]), 1)

    operator_error: list[Exception] = []

    def operator():
        try:
            with httpx.Client(timeout=10.0, follow_redirects=False) as op:
                start = op.get(
                    f"{relay}/auth/oidc/keycloak/login",
                    params={"device_user_code": user_code},
                )
                assert start.status_code == 302
                final = login_via_keycloak(
                    authorization_url=start.headers["location"],
                    username=keycloak_setup.user_username,
                    password=keycloak_setup.user_password,
                    follow_relay_callback=True,
                )
                assert final.status_code == 200
        except Exception as exc:
            operator_error.append(exc)

    op_thread = threading.Thread(target=operator)
    op_thread.start()
    try:
        deadline = time.time() + 60
        with httpx.Client(timeout=10.0) as client:
            while time.time() < deadline:
                time.sleep(interval)
                poll = client.post(
                    f"{relay}/auth/device/token",
                    data={"grant_type": _DEVICE_GRANT, "device_code": device_code},
                )
                if poll.status_code == 200:
                    return poll.json()
                err = poll.json().get("error", "")
                if err in ("authorization_pending", "slow_down"):
                    if err == "slow_down":
                        interval += 5
                    continue
                pytest.fail(f"Unexpected device-flow error: {poll.status_code} {poll.text}")
        pytest.fail("device-flow polling never completed")
    finally:
        op_thread.join(timeout=10)
        if operator_error:
            raise operator_error[0]


class TestPulsarByocToolExecution(
    integration_util.IntegrationTestCase,
    integration_util.ConfiguresDatabaseVault,
):
    """Real-tool-on-real-Pulsar BYOC e2e."""

    framework_tool_and_types = True
    dataset_populator: DatasetPopulator

    # All ClassVars below get populated in ``_prepare_galaxy`` (and are
    # safe to read in the test methods, which only run after that hook).
    # The non-Optional ones have no default; mypy permits this for
    # ClassVars set before any access.
    _compose_env: ClassVar[dict] = {}
    _keycloak_port: ClassVar[int]
    _relay_proc: ClassVar[Optional[subprocess.Popen]] = None  # may be None if tearDown runs before bring-up
    _pulsar_proc: ClassVar[Optional[subprocess.Popen]] = None
    _relay_base_url: ClassVar[str]
    _relay_port: ClassVar[int]
    _byoc_secondary_token: ClassVar[str]
    _byoc_manager_name: ClassVar[str]
    _byoc_resource_id: ClassVar[Optional[int]] = None  # genuinely None until setUp() inserts the row
    _tmp_dir: ClassVar[Path]

    # --- IntegrationTestCase hooks ------------------------------------------

    @classmethod
    def _prepare_galaxy(cls) -> None:
        if not _docker_running():
            pytest.skip("Docker daemon not reachable; skipping BYOC tool-execution suite.")
        compose = _compose_cmd()
        if compose is None:
            pytest.skip("docker / docker-compose not available")

        # Per-class working dir for Pulsar's staging/persistence and the
        # rendered job_conf/tpv_config files. ``BYOC_E2E_TMP`` lets a tester
        # pin it to a known path for ad-hoc debugging; otherwise mkdtemp.
        override = os.environ.get("BYOC_E2E_TMP")
        if override:
            cls._tmp_dir = Path(override)
            cls._tmp_dir.mkdir(parents=True, exist_ok=True)
        else:
            import tempfile

            cls._tmp_dir = Path(tempfile.mkdtemp(prefix="byoc_e2e_"))

        cls._bring_up_keycloak(compose)
        keycloak_setup = cls._provision_keycloak()
        cls._bring_up_relay(keycloak_setup)
        tokens = _drive_device_flow_with_pair(cls._relay_base_url, keycloak_setup)
        cls._byoc_secondary_token = tokens["refresh_token_secondary"]
        # manager_name = the relay user's username, which Keycloak maps from
        # the OIDC claim_username configured for the relay. We pull it from
        # /auth/me using the access token rather than decoding the JWT here.
        me = httpx.get(
            f"{cls._relay_base_url}/auth/me",
            headers={"Authorization": f"Bearer {tokens['access_token']}"},
            timeout=5.0,
        )
        me.raise_for_status()
        cls._byoc_manager_name = me.json()["username"]

        # Pre-create the topics pulsar will subscribe to. The relay does not
        # auto-create topics on long-poll subscription (only on owner POST),
        # so without this the GET /api/v1/topics/{name} signal we use in
        # _bring_up_pulsar would never go 200. Mirrors the
        # ``create_or_verify_topic`` loop Galaxy runs during BYOC bootstrap.
        cls._pre_create_topics(access_token=tokens["access_token"])

        cls._bring_up_pulsar(
            primary_token=tokens["refresh_token"],
            access_token=tokens["access_token"],
        )
        cls._render_galaxy_config_files()

    @classmethod
    def _pre_create_topics(cls, *, access_token: str) -> None:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        for prefix in ("job_setup", "job_status_request", "job_kill", "job_status_update"):
            topic_name = f"{prefix}_{cls._byoc_manager_name}"
            r = httpx.post(
                f"{cls._relay_base_url}/api/v1/topics",
                headers=headers,
                json={"topic_name": topic_name},
                timeout=5.0,
            )
            if r.status_code not in (200, 201, 400, 409):
                pytest.fail(f"Failed to pre-create relay topic {topic_name}: HTTP {r.status_code} {r.text}")

    @classmethod
    def handle_galaxy_config_kwds(cls, config) -> None:
        super().handle_galaxy_config_kwds(config)
        config["enable_pulsar_byoc"] = True
        config["pulsar_byoc_relay_url"] = cls._relay_base_url
        config["job_config_file"] = str(cls._tmp_dir / "job_conf.yml")
        # Pulsar pulls staged files from this URL — must point at the live
        # IntegrationTestCase web port, not the default 8080.
        config["galaxy_infrastructure_url"] = "http://localhost:$GALAXY_WEB_PORT"
        # BYOC stores the relay refresh token in the user vault.
        cls._configure_database_vault(config)
        config["enable_celery_tasks"] = False
        config["metadata_strategy"] = "directory"

    @classmethod
    def _configure_app(cls) -> None:
        super()._configure_app()
        # Galaxy is now up. Insert the BYOC resource + vault secret for
        # whichever user dataset_populator will end up running as.
        # We resolve that user lazily in setUp() because dataset_populator
        # provisions on first use.

    def setUp(self) -> None:
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        cls = type(self)
        if cls._byoc_resource_id is not None:
            return
        # First test: create the resource scoped to the populator's user.
        user_id_encoded = self.dataset_populator.user_id()
        user_id = self._app.security.decode_id(user_id_encoded)
        user = self._app.model.session.get(model.User, user_id)
        assert user is not None, "expected dataset_populator to provision a user"

        resource = model.PulsarByocResource(
            user_id=user.id,
            manager_name=cls._byoc_manager_name,
            relay_url=cls._relay_base_url,
            status=STATUS_ACTIVE,
        )
        self._app.model.session.add(resource)
        self._app.model.session.commit()
        cls._byoc_resource_id = resource.id

        UserVaultWrapper(self._app.vault, user).write_secret(
            f"pulsar_byoc/{resource.id}/relay_refresh_token",
            cls._byoc_secondary_token,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        # Stop the BYOC subprocesses before Galaxy's teardown (which calls
        # into the model session). Order matters: Pulsar first so the relay
        # has no lingering long-polls, then the relay, then Keycloak.
        for proc, name in (
            (cls._pulsar_proc, "pulsar"),
            (cls._relay_proc, "relay"),
        ):
            if proc is None:
                continue
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
            stdout, stderr = proc.communicate() if proc.poll() is None else (b"", b"")
            if stdout:
                print(f"\n--- {name} stdout ---\n{stdout.decode(errors='replace')}")
            if stderr:
                print(f"\n--- {name} stderr ---\n{stderr.decode(errors='replace')}")
        if cls._keycloak_port is not None:
            compose = _compose_cmd() or []
            subprocess.run(
                [*compose, "-f", str(COMPOSE_FILE), "down", "-v"],
                env=cls._compose_env,
            )
        super().tearDownClass()

    # --- Sub-fixtures -------------------------------------------------------

    @classmethod
    def _bring_up_keycloak(cls, compose: list[str]) -> None:
        cls._keycloak_port = _free_port()
        cls._compose_env = {**os.environ, "KEYCLOAK_HOST_PORT": str(cls._keycloak_port)}
        subprocess.run(
            [*compose, "-f", str(COMPOSE_FILE), "up", "-d", "keycloak"],
            check=True,
            env=cls._compose_env,
        )
        base_url = f"http://localhost:{cls._keycloak_port}"
        deadline = time.time() + 180
        while time.time() < deadline:
            try:
                with httpx.Client(timeout=2.0) as c:
                    r = c.get(f"{base_url}/realms/master")
                    if r.status_code in (200, 302):
                        return
            except Exception:
                pass
            time.sleep(2)
        subprocess.run([*compose, "-f", str(COMPOSE_FILE), "logs", "keycloak"], env=cls._compose_env)
        pytest.fail("Keycloak did not become ready within 3 minutes")

    @classmethod
    def _provision_keycloak(cls):
        kc_base = f"http://localhost:{cls._keycloak_port}"
        relay_port = _free_port()
        cls._relay_base_url = f"http://localhost:{relay_port}"
        cls._relay_port = relay_port
        callback = f"{cls._relay_base_url}/auth/oidc/keycloak/callback"
        return provision(redirect_uris=[callback], setup=KeycloakSetup(base_url=kc_base))

    @classmethod
    def _bring_up_relay(cls, keycloak_setup) -> None:
        env = {
            **os.environ,
            "PULSAR_JWT_SECRET_KEY": "byoc-tool-execution-jwt-secret-1234567890abcdef",
            "PULSAR_BOOTSTRAP_ADMIN_USERNAME": "admin",
            "PULSAR_BOOTSTRAP_ADMIN_PASSWORD": "adminpw1234",
            "PULSAR_BOOTSTRAP_ADMIN_EMAIL": "admin@example.com",
            "PULSAR_ALLOWED_ORIGINS": f'["{cls._relay_base_url}"]',
            "PULSAR_TRUSTED_HOSTS": '["localhost", "127.0.0.1"]',
            "PULSAR_OIDC__ENABLED": "true",
            "PULSAR_OIDC__BASE_URL": cls._relay_base_url,
            "PULSAR_OIDC__PROVIDERS__KEYCLOAK__DISPLAY_NAME": "Keycloak",
            "PULSAR_OIDC__PROVIDERS__KEYCLOAK__DISCOVERY_URL": keycloak_setup.discovery_url,
            "PULSAR_OIDC__PROVIDERS__KEYCLOAK__CLIENT_ID": keycloak_setup.client_id,
            "PULSAR_OIDC__PROVIDERS__KEYCLOAK__CLIENT_SECRET": keycloak_setup.client_secret,
            "PULSAR_OIDC__PROVIDERS__KEYCLOAK__CLAIM_USERNAME": "preferred_username",
        }
        cls._relay_proc = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "uvicorn",
                "pulsar_relay.main:app",
                "--host",
                "127.0.0.1",
                "--port",
                str(cls._relay_port),
                "--log-level",
                "warning",
            ],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        deadline = time.time() + 30
        while time.time() < deadline:
            try:
                with httpx.Client(timeout=1.0) as c:
                    if c.get(f"{cls._relay_base_url}/health").status_code == 200:
                        return
            except Exception:
                pass
            time.sleep(0.3)
        stdout, stderr = cls._relay_proc.communicate(timeout=2)
        pytest.fail(
            "Relay subprocess did not start.\n"
            f"stdout={stdout.decode(errors='replace')}\n"
            f"stderr={stderr.decode(errors='replace')}"
        )

    @classmethod
    def _bring_up_pulsar(cls, *, primary_token: str, access_token: str) -> None:
        """Write Pulsar's app.yml + credentials and start the daemon."""
        pulsar_dir = cls._tmp_dir / "pulsar"
        staging = pulsar_dir / "staging"
        persistence = pulsar_dir / "persistence"
        for p in (pulsar_dir, staging, persistence):
            p.mkdir(parents=True, exist_ok=True)

        credentials_path = pulsar_dir / "relay_credentials.json"
        CredentialsFile(str(credentials_path)).save(
            {
                "relay_url": cls._relay_base_url,
                "refresh_token": primary_token,
                "issued_at": "2026-05-11T00:00:00+00:00",
            }
        )

        app_yaml_path = pulsar_dir / "app.yml"
        app_yaml_path.write_text(
            PULSAR_APP_TEMPLATE.read_text().format(
                manager_name=cls._byoc_manager_name,
                message_queue_url=cls._relay_base_url,
                credentials_file=str(credentials_path),
                staging_directory=str(staging),
                persistence_directory=str(persistence),
            )
        )
        server_ini_path = pulsar_dir / "server.ini"
        pulsar_log_path = pulsar_dir / "pulsar.log"
        server_ini_path.write_text(
            "[server:main]\nuse = egg:Paste#http\nhost = 127.0.0.1\nport = 0\n"
            "\n"
            "[loggers]\nkeys=root\n\n"
            "[handlers]\nkeys=console,file\n\n"
            "[formatters]\nkeys=default\n\n"
            "[logger_root]\nlevel=DEBUG\nhandlers=console,file\n\n"
            "[handler_console]\nclass=StreamHandler\nargs=(sys.stderr,)\n"
            "level=DEBUG\nformatter=default\n\n"
            f"[handler_file]\nclass=FileHandler\nargs=('{pulsar_log_path}', 'w')\n"
            "level=DEBUG\nformatter=default\n\n"
            "[formatter_default]\n"
            "format=%(asctime)s %(name)s %(levelname)s %(message)s\n"
        )

        env = {**os.environ}
        env["PYTHONUNBUFFERED"] = "1"
        cls._pulsar_proc = subprocess.Popen(
            [
                sys.executable,
                "-u",
                "-m",
                "pulsar.main",
                "--config_dir",
                str(pulsar_dir),
                "--ini_path",
                str(server_ini_path),
            ],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Wait for Pulsar to subscribe by polling the relay's /api/v1/topics
        # for ``job_setup_<manager_name>``. The relay auto-creates the topic
        # on first subscribe, so its appearance is the signal we want.
        topic = f"job_setup_{cls._byoc_manager_name}"
        deadline = time.time() + 30
        headers = {"Authorization": f"Bearer {access_token}"}
        while time.time() < deadline:
            try:
                with httpx.Client(timeout=1.0) as c:
                    r = c.get(f"{cls._relay_base_url}/api/v1/topics/{topic}", headers=headers)
                    if r.status_code == 200:
                        return
            except Exception:
                pass
            if cls._pulsar_proc.poll() is not None:
                stdout, stderr = cls._pulsar_proc.communicate(timeout=2)
                pytest.fail(
                    "Pulsar subprocess exited before subscribing.\n"
                    f"stdout={stdout.decode(errors='replace')}\n"
                    f"stderr={stderr.decode(errors='replace')}"
                )
            time.sleep(0.5)
        cls._pulsar_proc.terminate()
        try:
            stdout, stderr = cls._pulsar_proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            cls._pulsar_proc.kill()
            stdout, stderr = cls._pulsar_proc.communicate()
        pytest.fail(
            f"Pulsar did not subscribe to {topic} within 30s\n"
            f"stdout={stdout.decode(errors='replace')}\n"
            f"stderr={stderr.decode(errors='replace')}"
        )

    @classmethod
    def _render_galaxy_config_files(cls) -> None:
        # Pulsar's staging_directory must equal the destination's
        # jobs_directory so the tool_script paths Galaxy bakes into command_line
        # resolve on the pulsar side. Use str.replace rather than .format here
        # because the TPV file is full of literal ``{app...}`` rule expressions.
        jobs_dir = cls._tmp_dir / "pulsar" / "staging"
        tpv_path = cls._tmp_dir / "tpv_config.yml"
        tpv_path.write_text(TPV_CONFIG_TEMPLATE.read_text().replace("__JOBS_DIR__", str(jobs_dir)))

        job_conf_path = cls._tmp_dir / "job_conf.yml"
        job_conf_path.write_text(JOB_CONF_TEMPLATE.read_text().format(tpv_config_file=str(tpv_path)))

    # --- The test itself ----------------------------------------------------

    def test_framework_tool_runs_via_byoc(self) -> None:
        """Submit ``environment_variables`` and verify it completes via the
        ``pulsar_byoc`` runner."""
        cls = type(self)
        assert cls._byoc_resource_id is not None
        with self.dataset_populator.test_history() as history_id:
            response = self.dataset_populator.run_tool(
                "environment_variables",
                inputs={"inttest": "3"},
                history_id=history_id,
            )
            self.dataset_populator.wait_for_job(response["jobs"][0]["id"], assert_ok=True)
            job_id_encoded = response["jobs"][0]["id"]
            job_id = self._app.security.decode_id(job_id_encoded)
            from sqlalchemy import select as _select

            job = self._app.model.session.scalars(_select(model.Job).filter_by(id=job_id)).one()
            assert job.job_runner_name == "pulsar_byoc", f"job ran on {job.job_runner_name!r}, expected pulsar_byoc"
            assert job.state == model.Job.states.OK
            # The TPV rule should have injected the resource id into the
            # destination params.
            params = job.destination_params or {}
            assert str(params.get("pulsar_byoc_resource_id")) == str(cls._byoc_resource_id)
            assert params.get("manager") == cls._byoc_manager_name
