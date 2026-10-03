from types import SimpleNamespace
from typing import (
    Any,
    cast,
)
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from galaxy import exceptions
from galaxy.app_unittest_utils import galaxy_mock
from galaxy.files import (
    ConfiguredFileSources,
    ConfiguredFileSourcesConf,
)
from galaxy.files.models import FileSourcePluginsConfig
from galaxy.managers.context import ProvidesHistoryContext
from galaxy.model import History
from galaxy.schema.fetch_data import FetchDataPayload
from galaxy.schema.fields import Security
from galaxy.webapps.galaxy.api import get_trans
from galaxy.webapps.galaxy.api.tools import (
    FetchTools,
    router,
)
from galaxy.webapps.galaxy.services.tools import ToolsService


class _ToolsServiceUnderTest(ToolsService):
    def _create(self, trans, payload, **kwd):
        return payload


class TestToolsService:
    def setup_method(self):
        self.trans = galaxy_mock.MockTrans()
        self.app = self.trans.app
        Security.security = self.app.security
        self.app.config.check_upload_content = True
        self.authnz_manager = Mock()
        self.app.authnz_manager = self.authnz_manager
        self.trans.init_user_in_database()
        history = History(user=self.trans.user)
        self.trans.sa_session.add(history)
        self.trans.sa_session.commit()
        self.trans.set_history(history)

    def _service(self):
        return _ToolsServiceUnderTest(
            config=self.app.config,
            toolbox_search=cast(Any, object()),
            security=self.app.security,
            history_manager=cast(Any, object()),
        )

    def test_tool_lookup_only_materializes_at_explicit_boundary(self):
        toolbox = Mock()
        cast(Any, self.app).toolbox = toolbox
        tool = Mock()
        tool.allow_user_access.return_value = True
        toolbox.get_tool = Mock(return_value=tool)
        toolbox.materialize_tool = Mock(return_value="parsed")
        service = self._service()

        assert service._get_tool(self.trans, "cat1", user=self.trans.user) is tool
        toolbox.materialize_tool.assert_not_called()

        assert (
            service._get_materialized_tool(self.trans, "cat1", user=self.trans.user, materialization_reason="detail")
            == "parsed"
        )
        toolbox.materialize_tool.assert_called_once_with(tool, reason="detail")

    def test_create_fetch_does_not_refresh_when_fetch_has_no_authorization_header(self):
        self.app.file_sources = ConfiguredFileSources(
            FileSourcePluginsConfig(),
            ConfiguredFileSourcesConf(
                conf_dict=[
                    {
                        "type": "http",
                        "id": "test_plain",
                        "url_regex": r"^https?://example\.org/",
                    }
                ]
            ),
        )

        service = self._service()
        payload = FetchDataPayload.model_validate(
            {
                "history_id": self.app.security.encode_id(self.trans.history.id),
                "targets": [
                    {
                        "destination": {"type": "hdas"},
                        "elements": [
                            {
                                "src": "url",
                                "url": "https://example.org/data.txt",
                                "ext": "txt",
                            }
                        ],
                    }
                ],
            }
        )

        service.create_fetch(cast(ProvidesHistoryContext, self.trans), payload)
        cast(Mock, self.authnz_manager.refresh_expiring_oidc_tokens).assert_not_called()

    def _service_with_tool_directory(self, tool_dir, tool_version="1.0"):
        toolbox = Mock()
        cast(Any, self.app).toolbox = toolbox
        tool = Mock(tool_dir=str(tool_dir), version=tool_version)
        tool.allow_user_access.return_value = True
        toolbox.get_tool.return_value = tool
        toolbox.materialize_tool.return_value = tool
        return self._service()

    @pytest.mark.parametrize("image_file", ["plot.png", "images/plot.svg", "static/images/plot.png"])
    def test_help_image_relative_paths(self, tmp_path, image_file):
        image_path = tmp_path / image_file
        image_path.parent.mkdir(parents=True, exist_ok=True)
        image_path.write_bytes(b"image")
        service = self._service_with_tool_directory(tmp_path)
        path, media_type = service.get_tool_help_image(self.trans, "local", image_file, "1.0")
        assert path == str(image_path.resolve())
        assert media_type == ("image/svg+xml" if image_file.endswith(".svg") else "image/png")
        cast(Mock, self.app.toolbox).get_tool.assert_called_once_with("local", "1.0")

    def test_help_image_static_directory_takes_precedence(self, tmp_path):
        (tmp_path / "plot.png").write_bytes(b"root")
        static_images = tmp_path / "static" / "images"
        static_images.mkdir(parents=True)
        image_path = static_images / "plot.png"
        image_path.write_bytes(b"static")
        service = self._service_with_tool_directory(tmp_path)
        path, _ = service.get_tool_help_image(self.trans, "local", "plot.png")
        assert path == str(image_path.resolve())

    @pytest.mark.parametrize("image_file", ["../../../outside.png", "tool.xml", "script.py", "index.html"])
    def test_help_image_rejects_unsafe_paths_and_non_images(self, tmp_path, image_file):
        service = self._service_with_tool_directory(tmp_path)
        with pytest.raises(exceptions.RequestParameterInvalidException):
            service.get_tool_help_image(self.trans, "local", image_file)

    def test_help_image_rejects_symlink_escape(self, tmp_path):
        tool_dir = tmp_path / "tool"
        tool_dir.mkdir()
        outside = tmp_path / "outside.png"
        outside.write_bytes(b"private")
        (tool_dir / "plot.png").symlink_to(outside)
        service = self._service_with_tool_directory(tool_dir)
        with pytest.raises(exceptions.RequestParameterInvalidException):
            service.get_tool_help_image(self.trans, "local", "plot.png")
        with pytest.raises(exceptions.RequestParameterInvalidException):
            service.get_tool_help_image(self.trans, "local", str(outside))

    def test_help_image_missing(self, tmp_path):
        service = self._service_with_tool_directory(tmp_path)
        with pytest.raises(exceptions.ObjectNotFound):
            service.get_tool_help_image(self.trans, "local", "missing.png")

    def test_help_image_does_not_fall_back_to_another_version(self, tmp_path):
        (tmp_path / "plot.png").write_bytes(b"image")
        service = self._service_with_tool_directory(tmp_path)
        with pytest.raises(exceptions.ObjectNotFound, match="Tool version not found"):
            service.get_tool_help_image(self.trans, "local", "plot.png", "0.9")

    def test_help_image_respects_tool_access(self, tmp_path):
        service = self._service_with_tool_directory(tmp_path)
        cast(Mock, self.app.toolbox).get_tool.return_value.allow_user_access.return_value = False
        with pytest.raises(exceptions.AuthenticationFailed):
            service.get_tool_help_image(self.trans, "local", "plot.png")

    def test_help_image_checks_access_for_current_user(self, tmp_path):
        (tmp_path / "plot.png").write_bytes(b"image")
        service = self._service_with_tool_directory(tmp_path)
        tool = cast(Mock, self.app.toolbox).get_tool.return_value
        tool.allow_user_access.side_effect = lambda user: user is self.trans.user
        assert service.get_tool_help_image(self.trans, "local", "plot.png")[1] == "image/png"
        tool.allow_user_access.assert_called_once_with(self.trans.user)

    def test_help_image_api_serves_image(self, tmp_path):
        image_file = "plot +#.svg"
        contents = b'<svg xmlns="http://www.w3.org/2000/svg"/>'
        (tmp_path / image_file).write_bytes(contents)
        service = self._service_with_tool_directory(tmp_path, tool_version="1.0+test")
        app = FastAPI()
        app.include_router(router)
        app.dependency_overrides[FetchTools] = lambda: SimpleNamespace(service=service)
        app.dependency_overrides[get_trans] = lambda: self.trans
        with TestClient(app) as client:
            response = client.get(
                "/api/tools/local%3A%20tool/help_image",
                params={"tool_version": "1.0+test", "image_file": image_file},
            )
        assert response.status_code == 200
        assert response.content == contents
        assert response.headers["content-type"] == "image/svg+xml"
        assert response.headers["x-content-type-options"] == "nosniff"
        cast(Mock, self.app.toolbox).get_tool.assert_called_once_with("local: tool", "1.0+test")
