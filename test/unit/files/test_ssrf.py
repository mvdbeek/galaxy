import socket

import pytest

from galaxy.exceptions import ConfigDoesNotAllowException
from galaxy.files import ConfiguredFileSources
from galaxy.files.uris import stream_url_to_file


def test_private_http_url_rejected_before_request(tmp_path, httpserver):
    httpserver.expect_request("/data").respond_with_data("private content")
    target = tmp_path / "download"
    with pytest.raises(ConfigDoesNotAllowException):
        stream_url_to_file(
            httpserver.url_for("/data").replace("localhost", "127.0.0.1"),
            target_path=str(target),
        )
    assert httpserver.log == []
    assert not target.exists()


@pytest.mark.parametrize("plugin", ["http", "ftp"])
def test_private_ftp_url_rejected(tmp_path, plugin):
    serialized = ConfiguredFileSources.from_dict(None).to_dict(for_serialization=True)
    serialized["file_sources"] = [{"type": plugin, "id": "test"}]
    target = tmp_path / "download"
    with socket.socket() as endpoint:
        endpoint.bind(("127.0.0.1", 0))
        port = endpoint.getsockname()[1]
        if plugin == "ftp":
            serialized["file_sources"][0]["port"] = port
        sources = ConfiguredFileSources.from_dict(serialized)
        url = f"ftp://127.0.0.1:{port}/data"
        with pytest.raises(ConfigDoesNotAllowException):
            stream_url_to_file(url, file_sources=sources, target_path=str(target))
    assert not target.exists()
